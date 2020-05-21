import QtQuick 2.9
import QtQuick.Window 2.3
import QtQuick.Controls 2.2
import QtQuick.Controls.Material 2.2
import QtQuick.Layouts 1.3
import Qt.labs.settings 1.0
import QtQuick.Dialogs 1.1
import QtQml 2.2

ApplicationWindow {
    id: mainWindow
    objectName: "mainWindow"
    visible: true
    width: 640
    height: 480

    Material.theme: setting.theme
    Material.accent: setting.accent
    Material.primary: setting.primary

}
