import re

from bs4 import BeautifulSoup


def remove_emojis(text):
    """
    Remove emojis and emoticons from the input text.

    Args:
        text (str): The input text.

    Returns:
        str: Text with emojis and emoticons removed.
    """
    # Remove emojis (Unicode characters)
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    text = emoji_pattern.sub(r"", text)

    # Remove emoticons (ASCII-based)
    emoticon_pattern = re.compile(r"[:;=][-']?[)D\]\(\]/\\OpP3\*]")
    text = emoticon_pattern.sub(r"", text)

    return text


def convert_emoticons_to_words(text):
    """
    Convert common emoticons to corresponding words in the input text.

    Args:
        text (str): The input text.

    Returns:
        str: Text with emoticons replaced by words.
    """
    emoticon_map = {
        ":)": "smile",
        ":D": "laugh",
        ":(": "sad",
        ":P": "playful",
        # Add more emoticons and their corresponding words
    }
    for emoticon, word in emoticon_map.items():
        text = text.replace(emoticon, f" {word} ")
    return text


def remove_urls(text):
    """
    Remove URLs from the input text.

    Args:
        text (str): The input text.

    Returns:
        str: Text with URLs removed.
    """
    url_pattern = re.compile(r"https?://\S+|www\.\S+")
    text = url_pattern.sub(r"", text)
    return text


def remove_html_tags(text):
    """
    Remove HTML tags from the input text.

    Args:
        text (str): The input text containing HTML tags.

    Returns:
        str: Text with HTML tags removed.
    """
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()
