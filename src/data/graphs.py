import matplotlib.pyplot as plt
import numpy as np


def prepare_data():
    # Algorithms
    algorithms = [
        "Flescher-Kincaid",
        "Flescher-Kincaid(NLP entity count)",
        "Experimental"
    ]

    # Works
    works = ["TTTC Intro", "Ulysses 'Proteus'"]

    # Scores
    scores = [
        [(12.6, 52.73), (2.0, 96.38)],  # Flescher-Kincaid
        [(12.81, 50.63), (2.1, 95.38)],  # Flescher-Kincaid(NLP entity count)
        [(15.6, 27), (17.8, 13)]  # Experimental
    ]

    # Split scores into separate lists for easier plotting
    grade_level_scores = [[score[0] for score in algorithm_scores]
                          for algorithm_scores in scores]
    reading_ease_scores = [[score[1] for score in algorithm_scores]
                           for algorithm_scores in scores]

    return algorithms, works, grade_level_scores, reading_ease_scores


def add_value_labels(ax, spacing=5):
    for rect in ax.patches:
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2
        space = spacing
        va = 'bottom'

        if y_value < 0:
            space *= -1
            va = 'top'

        label = "{:.2f}".format(y_value)
        ax.annotate(label, (x_value, y_value),
                    xytext=(0, space),
                    textcoords="offset points",
                    ha='center', va=va)


def plot_graphs(algorithms, works, grade_level_scores, reading_ease_scores):
    bar_width = 0.25
    r1 = np.arange(len(grade_level_scores[0]))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]

    fig, axs = plt.subplots(2, figsize=(10, 12))

    axs[0].bar(r1, grade_level_scores[0], color='b',
               width=bar_width, edgecolor='grey', label=algorithms[0])
    axs[0].bar(r2, grade_level_scores[1], color='r',
               width=bar_width, edgecolor='grey', label=algorithms[1])
    axs[0].bar(r3, grade_level_scores[2], color='g',
               width=bar_width, edgecolor='grey', label=algorithms[2])
    axs[0].set_xlabel('Works', fontweight='bold')
    axs[0].set_ylabel('Flesch-Kincaid Grade Level', fontweight='bold')
    axs[0].set_title(
        'Comparison of Flesch-Kincaid Grade Level by Algorithm and Work')
    axs[0].set_xticks(
        [r + bar_width for r in range(len(grade_level_scores[0]))])
    axs[0].set_xticklabels(works)
    axs[0].legend()
    add_value_labels(axs[0])

    axs[1].bar(r1, reading_ease_scores[0], color='b',
               width=bar_width, edgecolor='grey', label=algorithms[0])
    axs[1].bar(r2, reading_ease_scores[1], color='r',
               width=bar_width, edgecolor='grey', label=algorithms[1])
    axs[1].bar(r3, reading_ease_scores[2], color='g',
               width=bar_width, edgecolor='grey', label=algorithms[2])
    axs[1].set_xlabel('Works', fontweight='bold')
    axs[1].set_ylabel('Flesch Reading Ease', fontweight='bold')
    axs[1].set_title('Comparison of Flesch Reading Ease by Algorithm and Work')
    axs[1].set_xticks(
        [r + bar_width for r in range(len(reading_ease_scores[0]))])
    axs[1].set_xticklabels(works)
    axs[1].legend()
    add_value_labels(axs[1])

    plt.tight_layout()
    plt.show()


def main():
    algorithms, works, grade_level_scores, reading_ease_scores = prepare_data()
    plot_graphs(algorithms, works, grade_level_scores, reading_ease_scores)


if __name__ == "__main__":
    main()
