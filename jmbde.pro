QT += core quick quickcontrols2
CONFIG += c++17

SOURCES = \
    src/jmbde/__init__.py \
    src/jmbde/__main__.py \
    src/jmbde/logger.py \
    tests/__init__.py \
    tests/basic_test.py

FORMS += \
    src/jmbde/forms/aboutdialog.ui \
    src/jmbde/forms/chipcardinputarea.ui \
    src/jmbde/forms/cityinputarea.ui \
    src/jmbde/forms/computerinputarea.ui \
    src/jmbde/forms/csvimportdialog.ui \
    src/jmbde/forms/departmentinputarea.ui \
    src/jmbde/forms/employeeinputarea.ui \
    src/jmbde/forms/functioninputarea.ui \
    src/jmbde/forms/mainwindow.ui \
    src/jmbde/forms/manufacturerinputarea.ui \
    src/jmbde/forms/mobileinputarea.ui \
    src/jmbde/forms/osinputarea.ui \
    src/jmbde/forms/phoneinputarea.ui \
    src/jmbde/forms/preferencesdialog.ui \
    src/jmbde/forms/printerinputarea.ui \
    src/jmbde/forms/processorinputarea.ui \
    src/jmbde/forms/softwareinputarea.ui \
    src/jmbde/forms/titleinputarea.ui

RESOURCES += \
    src/resources/jmbde.qrc

lupdate_only {
    SOURCES +=
        qml/main.qml
}

TRANSLATIONS += \
    src/jmbde/languages/jmbde_ar_DZ.ts \
    src/jmbde/languages/jmbde_bg.ts \
    src/jmbde/languages/jmbde_ca_ES.ts \
    src/jmbde/languages/jmbde_cs.ts \
    src/jmbde/languages/jmbde_de.ts \
    src/jmbde/languages/jmbde_en.ts \
    src/jmbde/languages/jmbde_en_US.ts \
    src/jmbde/languages/jmbde_es.ts \
    src/jmbde/languages/jmbde_es_ES.ts \
    src/jmbde/languages/jmbde_fr.ts \
    src/jmbde/languages/jmbde_fr_FR.ts \
    src/jmbde/languages/jmbde_he.ts \
    src/jmbde/languages/jmbde_hu.ts \
    src/jmbde/languages/jmbde_it.ts \
    src/jmbde/languages/jmbde_ja.ts \
    src/jmbde/languages/jmbde_js.ts \
    src/jmbde/languages/jmbde_nb.ts \
    src/jmbde/languages/jmbde_nl.ts \
    src/jmbde/languages/jmbde_pl.ts \
    src/jmbde/languages/jmbde_pt.ts \
    src/jmbde/languages/jmbde_pt_PT.ts \
    src/jmbde/languages/jmbde_ru.ts \
    src/jmbde/languages/jmbde_tr.ts \
    src/jmbde/languages/jmbde_uk.ts \
    src/jmbde/languages/jmbde_zh_TCN.ts \
    src/jmbde/languages/jmbde_zh_TW.ts
