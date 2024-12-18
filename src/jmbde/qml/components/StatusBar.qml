// SPDX-FileCopyrightText: Jürgen Mülbert
// SPDX-License-Identifier: GPL-3.0-or-later

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    id: statusBar

    // Properties
    property string message: ""
    property bool loading: false
    property var statistics: ({})
    property bool error: false
    property int messageTimeout: 5000

    // Styling
    height: 32
    color: Material.theme === Material.Dark ? Qt.darker(Material.background, 1.1) : Qt.lighter(Material.background, 1.1)
    border.color: Material.dividerColor
    border.width: 1

    // Message timer
    Timer {
        id: messageTimer
        interval: statusBar.messageTimeout
        onTriggered: statusBar.message = ""
    }

    // Layout
    RowLayout {
        anchors {
            fill: parent
            leftMargin: 8
            rightMargin: 8
        }
        spacing: 12

        // Status message
        Label {
            id: messageLabel
            text: statusBar.message
            color: statusBar.error ? Material.color(Material.Red) : Material.foreground
            elide: Text.ElideRight
            Layout.fillWidth: true
            font.pointSize: settings.getValue("ui.font_size") - 1

            Behavior on color {
                ColorAnimation { duration: 200 }
            }
        }

        // Loading indicator
        BusyIndicator {
            id: busyIndicator
            visible: statusBar.loading
            running: visible
            Layout.preferredHeight: parent.height - 8
            Layout.preferredWidth: height
        }

        // Vertical divider
        Rectangle {
            visible: statisticsLayout.visible
            color: Material.dividerColor
            width: 1
            Layout.fillHeight: true
            Layout.margins: 4
        }

        // Statistics
        RowLayout {
            id: statisticsLayout
            spacing: 16
            visible: statusBar.statistics && Object.keys(statusBar.statistics).length > 0

            Repeater {
                model: statusBar.statistics ? Object.keys(statusBar.statistics) : []

                delegate: Label {
                    text: {
                        const key = modelData
                        const value = statusBar.statistics[key]
                        return `${key}: ${value}`
                    }
                    font.pointSize: settings.getValue("ui.font_size") - 1
                    opacity: 0.8
                }
            }
        }

        // Memory usage (optional, for debugging)
        Label {
            visible: settings.getValue("ui.debug_mode")
            text: {
                const memory = mainApp.get_memory_usage()
                return `Memory: ${(memory / 1024 / 1024).toFixed(1)} MB`
            }
            font.pointSize: settings.getValue("ui.font_size") - 1
            opacity: 0.7
        }
    }

    // Public methods
    function showMessage(msg, isError = false, timeout = messageTimeout) {
        message = msg
        error = isError
        if (timeout > 0) {
            messageTimer.interval = timeout
            messageTimer.restart()
        }
    }

    function clearMessage() {
        message = ""
        error = false
        messageTimer.stop()
    }

    function setLoading(isLoading) {
        loading = isLoading
    }

    function updateStatistics(stats) {
        statistics = stats
    }

    // Mouse area for potential interaction
    MouseArea {
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: true

        // Optional tooltip showing full message if truncated
        ToolTip {
            visible: mouseArea.containsMouse && messageLabel.truncated
            text: statusBar.message
            delay: 1000
        }
    }

    // Optional right-click menu
    Menu {
        id: contextMenu

        MenuItem {
            text: qsTr("Copy Message")
            enabled: statusBar.message !== ""
            onTriggered: {
                clipboard.setText(statusBar.message)
                showMessage(qsTr("Message copied to clipboard"), false, 2000)
            }
        }

        MenuItem {
            text: qsTr("Clear Message")
            enabled: statusBar.message !== ""
            onTriggered: clearMessage()
        }

        MenuSeparator {}

        MenuItem {
            text: qsTr("Refresh Statistics")
            onTriggered: {
                const stats = mainApp.get_statistics()
                updateStatistics(stats)
            }
        }
    }

    // Right-click handling
    MouseArea {
        anchors.fill: parent
        acceptedButtons: Qt.RightButton
        onClicked: contextMenu.popup()
    }
