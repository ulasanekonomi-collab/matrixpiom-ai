import pandas as pd


def create_empty_matrix(actors):

    matrix = pd.DataFrame(
        0,
        index=actors,
        columns=actors
    )

    for actor in actors:
        matrix.loc[actor, actor] = 0

    return matrix
