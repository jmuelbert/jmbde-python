#!/bin/bash
# -*- coding: utf-8 -*-

# Package info
PPA="ppa:jmuelbert/stable"
NAME="jmbde-python"
VERSION="0.1"
GPG_KEY_FILE="gpg_key"
SUITES=("trusty" "utopic" "vivid")

# Read PGP key from gpg_key file
if [[ ! -f $GPG_KEY_FILE ]]; then
  echo "Error: GPG key file not found: $GPG_KEY_FILE" >&2
  exit 1
fi
GPG_KEY=$(<"$GPG_KEY_FILE")

# Generate Debian source package and .orig.tar.gz
if ! python3 setup.py --command-packages=stdeb.command sdist_dsc; then
  echo "Error: Failed to generate Debian source package." >&2
  exit 1
fi

DATE=$(date -R)

# Clean up .pyc files
find . -name "*.pyc" -exec rm -f {} +

# Function to build and upload package
build_and_upload() {
  local suite="$1"

  pushd deb_dist || {
    echo "Error: Failed to enter deb_dist directory."
    exit 1
  }
  pushd "${NAME}-${VERSION}" || {
    echo "Error: Failed to enter ${NAME}-${VERSION} directory."
    exit 1
  }

  # Update changelog to include Ubuntu release
  local changelog="${NAME} (${VERSION}-1ppa1~${suite}1) ${suite}; urgency=low
  * Initial release
 -- Jürgen Mülbert <juergen.muelbert@gmail.com>  ${DATE}
"
  echo "$changelog" >debian/changelog
  cat debian/changelog

  if ! debuild -S -sa -k"$GPG_KEY"; then
    echo "Error: Failed to build package for suite: $suite" >&2
    popd || exit 1
    popd || exit 1
    return 1
  fi

  # Upload to PPA
  if ! dput "$PPA" ./*.changes; then
    echo "Error: Failed to upload to PPA for suite: $suite" >&2
    popd || exit 1
    popd || exit 1
    return 1
  fi

  # Cleanup
  rm -rf ./*.dsc ./*.changes
  popd || exit 1
  popd || exit 1
}

# Loop through suites and build/upload packages
for suite in "${SUITES[@]}"; do
  build_and_upload "$suite" || exit 1
done

# Cleanup
rm -rf ./*.tar.gz deb_dist/ dist/
echo "Cleanup completed."
