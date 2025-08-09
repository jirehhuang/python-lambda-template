---
name: Convert template
about: Convert template
title: Convert template
labels: []
assignees: []
---

# Checklist

- [ ] Add `main` ruleset
- [ ] Tailor the README
- [ ] Delete the issue template
- [ ] Modify the docstring in `__init__.py`

# Instructions

## Add `main` ruleset

You should create and activate a branch ruleset named `main ruleset` that applies to the default branch (`main`). Ensure the following are selected:

- Restrict deletions
- Require a pull request before merging
    - Require conversation resolution before merging
    - Automatically request Copilot code review
    - Allowed merge methods: Merge, Squash
- Block force pushes
