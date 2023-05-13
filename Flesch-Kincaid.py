import textstat
import spacy

import tkinter as tk
from tkinter import messagebox

# load spacy as nlp
nlp = spacy.load('en_core_web_sm')


def calculate_flesch_scores(text):

    fk_grade_level = textstat.flesch_reading_ease(text)
    fre_score = textstat.flesch_reading_ease(text)

    return fk_grade_level, fre_score


def display_scores():
    text = text_entry.get("1.0", "end-1c")  # get text from text entry widget
    fk_grade, fre_score = calculate_flesch_scores(text)
    messagebox.showinfo(
        "Scores", f"Flesch-Kincaid Grade Level: {fk_grade}\nFlesch Reading Ease: {fre_score}")


root = tk.Tk()

# text entry widget
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

# button to calculate scores
calc_button = tk.Button(root, text="Calculate scores", command=display_scores)
calc_button.pack()

root.mainloop()
