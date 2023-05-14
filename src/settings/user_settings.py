import json
import os
import darkdetect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import qApp


class UserSettings:
    def __init__(self, parent, settings_file='settings.json'):
        self.parent = parent
        self.settings_file = settings_file
        self.settings = self.load_settings()
        self.toggle_mode()
        
    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as file:
                settings = json.load(file)
        else:
            settings = self.default_settings()
            self.save_settings()
        font = QFont()
        font.fromString(settings['font'])
        font.setPointSize(16)  # Set the desired font size
        settings['font'] = font.toString()
        return settings
        
    def save_settings(self):
        with open(self.settings_file, 'w') as file:
            json.dump(self.settings, file)      
    
    def default_settings(self):
        return {
            'font': 'Arial',
            'change_application_font': False,
            'mode': 'dark' if darkdetect.isLight() else 'light',
        }

    def get_settings(self):
        return self.settings
    
    def update_settings(self, new_settings):
        self.settings.update(new_settings)
        self.save_settings()
                    
    def toggle_application_font(self):
        self.settings['change_application_font'] = not self.settings['change_application_font']
        self.save_settings()

    def toggle_mode(self):
        self.settings['mode'] = 'dark' if self.settings['mode'] == 'light' else 'light'
        self.save_settings()
        self.load_stylesheet()

    def change_language(self, language):
        self.settings['language'] = language
        self.save_settings()
        
    def load_stylesheet(self):
        if self.settings['mode'] == 'light':
            with open('src/styles/light.qss', 'r') as f:
                stylesheet = f.read()
        else:
            with open('src/styles/dark.qss', 'r') as f:
                stylesheet = f.read()
        qApp.setStyleSheet(stylesheet)


