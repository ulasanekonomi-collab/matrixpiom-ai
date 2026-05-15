from modules.dictionaries import RELATION_KEYWORDS


def detect_pairwise_relations(text, actors):

    relations = []

    sentences = text.lower().split(".")

    for sentence in sentences:

        for relation_type, keywords in RELATION_KEYWORDS.items():

            for keyword, score in keywords.items():

                if keyword in sentence:

                    for source in actors:

                        source_lower = source.lower()

                        if source_lower in sentence:

                            # KHUSUS POWER
                            if relation_type == "power":

                                relations.append({
                                    "source": source,
                                    "target": "SYSTEM",
                                    "keyword": keyword,
                                    "score": score,
                                    "relation_type": relation_type
                                })

                            # RELASI ANTAR AKTOR
                            for target in actors:

                                if source != target:

                                    target_lower = target.lower()

                                    if target_lower in sentence:

                                        source_index = sentence.find(source_lower)
                                        keyword_index = sentence.find(keyword)
                                        target_index = sentence.find(target_lower)

                                        if source_index < keyword_index < target_index:

                                            relations.append({
                                                "source": source,
                                                "target": target,
                                                "keyword": keyword,
                                                "score": score,
                                                "relation_type": relation_type
                                            })

    return relations
