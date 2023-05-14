from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import qApp


class FontManager:
    def __init__(self, parent, user_settings):
        self.parent = parent
        self.user_settings = user_settings
        self.load_font()
        
    def load_font(self):
        font = QFont()
        font.fromString(self.user_settings.get_settings()['font'])
        self.font = font
        
    def apply_font(self):
        if self.user_settings.settings['change_application_font']:
            qApp.setFont(self.font)
        else:
            self.parent.text_edit.setFont(self.font)
            
    def change_font(self, font):
        current_font = QFont()
        current_font.fromString(self.user_settings.settings['font'])
        
        print(f"Old font size: {current_font.pointSize()}")  # Debugging line
    
        font.setPointSize(current_font.pointSize())  # Preserving old font size
        
        print(f"New font size: {font.pointSize()}")  # Debugging line

        self.user_settings.settings['font'] = font.toString()
        self.user_settings.save_settings()
        self.load_font()
        self.apply_font()