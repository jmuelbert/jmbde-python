#!/bin/bash

while getopts "trqh" arg; do
    case $arg in
    t)
        translate="1"
        ;;
    r)
        resources="1"
        ;;
    q)
        create_qm_files="1"
        ;;
    *)
        echo "-t updates ui.ts file."
        echo "-r updates resources.py file."
        echo "-q create qm files from ts files."
        ;;
    esac
done

# finding parent directory
dir=$(pwd)
parent_dir=$(dirname $dir)

if [ "$translate" == "1" ]; then

    # generate ui.ts file
    pyside2-lupdate -verbose "$dir/translation_files.pro"
    echo "$dir/translations/ui.ts is generated!"
fi

if [ "$resources" == "1" ]; then

    # generate resource.py file
    pyside2-rcc resources.qrc -o "$parent_dir/src/jmbde/resources.py"

    echo "$parent_dir/src/jmbde/resource.py is generated!"
fi

if [ "$create_qm_files" == "1" ]; then

    # generate qm files from ts files
    lrelease "$dir/translations/*.ts"
fi
