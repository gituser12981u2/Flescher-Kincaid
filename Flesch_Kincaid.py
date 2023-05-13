import textstat
import spacy

import tkinter as tk
from tkinter import messagebox

# load spacy as nlp
nlp = spacy.load('en_core_web_sm')


def calculate_flesch_scores(text):

    fk_grade_level = textstat.flesch_kincaid_grade(text)  # type: ignore
    fre_score = textstat.flesch_reading_ease(text)  # type: ignore

    return fk_grade_level, fre_score


# Only run the front-end code if the file is executed directly
if __name__ == '__main__':
    import tkinter as tk
    from tkinter import messagebox

    def display_scores():
        # get text from text entry widget
        text = text_entry.get("1.0", "end-1c")
        fk_grade, fre_score = calculate_flesch_scores(text)
        messagebox.showinfo(
            "Scores", f"Flesch-Kincaid Grade Level: {fk_grade}\nFlesch Reading Ease: {fre_score}")

    root = tk.Tk()

    # text entry widget
    text_entry = tk.Text(root, height=10, width=50)
    text_entry.pack()

    # button to calculate scores
    calc_button = tk.Button(
        root, text="Calculate scores", command=display_scores)
    calc_button.pack()

    root.mainloop()
