#!/bin/bash

SOURCE_DIR=resources
DEST_DIR=src/jmbde

for f in $SOURCE_DIR/forms/*.ui; do
    fileName=$(basename -s ".ui" "$f")
    echo "Compile $f to $DEST_DIR/gui/forms/ui_$fileName.py"
    pyside6-uic -o "$DEST_DIR/gui/forms/ui_$fileName.py" "$f"
done

#
# translations
#
# Generate translations source of QML and ui files
# lupdate jmbde.pro
# Generate translations source of Python files
for lang in ar bg ca cs da en es fa fi fr gd gl he hu it ja ko lt lv nl pl pt ru sk tr uk zh_CN zh_TW; do
    pyside6-lupdate -recursive -no-obsolete -extensions py $DEST_DIR/** -ts $SOURCE_DIR/translations/jmbde_$lang.ts
done

# lrelease jmbde.pro
for f in $SOURCE_DIR/translations/*.ts; do
    fileName=$(basename -s ".ts" "$f")
    echo "Compile Translation {$f} to $DEST_DIR/translations/ui_$fileName.py"
    pyside6-lrelease -qm "$SOURCE_DIR/translations/$fileName.qm" "$f"
done

#
# Resources
#
echo "Compile Resources from $DEST_DIR/resources.py to $SOURCE_DIR/resources.qrc"
pyside6-rcc -o $DEST_DIR/gui/resources_rc.py $SOURCE_DIR/resources.qrc
