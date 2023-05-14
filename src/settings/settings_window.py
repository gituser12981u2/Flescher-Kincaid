from PyQt5.QtWidgets import (QDialog, QTabWidget, QVBoxLayout, QWidget, QLabel, 
                             QFontComboBox, QCheckBox, QStyledItemDelegate)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class SettingsWindow(QDialog):
    def __init__(self, settings_manager, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.settings_manager = settings_manager

        self.setWindowTitle("Settings")
        if parent is not None:
            self.resize(int(parent.width() * 0.9), int(parent.height() * 0.9))

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

    def setup_appearance_tab(self):
        layout = QVBoxLayout(self.appearance_tab)

        layout.addWidget(QLabel("Font:"))

        self.font_combo_box = QFontComboBox()
        self.font_combo_box.setCurrentFont(QFont(self.settings_manager.user_settings.settings['font']))
        self.font_combo_box.setMinimumHeight(50)
        self.font_combo_box.setMinimumWidth(300)
        self.font_combo_box.currentFontChanged.connect(self.settings_manager.font_manager.change_font)
        layout.addWidget(self.font_combo_box)

        self.font_checkbox = QCheckBox("Apply font to entire application")
        self.font_checkbox.setChecked(
            self.settings_manager.user_settings.settings['change_application_font'])
        self.font_checkbox.stateChanged.connect(
            self.settings_manager.user_settings.toggle_application_font)
        layout.addWidget(self.font_checkbox)
