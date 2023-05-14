from PyQt5.QtWidgets import (QDialog, QTabWidget, QVBoxLayout, QWidget, QLabel,
                             QFontComboBox, QCheckBox, QMainWindow, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class SettingsWindow(QDialog):
    def __init__(self, settings_manager, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.settings_manager = settings_manager

        # Check if parent is of correct type
        if not isinstance(parent, (QMainWindow, QWidget)):
            raise TypeError(
                f"Expected parent of type QMainWindow or QWidget, got {type(parent)}")

        self.setWindowTitle("Settings")
        if parent is not None:
            self.resize(int(parent.width() * 0.75),
                        int(parent.height() * 0.75))

        self.tab_widget = QTabWidget()
        self.tab_widget.setMinimumWidth(400)

        self.appearance_tab = QWidget()
        self.setup_appearance_tab()

        self.language_tab = QWidget()
        # Set up language tab...

        self.tab_widget.addTab(self.appearance_tab, "Appearance")
        self.tab_widget.addTab(self.language_tab, "Language")

        self.layout = QVBoxLayout()  # type: ignore
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)
        self.center()

    def showEvent(self, event):
        super(SettingsWindow, self).showEvent(event)
        self.center()

    def center(self):
        main_window_geometry = self.parent().frameGeometry()
        center_point = main_window_geometry.center()

        # Move the dialog to the center
        self.move(int(center_point.x() - self.width() / 2),
                  int(center_point.y() - self.height() / 2))

    def setup_appearance_tab(self):
        layout = QVBoxLayout(self.appearance_tab)

        layout.addWidget(QLabel("Font:"))

        self.font_combo_box = QFontComboBox()
        self.font_combo_box.setCurrentFont(
            QFont(self.settings_manager.user_settings.settings['font']))
        self.font_combo_box.setMinimumHeight(50)
        self.font_combo_box.setMinimumWidth(300)
        self.font_combo_box.currentFontChanged.connect(
            self.settings_manager.font_manager.change_font)
        layout.addWidget(self.font_combo_box)

        self.font_checkbox = QCheckBox("Apply font to entire application")
        self.font_checkbox.setChecked(
            self.settings_manager.user_settings.settings['change_application_font'])
        self.font_checkbox.stateChanged.connect(
            self.settings_manager.user_settings.toggle_application_font)
        layout.addWidget(self.font_checkbox)

        # Add day/night auto checkbox
        self.day_night_auto_checkbox = QCheckBox(
            "Auto toggle light/dark mode based on time")
        self.day_night_auto_checkbox.setChecked(
            self.settings_manager.user_settings.settings.get('day/night auto', False))
        self.day_night_auto_checkbox.stateChanged.connect(
            self.toggle_day_night_auto)
        layout.addWidget(self.day_night_auto_checkbox)

    def toggle_day_night_auto(self, checked):
        self.settings_manager.user_settings.settings['day/night auto'] = bool(
            checked)
        if bool(checked):
            self.settings_manager.user_settings.settings['mode'] = self.settings_manager.theme_manager.get_sunrise_sunset_based_mode(
            )
        self.settings_manager.user_settings.save_settings()
        self.settings_manager.theme_manager.load_stylesheet()

        # Show warning message box when the checkbox is checked
        if checked:
            msgBox = QMessageBox()
            msgBox.setText(
                "Day/Night auto mode is enabled. The theme will be controlled based on the time of day "
                "after application restart. Please note that your manual theme changes will not be saved "
                "when this mode is enabled.")
            msgBox.exec_()
