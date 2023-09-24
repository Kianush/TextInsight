import matplotlib.pyplot as plt
from wordcloud import WordCloud

# sentiment_counts = {
#    'positive': 10,
#    'neutral': 15,
#    'negative': 5
# }


def plot_histogram(sentiment_counts):
    labels = list(sentiment_counts.keys())
    values = list(sentiment_counts.values())

    # Colors: green for positive, blue for neutral, red for negative
    plt.bar(labels, values, color=['green', 'blue', 'red'])
    plt.xlabel('Sentiment')
    plt.ylabel('Word Count')
    plt.title('Sentiment Word Count')
    plt.show()


def plot_horizontal_bar_chart(data):
    words, counts = zip(*data)  # Unzip the data into two lists: words and counts

    plt.barh(words, counts, color='blue')
    plt.xlabel('Word Count')
    plt.ylabel('Words')
    plt.title('Top Words in Text')
    plt.gca().invert_yaxis()  # Invert the y-axis to have the word with the highest count at the top
    plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility if needed
    plt.tight_layout()  # Adjust layout for better visibility
    plt.show()


def draw_two_histograms(top_words, sentiment_counts):
    # Create a 1 row, 2 columns subplot grid
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Plot the top N words histogram (on the left)
    words, counts = zip(*top_words)  # Unzipping the list of tuples
    axs[0].barh(words, counts, color='skyblue')
    axs[0].invert_yaxis()  # So that the top word is on top
    axs[0].set_title('Top N Words in Text')
    axs[0].set_xlabel('Counts')
    axs[0].set_ylabel('Words')

    # Plot the sentiment counts histogram (on the right)
    sentiments, sentiment_vals = zip(*sentiment_counts.items())
    # Assuming the order: positive, neutral, negative
    axs[1].bar(sentiments, sentiment_vals, color=['green', 'gray', 'red'])
    axs[1].set_title('Sentiment Counts')
    axs[1].set_ylabel('Counts')
    axs[1].set_xlabel('Sentiments')

    plt.tight_layout()
    plt.show()


def plot_histograms_wordcloud(top_n_words, sentiment_counts, text):
    # Create a figure and a 2x2 grid of subplots
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12))

    # Plot the top N words histogram on the left
    words, counts = zip(*top_n_words)
    axes[0, 0].barh(words, counts)
    axes[0, 0].invert_yaxis()
    axes[0, 0].set_title('Top N Words')
    axes[0, 0].set_xlabel('Counts')
    axes[0, 0].set_ylabel('Words')

    # Plot the sentiment counts histogram in the middle
    sentiments, sentiment_values = zip(*sentiment_counts.items())
    axes[0, 1].bar(sentiments, sentiment_values, color=['red', 'gray', 'green'])
    axes[0, 1].set_title('Sentiment Counts')
    axes[0, 1].set_ylabel('Counts')
    axes[0, 1].set_xlabel('Sentiment')

    # Remove the blank plot on the bottom left
    fig.delaxes(axes[1, 0])

    # Generate the word cloud on the bottom right
    wordcloud = WordCloud(background_color="white").generate(text)
    axes[1, 1].imshow(wordcloud, interpolation='bilinear')
    axes[1, 1].axis("off")
    axes[1, 1].set_title('Word Cloud')

    plt.tight_layout()
    plt.show()

