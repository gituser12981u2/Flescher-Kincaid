import unittest

from Flesch_Kincaid import calculate_flesch_scores


class TestFleschScores(unittest.TestCase):
    def test_flesch_scores(self):
        # Test input texts
        text1 = "This is a sample text for testing."
        text2 = "Another example text to test."

        # Calculate scores for text1
        fk_grade1, fre_score1 = calculate_flesch_scores(text1)
        self.assertIsNotNone(fk_grade1)
        self.assertIsNotNone(fre_score1)

        # Calculate scores for text2
        fk_grade2, fre_score2 = calculate_flesch_scores(text2)
        self.assertIsNotNone(fk_grade2)
        self.assertIsNotNone(fre_score2)

        # Print the scores
        print("Scores for Text 1:")
        print(f"Flesch-Kincaid Grade Level: {fk_grade1}")
        print(f"Flesch Reading Ease: {fre_score1}")
        print("")

        print("Scores for Text 2:")
        print(f"Flesch-Kincaid Grade Level: {fk_grade2}")
        print(f"Flesch Reading Ease: {fre_score2}")


if __name__ == '__main__':
    unittest.main()
