#!/usr/bin/env bash
#
# SPDX-FileCopyRightText: 2023 Macklan Weinstein <macklan.weinstein@gmail.com>
#
# SPDX-License-Identifier: MIT
# Original File: https://github.com/scruffaluff/scaffold-python/tree/main/%7B%7Bcookiecutter.project_name%7D%7D/scripts
#
# Installs Tmate and creates a session suitable for CI. Based on logic from
# https://github.com/mxschmitt/action-tmate.

# Exit immediately if a command exits or pipes a non-zero return code.
#
# Flags:
#   -e: Exit immediately when a command pipeline fails.
#   -o: Persist nonzero exit codes through a Bash pipe.
#   -u: Throw an error when an unset variable is encountered.
set -eou pipefail

#######################################
# Show CLI help information.
# Cannot use function name help, since help is a pre-existing command.
# Outputs:
#   Writes help information to stdout.
#######################################
usage() {
  case "$1" in
  main)
    cat 1>&2 <<EOF
$(version)
Installs Tmate and creates a remote session. Users can close the session by
creating the file /close-tmate.

USAGE:
    setup-tmate [OPTIONS]

OPTIONS:
        --debug      Show Bash debug traces
    -h, --help       Print help information
    -v, --version    Print version information
EOF
    ;;
  *)
    error "No such usage option '$1'"
    ;;
  esac
}

#######################################
# Assert that command can be found in system path.
# Will exit script with an error code if command is not in system path.
# Arguments:
#   Command to check availability.
# Outputs:
#   Writes error message to stderr if command is not in system path.
#######################################
assert_cmd() {
  # Flags:
  #   -v: Only show file path of command.
  #   -x: Check if file exists and execute permission is granted.
  if [[ ! -x "$(command -v "$1")" ]]; then
    error "Cannot find required $1 command on computer"
  fi
}

#######################################
# Print error message and exit script with error code.
# Outputs:
#   Writes error message to stderr.
#######################################
error() {
  local bold_red='\033[1;31m'
  local default='\033[0m'

  printf "${bold_red}error${default}: %s\n" "$1" >&2
  exit 1
}

#######################################
# Install Tmate.
#######################################
install_tmate() {
  local arch_type tmate_arch
  local tmate_version='2.4.0'

  # Short form machine flag '-m' should be used since processor flag and long
  # form machine flag '--machine' are non-portable. For more information, visit
  # https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html#index-_002dp-12.
  arch_type="$(uname -m)"
  case "${arch_type}" in
  x86_64 | amd64)
    tmate_arch='amd64'
    ;;
  arm64 | aarch64)
    tmate_arch='arm64v8'
    ;;
  *)
    error "Unsupported architecture ${arch_type}"
    ;;
  esac

  # Install OpenSSH and archive utils.
  #
  # Flags:
  #   -v: Only show file path of command.
  #   -x: Check if file exists and execute permission is granted.
  if [[ -x "$(command -v apk)" ]]; then
    ${1:+sudo} apk add curl openssh-client xz
  elif [[ -x "$(command -v apt-get)" ]]; then
    ${1:+sudo} apt-get update
    ${1:+sudo} apt-get install -y curl openssh-client xz-utils
  elif [[ -x "$(command -v dnf)" ]]; then
    ${1:+sudo} dnf install -y curl openssh xz
  elif [[ -x "$(command -v pacman)" ]]; then
    ${1:+sudo} pacman -Suy --noconfirm
    ${1:+sudo} pacman -S --noconfirm curl openssh xz
  elif [[ -x "$(command -v zypper)" ]]; then
    ${1:+sudo} zypper install -y curl openssh tar xz
  fi

  assert_cmd curl
  assert_cmd tar

  curl -LSfs "https://github.com/tmate-io/tmate/releases/download/${tmate_version}/tmate-${tmate_version}-static-linux-${tmate_arch}.tar.xz" -o /tmp/tmate.tar.xz
  tar xvf /tmp/tmate.tar.xz -C /tmp --strip-components 1
  ${1:+sudo} install /tmp/tmate /usr/local/bin/tmate
  rm /tmp/tmate /tmp/tmate.tar.xz
}

#######################################
# Print Setup Tmate version string.
# Outputs:
#   Setup Tmate version string.
#######################################
version() {
  echo 'SetupTmate 0.0.1'
}

#######################################
# Installs Tmate and creates a remote session.
#######################################
setup_tmate() {
  local use_sudo=''

  # Check if user is not root.
  if [[ "${EUID}" -ne 0 ]]; then
    assert_cmd sudo
    use_sudo=1
  fi

  # Install Tmate if not available.
  #
  # Flags:
  #   -v: Only show file path of command.
  #   -x: Check if file exists and execute permission is granted.
  if [[ ! -x "$(command -v tmate)" ]]; then
    install_tmate "${use_sudo}"
  fi

  # Launch new Tmate session with custom socket.
  #
  # Flags:
  #   -S: Set Tmate socket path.
  tmate -S /tmp/tmate.sock new-session -d
  tmate -S /tmp/tmate.sock wait tmate-ready
  ssh_connect="$(tmate -S /tmp/tmate.sock display -p '#{tmate_ssh}')"
  web_connect="$(tmate -S /tmp/tmate.sock display -p '#{tmate_web}')"

  while true; do
    echo "SSH: ${ssh_connect}"
    echo "Web shell: ${web_connect}"

    # Check if script should exit.
    #
    # Flags:
    #   -f: Check if file exists and is a socket.
    #   -f: Check if file exists and is a regular file.
    if [[ ! -S /tmp/tmate.sock || -f /close-tmate ]]; then
      break
    fi

    sleep 5
  done
}

#######################################
# Script entrypoint.
#######################################
main() {
  # Parse command line arguments.
  while [[ "$#" -gt 0 ]]; do
    case "$1" in
    --debug)
      set -o xtrace
      shift 1
      ;;
    -h | --help)
      usage 'main'
      exit 0
      ;;
    -v | --version)
      version
      exit 0
      ;;
    *) ;;
    esac
  done

  setup_tmate
}

# Variable BASH_SOURCE cannot be used to load script as a library. Piping the
# script to Bash gives the same BASH_SOURCE result as sourcing the script.
main "$@"
