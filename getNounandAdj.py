import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def enclose_noun_with_stars(sentence):
    # Process the sentence with spaCy
    doc = nlp(sentence)

    # Find the first noun in the sentence
    noun_found = False
    enclosed_sentence = ""
    for token in doc:
        if token.pos_ == "NOUN" and not noun_found:
            enclosed_sentence += "**" + token.text + "** "
            noun_found = True
        else:
            enclosed_sentence += token.text + " "

    return enclosed_sentence.strip()

def split_paragraph_into_sentences(paragraph):
    # Process the paragraph with spaCy
    doc = nlp(paragraph)

    # Split the paragraph into sentences
    sentences = [sent.text for sent in doc.sents]

    return sentences

# Example paragraph
def preProcess(paragraph):
    # paragraph = "Once upon a time in a mystical land, there lived a brave young knight named Arthur. He was known for his unwavering courage and noble heart. One fateful day, a wicked sorcerer named Malachi cast a dark spell over the kingdom, plunging it into eternal darkness. The people were filled with fear and despair, longing for a savior to restore light and hope. Hearing their cries, Arthur embarked on a perilous journey to defeat Malachi and bring back the light. Along his quest, he encountered mythical creatures, faced treacherous obstacles, and forged alliances with unlikely allies. With each step, Arthur grew stronger and more determined. After countless battles and sacrifices, he finally reached Malachi's lair. In a fierce duel, Arthur's sword clashed against Malachi's dark magic, but with his indomitable spirit, Arthur emerged victorious. As the sunlight broke through the clouds, the kingdom rejoiced, and Arthur was hailed as a true hero. His name became a legend, inspiring generations to come. And so, the story of Arthur, the brave knight who triumphed over darkness, was forever etched in the annals of history."

    # Split the paragraph into sentences
    sentences = split_paragraph_into_sentences(paragraph)

    # Enclose a noun in each sentence with **
    result = [enclose_noun_with_stars(sentence) for sentence in sentences]

    return result
