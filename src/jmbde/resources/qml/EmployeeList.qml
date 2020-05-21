import QtQuick 2.6
import QtQuick.Controls 2.2

Rectangle {
    anchors.fill: parent
    color: "lightgrey"

    ListView {
        id: listExample
        anchors.fill: parent
        model: EmployeeModel
        delegate:
            Item {
            width: 200
            height: 60
            Row {
                Text {
                    width: 60
                    text:  name + " " + age
                    horizontalAlignment: Text.AlignHCenter
                    anchors.verticalCenter: parent.verticalCenter
                }
                Button{
                    width: 20
                    text: "+"
                    onClicked: EmployeeModel.editPerson(index, name, age+1)
                }
                Button{
                    width: 20
                    text: "-"
                    onClicked: EmployeeModel.editPerson(index, name, age-1)
                }
                Button{
                    width: 20
                    text: "X"
                    onClicked: EmployeeModel.deletePerson(index)
                }
            }
        }
    }

    Button {
        width: 50
        height: 25
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        text: "add"
        onClicked: {
            console.log("qml adding")
            EmployeeModel.addPerson("luis", 22)
        }
    }
}
