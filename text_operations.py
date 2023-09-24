from text_reader import *
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords


def setup_stop_words():
    nltk.download('stopwords')
    english_stopwords = set(stopwords.words('english'))
    russian_stopwords = set(stopwords.words('russian'))
    arabic_stopwords = set(stopwords.words('arabic'))
    # czech_stopwords = set(stopwords.words('czech'))
    # ukrainian_stopwords = set(stopwords.words('ukrainian'))
    # unite
    all_stopwords = english_stopwords.union(russian_stopwords, arabic_stopwords)
    return all_stopwords


def analyze_text(text_reader_instance):
    text = text_reader_instance.get_text()
    words = text.split()
    word_count = len(words)
    print(f"analyze text: \nNumber of words in the text: {word_count}")


def top_words(text, the_stopwords, n=10):
    # words of text, using regex
    # words = re.findall(r'\w+', text.lower())
    words = [word for word in re.findall(r'\w+', text.lower()) if word not in the_stopwords]
    # complicated object, frequency of words
    word_counts = Counter(words)

    # return top n
    return word_counts.most_common(n)


def count_sentiment_words(text, positive, neutral, negative):
    # Tokenize the text
    words = re.findall(r'\w+', text.lower())  # Convert to lowercase and tokenize

    word_counts = Counter(words)

    positive_count = sum(word_counts[word] for word in positive if word in word_counts)
    neutral_count = sum(word_counts[word] for word in neutral if word in word_counts)
    negative_count = sum(word_counts[word] for word in negative if word in word_counts)

    return {
        'positive': positive_count,
        'neutral': neutral_count,
        'negative': negative_count
    }
