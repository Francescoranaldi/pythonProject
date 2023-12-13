import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def process_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()
    return text


def extract_and_count_words(text):
    # Extract words with conditions 1a and 1b
    words = re.findall(r'\b[A-Z][a-zA-Z]{3,}\b', text)

    # Count occurrences using Counter
    word_counts = Counter(words)

    return word_counts


def generate_and_save_bar_chart(word_counts, output_file):
    # Generate bar chart for top 10 words
    top_words = dict(word_counts.most_common(10))

    plt.bar(top_words.keys(), top_words.values())
    plt.xlabel('Words')
    plt.ylabel('Occurrences')
    plt.title('Top 10 Most Common Words')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()


def generate_and_save_word_cloud(words, output_file):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(words)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(output_file)
    plt.show()


if __name__ == "__main__":
    # Read text file
    text_file_path = 'jobs_speech.txt'
    text_data = process_text_file(text_file_path)

    # Extract and count words
    word_counts = extract_and_count_words(text_data)

    # Generate and save bar chart
    bar_chart_output = 'bar_chart.png'
    generate_and_save_bar_chart(word_counts, bar_chart_output)

    # Generate and save word cloud for all words
    word_cloud_output_all = 'word_cloud_all.png'
    generate_and_save_word_cloud(dict(word_counts), word_cloud_output_all)

    # Generate and save word cloud for top words
    top_words = dict(word_counts.most_common(50))
    word_cloud_output_top = 'word_cloud_top.png'
    generate_and_save_word_cloud(top_words, word_cloud_output_top)



