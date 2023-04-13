# Import the SpellChecker class from the spellchecker module
from spellchecker import SpellChecker

# Create a SpellChecker instance
spell = SpellChecker()


def correct_spelling(text):
    words = text.split()                                    # Split the text into individual words
    corrected_text = []                                     # Initialize an empty list to store the corrected words
    for word in words:
        corrected_word = spell.correction(word)             # Use the SpellChecker instance to correct the word
        corrected_text.append(corrected_word)
    
    return " ".join(corrected_text)                         # Join the corrected words back into a single string

text = "Ths is an exaple of incorect speeling."
corrected_text = correct_spelling(text)
print(corrected_text)
