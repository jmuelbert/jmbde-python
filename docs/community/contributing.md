# Contributing

Thank you for being interested in contributing to jmbde-python. There are many ways you can contribute to the project:

- Try jmbde-python and [report bugs/issues you find](https://github.com/jmuelbert/jmbde-python/issues/new)
- [Implement new features](https://github.com/jmuelbert/jmbde-python/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
- [Review Pull Requests of others](https://github.com/jmuelbert/jmbde-python/pulls)
- Write documentation
- Participate in discussions

## Reporting Bugs or Other Issues

Found something that jmbde-python should support? Stumbled upon some unexpected behavior?

Contributions should generally start out with [a discussion](https://github.com/jmuelbert/jmbde-python/discussions). Possible bugs may be raised as a "Potential Issue" discussion, feature requests may be raised as an "Ideas" discussion. We can then
determine if the discussion needs to be escalated into an "Issue" or not, or if we'd consider a pull request.

Try to be more descriptive as you can and in case of a bug report, provide as much information as possible like:

- OS platform
- Python version
- Installed dependencies and versions (`python -m pip freeze`)
- Code snippet
- Error traceback

You should always try to reduce any examples to the _simplest possible case_ that demonstrates the issue.

The usual process to make a contribution is to:

1. Check for existing related issues
1. Fork the repository and create a new branch
1. Make your changes
1. Make sure formatting, linting and tests passes.
1. Add tests if possible to cover the lines you added.
1. Commit, and send a Pull Request.

## Clone the repository

Clone the `jmbde-python` repository, `cd` into it, and create a new branch for your contribution:

```bash
cd jmbde-python
git checkout -b add-my-contribution
```

## Run the tests

Run the test suite while developing:

```bash
hatch run test
```

Run the test suite with coverage report:

```bash
hatch run cov
```

Run the extended test suite with coverage:

```bash
hatch run full
```

## Lint

Run automated formatting:

```bash
hatch run lint:fmt
```

Run full linting and type checking with ruff:

```bash
hatch fmt
```

Run linting with pylint:

```bash
hatch run lint:py-lint
```

Run pre-commit

```bash
hatch run check:precommit
```

## Docs

Start the documentation in development:

```bash
hatch run docs:serve
```

Build and validate the documentation website:

```bash
hatch run docs:build-check
```
