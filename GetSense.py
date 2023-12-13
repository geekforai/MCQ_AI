
import re
from pywsd.lesk import simple_lesk

def extract_word_between_tags(sentence):
    start_tag = "[TGT]"
    end_tag = "[TGT]"

    start_index = sentence.find(start_tag) + len(start_tag)
    end_index = sentence.find(end_tag, start_index)

    if start_index == -1 or end_index == -1:
        return None
    
    word = sentence[start_index:end_index].strip()
    return word

def get_sense(sentence):
    # Extract the ambiguous word within [TGT] tags
    answer=extract_word_between_tags(sentence)
    re_result = re.search(r"\[TGT\](.*)\[TGT\]", sentence)
    if re_result is None:
        print("\nIncorrect input format. Please try again.")
        return None, None

    ambiguous_word = re_result.group(1).strip()

    # Apply Lesk algorithm to disambiguate the sense
    sense = simple_lesk(sentence, ambiguous_word, pos='n')
    meaning = sense.definition()

    return sense, meaning, answer