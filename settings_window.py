from PyQt5.QtWidgets import QDialog, QTabWidget, QVBoxLayout, QWidget, QLabel, QFontComboBox, QCheckBox, QStyledItemDelegate, QStyleOptionViewItem
from PyQt5.QtCore import Qt


class SettingsWindow(QDialog):
    def __init__(self, settings, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.settings = settings

        self.setWindowTitle("Settings")
        if parent is not None:
            self.resize(int(parent.width() * 0.9), int(parent.height() * 0.9))

        self.tab_widget = QTabWidget()

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
        self.font_combo_box.setItemDelegate(FontSizeDelegate())
        self.font_combo_box.setMinimumHeight(30)
        self.font_combo_box.setStyleSheet("QFontComboBox { font-size: 14px; }")
        self.font_combo_box.currentFontChanged.connect(
            self.settings.change_font)
        layout.addWidget(self.font_combo_box)

        self.font_checkbox = QCheckBox("Apply font to entire application")
        self.font_checkbox.setChecked(
            self.settings.settings['change_application_font'])
        self.font_checkbox.stateChanged.connect(
            self.settings.toggle_application_font)
        layout.addWidget(self.font_checkbox)

    def toggle_application_font(self, state):
        self.settings.settings['change_application_font'] = state == Qt.Checked
        if state == Qt.Checked:  # type: ignore
            self.settings.settings['change_application_font'] = True
        else:
            self.settings.reset_font()


class FontSizeDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.font.setPointSize(12)  # set the font size for the items
