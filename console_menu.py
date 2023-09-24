from text_reader import *
from files_operations import get_file_path_from_user
from text_operations import *
from settings import *
from graphs import *


def menu():
    the_settings = Settings()
    the_settings.load_from_config()
# just once it is an initial
#    fill_style_dictionary(the_settings.style_dictionary)
    text_reader_instance = TextReader(the_settings.max_words)
    the_stopwords = setup_stop_words()
    while True:
        print("\nMenu:")
        print("1. Type a text for analysis or load from file")
        print("2. Settings")
        print("3. Exit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == '1':
            print("\nYou chose: Type a text for analysis or load from file")
            # Here you can add the functionality or call a function related to this choice
            load_text_submenu(text_reader_instance)
            analyze_text(text_reader_instance)
            the_top = top_words(text_reader_instance.get_text(), the_stopwords, the_settings.top_number)
            print(the_top)
            results_sentiment_words = count_sentiment_words(text_reader_instance.get_text(),
                                                            the_settings.style_dictionary.positive,
                                                            the_settings.style_dictionary.neutral,
                                                            the_settings.style_dictionary.negative)
            print(results_sentiment_words)
            # plot_horizontal_bar_chart(the_top)
            # plot_histogram(results_sentiment_words)
            # draw_two_histograms(the_top, results_sentiment_words)
            plot_histograms_wordcloud(the_top, results_sentiment_words, text_reader_instance.get_text())
        elif choice == '2':
            print("\nYou chose: Settings")
            # Here you can add the functionality or call a function related to this choice
            settings_submenu(the_settings)
            the_settings.save_to_config()
        elif choice in ['3', 'q']:
            print("\nGoodbye!")
            break

        else:

            print("\nInvalid choice! Please try again.")


def load_text_submenu(text_reader_instance):
    while True:
        print("\nSubmenu:")
        print("1. Text typing")
        print("2. Load from file")
        print("3. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("\nYou chose: Text typing")
            # Here you can add functionality or call a function related to this choice
            text_reader_instance.read_from_console()
            print("\nYour text: ")
            print(text_reader_instance.get_text())
            return
        elif choice == '2':
            print("\nYou chose: Load from file")
            # Here you can add functionality or call a function related to this choice
            path = get_file_path_from_user()
            if path:
                print(f"You provided a valid path: {path}")
                text_reader_instance.read_from_file(path)
                return
            else:
                print("No valid path provided.")
        elif choice == '3':
            print("\nReturning to main menu...")
            break

        else:
            print("\nInvalid choice! Please try again.")


def settings_submenu(the_settings):
    while True:
        print("\nSettings Submenu:")
        print("1. Set top number")
        print("2. Set dictionary")
        print("3. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            the_settings.top_number = int(input("\nEnter the top number: "))
            print(f"You set the top number to: {the_settings.top_number}")
            # You can store or use the top_number as needed

        elif choice == '2':
            print("\nYou chose: Set dictionary")
            # Here, you can add functionality or call a function related to setting the dictionary
            words_submenu(the_settings)
        elif choice == '3':
            print("\nReturning to main menu...")
            break

        else:
            print("\nInvalid choice! Please try again.")


def words_submenu(the_settings):
    while True:
        print("\nWords Submenu:")
        print("1. Positive words")
        print("2. Neutral words")
        print("3. Negative words")
        print("4. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("\nYou chose: Positive words")
            # Here, you can add functionality or call a function related to handling positive words
            style_submenu(the_settings.style_dictionary, "positive")
        elif choice == '2':
            print("\nYou chose: Neutral words")
            # Here, you can add functionality or call a function related to handling neutral words
            style_submenu(the_settings.style_dictionary, "neutral")
        elif choice == '3':
            print("\nYou chose: Negative words")
            # Here, you can add functionality or call a function related to handling negative words
            style_submenu(the_settings.style_dictionary, "negative")
        elif choice == '4':
            print("\nReturning to main menu...")
            break

        else:
            print("\nInvalid choice! Please try again.")


def style_submenu(style_dictionary, style_name):
    if style_name not in ["negative", "neutral", "positive"]:
        raise ValueError("Invalid style. Choose among 'negative', 'neutral', or 'positive'")

    while True:
        print(f"\n--- {style_name.capitalize()} Words Submenu ---")
        print("1. Add words")
        print("2. Remove words")
        print("3. Print the words")
        print("4. Return to the main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            words = input(f"Enter {style_name} words separated by comma (,): ").split(',')
            for word in words:
                word = word.strip()  # Remove any spaces before or after the word
                style_dictionary.add_word(style_name, word)
            print(f"{len(words)} words added to {style_name} words list.")

        elif choice == '2':
            words = input(f"Enter {style_name} words to remove separated by comma (,): ").split(',')
            for word in words:
                word = word.strip()  # Remove any spaces before or after the word
                style_dictionary.remove_word(style_name, word)
            print(f"{len(words)} words removed from {style_name} words list.")

        elif choice == '3':
            print(f"List of {style_name} words:")
            style_dictionary.print_words_of_style(style_name)

        elif choice == '4' or choice.lower() == 'q':
            break

        else:
            print("Invalid choice. Please try again.")

