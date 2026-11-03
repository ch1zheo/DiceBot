# Contributing to DiceBot

Thanks for taking the time to improve DiceBot.

## Reporting bugs

Open an issue and include:

- what you expected to happen and what actually happened;
- steps to reproduce the problem;
- your operating system and Python version;
- the relevant part of the console output, with the bot token removed.

## Suggesting features

Open an issue and describe the use case behind the idea. Keep the scope small: DiceBot is a deliberately simple bot.

## Pull requests

1. Branch from `main`.
2. Keep one change per pull request.
3. Match the existing code style.
4. User-facing strings and buttons are localized: add or update every text in both `locales/en.py` and `locales/ru.py`, and never hardcode user-facing text in `main.py`. Console logs stay in Russian.
5. Run the bot manually with a test token and check `/start`, `/dice` and the reply-keyboard button with both a Russian-language and an English-language Telegram client.
6. Add an entry under `[Unreleased]` in [CHANGELOG.md](CHANGELOG.md).
7. Never commit secrets: keep your token in `.env`, which is ignored by Git.
8. Describe how you tested the change in the pull request.

## Questions

If something is unclear, open an issue and ask before writing code.
