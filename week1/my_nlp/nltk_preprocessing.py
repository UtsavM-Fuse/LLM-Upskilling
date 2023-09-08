import os
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from my_nltk.my_nltk_module import (
    tokenize_words,
    tokenize_sentence,
    lower_casing,
    remove_stop_words,
    stemming,
    lemmatization,
)
from text_preprocessing.text_preprocessing import (
    remove_html_tags,
    remove_emojis,
    remove_urls,
    convert_emoticons_to_words,
)

# Download NLTK data (if not already downloaded)
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")


def preprocess_text(text):
    """
    Perform text preprocessing on the input text.

    Args:
        text (str): The input text to be preprocessed.

    Returns:
        str: The preprocessed text.
    """
    # Remove HTML tags
    text = remove_html_tags(text)

    # Remove emojis and emoticons
    text = remove_emojis(text)

    # Convert emoticons to words
    text = convert_emoticons_to_words(text)

    # Remove URLs
    text = remove_urls(text)

    # Tokenize words
    words = tokenize_words(text)

    # Convert words to lowercase
    words = [lower_casing(word) for word in words]

    # Remove stopwords
    words = remove_stop_words(" ".join(words))

    # # Perform lemmatization and extract lemmatized words
    # lemmatized_words = [lemma for _, lemma in lemmatization(" ".join(words))]

    # Join the processed words back into a sentence
    processed_text = " ".join(words)

    return processed_text


def main():
    # Retrieve input and output file paths from environment variables
    input_file_path = os.getenv("INPUT_FILE_PATH", "./data/quotes_scraped.csv")
    output_file_path = os.getenv(
        "OUTPUT_FILE_PATH", "./outputs/quotes_scraped_cleaned.csv"
    )

    # Read the CSV file
    df = pd.read_csv(input_file_path)

    # Apply text preprocessing to the 'description' column
    df["Quote Text"] = df["Quote Text"].apply(preprocess_text)

    # Save the processed data to a new CSV file
    df.to_csv(output_file_path, index=False)

    print("Text preprocessing completed. Processed data saved to:", output_file_path)


if __name__ == "__main__":
    main()
