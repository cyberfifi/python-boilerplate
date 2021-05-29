# nemean
A python boilerplate repository. It has below features:

- Use [black](https://pypi.org/project/black/) for code formatting and linting.
- Use [pytest](https://pypi.org/project/pytest/) for unit testing.
- Use [pipenv](https://pypi.org/project/pipenv/) for dependency and runtime env management.
- Use [pre-commit](https://pypi.org/project/pre-commit/) for pre-commit hooks.

# Prerequisits
1. Install python3 and pipenv

# Getting Started
1. run `pipenv install && pipenv install --dev`. You only need to run this when the dependency is changed.
2. run `pipenv shell`
3. run `pre-commit install`
4. run `pipenv run python src/main.py`
