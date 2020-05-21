#!/bin/bash
../venv/bin/pyinstaller jmbde_python.spec
mv dist/jmbde dist/opt/
rm target/jmbde_python.rpm
fpm -s dir --log error --rpm-rpmbuild-define "_build_id_links none" -C dist -n jmbde -v 0.1 --vendor jmuelbert -t rpm -p target/jmbde_python.rpm
