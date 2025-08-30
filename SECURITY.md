# Security Policy

## Supported Versions

We are committed to maintaining the security of the MKZenith project. Below you'll find information about our security policy and how to report vulnerabilities.

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1   | :x:                |

## Reporting a Vulnerability

We take all security vulnerabilities seriously. Thank you for improving the security of our open-source software. We appreciate your efforts and responsible disclosure and will make every effort to acknowledge your contributions.

### How to Report a Security Vulnerability

Please report (suspected) security vulnerabilities by emailing security@mkworldwide.ai. You will receive a response within 48 hours. If the issue is confirmed, we will release a patch as soon as possible depending on complexity but historically within a few days.

### Security Updates and Advisories

Security updates will be released as minor or patch version updates following [Semantic Versioning](https://semver.org/). All security advisories will be published as GitHub Security Advisories in the [Security Advisories](https://github.com/MKWorldWide/MKZenith/security/advisories) section.

## Secure Development Practices

### Dependencies

We take the following steps to ensure the security of our dependencies:
- Dependencies are regularly audited using `safety` and GitHub's Dependabot
- All dependencies are pinned to specific versions in `requirements.txt`
- Security updates are applied as soon as possible after being released

### Code Review

All code changes must go through a pull request review process where at least one maintainer must approve the changes before merging. Security-sensitive changes require additional review.

### Automated Security Testing

Our CI pipeline includes the following security checks:
- Static code analysis with `bandit`
- Dependency vulnerability scanning with `safety`
- Secret scanning to prevent accidental exposure of credentials

## Security Best Practices for Users

### Secure Configuration

- Always use the latest version of MKZenith
- Store sensitive information (API keys, credentials) in environment variables, not in code
- Use the principle of least privilege when setting up service accounts and API keys
- Regularly rotate your API keys and credentials

### Reporting Security Issues

When reporting security issues, please include:
- A description of the vulnerability
- Steps to reproduce the issue
- The version of MKZenith you're using
- Any relevant logs or error messages

## Security Updates

Security updates are released as soon as possible. We recommend always using the latest stable release to ensure you have the most recent security patches.

## Security Disclosures

For any security-related questions or concerns, please contact us at security@mkworldwide.ai.

## Security Acknowledgments

We would like to thank the following individuals and organizations for responsibly disclosing security issues and helping us improve the security of MKZenith:

- [Your Name Here] - For being a responsible security researcher

## Legal

By reporting security issues, you agree that you will not publicly disclose the vulnerability until we have had a reasonable amount of time to address it. We will work with you to ensure that the vulnerability is properly fixed and that a security advisory is published.
