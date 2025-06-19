# ShellRosetta

**Translate Linux/Bash commands to PowerShell and vice versa, with support for flags, pipelines, and the most common workflows.**

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## What is ShellRosetta?

ShellRosetta is a developer productivity tool that helps you translate CLI commands between Linux/Bash and PowerShell.  
It handles not just the base commands, but also common flags, piped commands, and networking or system utilities.

## Features

- 🔄 **Bidirectional translation**: Linux/Bash ↔ PowerShell
- 🏷️ **Flag-aware**: Handles multi-flag combos like `ls -alh` or `rm -rf`
- 🔗 **Pipeline support**: Translates piped commands (e.g., `ls -l | grep foo`)
- 🌐 **Networking/system commands**: Maps ping, traceroute, netstat, etc.
- 💡 **Easy to expand**: Add new commands/flags by editing `mappings.py`
- 🧩 **Bash/Zsh autocomplete**: Included script for tab completion
- ✅ **Unit tests included**: See `tests/`

## Quickstart

1. **Clone and install locally:**

    ```sh
    git clone https://github.com/sdirishguy/shellrosetta.git
    cd shellrosetta
    pip install .
    ```

2. **Usage:**

    ```sh
    shellrosetta lnx2ps "ls -alh | grep error"
    shellrosetta ps2lnx "Get-ChildItem -Force | Select-String error"
    ```

3. **(Optional) Add aliases to your shell:**

    ```sh
    echo "alias lnx2ps='shellrosetta lnx2ps'" >> ~/.bashrc
    echo "alias ps2lnx='shellrosetta ps2lnx'" >> ~/.bashrc
    source ~/.bashrc
    ```

4. **(Optional) Enable tab-completion:**  
   Add the contents of `shellrosetta/autocomplete.sh` to your `~/.bashrc` or `~/.zshrc` and reload your shell.

## Examples

```sh
shellrosetta lnx2ps "ls -la"
# ➔ Get-ChildItem -Force | Format-List

shellrosetta lnx2ps "rm -rf /var/tmp"
# ➔ Remove-Item -Recurse -Force /var/tmp

shellrosetta ps2lnx "Get-ChildItem -Force | Select-String foo"
# ➔ ls -a | grep foo
```
## Project Structure
shellrosetta/
  shellrosetta/
    __init__.py
    cli.py
    core.py
    mappings.py
    autocomplete.sh
  tests/
    test_core.py
  setup.py
  README.md
  LICENSE
  .gitignore


## License
MIT

## Author
David Donohue
github.com/sdirishguy