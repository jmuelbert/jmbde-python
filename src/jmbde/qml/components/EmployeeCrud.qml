// SPDX-FileCopyrightText: Jürgen Mülbert
// SPDX-License-Identifier: GPL-3.0-or-later

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material
import QtQml

ApplicationWindow {
    id: root
    visible: true
    width: 800
    height: 600
    title: qsTr("Employee Manager")

    // Global Material Theme
    Material.theme: Material.Light
    Material.accent: Material.Blue

    property bool isValidName: false
    property bool isValidPosition: false
    property bool isValidEmail: true  // Optional field
    property bool isValidPhone: true  // Optional field

    // Main Employee List
    ListView {
        id: employeeList
        anchors.fill: parent
        model: employee_Model
        clip: true

        delegate: ItemDelegate {
            width: employeeList.width
            height: 80

            RowLayout {
                anchors.fill: parent
                anchors.margins: 10
                spacing: 10

                ColumnLayout {
                    Layout.fillWidth: true
                    spacing: 5

                    Label {
                        text: model.name
                        font.bold: true
                        font.pointSize: settings.getValue("ui.font_size") + 2
                    }

                    Label {
                        text: model.position
                        color: Material.accent
                    }

                    Label {
                        text: model.department || qsTr("No Department")
                        font.italic: !model.department
                        opacity: 0.7
                    }
                }

                ColumnLayout {
                    Layout.preferredWidth: 200
                    spacing: 5

                    Label {
                        text: model.email || qsTr("No Email")
                        font.italic: !model.email
                    }

                    Label {
                        text: model.phone || qsTr("No Phone")
                        font.italic: !model.phone
                    }
                }

                RowLayout {
                    spacing: 5

                    Button {
                        icon.name: "edit"
                        text: qsTr("Edit")
                        onClicked: {
                            editEmployeeDialog.openWithModel(model)
                        }
                    }

                    Button {
                        icon.name: "delete"
                        text: qsTr("Delete")
                        Material.accent: Material.Red
                        onClicked: deleteConfirmDialog.prompt(model.id, model.name)
                    }
                }
            }
        }

        ScrollBar.vertical: ScrollBar {}
    }

    // Common Dialog Base
    Dialog {
        id: baseEmployeeDialog
        modal: true
        width: 400
        property bool isEditMode: false
        property var currentModel: null

        function resetFields() {
            nameField.text = isEditMode && currentModel ? currentModel.name : ""
            positionField.text = isEditMode && currentModel ? currentModel.position : ""
            emailField.text = isEditMode && currentModel ? currentModel.email || "" : ""
            phoneField.text = isEditMode && currentModel ? currentModel.phone || "" : ""
            departmentField.currentText = isEditMode && currentModel ? currentModel.department || "" : ""
            root.isValidName = false
            root.isValidPosition = false
            root.isValidEmail = true
            root.isValidPhone = true
        }

        onAccepted: {
            if (root.isValidName && root.isValidPosition && root.isValidEmail && root.isValidPhone) {
                if (isEditMode) {
                    mainApp.update_employee(
                        currentModel.id,
                        nameField.text,
                        positionField.text,
                        emailField.text,
                        phoneField.text,
                        departmentField.currentText
                    )
                } else {
                    mainApp.add_employee(
                        nameField.text,
                        positionField.text,
                        emailField.text,
                        phoneField.text,
                        departmentField.currentText
                    )
                }
                resetFields()
            }
        }

        ColumnLayout {
            anchors.fill: parent
            spacing: 20

            TextField {
                id: nameField
                Layout.fillWidth: true
                placeholderText: qsTr("Name *")
                onTextChanged: root.isValidName = text.length >= 2
            }

            TextField {
                id: positionField
                Layout.fillWidth: true
                placeholderText: qsTr("Position *")
                onTextChanged: root.isValidPosition = text.length >= 2
            }

            TextField {
                id: emailField
                Layout.fillWidth: true
                placeholderText: qsTr("Email")
                validator: RegularExpressionValidator {
                    regularExpression: /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/
                }
                onTextChanged: root.isValidEmail = text === "" || acceptableInput
            }

            TextField {
                id: phoneField
                Layout.fillWidth: true
                placeholderText: qsTr("Phone")
                validator: RegularExpressionValidator {
                    regularExpression: /^[\d\s-+()]{10,}$/
                }
                onTextChanged: root.isValidPhone = text === "" || acceptableInput
            }

            ComboBox {
                id: departmentField
                Layout.fillWidth: true
                model: mainApp.get_departments()
                editable: true
                // placeholderText: qsTr("Department")
            }
        }
    }

    // Add Employee Dialog
    Dialog {
        id: addEmployeeDialog
        title: qsTr("Add New Employee")
        standardButtons: Dialog.Save | Dialog.Cancel

        onOpened: {
            baseEmployeeDialog.isEditMode = false
            baseEmployeeDialog.resetFields()
        }
    }

    // Edit Employee Dialog
    Dialog {
        id: editEmployeeDialog
        title: qsTr("Edit Employee")
        standardButtons: Dialog.Save | Dialog.Cancel

        function openWithModel(model) {
            baseEmployeeDialog.isEditMode = true
            baseEmployeeDialog.currentModel = model
            baseEmployeeDialog.resetFields()
            open()
        }
    }

    // Delete Confirmation Dialog
    Dialog {
        id: deleteConfirmDialog
        title: qsTr("Confirm Delete")
        modal: true
        standardButtons: Dialog.Yes | Dialog.No

        property int employeeId: -1
        property string employeeName: ""

        function prompt(id, name) {
            employeeId = id
            employeeName = name
            open()
        }

        Label {
            text: qsTr("Are you sure you want to delete %1?").arg(deleteConfirmDialog.employeeName)
            wrapMode: Text.WordWrap
        }

        onAccepted: {
            mainApp.delete_employee(employeeId)
        }
    }
}
