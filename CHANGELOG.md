# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Colors! A `style()` function that "style" a string with ANSI escape sequences.
- Prompts! You can now `prompt_str` to get any input, `prompt_bool` to get a yes or no, `prompt_int` for a valid integer, and `prompt_opt` to get the user's choice from a list of `Option`s.
- Some utilities: `clear` for clearing the terminal, and `get_input` which just applies default styling to a regular `input` call.

## [v0.1.0] - Hello World!

This is the starting point for the project. Just a package you can install via PyPI that you can use to print some kind of "Hello World". Bleak yet brimming with potential!