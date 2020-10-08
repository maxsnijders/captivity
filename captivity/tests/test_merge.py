import pytest

def test_merge_with_duplicate_columns():
    import captivity
    import pandas as pd

    with pytest.raises(captivity.CaptivityException):
        pd.DataFrame({"a": [1], "b": [2]}).merge(
            pd.DataFrame({"a": [0, 2], "b": [3, 4]}),
            on="a",
        )

    captivity.warning_mode()
    with pytest.warns(captivity.CaptivityWarning):
        pd.DataFrame({"a": [1], "b": [2]}).merge(
            pd.DataFrame({"a": [0, 2], "b": [3, 4]}),
            on=["a"],
        )

    captivity.exception_mode()
    with pytest.raises(captivity.CaptivityException):
        pd.DataFrame({"a": [1], "b": [2]}).merge(
            pd.DataFrame({"a": [0, 2], "b": [3, 4]}),
            on="a",
        )

    pd.DataFrame({"a": [1], "b": [2]}).merge(
        pd.DataFrame({"a": [0, 2], "b": [3, 4]}),
        on=["a", "b"],
    )
