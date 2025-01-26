# Security and Linting

## Security Checks
- **`pip-audit`**: Scans for dependency vulnerabilities.
- **`safety`**: Checks known vulnerabilities in dependencies.
- **`bandit`**: Performs static analysis for Python code.

## How to Run
Use Hatch for streamlined checks:
```bash
hatch run security:all
