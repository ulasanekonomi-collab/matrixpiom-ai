from modules.dictionaries import RELATION_KEYWORDS


def detect_pairwise_relations(text, actors):

    relations = []

    sentences = text.split(".")

    for sentence in sentences:

        lower_sentence = sentence.lower()

        for relation_type, keywords in RELATION_KEYWORDS.items():

            for keyword, score in keywords.items():

                if keyword in lower_sentence:

                    keyword_pos = lower_sentence.find(keyword)

                    source = None
                    target = None

                    for actor in actors:

                        actor_pos = lower_sentence.find(actor.lower())

                        if actor_pos == -1:
                            continue

                        if actor_pos < keyword_pos:
                            source = actor

                        elif actor_pos > keyword_pos and target is None:
                            target = actor

                    if source and target:

                        relations.append({
                            "source": source,
                            "target": target,
                            "relation_type": relation_type,
                            "keyword": keyword,
                            "score": score
                        })

    return relations
