import datetime
import darkdetect
from PyQt5.QtWidgets import qApp

class ThemeManager:
    def __init__(self, user_settings):
        self.user_settings = user_settings
        self.toggle_mode()
    
    def get_time_based_mode(self):
        now = datetime.datetime.now()
        if now.hour >= 6 and now.hour < 18:
            return 'light'
        else:
            return 'dark'
        
    def toggle_mode(self):
        self.user_settings.settings['mode'] = 'dark' if self.user_settings.settings['mode'] == 'light' else 'light'
        self.user_settings.save_settings()
        self.load_stylesheet()

        
    def load_stylesheet(self):
        if self.user_settings.settings['mode'] == 'light':
            with open('src/styles/light.qss', 'r') as f:
                stylesheet = f.read()
        else:
            with open('src/styles/dark.qss', 'r') as f:
                stylesheet = f.read()
        qApp.setStyleSheet(stylesheet)
    

    # add somewhere else later
    def change_language(self, language):
        self.user_settings.settings['language'] = language
        self.user_settings.save_settings()