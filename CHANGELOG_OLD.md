# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Have release workflows force merge release PRs

## [0.1.69] - 2024-08-29
### Fixed
- Synchronized files from root into template
- Azure DevOps template functions fixed to not use old Python library

## [0.1.68] - 2024-08-27
### Changed
- Devcontainer moved to use Python 3.12 and versioned requirements
- Azure DevOps Python library dependency removed

### Fixed
- Azure DevOps pipeline creation

## [0.1.67] - 2024-04-06
### Fixed
- Formatting of include in copier.yml

## [0.1.66] - 2024-04-06
### Fixed
- Add dummy question to override file

## [0.1.65] - 2024-04-06
### Added 
- Question override file for child templates

## [0.1.64] - 2024-04-05
### Added
- Stage, job, and explicit pool in Azure DevOps release pipeline

## [0.1.63] - 2024-04-05
### Fixed
- Bad indent in Azure DevOps release pipeline

## [0.1.62] - 2024-04-05
### Fixed
- Subtemplate generation for Azure DevOps

## [0.1.61] - 2024-04-05
### Changed
- Improve copier.yml formatting

## [0.1.60] - 2024-04-05
### Fixed
- Bad URL construction for azdo projects with spaces

## [0.1.59] - 2024-04-05
### Fixed
- Properly escape Azure DevOps projects with spaces

## [0.1.58] - 2024-04-05
### Fixed
- Restore folder wiping
- Raw out parts of github release workflow

## [0.1.57] - 2024-04-05
### Fixed
- Don't wipe target folders as part of subtemplate

## [0.1.56] - 2024-04-05
### Fixed
- URL generation in workflow

## [0.1.55] - 2024-04-05
### Fixed
- Use Force instead of Hidden on Get-ChildItem

## [0.1.54] - 2024-04-05
### Fixed
- Use same renaming format both ways for subtemplate

## [0.1.53] - 2024-04-05
### Fixed
- Ensure hidden files are processed for subtemplate rename

## [0.1.52] - 2024-04-05
### Fixed
- Fix params for Move-Item

## [0.1.51] - 2024-04-05
### Fixed
- Use Move-Item instead of Rename-Item

## [0.1.50] - 2024-04-05
### Fixed
- Force pwsh renames

## [0.1.49] - 2024-04-05
### Fixed
- Target correct directory for file renames

## [0.1.48] - 2024-04-05
### Fixed
- Reformat pwsh oneliners

## [0.1.47] - 2024-04-05
### Fixed
- Have rename-template-files task remove directories if there would be a conflict

## [0.1.46] - 2024-04-05
### Fixed
- Wrap square bracket for pwsh

## [0.1.45] - 2024-04-05
### Fixed
- Escape square bracket for pwsh

## [0.1.44] - 2024-04-05
### Fixed
- Use pwsh for rename-template-files task

## [0.1.43] - 2024-04-05
### Fixed
- Fix bad variables for move targets

## [0.1.42] - 2024-04-05
### Fixed
- Try using shutil.copytree for directory rename

## [0.1.41] - 2024-04-05
### Fixed
- Try another method of renaming

## [0.1.40] - 2024-04-05
### Fixed
- Try renaming just files as part of rename-template-files

## [0.1.39] - 2024-04-05
### Fixed
- Switch rename-template-files back to shutil.move
- Change how folders are renamed

## [0.1.38] - 2024-04-05
### Fixed
- Change how rename-template-files target paths are build

## [0.1.37] - 2024-04-05
### Fixed
- Reorder rename-template-files operations

## [0.1.36] - 2024-04-05
### Fixed
- Fix rename-template-files task root path

## [0.1.35] - 2024-04-05
### Fixed
- Update rename-template-files task to only alter files in template, not subtemplate

## [0.1.34] - 2024-04-05
### Fixed
- Fixed root path for rename-template-files task

## [0.1.33] - 2024-04-05
### Fixed
- rename-template-files task will now overwrite files

## [0.1.32] - 2024-04-05
### Added
- Dynamic repo URL in workflow doc

### Fixed
- New renaming-based subtemplate methodology

## [0.1.31] - 2024-04-05
### Fixed
- Fix bad template subtemplate generation

## [0.1.30] - 2024-04-05
### Fixed
- Whitespace issues in github release workflow
- Remove unneeded .versionrc.json

## [0.1.29] - 2024-04-04
### Fixed
- Remove now-defunct tarball from delete-unneeded-template-files task

## [0.1.28] - 2024-04-04
### Changed
- Root-level files synchronized into template
- Switch subtemplate generation from zip to copying to a subdirectory

## [0.1.27] - 2024-04-04
### Fixed
- Tagging in Azure DevOps repos

## [0.1.26] - 2024-04-04
### Fixed
- Ensure tasks.py exists for Standard projects

## [0.1.25] - 2024-04-04
### Fixed
- Typo in deleted-unneeded-template-files task name

## [0.1.24] - 2024-04-04
### Fixed
- Remove template-only files from being laid down in Standard mode
- Bad indentation in copier.yml tasks
- Removed hardcoded test repo name from create-pipelines-azdo task

## [0.1.23] - 2024-04-03
### Fixed
- Bad copier task names

## [0.1.22] - 2024-04-03
### Changed
- Switch to using tarball for template copy

### Fixed
- Tarball deletion will gracefully fail if file is missing

## [0.1.21] - 2024-04-03
### Fixed
- Escaping in github release workflows

## [0.1.20] - 2024-04-03
### Fixed
- Ensure template_copy.zip is included in release tag

## [0.1.19] - 2024-04-03
### Added
- Add full automation for template inheritance links

## [0.1.18] - 2024-04-03
### Added
- Make template inheritance links (somewhat) dynamic

### Fixed
- Commit formatting on Azure DevOps pipelines autocommits

## [0.1.17] - 2024-04-03
### Fixed
- Actually fix versionrc.json parserOpts for Azure DevOps

## [0.1.16] - 2024-04-03
### Fixed
- Jinja whitespace formatting in README docs
- versionrc.json parserOpts for Azure DevOps
- extract-changelog-release removed when in Keep a Changelog mode

## [0.1.15] - 2024-04-03
### Added
- Add Azure DevOps template release pipeline
- Add Azure DevOps pipeline creation

## [0.1.14] - 2024-04-02
### Fixed
- Fix run statements in release workflows

## [0.1.13] - 2024-04-02
### Added
- Support for choosing between Keep a Changelog and Conventional Changelog

### Fixed
- Update bad variable in standard project readme
- 'template_copy.zip' will no longer be committed to git for template repos

### Changed
- GitVersion replaced with commit-and-tag-version

## [0.1.12] - 2024-04-01
### Fixed
- Actually fix is_prerelease computer value in copier.yml

## [0.1.11] - 2024-04-01
### Fixed
- is_prerelease computer value in copier.yml

## [0.1.10] - 2024-04-01
### Fixed
- Lifecycle question in copier.yml

## [0.1.9] - 2024-04-01
### Fixed
- Remove copier.yml 'when' statements that caused important answers to be lost on template updates
- Remove template_copy.zip before generating new one

## [0.1.8] - 2024-04-01
### Added
- Project lifecycle state management

### Fixed
- Project name in template README

## [0.1.7] - 2024-03-30
### Fixed
- Attempt to unbreak copier.yml

## [0.1.6] - 2024-03-30
### Added
- Release PRs will now automerge

### Fixed
- Validators won't block upgrades anymore
- Documentation is automatically chosen
- Disable validators to allow updating

## [0.1.4] - 2024-03-28
### Fixed
- License file generation
- Better handling of tags and repo rulesets already existing

## [0.1.3] - 2024-03-28
### Fixed
- GitHub tags are only created when they don't already exist (attempt 2)

## [0.1.2] - 2024-03-28
### Fixed
- GitHub tags are only created when they don't already exist

## [0.1.1] - 2024-03-28
### Fixed
- Tagging of proper commit in releases
- Creation of sub-templates

## [0.1.0] - 2024-03-27
### Added
- Initial release

[Unreleased]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.69..HEAD
[0.1.69]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.68..v0.1.69
[0.1.68]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.67..v0.1.68
[0.1.67]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.66..v0.1.67
[0.1.66]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.65..v0.1.66
[0.1.65]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.64..v0.1.65
[0.1.64]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.63..v0.1.64
[0.1.63]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.62..v0.1.63
[0.1.62]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.61..v0.1.62
[0.1.61]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.60..v0.1.61
[0.1.60]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.59..v0.1.60
[0.1.59]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.58..v0.1.59
[0.1.58]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.57..v0.1.58
[0.1.57]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.56..v0.1.57
[0.1.56]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.55..v0.1.56
[0.1.55]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.54..v0.1.55
[0.1.54]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.53..v0.1.54
[0.1.53]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.52..v0.1.53
[0.1.52]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.51..v0.1.52
[0.1.51]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.50..v0.1.51
[0.1.50]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.49..v0.1.50
[0.1.49]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.48..v0.1.49
[0.1.48]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.47..v0.1.48
[0.1.47]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.46..v0.1.47
[0.1.46]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.45..v0.1.46
[0.1.45]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.44..v0.1.45
[0.1.44]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.43..v0.1.44
[0.1.43]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.42..v0.1.43
[0.1.42]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.41..v0.1.42
[0.1.41]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.40..v0.1.41
[0.1.40]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.39..v0.1.40
[0.1.39]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.38..v0.1.39
[0.1.39]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.38..v0.1.39
[0.1.38]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.37..v0.1.38
[0.1.37]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.36..v0.1.37
[0.1.36]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.35..v0.1.36
[0.1.35]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.34..v0.1.35
[0.1.34]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.33..v0.1.34
[0.1.33]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.32..v0.1.33
[0.1.32]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.31..v0.1.32
[0.1.31]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.30..v0.1.31
[0.1.30]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.29..v0.1.30
[0.1.29]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.28..v0.1.29
[0.1.28]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.27..v0.1.28
[0.1.27]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.26..v0.1.27
[0.1.26]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.25..v0.1.26
[0.1.25]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.24..v0.1.25
[0.1.24]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.23..v0.1.24
[0.1.23]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.22..v0.1.23
[0.1.22]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.21..v0.1.22
[0.1.21]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.20..v0.1.21
[0.1.20]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.19..v0.1.20
[0.1.19]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.18..v0.1.19
[0.1.18]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.17..v0.1.18
[0.1.17]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.16..v0.1.17
[0.1.16]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.15..v0.1.16
[0.1.15]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.14..v0.1.15
[0.1.14]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.13..v0.1.14
[0.1.13]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.12..v0.1.13
[0.1.12]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.11..v0.1.12
[0.1.11]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.10..v0.1.11
[0.1.10]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.9..v0.1.10
[0.1.9]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.8..v0.1.9
[0.1.8]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.7..v0.1.8
[0.1.7]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.6..v0.1.7
[0.1.6]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.4..v0.1.6
[0.1.5]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.5..v0.1.5
[0.1.5]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.4..v0.1.5
[0.1.4]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.3..v0.1.4
[0.1.3]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.2..v0.1.3
[0.1.2]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.1..v0.1.2
[0.1.1]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.0..v0.1.1
[0.1.1]: https://github.com/natescherer/postmodern-repo-copiertemplate/compare/v0.1.0..v0.1.1
[0.1.0]: https://github.com/natescherer/postmodern-repo-template/tree/v0.1.0