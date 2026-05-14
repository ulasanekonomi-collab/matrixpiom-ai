from modules.dictionaries import RELATION_KEYWORDS

def detect_relation_score(text):

    detected_relations = []

    text = text.lower()

    for relation_type, keywords in RELATION_KEYWORDS.items():

        for keyword, value in keywords.items():

            if keyword in text:

                detected_relations.append({
                    "type": relation_type,
                    "keyword": keyword,
                    "score": value
                })

    return detected_relations
