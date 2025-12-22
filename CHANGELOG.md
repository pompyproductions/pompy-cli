# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Colors!** A `style()` function that "style" a string with ANSI escape sequences, and a "padding" option to add spaces left and right.
- **Prompts!** You can now `prompt_str` to get any input, `prompt_bool` to get a yes or no, `prompt_int` for a valid integer, and `prompt_opt` to get the user's choice from a list of `Option`s.
- **Context!** An optional `CLIContext` object you can use as a configurable alternative to the functions.
- **Styled headers!** `CLIContext` accepts a `Header`, that is printed on top & refreshed on "clear".
- **Utilities!** `clear` for clearing the terminal, and `get_input` which just applies default styling to a regular `input` call.
- **Help pages!** `prompt_opt` supports "help" and "quit" commands.
- **Demos!** You can check out the basic functionality by running `demo_basic.py` or `demo_context.py` as main.

## [v0.1.0] — Hello World! (2025-12-06)

This is the starting point for the project. Just a package you can install via PyPI that you can use to print some kind of "Hello World". Bleak yet brimming with potential!