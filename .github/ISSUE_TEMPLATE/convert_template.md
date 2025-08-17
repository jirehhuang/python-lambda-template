---
name: Convert template
about: Convert template
title: Convert template
labels: []
assignees: []
---

# Checklist

- [ ] Add `main` ruleset
- [ ] Update `FUNCTION_NAME` in [continuous_integration.yml](.github/workflows/continuous_integration.yml)
- [ ] Create Lambda execution role
- [ ] Modify the docstring in [`__init__.py`](lambda_function/__init__.py)
- [ ] Tailor the [README](README.md)
- [ ] Delete the issue template

# Instructions

## Add `main` ruleset

Create and activate a branch ruleset named `main ruleset` that applies to the default branch (`main`). Ensure the following are selected:

- Restrict deletions
- Require a pull request before merging
    - Require conversation resolution before merging
    - Automatically request Copilot code review
    - Allowed merge methods: Merge, Squash
- Block force pushes

## Create Lambda execution role

[Create Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html#permissions-executionrole-console) named `${FUNCTION_NAME}-role` with policy `AWSLambdaBasicExecutionRole`. Attach any additional policies that the function will require, such as `AmazonDynamoDBFullAccess`.
