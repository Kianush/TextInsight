import json
import os


class StyleDictionary:
    def __init__(self):
        self.negative = {}
        self.neutral = {}
        self.positive = {}

    def add_word(self, style, word):
        if style not in ["negative", "neutral", "positive"]:
            raise ValueError("Invalid style. Choose among 'negative', 'neutral', or 'positive'")
        self.__dict__[style][word] = True

    def remove_word(self, style, word):
        if style not in ["negative", "neutral", "positive"]:
            raise ValueError("Invalid style. Choose among 'negative', 'neutral', or 'positive'")
        if word in self.__dict__[style]:
            del self.__dict__[style][word]

    def print_words_of_style(self, style):
        if style not in ["negative", "neutral", "positive"]:
            print(f"Warning: The style '{style}' does not exist!")
            return

        print(f"Words for the {style} style:")
        words = list(self.__dict__[style].keys())
        for word in words:
            print(word)


class Settings:
    def __init__(self, max_words=10000000):
        self.top_number = 0
        self.style_dictionary = StyleDictionary()
        self.max_words = max_words

    def save_to_config(self, file_name="settings.def"):
        config = {
            'top_number': self.top_number,
            'max_words': self.max_words,
            'negative_words': list(self.style_dictionary.negative.keys()),
            'neutral_words': list(self.style_dictionary.neutral.keys()),
            'positive_words': list(self.style_dictionary.positive.keys())
        }
        with open(file_name, 'w') as f:
            json.dump(config, f, indent=4)

    def load_from_config(self, file_name="settings.def"):
        if not os.path.exists(file_name):
            # Warning if file does not exist
            print("Warning: 'settings.def' not found. Creating with default values.")

            # Default configuration
            config = {
                'top_number': self.top_number,
                'max_words': self.max_words,
                'negative_words': list(self.style_dictionary.negative.keys()),
                'neutral_words': list(self.style_dictionary.neutral.keys()),
                'positive_words': list(self.style_dictionary.positive.keys())
            }

            # Save the default configuration to the file
            with open(file_name, 'w') as f:
                json.dump(config, f)
            return
        with open(file_name, 'r') as f:
            config = json.load(f)
            self.top_number = config['top_number']
            self.max_words = config['max_words']
            self.style_dictionary.negative = {word: True for word in config['negative_words']}
            self.style_dictionary.neutral = {word: True for word in config['neutral_words']}
            self.style_dictionary.positive = {word: True for word in config['positive_words']}


def fill_style_dictionary(instance):
    # Words data grouped by language
    words_data = {
        'english': {
            'negative': ["sad", "terrible", "horrible", "bad", "negative"],
            'neutral': ["book", "table", "chair", "pencil", "window"],
            'positive': ["happy", "wonderful", "fantastic", "positive", "excellent"]
        },
        'russian': {
            'negative': ["грустный", "ужасный", "плохой", "отрицательный"],
            'neutral': ["книга", "стол", "стул", "карандаш", "окно"],
            'positive': ["счастливый", "замечательный", "отличный", "положительный"]
        },
        'ukrainian': {
            'negative': ["сумний", "жахливий", "поганий", "негативний"],
            'neutral': ["книга", "стіл", "стілець", "олівець", "вікно"],
            'positive': ["щасливий", "чудовий", "відмінний", "позитивний"]
        },
        'czech': {
            'negative': ["smutný", "hrozný", "špatný", "negativní"],
            'neutral': ["kniha", "stůl", "židle", "tužka", "okno"],
            'positive': ["šťastný", "skvělý", "vynikající", "pozitivní"]
        },
        'arabic': {
            'negative': ["حزين", "فظيع", "سيئ", "سلبي"],
            'neutral': ["كتاب", "طاولة", "كرسي", "قلم رصاص", "نافذة"],
            'positive': ["سعيد", "رائع", "ممتاز", "إيجابي"]
        }
    }

    for lang, style_words in words_data.items():
        for style, words in style_words.items():
            for word in words:
                instance.add_word(style, word)


