import pandas as pd


def classify_power_level(score):

    if score >= 15:
        return "Dominan"

    elif score >= 10:
        return "Kuat"

    elif score >= 5:
        return "Moderat"

    else:
        return "Lemah"


def compute_power_index(
    actors,
    influence_matrix,
    power_matrix,
    collaboration_matrix,
    conflict_matrix
):

    results = []

    for actor in actors:

        influence_score = influence_matrix.loc[actor].sum()

        power_score = power_matrix.loc[actor].sum()

        collaboration_score = (
            collaboration_matrix.loc[actor].sum()
        )

        conflict_score = abs(
            conflict_matrix.loc[actor].sum()
        )

        power_index = (
            influence_score
            + power_score
            + (0.5 * collaboration_score)
            - (0.3 * conflict_score)
        )

        category = classify_power_level(
            power_index
        )

        results.append({
            "Actor": actor,
            "Influence": influence_score,
            "Power": power_score,
            "Collaboration": collaboration_score,
            "Conflict": conflict_score,
            "Power Index": round(power_index, 2),
            "Category": category
        })

    return pd.DataFrame(results)
