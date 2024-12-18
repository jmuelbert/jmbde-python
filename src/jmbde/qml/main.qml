// SPDX-FileCopyrightText: Jürgen Mülbert
// SPDX-License-Identifier: GPL-3.0-or-later

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Window
import Qt.labs.platform as Platform

import "components" as Components

ApplicationWindow {
    id: mainWindow
    title: qsTr("JMBDE - Business Data Management")
    width: settings.getValue("ui.window_width") || 1024
    height: settings.getValue("ui.window_height") || 768
    visible: true

    // Theme and styling
    Material.theme: settings.theme === "dark" ? Material.Dark : Material.Light
    Material.accent: Material.Blue
    font.pointSize: settings.getValue("ui.font_size") || 10

    // Properties
    property bool isLoading: false
    property string statusMessage: ""

    // Menu Bar
    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")

            Action {
                text: qsTr("&New Employee")
                shortcut: StandardKey.New
                onTriggered: employeeCrud.showAddDialog()
            }
            MenuSeparator { }
            Action {
                text: qsTr("&Settings")
                onTriggered: settingsDialog.open()
            }
            MenuSeparator { }
            Action {
                text: qsTr("E&xit")
                shortcut: StandardKey.Quit
                onTriggered: Qt.quit()
            }
        }

        Menu {
            title: qsTr("&View")

            Action {
                text: qsTr("&Dark Theme")
                checkable: true
                checked: settings.theme === "dark"
                onTriggered: settings.theme = checked ? "dark" : "light"
            }
        }

        Menu {
            title: qsTr("&Help")

            Action {
                text: qsTr("&About")
                onTriggered: aboutDialog.open()
            }
        }
    }

    // Tool Bar
    header: ToolBar {
        visible: settings.getValue("ui.show_toolbar")

        RowLayout {
            anchors.fill: parent
            spacing: 10

            ToolButton {
                icon.name: "add"
                text: qsTr("Add Employee")
                onClicked: employeeCrud.showAddDialog()
            }

            TextField {
                id: searchField
                Layout.fillWidth: true
                placeholderText: qsTr("Search employees...")
                onTextChanged: employeeModel.filterText = text
            }

            ComboBox {
                id: departmentFilter
                model: mainApp.get_departments()
                Layout.preferredWidth: 200
                placeholderText: qsTr("All Departments")
                onCurrentTextChanged: {
                    employeeModel.departmentFilter = currentText === placeholderText ? "" : currentText
                }
            }

            Switch {
                text: qsTr("Show Inactive")
                onCheckedChanged: employeeModel.showInactive = checked
            }
        }
    }

    // Main Content
    Components.EmployeeCrud {
        id: employeeCrud
        anchors.fill: parent
    }

    // Status Bar
    footer: Component.StatusBar {
        visible: settings.getValue("ui.show_statusbar")

        RowLayout {
            anchors.fill: parent

            Label {
                text: statusMessage
                Layout.fillWidth: true
            }

            BusyIndicator {
                visible: isLoading
                running: visible
                Layout.preferredHeight: 20
                Layout.preferredWidth: 20
            }

            Label {
                text: {
                    const stats = mainApp.get_statistics()
                    return qsTr("Total: %1 | Active: %2 | Departments: %3")
                        .arg(stats.total_employees)
                        .arg(stats.active_employees)
                        .arg(stats.departments)
                }
            }
        }
    }

    // Dialogs
    Dialog {
        id: settingsDialog
        title: qsTr("Settings")
        modal: true
        standardButtons: Dialog.Ok | Dialog.Cancel

        ColumnLayout {
            spacing: 20

            GroupBox {
                title: qsTr("Interface")
                Layout.fillWidth: true

                ColumnLayout {
                    anchors.fill: parent

                    CheckBox {
                        text: qsTr("Show Toolbar")
                        checked: settings.getValue("ui.show_toolbar")
                        onCheckedChanged: settings.setValue("ui.show_toolbar", checked)
                    }

                    CheckBox {
                        text: qsTr("Show Status Bar")
                        checked: settings.getValue("ui.show_statusbar")
                        onCheckedChanged: settings.setValue("ui.show_statusbar", checked)
                    }

                    SpinBox {
                        from: 8
                        to: 24
                        value: settings.getValue("ui.font_size")
                        onValueChanged: settings.setValue("ui.font_size", value)
                        Layout.fillWidth: true
                    }
                }
            }
        }
    }

    Dialog {
        id: aboutDialog
        title: qsTr("About JMBDE")
        modal: true
        standardButtons: Dialog.Close

        ColumnLayout {
            spacing: 20

            Image {
                source: "qrc:/images/logo.png"
                Layout.alignment: Qt.AlignHCenter
                Layout.preferredWidth: 100
                Layout.preferredHeight: 100
            }

            Label {
                text: "JMBDE - Business Data Management"
                font.bold: true
                Layout.alignment: Qt.AlignHCenter
            }

            Label {
                text: "Version 1.0.0"
                Layout.alignment: Qt.AlignHCenter
            }

            Label {
                text: "© 2018-2024 Jürgen Mülbert"
                Layout.alignment: Qt.AlignHCenter
            }
        }
    }

    // Error handling
    Connections {
        target: mainApp

        function onErrorOccurred(error) {
            errorDialog.text = error
            errorDialog.open()
        }

        function onOperationSucceeded(message) {
            statusMessage = message
            successSnackbar.show(message)
        }
    }

    Dialog {
        id: errorDialog
        title: qsTr("Error")
        modal: true
        standardButtons: Dialog.Ok

        property alias text: errorLabel.text

        Label {
            id: errorLabel
            wrapMode: Text.WordWrap
            color: "red"
        }
    }

    Component.Snackbar {
        id: successSnackbar
        timeout: 3000
        showButton: true
        buttonText: qsTr("Undo")

        // Optional: Handle undo action
        onButtonClicked: {
            // Implement undo logic here
            console.log("Undo clicked")
        }
    }

    // Window state handling
    Component.onCompleted: {
        x = Screen.width / 2 - width / 2
        y = Screen.height / 2 - height / 2
    }

    onClosing: {
        settings.setValue("ui.window_width", width)
        settings.setValue("ui.window_height", height)
    }
}
