import pytest
import example_pytest as ex

# a, b　の値を組み合わせてテスト
@pytest.mark.parametrize("a", [1, 2, 3, 0])
@pytest.mark.parametrize("b", [1, 2, 3, 4])
def test_addition(a, b):
    result = ex.addition(a, b)
    assert result == (a + b)

@pytest.mark.parametrize("a", [1, 2, 3, 0])
@pytest.mark.parametrize("b", [1, 2, 3, 4])
def test_subtraction(a, b):
    result = ex.subtraction(a, b)
    assert result == (a - b)


@pytest.mark.parametrize("a", [1, 2, 3, 0])
@pytest.mark.parametrize("b", [1, 2, 3, 4])
def test_multiplication(a, b):
    result = ex.multiplication(a, b)
    assert result == (a * b)


# 組み合わせを指定し、期待する結果と比較する
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1.0),
    (2, 1, 2.0),
    (5, 2, 2.5),
    (1, 0, ZeroDivisionError),
])
def test_division(a, b, expected):
    try:
        result = ex.division(a, b)
        assert result == expected
    except ZeroDivisionError as e:
        assert isinstance(e, expected)


def test_file(tmp_file):
    """conftest.py に定義した def tmp_file の復帰地を tmp_file 変数を指定して受け取る

    Parameters
    ----------
    tmp_file : str
        一時ファイルパス
    """
    print(tmp_file)
    assert isinstance(tmp_file, str)
