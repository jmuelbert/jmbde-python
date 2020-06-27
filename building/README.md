# Building

## macOS

1. Create a python environment

    ```bash
    conda create -n python37 python=3.7
    conda activate python37
    ```

2. Install requierements.

    ```bash
    pip install -r requierments.txt
    ```

3. Update the translations. Install Qt first and make sure you can run `lupdate` and `lrelease` commands.

    ```bash
    # Generate translations source of QML files
    lupdate jmbde.pro

    # Generate translations source of Python files
    pyside2-lupdate src/jmbde/*.py -ts resources/translations/app_LANG.ts

    # Generate translations target
    lrelease resources/translations/app_LANG.ts
    ```

4. Build with `PyInstaller`

    ```bash
    # Install the latest develop version of PyInstaller

    # You may need rebuild the bootloader of PyInstaller againt 10.14 SDK to fully support dark theme
    # See: https://pyinstaller.readthedocs.io/en/latest/bootloader-building.html

    rm -rf build
    rm -rf dist

    pyside2-rcc resources/resources.qrc -o src/jmbde/resource.py

    pyinstaller -w src/jmbde/__main__.py \
        --hidden-import "socks" \
        --hidden-import "PIL" \
        --add-data "LICENSE:." \
        --add-data "conf/jmbde.conf:conf" \
        --add-data "conf/qtquickcontrols2.conf:conf" \
        --add-data "resources/translations/*.qm:translations" \
        --name "jmbde" \
        --icon "resources/icons/app.icns" \
        --noupx

    cp building/macOS/Info.plist dist/jmbde.app/Contents

    # Remove useless libraries
    cd dist/jmbde.app/Contents/MacOS
    rm -f Qt3D* QtBluetooth QtBodymovin QtCharts QtDataVisualization QtGamepad QtLocation QtMultimedia QtMultimediaQuick QtNfc QtPositioning QtPositioningQuick QtPurchasing QtQuick3D* QtQuickTest QtRemoteObjects QtScxml QtSensors QtSql QtTest QtVirtualKeyboard QtWeb*
    rm -f libopenblas*
    cd PySide2/qml
    rm -rf Qt3D* QtAudioEngine QtBluetooth QtCharts QtDataVisualization QtGamepad QtLocation QtMultimedia QtNfc QtPositioning QtPurchasing QtQuick3D* QtRemoteObjects QtScxml QtSensors QtTest QtWeb*
    cd ../../../Resources
    rm -rf PyInstaller
    cd ../../../..
    ```

    `jmbde.app` will be in `dist`.

5. Package with `appdmg`. Install [Node.js](https://nodejs.org) first, then run the following commands:

    ```bash
    npm install -g appdmg
    appdmg building/macOS/jmbde.dmg.json dist/jmbde.dmg
    ```

    `jmbde.dmg` will be in `dist`.

## Windows

1. See setcion 1 in [macOS](#macOS).
2. See setcion 2 in [macOS](#macOS).
3. See setcion 3 in [macOS](#macOS).
4. Build with `PyInstaller`.

    ```powershell
    :: Install the latest develop version of PyInstaller

    rd /s /Q build
    rd /s /Q dist
    del /F /S /Q jmbde.spec
    ```


    pyside2-rcc resources/resources.qrc -o src/jmbde/resource.py

    pyinstaller -w src/jmbde/__main__.py ^
        --hidden-import "socks" ^
        --hidden-import "PIL" ^
        --add-data "LICENSE;." ^
        --add-data "conf/jmbde.conf;conf" ^
        --add-data "conf/qtquickcontrols2.conf;conf" ^
        --add-data "resources/translations/*.qm;translations" ^
        --name "jmbde" ^
        --icon "resources/icons/app.ico" ^
        --version-file "building/Windows/jmbde.win.version" ^
        --noupx

    :: Remove useless libraries
    cd dist/jmbde
    del /F /S /Q Qt3D* QtBluetooth QtBodymovin QtCharts QtDataVisualization QtGamepad QtLocation QtMultimedia QtMultimediaQuick QtNfc QtPositioning QtPositioningQuick QtPurchasing QtQuick3D* QtQuickTest QtRemoteObjects QtScxml QtSensors QtSql QtTest QtVirtualKeyboard QtWeb*
    cd PySide2/qml
    del /F /S /Q Qt3D* QtAudioEngine QtBluetooth QtCharts QtDataVisualization QtGamepad QtLocation QtMultimedia QtNfc QtPositioning QtPurchasing QtQuick3D* QtRemoteObjects QtScxml QtSensors QtTest QtWeb*
    cd ../../../..
    ```

    All compiled files will be in `dist\jmbde`.
    ```

5. Package with Inno Setup. Install [Inno Setup 6](http://www.jrsoftware.org/isinfo.php) first and add installation directory to PATH.

    ```powershell
    ISCC.exe building/Windows/jmbde.iss
    ```

    `jmbde.exe` installer will be in the `dist`.

6. If you need a x86 version, please make sure you have a x86 version python environment, and modify the `jmbde.iss` accordingly.

    ```text
    DefaultDirName={autopf64}\{#MyAppName} -> DefaultDirName={autopf32}\{#MyAppName}
    OutputBaseFilename=jmbde-x64 -> OutputBaseFilename=jmbde-x86
    ```
