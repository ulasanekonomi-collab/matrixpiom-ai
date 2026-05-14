import re

STOPWORDS = [
    "dan",
    "atau",
    "yang",
    "di",
    "ke",
    "dari",
    "untuk",
    "dengan",
    "karena",
]

def extract_actors(text):

    candidates = re.findall(
        r'\b[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*',
        text
    )

    actors = []

    for item in candidates:

        if item.lower() not in STOPWORDS:

            if item not in actors:
                actors.append(item)

    return actors
