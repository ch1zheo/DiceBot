# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.2.1] - 2026-11-03

### Added

- Automatic language detection based on the Telegram client language: Russian for Russian-language clients, English for everyone else.
- Translation package `locales/` with `en.py` and `ru.py`.
- English and Russian sections in `README.md`.
- `CONTRIBUTING.md` and `CHANGELOG.md`.
- GitHub Actions workflow that compiles the project and checks the import on Python 3.10 and 3.12.

### Changed

- Renamed the example environment file to `.env.example`.
- Documented the project structure and installation steps for Windows, Linux and macOS.

[Unreleased]: https://github.com/ch1zheo/DiceBot/compare/v2.2.1...HEAD
[2.2.1]: https://github.com/ch1zheo/DiceBot/releases/tag/v2.2.1
