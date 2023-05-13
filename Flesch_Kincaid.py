import textstat

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel, QComboBox, QAction
from PyQt5.QtGui import QFont, QScreen
from PyQt5.QtCore import Qt


class ReadabilityIndex:
    def __init__(self, name, description, calculation_function, additional_function=None):
        self.name = name
        self.description = description
        self.calculation_function = calculation_function
        self.additional_function = additional_function


READABILITY_INDICES = [
    ReadabilityIndex("Flesch-Kincaid",
                     "Flesch-Kincaid is a readability index that measures the grade level required to understand the text.",
                     textstat.flesch_kincaid_grade,  # type: ignore
                     textstat.flesch_reading_ease),  # type: ignore
    ReadabilityIndex("Gunning Fog index",
                     "Gunning Fog index estimates the years of formal education required to understand the text.",
                     textstat.gunning_fog),   # type: ignore
    ReadabilityIndex("SMOG",
                     "SMOG is a grade formula that measures the reading level based on the number of complex words in the text.",
                     textstat.smog_index),  # type: ignore
    ReadabilityIndex("Coleman-Liau Index",
                     "Coleman-Liau Index calculates the grade level based on characters per word and words per sentence.",
                     textstat.coleman_liau_index),  # type: ignore
    ReadabilityIndex("ARI",
                     "ARI (Automated Readability Index) provides the grade level required to understand the text.",
                     textstat.automated_readability_index)  # type: ignore
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Readability Analyzer")
        self.setStyleSheet("background-color: #fafafa;")
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        self.setFixedSize(int(screen.width() * 0.7),
                          int(screen.height() * 0.7))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(50, 50, 50, 50)
        self.central_widget.setLayout(self.layout)

        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont('Verdana', 16))
        self.layout.addWidget(self.text_edit)

        self.combo_box = QComboBox()
        self.combo_box.setFont(QFont('Verdana', 16))
        self.combo_box.currentIndexChanged.connect(self.combo_box_changed)
        self.layout.addWidget(self.combo_box)

        self.index_description_label = QLabel()
        self.index_description_label.setStyleSheet(
            "QLabel { font-size: 18px; margin-top: 20px; }")
        self.layout.addWidget(self.index_description_label)

        self.calc_button = QPushButton("Calculate scores")
        self.calc_button.setStyleSheet(
            "QPushButton { background-color: #007BFF; color: white; border-radius: 10px; padding: 15px; font-size: 20px; }")
        self.calc_button.clicked.connect(self.display_scores)
        self.layout.addWidget(self.calc_button)

        self.result_label = QLabel()
        self.result_label.setStyleSheet(
            "QLabel { font-size: 22px; margin-top: 15px; }")
        self.layout.addWidget(self.result_label)

        self.create_menu()

        self.populate_combo_box()

    def create_menu(self):
        self.menuBar = self.menuBar()
        self.settingsMenu = self.menuBar.addMenu('Settings')

        self.toggleModeAction = QAction('Toggle light/dark mode', self)
        self.toggleModeAction.triggered.connect(self.toggle_mode)
        self.settingsMenu.addAction(self.toggleModeAction)

        self.changeLanguageAction = QAction('Change language', self)
        self.changeLanguageAction.triggered.connect(self.change_language)
        self.settingsMenu.addAction(self.changeLanguageAction)

        self.changeFontAction = QAction('Change font', self)
        self.changeFontAction.triggered.connect(self.change_font)
        self.settingsMenu.addAction(self.changeFontAction)

    def toggle_mode(self):
        pass  # Implement this method

    def change_language(self):
        pass  # Implement this method

    def change_font(self):
        pass  # Implement this method

    def populate_combo_box(self):
        for index in READABILITY_INDICES:
            self.combo_box.addItem(index.name)
        self.index_description_label.setText(
            READABILITY_INDICES[0].description)

    def combo_box_changed(self, index):
        self.index_description_label.setText(
            READABILITY_INDICES[index].description)

    def display_scores(self):
        text = self.text_edit.toPlainText()
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
