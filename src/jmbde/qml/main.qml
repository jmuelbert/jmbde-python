import QtQuick 6.2
import QtQuick.Controls 6.2

ApplicationWindow {
    visible: true
    width: 600
    height: 400
    title: "Employee Manager"

    Column {
        spacing: 10
        anchors.fill: parent
        anchors.margins: 20

        // Header
        Text {
            text: "Employee Management"
            font.pixelSize: 24
            font.bold: true
            anchors.horizontalCenter: parent.horizontalCenter
        }

        // Input Row
        Row {
            spacing: 10
            TextField {
                id: nameField
                placeholderText: "Name"
                width: 150
            }
            TextField {
                id: positionField
                placeholderText: "Position"
                width: 150
            }
            Button {
                text: "Add Employee"
                onClicked: {
                    mainApp.add_employee(nameField.text, positionField.text);
                    nameField.text = "";
                    positionField.text = "";
                }
            }
        }

        // Employee List
        ListView {
            id: employeeList
            model: employeeModel
            width: parent.width
            height: 250
            delegate: Rectangle {
                width: parent.width
                height: 50
                color: index % 2 === 0 ? "#f0f0f0" : "#ffffff"
                border.color: "#cccccc"
                Row {
                    spacing: 10
                    anchors.verticalCenter: parent.verticalCenter
                    Text {
                        text: "ID: " + model.id
                        width: 50
                    }
                    Text {
                        text: "Name: " + model.name
                        width: 150
                    }
                    Text {
                        text: "Position: " + model.position
                        width: 150
                    }
                    Button {
                        text: "Edit"
                        onClicked: {
                            nameField.text = model.name;
                            positionField.text = model.position;
                            mainApp.update_employee(model.id, nameField.text, positionField.text);
                            employeeModel.refresh();
                        }
                    }
                    Button {
                        text: "Delete"
                        onClicked: {
                            mainApp.delete_employee(model.id);
                        }
                    }
                }
            }
        }
    }
}
