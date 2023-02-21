import pytest
from pathlib import Path

@pytest.fixture(scope="session")
def tmp_file(tmpdir_factory) -> str:
    """テスト全体で利用する処理を conftext.py に記述して共有できる。

    tmpdir_factory は、pytest が一時的にディレクトリを作成して渡してくれる。
    本処理は、一時ディレクトリに pytest_dir を作成して、
    その中の tmp.txt ファイルまでのパスを作成して返す。

    Parameters
    ----------
    tmpdir_factory : _pytest._py.path.LocalPath
        一時ディレクトリオブジェクト

    Returns
    -------
    str
        一時ファイルパス
    """
    tmp_file = tmpdir_factory.mktemp("pytest_dir").join("tmp.txt")
    return str(tmp_file)


@pytest.fixture(scope="session")
def data_txt() -> str:
    dir = Path(__file__).parent
    data_dir = dir.joinpath("data")
    return str(data_dir.joinpath("data.txt"))
