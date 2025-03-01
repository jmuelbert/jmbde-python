#!/bin/bash

# Install the latest develop version of PyInstaller

# You may need rebuild the bootloader of PyInstaller against 10.14 SDK to fully support dark theme
# See: https://pyinstaller.readthedocs.io/en/latest/bootloader-building.html

rm -rf build
rm -rf dist
rm -f jmbde.spec

pyside2-rcc src/jmbde/resources/resources.qrc -o src/jmbde/rcs.py

pyinstaller -w src/jmbde/__main__.py \
  --hidden-import "socks" \
  --hidden-import "PIL" \
  --add-data "LICENSE:." \
  --add-data "conf/jmbde.conf:conf" \
  --add-data "conf/qtquickcontrols2.conf:conf" \
  --add-data "src/jmbde/resources/icons/app.ico:images" \
  --add-data "src/jmbde/translations/*.qm:translations" \
  --name "jmbde" \
  --icon "src/jmbde/resources/icons/app.icns" \
  --noupx

cp building/macOS/Info.plist dist/jmbde.app/Contents

# Remove useless libraries
cd dist/jmbde.app/Contents/MacOS || exit
rm -f Qt3D* QtBluetooth QtBodymovin QtCharts QtDataVisualization QtGamepad QtLocation QtMultimedia QtMultimediaQuick QtNfc QtPositioning QtPositioningQuick QtPurchasing QtQuick3D* QtQuickTest QtRemoteObjects QtScxml QtSensors QtSql QtTest QtVirtualKeyboard QtWeb*
rm -f libopenblas*
cd PySide2/qml || exit
rm -rf Qt3D* QtAudioEngine QtBluetooth QtCharts QtDataVisualization QtGamepad QtLocation QtMultimedia QtNfc QtPositioning QtPurchasing QtQuick3D* QtRemoteObjects QtScxml QtSensors QtTest QtWeb*
cd ../../../Resources || exit
rm -rf PyInstaller
cd ../../../.. || exit
