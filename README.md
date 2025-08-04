# ShellRosetta Project Analysis & Implementation Summary

**Translate Linux/Bash commands to PowerShell and vice versa—flags, pipes, networking, and more.**

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![Shell](https://img.shields.io/badge/shell-interactive-blue)](#interactive-shell-mode)
[![Tested](https://img.shields.io/badge/Tests-passing-brightgreen)](tests/)
[![PyPI version](https://badge.fury.io/py/shellrosetta.svg)](https://pypi.org/project/shellrosetta/)

---

## What is ShellRosetta?

ShellRosetta is a cross-platform CLI tool for developers, sysadmins, and anyone switching between Windows and Linux.

It instantly translates commands—including flags and arguments—between Linux/Bash and PowerShell. No more flipping between cheat sheets or Stack Overflow!

---

## Features

- 🖥️ **Interactive Shell Mode!** Open ShellRosetta as a REPL and translate commands live, just like in a real shell.
- 🔄 **Bi-directional translation:** Linux ↔ PowerShell, with accurate mappings for real-world scenarios.
- 🏷️ **Flag and multi-flag aware:** Understands combos like `ls -alh`, `rm -rf`, etc.
- 🔗 **Pipeline support:** Handles piped commands (e.g. `ls -l | grep foo`).
- 🌐 **Networking and system commands:** Supports `ping`, `curl`, `Get-NetTCPConnection`, and many more.
- 📋 **Extensive mappings:** Permissions, archiving, users, process management, environment variables, I/O redirection, and more.
- 🚦 **Helpful notes:** Outputs usage tips or warnings if there's no direct translation or if a flag behaves differently.
- 🧩 **Easily extensible:** Add or edit mappings in `mappings.py`—grow as you learn!
- ⚡ **Ready for shell aliases & tab-completion:** Bash/Zsh completion script included.
- 🤖 **Machine Learning Integration:** Learns from your translations and provides smart suggestions.
- 🔌 **Plugin System:** Extensible architecture with built-in plugins for Docker, Kubernetes, AWS, and Git.
- 🌐 **Web API:** REST API and beautiful web interface for programmatic access.
- 📊 **Advanced Features:** AST parsing, configuration management, and comprehensive testing.

---

## What's New in v1.1.0

- ✅ **Fixed all markdownlint formatting issues** in documentation
- ✅ **Enhanced CLI functionality** with better error handling and Windows compatibility
- ✅ **Improved documentation** with proper markdown formatting
- ✅ **Resolved import dependencies** (flask-cors installation)
- ✅ **Better cross-platform support** with readline handling for Windows

---

## Quickstart

**Install from PyPI:**

```bash
pip install shellrosetta
```

**Or clone and install locally:**

```bash
git clone https://github.com/sdirishguy/shellrosetta.git
cd shellrosetta
pip install .
```

**Usage:**

```bash
shellrosetta lnx2ps "ls -alh | grep error"
shellrosetta ps2lnx "Get-ChildItem -Force | Select-String error"
```

**Or test before installing:**

```bash
python -m shellrosetta.cli lnx2ps "ls -alh | grep error"
python -m shellrosetta.cli ps2lnx "Get-ChildItem -Force | Select-String error"
```

**(Optional) Add aliases to your shell:**

```bash
echo "alias lnx2ps='shellrosetta lnx2ps'" >> ~/.bashrc
echo "alias ps2lnx='shellrosetta ps2lnx'" >> ~/.bashrc
source ~/.bashrc
```

**(Optional) Enable tab-completion:**
Copy `shellrosetta/autocomplete.sh` somewhere (or use directly from the repo), then add this to your `~/.bashrc` or `~/.zshrc`:

```bash
source /path/to/shellrosetta/autocomplete.sh
```

Reload your shell:

```bash
source ~/.bashrc
# or
source ~/.zshrc
```

Now you get tab completion for commands and flags!

## Interactive Shell Mode

Run with no arguments for a live translation shell!

```bash
shellrosetta
```

You'll be prompted for your translation mode (lnx2ps or ps2lnx). Enter commands and see translations instantly, switching modes at any time with `mode` or exit with `exit`.

**Example session:**

```
$ shellrosetta
=================================================================
ShellRosetta: Linux ↔ PowerShell CLI Command Translator
Author: David Donohue
Repo: github.com/sdirishguy/shellrosetta
=================================================================
Welcome to ShellRosetta Interactive Mode!
Type 'exit' to quit, or 'mode' to switch translation direction.
Mode [lnx2ps/ps2lnx] (or 'exit'): lnx2ps
Type your LNX2PS commands below. Type 'mode' to switch, 'exit' to quit.

> ls -alh | grep foo

--- Translation ---
PowerShell Equivalent:
  Get-ChildItem -Force | Format-List # [Human-readable file sizes not natively available.] | Select-String foo
-------------------

> rm -rf /tmp
--- Translation ---
PowerShell Equivalent:
  Remove-Item -Recurse -Force /tmp
-------------------

> mode