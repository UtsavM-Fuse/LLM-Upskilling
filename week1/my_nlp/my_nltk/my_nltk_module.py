import nltk
import argparse
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download NLTK data
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")
nltk.download("wordnet")


def tokenize_words(text):
    """
    Tokenize the raw text into words and return a list of tokens.

    Args:
        text (str): The input raw text.

    Returns:
        list: A list of tokens.
    """
    return word_tokenize(text)


def tokenize_sentence(text):
    """
    Tokenize the raw text into sentences and return a list of sentences.

    Args:
        text (str): The input raw text.

    Returns:
        list: A list of sentences.
    """
    return sent_tokenize(text)


def lower_casing(text):
    """
    Convert the text to lowercase.

    Args:
        text (str): The input text.

    Returns:
        str: The lowercase version of the input text.
    """
    return text.lower()


def remove_stop_words(text):
    """
    Remove stopwords from the input text and return a list of tokens without stopwords.

    Args:
        text (str): The input text.

    Returns:
        list: A list of tokens without stopwords.
    """
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in word_tokens if word not in stop_words]
    return tokens_without_sw


def stemming(text):
    """
    Perform stemming on the input text and return a list of (word, stem) pairs.

    Args:
        text (str): The input text.

    Returns:
        list: A list of (word, stem) pairs.
    """
    ps = PorterStemmer()
    words = word_tokenize(text)
    token_stem_list = [(word, ps.stem(word)) for word in words]
    return token_stem_list


def get_wordnet_pos(word):
    """
    Map POS tag to WordNet POS tag for lemmatization.

    Args:
        word (str): The input word.

    Returns:
        str: The WordNet POS tag.
    """
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {
        "J": wordnet.ADJ,
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "R": wordnet.ADV,
    }
    return tag_dict.get(tag, wordnet.NOUN)


def lemmatization(text):
    """
    Perform lemmatization on the input text and return a list of (word, lemma) pairs.

    Args:
        text (str): The input text.

    Returns:
        list: A list of (word, lemma) pairs.
    """
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    token_lemma_list = [
        (token, lemmatizer.lemmatize(token, get_wordnet_pos(token))) for token in tokens
    ]
    return token_lemma_list


def named_entity_recognizer(text, binary_entity=True):
    """
    Identify named entities in the input text and return a list of (entity, label) pairs.

    Args:
        text (str): The input text.
        binary_entity (bool): Whether to return only binary entities (True) or entities with labels (False).

    Returns:
        list: A list of (entity, label) pairs.
    """
    words = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    chunks = nltk.ne_chunk(pos_tags, binary=binary_entity)
    entities = []
    labels = []

    for chunk in chunks:
        if hasattr(chunk, "label"):
            entities.append(" ".join(c[0] for c in chunk))
            labels.append(chunk.label())

    entities_labels = list(set(zip(entities, labels)))
    return entities_labels


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NLP Text Processing")
    parser.add_argument(
        "--text",
        type=str,
        default="The quick brown fox jumps over the lazy dog.",
        help="Input text for processing",
    )

    args = parser.parse_args()

    sample_text = args.text

    print("Word tokens:\n", tokenize_words(sample_text))
    print("Sentence tokens:\n", tokenize_sentence(sample_text))
    print("Lower Casing:\n", lower_casing(sample_text))
    print("Filtered sentence without stop words:\n", remove_stop_words(sample_text))

    token_stem_list = stemming(sample_text)
    print("Stemming:")
    for token_stem in token_stem_list:
        print(token_stem[0], "-->", token_stem[1])

    token_lemma_list = lemmatization(sample_text)
    print("Lemmatization:")
    for token_lemma in token_lemma_list:
        print(token_lemma[0], "-->", token_lemma[1])

    entities_labels = named_entity_recognizer(sample_text, False)
    entities_df = pd.DataFrame(entities_labels, columns=["Entities", "Labels"])
    print("Displaying Entities in Tabular format:\n", entities_df)
