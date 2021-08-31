
# Tagger

Simple spacy tagger as a web service. No dependencies other than spacy itself.

# Installation

It’s in the Dockerfile, but the short version is: `pip3 install -U spacy && python -m spacy download de_core_news_sm`. You do need python3 and pip3.

## API

`POST` a sentence to it (in plain text), get the tagged sentence, like:

```JSON
[
  {
  "spacy_orth": "was",
  "spacy_text": "was",
  "spacy_pos": "PRON",
  "spacy_tag": "PWS",
  "spacy_lemma": "was",
  "spacy_dep": "sb",
  "spacy_entity_type": ""
  }
]
````
