# Contributing guide

## Usage

New system:

- [Install pipx](https://pipx.pypa.io/stable/installation/)
- [Install poetry](https://python-poetry.org/docs/#installing-with-pipx)
- [Install poetry-shell-plugin](https://github.com/python-poetry/poetry-plugin-shell)

New clone of a repository:

```
poetry install
poetry run pre-commit install --hook-type pre-commit --hook-type commit-msg
poetry env use pythonX.Y
```

New terminal:

```
poetry shell
```

New code:

```
pytest tests
```

New staged changes:

```
pre-commit run
```
