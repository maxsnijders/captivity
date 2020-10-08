import pytest


def test_concat_with_duplicate_columns():
    import captivity
    import pandas as pd

    with pytest.raises(captivity.CaptivityException):
        pd.concat(
            [pd.DataFrame({"a": [1], "b": [2]}), pd.DataFrame({"c": [0], "b": [3]}),],
            axis=1,
        )

    pd.concat(
        [pd.DataFrame({"a": [1], "b": [2]}), pd.DataFrame({"c": [0], "b": [3]}),],
        axis=0,
    )
