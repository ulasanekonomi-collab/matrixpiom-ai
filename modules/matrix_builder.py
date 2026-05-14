import pandas as pd


def create_empty_matrix(actors):

    matrix = pd.DataFrame(
        "",
        index=actors,
        columns=actors
    )

    for actor in actors:
        matrix.loc[actor, actor] = "-"

    return matrix
