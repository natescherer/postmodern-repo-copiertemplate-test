# Postmodern Repo Copier Template

[![All Contributors](https://img.shields.io/github/all-contributors/natescherer/postmodern-repo-copiertemplate?color=ee8449&style=flat-square)](#contributors)
| :exclamation:  Notice: This project is currently in a Pre-Alpha state and is not ready for public use.  |
|-----------------------------------------|

A [Copier][copier] template for creating a basic repository with full, all-the-bells-and-whistles CI/CD. (And for creating other templates!)

This template is heavily inspired by the [Hypermodern Python Cookiecutter](hypermodern-cc).

Why Postmodern? Besides being a cheeky homage to this template's inspiration, I think that Postmodern philosophy's idea of the relativity of truth applies very well to software. There's no objectively best way to do CI/CD, this is just one way that works, and it might work for you too!

## Included Features

### Core

#### Support for Multiple CI/CD Platforms

- GitHub **Recommended**
   - Creating repos under both users and orgs is supported
   - See [GitHub Org Limitations](docs/github_org_limitations.md) for details about template features excluded for Orgs
- Azure DevOps
   - See [Azure DevOps Limitations](docs/azure_devops_limitations.md) for details about features missing for AzDO

#### Support for Public (Open-Source) and Private (Closed-Source) Repositories

This template fully supports both public/open-source and private/closed-source repositories. See [Public vs Private Repos](docs/public_vs_private_repos.md) for the difference.

#### Support for Existing Projects

Postmodern templates are designed to allow either the creation of new templates from scratch or adoption for existing projects with existing code repos.

#### Support for Template Updates

Keeping projects in sync with their parent template is a core feature of [Copier][copier], and this template will deploy a GitHub Actions Workflow/Azure DevOps Pipeline that will automate the update process.

#### Support for Child/Recursive Templates

It is highly encouraged for you to take this template and make your own child template that meets your needs. Your child template can (optionally) receive updates from this template.

### Repository Management

- Creation of new repos and `initial` branch containing template code
- Setting of repo settings & branch protection rules
- Creation of useful non-default issue labels: `awaiting pr` and `blocked`
- Contributor management and crediting via [All Contributors][all-contributors]
- GitHub Actions dependency updating via [Dependabot][dependabot]
- Synchronization with updates to this template via [cruft][cruft]
- (Optional) Secret management via [Doppler][doppler]

### Code Management and Formatting

- Code formatting (YAML and Markdown) via [Prettier][prettier]

### CI/CD

- [SemVer][semver] version number calculation via [GitVersion][gitversion]
- Changelog creation and upkeep in [Keep a Changelog][keep-a-changelog] format
- Simple/example release workflow via GitHub Actions

### Support Files

- `.gitignore`, set to ignore macOS `.DS_Store` files and Windows `Thumbs.db` files
- `CODE_OF_CONDUCT.md`, derived from [The Contributor Covenant][contributor-covenant]
- `CONTRIBUTING.md`, designed help novices to make their first contribution
- `LICENSE`, a copy of the [MIT License][mit-license]
- `README.md`, designed for general products

## Prerequisites

### Your Machine

There are two ways to install the prerequisites needed on your machine: running them inside of a [devcontainer][devcontainer], or installing them manually. Please see linked documentation for details:

[Prerequisites via Devcontainer](docs/prereqs_devcontainer.md) **Recommended**

[Prerequisites via Manual Installation](docs/prereqs_manual.md)

### GitHub

### One-Time Actions for all Postmodern repositories

1. Install the [AllContributors GitHub App][all-contributors-app] for your user or organization.
   - You can either give it access to all your repositories, which means you only need to do this step once, or you can select repositories individually, in which case you will need to do this for each new repo you create.
1. Ensure `Private vulnerability reporting > Automatically enable for new public repositories` is checked [here](https://github.com/settings/security_analysis).
1. Set up the Trunk.io GitHub integration using [their instructions](trunk-github-setup)
   - You can either give it access to all your repositories, which means you only need to do this step once, or you can select repositories individually, in which case you will need to do this for each new repo you create.

### Per-Repository Actions

1. (If using Doppler for secret management) Ensure you have a [Doppler][doppler] account created, then set up the GitHub Actions integration via [these instructions][doppler-actions-instructions].
   - This only needs done once for all repositories

## Using this template

1. Open a terminal to the parent directory where you want the repo subdirectory to be created
1. Run the following to initialize the template (and the linked GitHub repo):

   ```bash
   copier copy --trust gh:natescherer/postmodern-repo-template .
   ```

## Questions/Comments

If you have questions, comments, etc, please enter a GitHub Issue with the "question" tag.

## Contributing/Bug Reporting

Contributions and bug reports are gladly accepted! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/natescherer"><img src="https://avatars.githubusercontent.com/u/376408?v=4?s=100" width="100px;" alt="Nate Scherer"/><br /><sub><b>Nate Scherer</b></sub></a><br /><a href="#code-natescherer" title="Code">💻</a> <a href="#maintenance-natescherer" title="Maintenance">🚧</a> <a href="#doc-natescherer" title="Documentation">📖</a> <a href="#infra-natescherer" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/apps/github-actions"><img src="https://avatars.githubusercontent.com/in/15368?v=4?s=100" width="100px;" alt="github-actions[bot]"/><br /><sub><b>github-actions[bot]</b></sub></a><br /><a href="#maintenance-github-actions[bot]" title="Maintenance">🚧</a> <a href="#code-github-actions[bot]" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://allcontributors.org) specification.
Contributions of any kind are welcome!

## License

This project is licensed under The MIT License - see [LICENSE](LICENSE) for details.

## Repository Template

This repository is based on the template of itself. Neat, huh?

[all-contributors]: https://allcontributors.org/
[all-contributors-app]: https://github.com/apps/allcontributors/installations/new
[copier]: https://github.com/copier-org/copier
[contributor-covenant]: https://www.contributor-covenant.org/
[cruft]: https://cruft.github.io/cruft/
[dependabot]: https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide
[devcontainer]: https://containers.dev/
[doppler]: https://www.doppler.com
[doppler-actions-instructions]: https://docs.doppler.com/docs/github-actions
[gitversion]: https://gitversion.net/
[hypermodern-cc]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[keep-a-changelog]: https://keepachangelog.com/en/1.1.0/
[mit-license]: https://choosealicense.com/licenses/mit/
[prettier]: https://prettier.io/
[semver]: https://semver.org/
[trunk-github-setup]: https://docs.trunk.io/check/check-cloud-ci-integration/get-started
