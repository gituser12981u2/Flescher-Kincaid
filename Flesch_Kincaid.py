import textstat

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel, QComboBox
from PyQt5.QtGui import QTextCursor, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Readability Analyzer")
        self.setFixedSize(self.screen().size() * 0.7)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(50, 50, 50, 50)
        self.central_widget.setLayout(self.layout)

        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont('Arial', 14))
        self.layout.addWidget(self.text_edit)

        # Dropdown box for readibility assessers
        self.combo_box = QComboBox()
        self.combo_box.addItems(
            ["Flesch-Kincaid", "Gunning Fog index", "SMOG", "Coleman-Liau Index", "ARI"])
        self.combo_box.setFont(QFont('Arial', 14))
        self.combo_box.currentIndexChanged.connect(self.combo_box_changed)
        self.layout.addWidget(self.combo_box)

        # Descriptions
        self.index_description_label = QLabel()
        self.index_description_label.setStyleSheet(
            "QLabel { font-size: 14px; margin-top: 20px; }")
        self.layout.addWidget(self.index_description_label)

        # set the initial description based on the default index
        default_index = self.combo_box.itemText(0)
        self.index_description_label.setText(
            get_index_description(default_index))

        self.calc_button = QPushButton("Calculate scores")
        self.calc_button.setStyleSheet(
            "QPushButton { background-color: #007BFF; color: white; border-radius: 10px; padding: 10px; font-size: 16px; }")
        self.calc_button.clicked.connect(self.display_scores)
        self.layout.addWidget(self.calc_button)

        self.result_label = QLabel()
        self.result_label.setStyleSheet(
            "QLabel { font-size: 20px; margin-top: 15px; }")
        self.layout.addWidget(self.result_label)

    def combo_box_changed(self, index):
        index_name = self.combo_box.itemText(index)
        index_description = get_index_description(index_name)
        self.index_description_label.setText(index_description)

    def display_scores(self):
        text = self.text_edit.toPlainText()
        index = self.combo_box.currentText()
        scores = calculate_scores(text, index)
        result_text = ""
        for key, value in scores.items():
            result_text += f"{key}: {value}\n"
        self.result_label.setText(result_text.strip())


def calculate_scores(text, index):
    scores = {}

    if index == "Flesch-Kincaid":
        # type: ignore
        scores["Flesch-Kincaid Grade Level"] = textstat.flesch_kincaid_grade(  # type: ignore
            text)
        scores["Flesch Reading Ease"] = textstat.flesch_reading_ease(  # type: ignore
            text)
    elif index == "Gunning Fog index":
        scores["Gunning Fog Index"] = textstat.gunning_fog(  # type: ignore
            text)
    elif index == "SMOG":
        scores["SMOG Index"] = textstat.smog_index(text)  # type: ignore
    elif index == "Coleman-Liau Index":
        # type: ignore
        scores["Coleman-Liau Index"] = textstat.coleman_liau_index(text)
    elif index == "ARI":
        scores["ARI"] = textstat.automated_readability_index(  # type: ignore
            text)

    return scores


def get_index_description(index_name):
    descriptions = {
        "Flesch-Kincaid": "Flesch-Kincaid is a readability index that measures the grade level required to understand the text.",
        "Gunning Fog index": "Gunning Fog index estimates the years of formal education required to understand the text.",
        "SMOG": "SMOG is a grade formula that measures the reading level based on the number of complex words in the text.",
        "Coleman-Liau Index": "Coleman-Liau Index calculates the grade level based on characters per word and words per sentence.",
        "ARI": "ARI (Automated Readability Index) provides the grade level required to understand the text."
    }

    return descriptions.get(index_name, "Description not available.")


# Only run the front-end code if the file is executed directly
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
