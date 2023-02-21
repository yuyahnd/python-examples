# pytest
- 参考
    - https://docs.pytest.org/en/7.2.x/

## pyproject.toml 記述

```toml title="pyproject.toml"
[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = [
    "tests",
    "integration",
]
```

## pytest.ini 記述

```ini title="pytest.ini"
[pytest]
pythonpath = src
testpaths = 
    test
    integration
```

## tox.ini 記述

```ini title="tox.ini"
[pytest]
pythonpath = src
testpaths =
    tests
    integration
```
