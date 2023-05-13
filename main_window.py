from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel, QComboBox
from PyQt5.QtGui import QFont, QScreen
from PyQt5.QtCore import Qt
from settings import SettingsMenu
from readability_index import READABILITY_INDICES


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Readability Analyzer")
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        self.resize(int(screen.width() * 0.7),
                    int(screen.height() * 0.7))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()  # type: ignore
        self.layout.setContentsMargins(50, 50, 50, 50)
        self.central_widget.setLayout(self.layout)

        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont('Verdana', 16))
        self.text_edit.setStyleSheet("QTextEdit { border: 1px solid #888; }")
        self.layout.addWidget(self.text_edit)

        self.combo_box = QComboBox()
        self.combo_box.setFont(QFont('Verdana', 16))
        self.combo_box.setStyleSheet("QComboBox { border: 1px solid #888; }")
        self.combo_box.currentIndexChanged.connect(self.combo_box_changed)
        self.layout.addWidget(self.combo_box)

        self.index_description_label = QLabel()
        self.index_description_label.setStyleSheet(
            "QLabel { font-size: 18px; margin-top: 20px; }")
        self.layout.addWidget(self.index_description_label)

        self.calc_button = QPushButton("Calculate scores")
        self.calc_button.setStyleSheet(
            "QPushButton { background-color: #007BFF; color: white; border-radius: 10px; padding: 15px; font-size: 20px; }"
            "QPushButton:hover { background-color: #0056b3; }"
            "QPushButton:pressed { background-color: #003d80; }"
        )
        self.calc_button.clicked.connect(self.display_scores)
        self.layout.addWidget(self.calc_button)

        self.result_label = QLabel()
        self.result_label.setStyleSheet(
            "QLabel { font-size: 22px; margin-top: 15px; }")
        self.layout.addWidget(self.result_label)

        self.settings_menu = SettingsMenu(self)
        self.menuBar().addMenu(self.settings_menu)

        self.populate_combo_box()

    def populate_combo_box(self):
        for index in READABILITY_INDICES:
            self.combo_box.addItem(index.name)
        self.index_description_label.setText(
            READABILITY_INDICES[0].description)

    def combo_box_changed(self, index):
        self.index_description_label.setText(
            READABILITY_INDICES[index].description)

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


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
