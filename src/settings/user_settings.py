import json
import os
import darkdetect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import qApp


class UserSettings:
    def __init__(self, parent, settings_file='settings.json'):
        self.parent = parent
        self.settings_file = settings_file
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as file:
                self.settings = json.load(file)
            if 'change_application_font' not in self.settings:
                self.settings['change_application_font'] = False
        else:
            self.settings = {
                'mode': 'dark' if darkdetect.isDark() else 'light',
                'language': 'en',
                'font': QFont().toString(),
                'change_application_font': False,
            }
            self.save_settings()
            self.load_settings()
        self.load_stylesheet()

    def toggle_application_font(self):
        self.settings['change_application_font'] = not self.settings['change_application_font']
        self.save_settings()
        if self.settings['change_application_font']:
            self.change_application_font()
        else:
            self.reset_application_font()

    def toggle_mode(self):
        self.settings['mode'] = 'dark' if self.settings['mode'] == 'light' else 'light'
        self.save_settings()
        self.load_stylesheet()

    def change_language(self, language):
        self.settings['language'] = language
        self.save_settings()

    def change_font(self, font):
        current_font = QFont()
        current_font.fromString(self.settings['font'])
        font.setPointSize(current_font.pointSize())

        self.settings['font'] = font.toString()
        self.save_settings()
        self.apply_font()

    def apply_font(self):
        font = QFont()
        font.fromString(self.settings['font'])
        qApp.setFont(font)
        if self.settings['change_application_font']:
            qApp.setFont(font)
        else:
            self.parent.text_edit.setFont(font)

    def change_application_font(self):
        font = QFont()
        font.fromString(self.settings['font'])
        qApp.setFont(font)

    def reset_application_font(self):
        qApp.setFont(QFont())

    def reset_font(self):
        default_font = QFont()
        self.settings['font'] = default_font.toString()
        self.save_settings()
        self.apply_font()

    def save_settings(self):
        with open(self.settings_file, 'w') as file:
            json.dump(self.settings, file)

    def load_stylesheet(self):
        if self.settings['mode'] == 'light':
            with open('src/styles/light.qss', 'r') as f:
                stylesheet = f.read()
        else:
            with open('src/styles/dark.qss', 'r') as f:
                stylesheet = f.read()
        qApp.setStyleSheet(stylesheet)

    def load_settings(self):
        self.apply_font()
