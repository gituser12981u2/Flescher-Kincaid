from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QVBoxLayout, QWidget, QTextEdit, QLabel, QComboBox, QSizePolicy,
                             QAction, QDesktopWidget)
from PyQt5.QtGui import QFont, QScreen, QIcon
from PyQt5.QtCore import Qt, QPoint

from .settings.settings_window import SettingsWindow
from .settings.settings_manager import SettingsManager
from .settings.settings_menu import SettingsMenu
from .readability_index import READABILITY_INDICES


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.menuBar().addMenu(self.settings_menu)

        self.init_ui()
        self.create_toolbar()
        self.init_settings()
        self.populate_combo_box()

    def init_ui(self):
        self.setWindowTitle("Readability Analyzer")
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        self.resize(int(screen.width() * 0.7),
                    int(screen.height() * 0.7))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()  # type: ignore
        self.layout.setContentsMargins(50, 50, 50, 0)
        self.central_widget.setLayout(self.layout)

        self.create_text_edit()
        self.create_combo_box()
        self.create_index_description_label()
        self.create_calc_button()
        self.create_result_label()

    def create_text_edit(self):
        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont('Verdana', 16))
        self.text_edit.setStyleSheet("QTextEdit { border: 1px solid #888; }")
        self.layout.addWidget(self.text_edit)

    def create_combo_box(self):
        self.combo_box = QComboBox()
        self.combo_box.setFont(QFont('Verdana', 16))
        self.combo_box.setStyleSheet("QComboBox { border: 1px solid #888; }")
        self.combo_box.currentIndexChanged.connect(self.combo_box_changed)
        self.layout.addWidget(self.combo_box)

    def create_index_description_label(self):
        self.index_description_label = QLabel()
        self.index_description_label.setStyleSheet(
            "QLabel { font-size: 18px; margin-top: 20px; }")
        self.layout.addWidget(self.index_description_label)

    def create_calc_button(self):
        self.calc_button = QPushButton("Calculate scores")
        self.calc_button.setStyleSheet(
            "QPushButton { background-color: #007BFF; color: white; border-radius: 10px; padding: 15px; font-size: 20px; }"
            "QPushButton:hover { background-color: #0056b3; }"
            "QPushButton:pressed { background-color: #003d80; }"
        )
        self.calc_button.clicked.connect(self.display_scores)
        self.layout.addWidget(self.calc_button)

    def create_result_label(self):
        self.result_label = QLabel()
        self.result_label.setStyleSheet(
            "QLabel { font-size: 22px; margin-top: 15px; }")
        self.layout.addWidget(self.result_label)

    def create_toolbar(self):
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.setStyleSheet('QToolBar{spacing:10px;}')

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer)

        self.settings_action = QAction(
            QIcon('src/icons/settingsCog.png'), '', self)
        self.settings_action.triggered.connect(self.open_settings)
        self.toolbar.addAction(self.settings_action)
        self.toolbar.setToolButtonStyle(
            Qt.ToolButtonTextBesideIcon)  # type: ignore
        self.toolbar.setMovable(False)  # Prevent moving the toolbar

    def init_settings(self):
        self.settings_manager = SettingsManager(self)
        self.settings_manager.theme_manager.load_stylesheet()
        self.settings_window = SettingsWindow(self.settings_manager, self)
        self.settings_menu = SettingsMenu(
            self.settings_manager, self.settings_window)

    def open_settings(self):
        button = self.toolbar.widgetForAction(self.settings_action)
        point = button.mapToGlobal(QPoint(0, button.height()))
        self.settings_menu.exec_(point)

    def populate_combo_box(self):
        for index in READABILITY_INDICES:
            self.combo_box.addItem(index.name)
        self.index_description_label.setText(
            READABILITY_INDICES[0].description)

    def combo_box_changed(self, index):
        self.index_description_label.setText(
            READABILITY_INDICES[index].description)

    def show_settings_window(self):
        self.settings_window = SettingsWindow(self.settings_manager, self)
        self.settings_window.setModal(True)

        # Center the window
        qr = self.settings_window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.settings_window.move(qr.topLeft())

        self.settings_window.show()

    def display_scores(self):
        text = self.text_edit.toPlainText().strip()
        if not text:
            self.result_label.setText("Please input some text.")
            return

        index = READABILITY_INDICES[self.combo_box.currentIndex()]

        if index.name == "SMOG" and len(text.split('.')) < 3:
            self.result_label.setText(
                "SMOG analysis requires at least 3 sentences. Please provide more text.")
            return

        score = index.calculation_function(text)
        result_text = f"{index.name} Score: {score:.2f}"

        if index.additional_function:
            additional_score = index.additional_function(text)
            result_text += f"\nAdditional Score (e.g., Reading Ease for Flesch-Kincaid): {additional_score:.2f}"

        self.result_label.setText(result_text)
