# pyproject-setuptools
- 参考
    - https://packaging.python.org/ja/latest/specifications/declaring-project-metadata/

# setuptools 宣言

```
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

## 名称
```
[project]
name = "example_setuptools"
```

## version
```
[project]
version = "2020.0.0"
```

バージョンを動的にソースから指定する場合は、以下。
```
[project]
dynamic = ["version"]

[tool.setuptools.dynamic]
version = {attr = "example_setuptools.__version__"}
```

## 説明
```
[project]
description = "A small example setuptools"
```

## readme
```
[project]
# A single pyproject.toml file can only have one of the following.
readme = "README.md"
readme = "README.rst"
readme = {file = "README.txt", content-type = "text/markdown"}
```

## requires-python
```
[project]
requires-python = ">=3.8"
```

## ライセンス
```
[project]
# A single pyproject.toml file can only have one of the following.
license = {file = "LICENSE"}
license = {text = "MIT License"}
```

## authors/maintainers
```
[project]
authors = [
  {name = "Pradyun Gedam", email = "pradyun@example.com"},
  {name = "Tzu-Ping Chung", email = "tzu-ping@example.com"},
  {name = "Another person"},
  {email = "different.person@example.com"},
]
maintainers = [
  {name = "Brett Cannon", email = "brett@python.org"}
]
```

## keywords
プロジェクトのキーワードを指定する。
```
[project]
keywords = ["egg", "bacon", "sausage", "tomatoes", "Lobster Thermidor"]
```

## 分類詞 <classifiers>
```
[project]
classifiers = [
  "Development Status :: 4 - Beta",
  "Programming Language :: Python"
]
```

## urls
```
[project.urls]
homepage = "https://example.com"
documentation = "https://readthedocs.org"
repository = "https://github.com/me/spam.git"
changelog = "https://github.com/me/spam/blob/master/CHANGELOG.md"
```

## エントリポイント
```
[project.scripts]
spam-cli = "spam:main_cli"

[project.gui-scripts]
spam-gui = "spam:main_gui"

[project.entry-points."spam.magical"]
tomatoes = "spam:main_tomatoes"
```

## dependencies/optional-dependencies
```
[project]
dependencies = [
  "httpx",
  "gidgethub[httpx]>4.0.0",
  "django>2.1; os_name != 'nt'",
  "django>2.0; os_name == 'nt'",
]

[project.optional-dependencies]
gui = ["PyQt5"]
cli = [
  "rich",
  "click",
]
```

## dynamic
```
dynamic = ["version", "description", "optional-dependencies"]
```
