import re


def extract_semantic_tags(text):

    semantic_data = {
        "actor": [],
        "arena": [],
        "issue": [],
        "resource": [],
        "institution": []
    }

    patterns = {
        "actor": r"\\(actor\\)\\s+([A-Za-z\\s]+)",
        "arena": r"\\(arena\\)\\s+([A-Za-z\\s]+)",
        "issue": r"\\(issue\\)\\s+([A-Za-z\\s]+)",
        "resource": r"\\(resource\\)\\s+([A-Za-z\\s]+)",
        "institution": r"\\(institution\\)\\s+([A-Za-z\\s]+)"
    }
    relation_patterns = {
        "collaboration": r"\(relation:\s*collaboration\s*\)",
        "conflict": r"\(relation:\s*conflict\s*\)",
        "influence": r"\(relation:\s*influence\s*\)",
        "power": r"\(relation:\s*power\s*\)"
    }
    for key, pattern in patterns.items():

        matches = re.findall(pattern, text)

        semantic_data[key.upper()] = matches

    return semantic_data
    
def extract_relation_tags(text):

    import re

    relations = []

    actor_matches = list(
        re.finditer(r"\(actor\)\s*([A-Za-z\s]+)", text)
    )

    relation_matches = list(
        re.finditer(r"\(relation:\s*(.*?)\s*\)", text)
    )

    for i in range(len(relation_matches)):

        if i < len(actor_matches) - 1:

            source = actor_matches[i].group(1).strip()
            target = actor_matches[i + 1].group(1).strip()

            relation_type = relation_matches[i].group(1).strip()

            relations.append({
                "source": source,
                "target": target,
                "relation_type": relation_type,
                "score": 5,
                "keyword": relation_type
            })

    return relations

    for tag_type, pattern in patterns.items():

        matches = re.findall(pattern, text)

        cleaned_matches = [
            match.strip()
            for match in matches
        ]

        semantic_data[tag_type] = cleaned_matches

    return semantic_data
