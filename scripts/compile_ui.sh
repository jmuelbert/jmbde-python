#!/bin/bash
pyside2-uic -o src/jmbde/views/AboutDialog.py src/jmbde/forms/aboutdialog.ui
pyside2-uic -o src/jmbde/views/ChipCardInputArea.py src/jmbde/forms/chipcardinputarea.ui
pyside2-uic -o src/jmbde/views/CityInputArea.py src/jmbde/forms/cityinputarea.ui
pyside2-uic -o src/jmbde/views/ComputerInputArea.py src/jmbde/forms/computerinputarea.ui
pyside2-uic -o src/jmbde/views/CsvImportDialog.py src/jmbde/forms/csvimportdialog.ui
pyside2-uic -o src/jmbde/views/DepartmentInputArea.py src/jmbde/forms/departmentinputarea.ui
pyside2-uic -o src/jmbde/views/EmployeeInputArea.py src/jmbde/forms/employeeinputarea.ui
pyside2-uic -o src/jmbde/views/FunctionInputArea.py src/jmbde/forms/functioninputarea.ui
pyside2-uic -o src/jmbde/views/MainWindow.py src/jmbde/forms/mainwindow.ui
pyside2-uic -o src/jmbde/views/ManufacturerInputArea.py src/jmbde/forms/manufacturerinputarea.ui
pyside2-uic -o src/jmbde/views/MobileInputArea.py src/jmbde/forms/mobileinputarea.ui
pyside2-uic -o src/jmbde/views/OsInputArea.py src/jmbde/forms/osinputarea.ui
pyside2-uic -o src/jmbde/views/PhoneInputArea.py src/jmbde/forms/phoneinputarea.ui
pyside2-uic -o src/jmbde/views/PreferencesDialog.py src/jmbde/forms/preferencesdialog.ui
pyside2-uic -o src/jmbde/views/PrinterInputArea.py src/jmbde/forms/printerinputarea.ui
pyside2-uic -o src/jmbde/views/ProcessorInputArea.py src/jmbde/forms/processorinputarea.ui
pyside2-uic -o src/jmbde/views/SoftwareInputArea.py src/jmbde/forms/softwareinputarea.ui
pyside2-uic -o src/jmbde/views/TitleInputArea.py src/jmbde/forms/titleinputarea.ui
#
# translations
#
# Generate translations source of QML and ui files
lupdate jmbde.pro
# Generate translations source of Python files
pyside2-lupdate -verbose -noobsolete src/jmbde/*.py
pyside2-lupdate -verbose -noobsolete src/jmbde/models/*.py

lrelease jmbde.pro
#
# Resources
#
pyside2-rcc -o src/jmbde/resources.py src/jmbde/resources/resources.qrc
