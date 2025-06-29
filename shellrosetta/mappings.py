# shellrosetta/mappings.py

"""
Command and flag mappings for ShellRosetta:
- Direct mappings for single commands and common command+flag combos.
- Per-command flag maps for complex/flag-heavy translation.
- Notes for special cases or usage tips.
"""

# --- Direct mappings for Linux to PowerShell ---
LINUX_TO_PS = {
    "ls": ("Get-ChildItem", None),
    "ls -l": ("Get-ChildItem | Format-List", None),
    "ls -a": ("Get-ChildItem -Force", None),
    "ls -lh": ("Get-ChildItem | Format-List", "Human-readable file sizes not natively available."),
    "ls -al": ("Get-ChildItem -Force | Format-List", None),
    "ls -la": ("Get-ChildItem -Force | Format-List", None),
    "ls -R": ("Get-ChildItem -Recurse", None),
    "ls -alh": ("Get-ChildItem -Force | Format-List", "Human-readable file sizes not natively available."),
    "cd": ("Set-Location", None),
    "pwd": ("Get-Location", None),
    "mkdir": ("New-Item -ItemType Directory", None),
    "rm": ("Remove-Item", None),
    "rm -r": ("Remove-Item -Recurse", None),
    "rm -f": ("Remove-Item -Force", None),
    "rm -rf": ("Remove-Item -Recurse -Force", None),
    "cp": ("Copy-Item", None),
    "cp -r": ("Copy-Item -Recurse", None),
    "mv": ("Move-Item", None),
    "touch": ("New-Item -ItemType File", None),
    "cat": ("Get-Content", None),
    "head": ("Get-Content -TotalCount 10", "Default is 10 lines."),
    "head -n": ("Get-Content -TotalCount", None),  # Needs arg
    "tail": ("Get-Content -Tail 10", "Default is 10 lines."),
    "tail -n": ("Get-Content -Tail", None),  # Needs arg
    "ln -s": ("New-Item -ItemType SymbolicLink -Target", None),  # Needs arg
    "chmod": ("icacls", "Use 'icacls file /grant user:permissions'. Not as granular/flexible as Linux."),
    "chown": ("icacls file /setowner user", "Not native to PowerShell on Linux."),
    "chgrp": ("# [No direct equivalent in PowerShell]", None),
    "umask": ("# [No direct equivalent in PowerShell]", None),
    "tar -czvf": ("Compress-Archive", "Outputs .zip, not .tar.gz. For gzip, use third-party modules or 7-Zip."),
    "gzip": ("Compress-Archive", "Creates .zip by default."),
    "gunzip": ("Expand-Archive", "For .zip, not .gz. Use 7-Zip or other tool for .gz."),
    "zip": ("Compress-Archive", None),
    "unzip": ("Expand-Archive", None),
    "ps aux": ("Get-Process", None),
    "top": ("Get-Process | Sort-Object CPU -Descending", "Use Get-Process | Out-GridView for a dynamic view."),
    "kill": ("Stop-Process -Id", None),  # Needs arg
    "pkill": ("Stop-Process -Name", None),  # Needs arg
    "pgrep": ("Get-Process -Name", None),  # Needs arg
    "grep": ("Select-String", None),
    "find": ("Get-ChildItem -Recurse", None),
    "uname -a": ("Get-ComputerInfo | Select-Object OsName,OsVersion,OsArchitecture", None),
    "whoami": ("whoami", None),
    "df -h": ("Get-PSDrive", None),
    "du -sh": ("(Get-ChildItem dir -Recurse | Measure-Object -Property Length -Sum).Sum", None),
    "free -h": ("Get-ComputerInfo | Select-Object CsTotalPhysicalMemory", None),
    "uptime": ("(get-date) - (gcim Win32_OperatingSystem).LastBootUpTime", None),
    "lscpu": ("Get-CimInstance Win32_Processor", None),
    "lspci": ("Get-CimInstance Win32_PnPEntity | Where-Object { $_.PNPClass -eq 'PCI' }", None),
    "lsusb": ("Get-PnpDevice -PresentOnly | Where-Object { $_.Service -eq 'USBSTOR' }", None),
    "ifconfig": ("Get-NetIPAddress", None),
    "ping": ("Test-Connection", None),
    "netstat": ("Get-NetTCPConnection", None),
    "ss": ("Get-NetTCPConnection", None),
    "ssh": ("ssh", "Use OpenSSH or the Posh-SSH module in PowerShell."),
    "scp": ("scp", "Use OpenSSH or the Posh-SSH module in PowerShell."),
    "wget": ("Invoke-WebRequest", None),
    "curl": ("Invoke-WebRequest", None),
    "export": ("$env:", "e.g. $env:VAR='value'"),
    "echo $VAR": ("echo $env:VAR", None),
    "env": ("Get-ChildItem Env:", None),
    "unset": ("Remove-Item Env:", None),
    "printenv": ("Get-ChildItem Env:", None),
    "who": ("query user", None),
    "adduser": ("New-LocalUser -Name", "Requires admin"),
    "userdel -r": ("Remove-LocalUser -Name", "Requires admin"),
    "passwd -l": ("Disable-LocalUser -Name", None),
    "usermod -a -G": ("Add-LocalGroupMember -Group -Member", None),
    "history": ("Get-History", None),
    "clear": ("Clear-Host", None),
    "date": ("Get-Date", None),
    "cal": ("# [No direct equivalent in PowerShell]", None),
    "man": ("Get-Help", None),
    ">": (">", None),
    ">>": (">>", None),
    "<": ("Get-Content file | cmd", "Use pipe for input redirection"),
    "2>": ("2>", None),
    "&>": ("*>", None),
    "2>&1": ("2>&1", None),
}

# --- PowerShell to Linux direct mappings ---
PS_TO_LINUX = {
    "Get-ChildItem": ("ls", None),
    "Get-ChildItem -Force": ("ls -a", None),
    "Get-ChildItem | Format-List": ("ls -l", None),
    "Get-ChildItem -Force | Format-List": ("ls -la", None),
    "Get-ChildItem -Recurse": ("ls -R", None),
    "Set-Location": ("cd", None),
    "Get-Location": ("pwd", None),
    "New-Item -ItemType Directory": ("mkdir", None),
    "Remove-Item": ("rm", None),
    "Remove-Item -Recurse": ("rm -r", None),
    "Remove-Item -Force": ("rm -f", None),
    "Remove-Item -Recurse -Force": ("rm -rf", None),
    "Copy-Item": ("cp", None),
    "Copy-Item -Recurse": ("cp -r", None),
    "Move-Item": ("mv", None),
    "New-Item -ItemType File": ("touch", None),
    "Get-Content": ("cat", None),
    "Get-Content -TotalCount 10": ("head", "Default: 10 lines"),
    "Get-Content -TotalCount": ("head -n", None),
    "Get-Content -Tail 10": ("tail", "Default: 10 lines"),
    "Get-Content -Tail": ("tail -n", None),
    "New-Item -ItemType SymbolicLink -Target": ("ln -s", None),
    "icacls": ("chmod", "chmod has more flexible syntax"),
    "icacls file /setowner user": ("chown", None),
    "Compress-Archive": ("tar -czvf", "tar creates .tar.gz; Compress-Archive creates .zip"),
    "Expand-Archive": ("tar -xzvf or unzip", "unzip for .zip; tar -xzvf for .tar.gz"),
    "Get-Process": ("ps aux", None),
    "Sort-Object CPU -Descending": ("top", None),
    "Stop-Process -Id": ("kill", None),
    "Stop-Process -Name": ("pkill", None),
    "Get-Process -Name": ("pgrep", None),
    "Select-String": ("grep", None),
    "Get-ChildItem -Recurse": ("find", None),
    "Get-ComputerInfo | Select-Object OsName,OsVersion,OsArchitecture": ("uname -a", None),
    "whoami": ("whoami", None),
    "Get-PSDrive": ("df -h", None),
    "Measure-Object -Property Length -Sum": ("du -sh", None),
    "Get-ComputerInfo | Select-Object CsTotalPhysicalMemory": ("free -h", None),
    "(get-date) - (gcim Win32_OperatingSystem).LastBootUpTime": ("uptime", None),
    "Get-CimInstance Win32_Processor": ("lscpu", None),
    "Get-CimInstance Win32_PnPEntity | Where-Object { $_.PNPClass -eq 'PCI' }": ("lspci", None),
    "Get-PnpDevice -PresentOnly | Where-Object { $_.Service -eq 'USBSTOR' }": ("lsusb", None),
    "Get-NetIPAddress": ("ifconfig", None),
    "Test-Connection": ("ping", None),
    "Get-NetTCPConnection": ("netstat", None),
    "ssh": ("ssh", None),
    "scp": ("scp", None),
    "Invoke-WebRequest": ("wget", None),
    "$env:VAR=\"value\"": ("export VAR=value", None),
    "echo $env:VAR": ("echo $VAR", None),
    "Get-ChildItem Env:": ("env", None),
    "Remove-Item Env:VAR": ("unset VAR", None),
    "Get-History": ("history", None),
    "Clear-Host": ("clear", None),
    "Get-Date": ("date", None),
    "Get-Help": ("man", None),
}

# --- Per-command flag maps ---
LS_FLAGS_MAP = {
    "": "",
    "-l": "| Format-List",
    "-a": "-Force",
    "-h": "# [No direct PowerShell equivalent for -h (human-readable)]",
    "-r": "-Recurse",
    "-R": "-Recurse",
    "-la": "-Force | Format-List",
    "-al": "-Force | Format-List",
    "-lh": "| Format-List # [No direct PowerShell equivalent for -h]",
    "-ah": "-Force # [No direct PowerShell equivalent for -h]",
    "-alh": "-Force | Format-List # [No direct PowerShell equivalent for -h]",
    "-lah": "-Force | Format-List # [No direct PowerShell equivalent for -h]",
    "-lR": "| Format-List -Recurse",
    "-laR": "-Force | Format-List -Recurse",
    "-Ral": "-Force | Format-List -Recurse",
}

RM_FLAGS_MAP = {
    "": "",
    "-f": "-Force",
    "-r": "-Recurse",
    "-R": "-Recurse",
    "-rf": "-Recurse -Force",
    "-fr": "-Recurse -Force",
    "-rfv": "-Recurse -Force -Verbose",
    "-rvf": "-Recurse -Force -Verbose",
}

CP_FLAGS_MAP = {
    "": "",
    "-r": "-Recurse",
    "-R": "-Recurse",
    "-v": "-Verbose",
    "-rv": "-Recurse -Verbose",
    "-vr": "-Recurse -Verbose",
    "-f": "# [No direct PowerShell equivalent for -f (force overwrite)]",
}

MV_FLAGS_MAP = {
    "": "",
    "-v": "-Verbose",
    "-f": "# [No direct PowerShell equivalent for -f (force overwrite)]",
}

GREP_FLAGS_MAP = {
    "": "",
    "-i": "-CaseSensitive:$false",
    "-n": "-Context 0,0 # [No direct line numbers in PowerShell]",
    "-r": "-Recurse",
    "-R": "-Recurse",
    "-l": "-List",
    "-v": "-NotMatch",
    "-iv": "-CaseSensitive:$false -NotMatch",
    "-in": "-CaseSensitive:$false # [No direct line numbers in PowerShell]",
    "-ir": "-CaseSensitive:$false -Recurse",
    "-ri": "-Recurse -CaseSensitive:$false",
}

FIND_FLAGS_MAP = {
    "": "",
    "-name": "-Filter",
    "-type": "# [No direct PowerShell equivalent for -type]",
}

CAT_FLAGS_MAP = {
    "": "",
    "-n": "# [No direct PowerShell equivalent for -n (line numbers)]",
    "-b": "# [No direct PowerShell equivalent for -b]",
}
