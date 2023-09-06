# LLM Upskilling

Materials covering a wide range of topics in LLM.

# Activate Environment and Install Dependencies

```bash
virtualenv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

# Example Usages

```bash
python main.py
python week1/web_scraping/scrape_fake_python.py
python week1/web_scraping/scrape_fake_python.py --url https://realpython.github.io/fake-jobs/ --output-filename ./outputs/job_data.csv

python week1/web_scraping/scrape_quotes.py
python week1/web_scraping/scrape_quotes.py --url https://quotes.toscrape.com/ --output-filename ./outputs/quotes_scraped.csv

python week1/my_nlp/my_nltk/my_nltk_module.py
python week1/my_nlp/my_nltk/my_nltk_module.py --text "This is a custom sentence on which we can perform text processing."

python ./week1/my_nlp/text_preprocessing/nltk_preprocessing.py
```

# Project Folder structure (Week1)

```bash
week1/
│
├── my_nlp/
│   ├── __init__.py
│   ├── my_nltk/
│   │   ├── __init__.py
│   │   └── my_nltk_module.py
│   │
│   ├── my_spacy/
│   │   ├── __init__.py
│   │   └── my_spacy_module.py
│   │
│   └── text_preprocessing/
│       ├── __init__.py
│       ├── text_cleaning.py
│       ├── text_preprocessing.py
│       ├── nltk_preprocessing.py
│       └── spacy_preprocessing.py
│
└── web_scraping/
    ├── __init__.py
    ├── scrape_fake_python.py
    ├── scrape_quotes.py
    └── beautifulsoup_doc.md
```

# Links to Study Documents

-   [Documentation and Study Materials [ClickUp]](https://doc.clickup.com/9007106573/d/h/8cdv2gd-724/26501a3c91d321d)
