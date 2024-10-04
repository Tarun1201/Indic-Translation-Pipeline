import re
from nltk.tokenize import word_tokenize
import emoji
import nltk

nltk.download('punkt')
    
def remove_mentions_and_urls(sentence):

    pattern = r'(@\S+|https://\S+|#\S+)'
    sentence = sentence.replace('\n', '')
    sentence = re.sub(pattern, '', sentence)
    
    if '\n' in sentence:
        print(sentence)

    return sentence


def remove_emojis(text):

    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F700-\U0001F77F"  # alchemical symbols
                               u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                               u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                               u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                               u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               u"\U00002702-\U000027B0"  # Dingbats
                               u"\U000024C2-\U0001F251" 
                               "]+", flags=re.UNICODE)

    # Use re.sub to replace emojis with an empty string
    cleaned_text = emoji_pattern.sub(r'', text)

    return cleaned_text

def remove_english_words(text):
    cleaned_text = re.sub(r'[1234567890!%,.()/\-?|&*:;+=<@>"\'“”]', '', text)
    words = word_tokenize(cleaned_text, language='english', preserve_line=True)
    non_english_words = [word for word in words if not any(char.isalpha() and ord(char) < 128 for char in word)]
    return ' '.join(non_english_words)

def emoji_handler(sentence):
    emoji_list = []
    sentence_corr = sentence
    for element in emoji.emoji_list(sentence):
        sentence_corr = sentence_corr[:int(element['match_start'])] + '$' + sentence_corr[int(element['match_start']) + 1:]
        emoji_list.append(element['emoji'])
    return sentence_corr, emoji_list