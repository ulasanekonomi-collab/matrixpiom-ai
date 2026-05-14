from modules.dictionaries import RELATION_KEYWORDS


def detect_relation_score(text):

    score = 0

    detected_keywords = []

    for keyword, value in RELATION_KEYWORDS.items():

        if keyword in text.lower():

            score += value

            detected_keywords.append(keyword)

    return score, detected_keywords
