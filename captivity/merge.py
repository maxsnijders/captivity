import pandas as pd
from typing import Iterable


pd_merge = pd.merge


def captivity_merge(
    left: pd.DataFrame, right: pd.DataFrame, on: Iterable[str], *args, **kwargs
):
    from captivity import flag_issue

    problematic_columns = (
        set(left.columns).intersection(set(right.columns)).difference(on)
    )
    if len(problematic_columns) > 0:
        flag_issue(
            f"Merging dataframes with overlapping column names that are not in the on parameter is a bad idea. Problematic columns: {problematic_columns}"
        )
    return pd_merge(left=left, right=right, on=on, *args, **kwargs)


pd.DataFrame.merge = captivity_merge
pd.merge = captivity_merge
