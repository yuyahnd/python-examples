# PyPi 登録
- 参考
    - https://packaging.python.org/en/latest/tutorials/packaging-projects/
    - https://packaging.python.org/ja/latest/tutorials/packaging-projects/

- Python 3.9.6
- setuptools 58.0.4


## パッケージ作成

```
pypi-setuptools/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── example_package/
│       ├── __init__.py
│       └── example.py
└── tests/
```

## 必要ライブラリ
```
python3 -m pip install --upgrade pip
```

## ビルド
```
python3 -m pip install --upgrade build
python3 -m build
```

```
dist/
├── example_package-0.0.1-py3-none-any.whl
└── example_package-0.0.1.tar.gz
```

## .pypirc 作成
```
[distutils]
index-servers =
  pypi
  testpypi

[pypi]
repository=https://upload.pypi.org/legacy/
username=USER_NAME
password=password!

[testpypi]
repository=https://test.pypi.org/legacy/
username=USER_NAME
password=password!
```

## 配布物アーカイブをアップロードする
```
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```

```
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: __token__
Uploading example_package-0.0.1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 kB • 00:01 • ?
Uploading example_package-0.0.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 kB • 00:00 • ?
```

## 配布物テスト
```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package
```
## 本番 　PyPi　登録
```
python3 -m twine upload --repository pypi dist/*
```
