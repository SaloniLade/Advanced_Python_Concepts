
import string

def remove_punctuation(text):
    return text.translate(
        str.maketrans("", "", string.punctuation)
    )

def remove_extra_spaces(text):
    return " ".join(text.split())

def clean_text(text):
    return remove_extra_spaces(remove_punctuation(text))
