from modules.dictionaries import RELATION_KEYWORDS


def detect_pairwise_relations(text, actors):

    relations = []

    lower_text = text.lower()

    for keyword, score in RELATION_KEYWORDS.items():

        if keyword in lower_text:

            for source in actors:

                for target in actors:

                    if source != target:

                        if source.lower() in lower_text and target.lower() in lower_text:

                            relations.append({
                                "source": source,
                                "target": target,
                                "keyword": keyword,
                                "score": score
                            })

    return relations
