# Contributing guide

## Usage

### New AWS user

1. [Create an AWS account](https://signin.aws.amazon.com/signup?request_type=register)
2. [Add the GitHub OIDC identity provider to AWS IAM](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws#adding-the-identity-provider-to-aws)
3. [Create GitHub OIDC deploy role](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws#configuring-the-role-and-trust-policy)
	1. IAM > Roles > Create role
	2. Trusted entity type: Web identity
	3. Identity provider: http://tokens.actions.githubusercontent.com/ (created in previous step)
	4. Specify GitHub organization (`org`), repository, and branch
	5. Add permissions: `AWSLambda_FullAccess`, `IAMReadOnlyAccess`, and `AmazonAPIGatewayAdministrator`
	6. Role name:` github-{org}-oidc-lambda-deployer`
	7. Update `GH_OIDC_ROLE_NAME` in [continuous_integration.yml](.github/workflows/continuous_integration.yml)

### New system

1. Install [pyenv](https://github.com/pyenv/pyenv) and install Python X.Y
2. [Install pipx](https://pipx.pypa.io/stable/installation/)
3. [Install poetry](https://python-poetry.org/docs/#installing-with-pipx) with Python X.Y
4. Install [poetry-shell-plugin](https://github.com/python-poetry/poetry-plugin-shell)

### New Lambda project

1. Use this template > Create a new repository
2. Issues > New issue > Convert template
3. After the Lambda function is created in the convert template PR, add API Gateway

### New clone of repository

```
poetry install
poetry run pre-commit install --hook-type pre-commit --hook-type commit-msg
poetry env use pythonX.Y
```

### New terminal

```
poetry shell
```

### New code

```
pytest tests

pylint **/*.py
```

### New staged changes

```
pre-commit run
```
