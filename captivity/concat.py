import pandas as pd
from typing import Iterable
import itertools

pd_concat = pd.concat


def captivity_concat(objs: Iterable[pd.DataFrame], axis, *args, **kwargs):
    if axis == 1 or axis == "columns":
        problematic_columns = set(
            c
            for (first, second) in itertools.combinations(objs, 2)
            for c in set(first.columns).intersection(second.columns)
        )
        if len(problematic_columns) > 0:
            from captivity import flag_issue

            flag_issue(
                f"Column-wise concatenation would result in duplicate column labels for column: {problematic_columns}"
            )
    else:
        problematic_columns = set.union(*[set(df.columns) for df in objs]).difference(
            set.intersection(*[set(df.columns) for df in objs])
        )
        if len(problematic_columns) > 0:
            from captivity import flag_issue

            flag_issue(
                f"Row-wise concatenation with dataframes with columns that are not present everywhere: {problematic_columns}"
            )

    return pd_concat(objs, axis=axis, *args, **kwargs)


pd.concat = captivity_concat
