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
- [ ] Add API Gateway trigger

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

[Create Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html#permissions-executionrole-console) named `{FUNCTION_NAME}-role` with policy `AWSLambdaBasicExecutionRole`. Attach any additional policies that the function will require, such as `AmazonDynamoDBFullAccess`.

## Add API Gateway trigger

After creating the pull request for this convert template issue, a Lambda named `FUNCTION_NAME` should be created by the workflow. 

1. Create REST API
    1. Navigate to AWS Console > API Gateway > Create API > REST API (Build)
    1. New API, API name: `FUNCTION_NAME`, API Endpoint type: Regional > Create API
1. Add proxy resources
    1. Create resource > Resource path: /, Resource name: staging > Create resource
    1. Create resource > Proxy resource: True, Resource path: /staging/, Resource name: {proxy+} > Create resource
1. Add ANY method with Lambda proxy integration
    1. Select /staging/{proxy+}/ANY > Edit integration
    1. Select Lambda function, appropriate region, and ARN for `FUNCTION_NAME`
    1. Append `:{FUNCTION_NAME}-staging` to the Lambda function ARN (e.g., `...function:python-lambda-template:python-lambda-template-staging`) > Save
1. Require API key
    1. Select /staging/{proxy+}/ANY > Method request > Edit
    1. API key required: True > Save
1. Deploy API > Stage: No stage
1. Create usage plan and API keys
    1. Usage plans > Create usage plan > Name: `{FUNCTION_NAME}-plan-staging`
    1. Associated API keys > Add API key > Create and add new key, Name: `{FUNCTION_NAME}-api-key-staging`
    1. [Add to GitHub Actions Secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets) as `STAGING_API_KEY`

After merging the pull request into `main`, repeat these steps for "prod" in place of "staging" and re-run the workflow.
