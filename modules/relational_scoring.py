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

def detect_power_relations(text, semantic_tags):

    relations = []

    actors = semantic_tags.get("actor", [])
    resources = (
        semantic_tags.get("resource", []) +
        semantic_tags.get("institution", []) +
        semantic_tags.get("arena", [])
    )

    power_keywords = {
        "mengendalikan": 5,
        "menguasai": 5,
        "mendominasi": 5,
        "mengontrol": 5,
        "memiliki kewenangan": 4
    }

    text_lower = text.lower()

    for actor in actors:
        for resource in resources:

            actor_lower = actor.lower()
            resource_lower = resource.lower()

            if actor_lower in text_lower and resource_lower in text_lower:

                actor_index = text_lower.find(actor_lower)
                resource_index = text_lower.find(resource_lower)

                for keyword, score in power_keywords.items():

                    keyword_index = text_lower.find(keyword)

                    if (
                        keyword_index != -1 and
                        actor_index < keyword_index < resource_index
                    ):

                        relations.append({
                            "source": actor,
                            "target": resource,
                            "score": score,
                            "relation_type": "power",
                            "keyword": keyword
                        })

    return relations
