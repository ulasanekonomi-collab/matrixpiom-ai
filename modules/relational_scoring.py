from modules.dictionaries import RELATION_KEYWORDS


def detect_pairwise_relations(text, actors):

    relations = []

    lower_text = text.lower()

    last_target = None

    for relation_type, keywords in RELATION_KEYWORDS.items():

        for keyword, score in keywords.items():

            if keyword in lower_text:

                keyword_pos = lower_text.find(keyword)

                source = None
                target = None

                for actor in actors:

                    actor_pos = lower_text.find(actor.lower())

                    if actor_pos < keyword_pos:
                        source = actor

                    elif actor_pos > keyword_pos and target is None:
                        target = actor

                # fallback target
                if source and not target:
                    target = last_target

                # simpan target terakhir
                if target:
                    last_target = target

                if source and target:

                    relations.append({
                        "source": source,
                        "target": target,
                        "relation_type": relation_type,
                        "keyword": keyword,
                        "score": score
                    })

    return relations
