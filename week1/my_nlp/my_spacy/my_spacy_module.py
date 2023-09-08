import spacy
from spacy.language import Language
from spacy.tokens import Doc
import argparse

# Load spaCy model
nlp = spacy.load("en_core_web_sm")


# Add a Sentencizer component to split text into sentences
@Language.component("custom_sentencizer")
def sentencizer(doc):
    """
    Custom Sentencizer component to split text into sentences based on specific conditions.

    Args:
        doc (Doc): The spaCy Doc object.

    Returns:
        Doc: The processed spaCy Doc object.
    """
    for i, token in enumerate(doc[:-2]):
        if token.text == "|" and doc[i + 1].is_title:
            doc[i + 1].is_sent_start = True
        else:
            doc[i + 1].is_sent_start = False
    return doc


# Define custom pipeline components for each function
@Language.component("tokenize_words")
def tokenize_words(doc):
    """
    Custom tokenization component to tokenize text into words.

    Args:
        doc (Doc): The spaCy Doc object.

    Returns:
        Doc: The processed spaCy Doc object.
    """
    return doc


@Language.component("lower_casing")
def custom_lower_casing(doc):
    """
    Custom component to convert text to lowercase.

    Args:
        doc (Doc): The spaCy Doc object.

    Returns:
        Doc: The processed spaCy Doc object.
    """
    lowercase_tokens = [token.text.lower() for token in doc]
    return Doc(doc.vocab, words=lowercase_tokens)


@Language.component("remove_stop_words")
def custom_remove_stop_words(doc):
    """
    Custom component to remove stop words from text.

    Args:
        doc (Doc): The spaCy Doc object.

    Returns:
        Doc: The processed spaCy Doc object.
    """
    stop_words = set(nlp.Defaults.stop_words)
    filtered_tokens = [token.text for token in doc if token.text not in stop_words]
    return Doc(doc.vocab, words=filtered_tokens)


@Language.component("lemmatization")
def custom_lemmatization(doc):
    """
    Custom lemmatization component to lemmatize text.

    Args:
        doc (Doc): The spaCy Doc object.

    Returns:
        Doc: The processed spaCy Doc object.
    """
    lemmatized_tokens = []
    for token in doc:
        if not token.is_punct and not token.is_space and len(token.text.strip()) > 0:
            lemmatized_tokens.append(token.lemma_)
    return Doc(doc.vocab, words=lemmatized_tokens)


@Language.component("named_entity_recognizer")
def custom_named_entity_recognizer(doc):
    """
    Custom named entity recognition component.

    Args:
        doc (Doc): The spaCy Doc object.

    Returns:
        Doc: The processed spaCy Doc object.
    """
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    doc.set_extension("custom_named_entities", default=None)
    doc._.custom_named_entities = entities
    return doc


if __name__ == "__main__":
    # Set the default sample text if not provided
    # sample_text = os.environ.get(
    #     "SAMPLE_TEXT", "The quick brown fox jumping over the lazy dog."
    # )
    parser = argparse.ArgumentParser(description="NLP Text Processing")
    parser.add_argument(
        "--text",
        type=str,
        default="The quick brown fox jumps over the lazy dog.",
        help="Input text for processing",
    )

    args = parser.parse_args()

    sample_text = args.text

    # Add custom components to the spaCy pipeline
    nlp.add_pipe("sentencizer")
    # nlp.add_pipe("info_component", name="print_info", last=True)
    nlp.add_pipe("tokenize_words", after="sentencizer")
    nlp.add_pipe("lower_casing", after="tokenize_words")
    nlp.add_pipe("remove_stop_words", after="lower_casing")
    # nlp.add_pipe("lemmatization", after="remove_stop_words")
    nlp.add_pipe(
        "named_entity_recognizer", after="remove_stop_words"
    )  # custom_named_entity_recognizer

    # Process text using the custom NLP pipeline
    doc = nlp(sample_text)
    print(nlp.pipe_names)
    print(doc)
