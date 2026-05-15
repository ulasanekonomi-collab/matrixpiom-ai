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

    for tag_type, pattern in patterns.items():

        matches = re.findall(pattern, text)

        cleaned_matches = [
            match.strip()
            for match in matches
        ]

        semantic_data[tag_type] = cleaned_matches

    return semantic_data
