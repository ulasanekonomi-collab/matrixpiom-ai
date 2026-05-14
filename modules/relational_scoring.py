from modules.dictionaries import RELATION_KEYWORDS

def detect_pairwise_relations(text, actors):

    relations = []

    text = text.lower()

    for relation_type, keywords in RELATION_KEYWORDS.items():

        for keyword, score in keywords.items():

            if keyword in text:

                for source in actors:

                    for target in actors:

                        if source != target:

                            source_lower = source.lower()
                            target_lower = target.lower()

                            if source_lower in text and target_lower in text:

                                source_index = text.find(source_lower)
                                target_index = text.find(target_lower)
                                keyword_index = text.find(keyword)

                                if relation_type == "power":

                                    relations.append({
                                        "source": source,
                                        "target": "SYSTEM",
                                        "keyword": keyword,
                                        "score": score,
                                        "relation_type": relation_type
                                    })

                                elif source_index < keyword_index < target_index:

                                    relations.append({
                                        "source": source,
                                        "target": target,
                                        "keyword": keyword,
                                        "score": score,
                                        "relation_type": relation_type
                                    })

    return relations
