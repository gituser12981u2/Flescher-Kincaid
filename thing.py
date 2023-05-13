from Flesch_Kincaid import calculate_flesch_scores


def print_flesch_scores(text1, text2):
    # Calculate scores for TTTC Intro
    index = 'yes'
    fk_grade1, fre_score1 = calculate_flesch_scores(text1, index)
    print("Scores for TTTC Intro:")
    print(f"Flesch-Kincaid Grade Level: {fk_grade1}")
    print(f"Flesch Reading Ease: {fre_score1}")
    print("")

    # Calculate scores for Ulysses 'Proteus'
    index = 'yes'
    fk_grade2, fre_score2 = calculate_flesch_scores(text2, index)
    print("Scores for Ulysses 'Proteus':")
    print(f"Flesch-Kincaid Grade Level: {fk_grade2}")
    print(f"Flesch Reading Ease: {fre_score2}")
    print("")
    print("")

    # Print experimental values for TTTC Intro
    print("Experimental Values for TTTC Intro:")
    print("Flesch-Kincaid Grade Level: 15.6")
    print("Flesch Reading Ease: 27")
    print("")

    # Print experimental values for Ulysses 'Proteus'
    print("Experimental Values for Ulysses 'Proteus:")
    print("Flesch-Kincaid Grade Level: 17.8")
    print("Flesch Reading Ease: 13")


if __name__ == '__main__':
    # Test input texts
    text1 = """Emmanuel Kant described two truths of our world: the Phenomenal and Noumenal. The Truth in the Phenomenal realm is that of emotion intertwined in recounted thoughts—forever imbued in the lies of emotions; while the Noumenal world shows the mind only objective truths—unscathed by the attacking forces of emotions. Kantian ideas of the nature of Truth are extrapolated into many fields, including literature. Truth is prevalent in Tim O’Brien’s book of anecdotes, The Things They Carried, in which he explores what meaning his life has through the lens of storytelling and properties of Truths within the stories. Within O’Brien’s work he does not merely accept nor reject the ideas of Kantian Truth but posits on why emotion should be disgraced; why one should ever be in need of finding the Noumenal world. O’Brien spends his narrative recontuering about imbuing his own epistemology to further develop Kantian theorem of Truth, to push forth the idea of the Phenomenal world being that of truth, and emotion being the very fabric of truth. Importantly, the concept of truth is as fluid as the tides and ebbs of good storytelling. O’Brien’s finds himself bewitched by the idea of true Truth being in the Phenomenal world. He finds his meaning is that of a storyteller, whether his stories are steeped in Noumenal truth or not, O’Brien finds meaning in his job as a storyteller, and Truth, emotional truth, is all he wishes to impart on the reader.

"""
    text2 = """Ineluctable modality of the visible: at least that if no more, thought through my eyes. Signatures of all things I am here to read, seaspawn and seawrack, the nearing tide, that rusty boot. Snotgreen, bluesilver, rust: coloured signs. Limits of the diaphane. But he adds: in bodies. Then he was aware of them bodies before of them coloured. How? By knocking his sconce against them, sure. Go easy. Bald he was and a millionaire, maestro di color che sanno. Limit of the diaphane in. Why in? Diaphane, adiaphane. If you can put your five fingers through it it is a gate, if not a door. Shut your eyes and see.

Stephen closed his eyes to hear his boots crush crackling wrack and shells. You are walking through it howsomever. I am, a stride at a time. A very short space of time through very short times of space. Five, six: the nacheinander. Exactly: and that is the ineluctable modality of the audible. Open your eyes. No. Jesus! If I fell over a cliff that beetles o'er his base, fell through the nebeneinander ineluctably! I am getting on nicely in the dark. My ash sword hangs at my side. Tap with it: they do. My two feet in his boots are at the ends of his legs, nebeneinander. Sounds solid: made by the mallet of Los Demiurgos. Am I walking into eternity along Sandymount strand? Crush, crack, crick, crick. Wild sea money. Dominie Deasy kens them a'. 
"""
    print_flesch_scores(text1, text2)
