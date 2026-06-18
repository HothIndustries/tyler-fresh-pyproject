# tyler-fresh-pyproject

A very minimal Python project.

## Requirements

- Python 3.9+

## Run

```bash
python -m tyler_fresh_pyproject
```

## Copilot Cloud Agent

This repository includes a [Copilot setup steps file](.github/workflows/copilot-setup-steps.yml) that pre-configures the development environment when GitHub Copilot's cloud agent works on this repository.

### Allowing outbound API access (DNS firewall)

By default, Copilot's cloud agent runs behind an integrated DNS-based firewall that restricts outbound network access. If Copilot needs to reach an external API during a session (e.g. to run tests or fetch data), you have two options:

1. **Disable or customize the firewall** in your repository or organization settings — see the [GitHub docs on customizing or disabling the Copilot firewall](https://docs.github.com/enterprise-cloud@latest/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent) for step-by-step instructions.

2. **Configure a proxy** by setting the `https_proxy`, `http_proxy`, and/or `no_proxy` environment variables in the `copilot` GitHub Actions environment (repository **Settings → Environments → copilot**). These variables are automatically picked up by Copilot's agent at runtime:

   | Variable | Description |
   |---|---|
   | `https_proxy` | Proxy URL for HTTPS traffic (e.g. `http://proxy.local:8080`) |
   | `http_proxy` | Proxy URL for HTTP traffic |
   | `no_proxy` | Comma-separated list of hosts that bypass the proxy |
   | `ssl_cert_file` | Path to the SSL certificate presented by your proxy |

> **Note:** Environment variables that contain sensitive values (tokens, passwords) should be stored as GitHub Actions *secrets* in the `copilot` environment rather than plain variables.
