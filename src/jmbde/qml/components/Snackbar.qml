// SPDX-FileCopyrightText: Jürgen Mülbert
// SPDX-License-Identifier: GPL-3.0-or-later

import QtQuick
import QtQuick.Controls

Rectangle {
    id: root

    property int timeout: 2000
    property string backgroundColor: Material.accent
    property string textColor: "white"

    function show(message) {
        messageText.text = message
        animation.restart()
    }

    anchors.horizontalCenter: parent.horizontalCenter
    anchors.bottom: parent.bottom
    anchors.margins: 20
    height: 40
    radius: 4
    color: backgroundColor
    opacity: 0

    Label {
        id: messageText
        anchors.centerIn: parent
        color: root.textColor
        font.pixelSize: 14
    }

    SequentialAnimation {
        id: animation

        NumberAnimation {
            target: root
            property: "opacity"
            to: 1
            duration: 300
        }
        PauseAnimation {
            duration: root.timeout
        }
        NumberAnimation {
            target: root
            property: "opacity"
            to: 0
            duration: 300
        }
    }
}
