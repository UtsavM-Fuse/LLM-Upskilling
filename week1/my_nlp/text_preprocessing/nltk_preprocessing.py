import os
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

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
    # Tokenize words
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.lower() not in stop_words]

    # Perform stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    # Perform lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    # Join the processed words back into a sentence
    processed_text = " ".join(words)

    return processed_text


def main():
    # Retrieve input and output file paths from environment variables
    input_file_path = os.getenv(
        "INPUT_FILE_PATH", "./data/quotes_scraped.csv"
    )
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
