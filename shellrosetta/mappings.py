# shellrosetta/mappings.py

"""
All command and flag mappings for Linux <-> PowerShell translation.
Add new commands and flags here as the app grows.
"""

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

NETWORK_CMD_MAP = {
    "ping": "Test-Connection",
    "ifconfig": "Get-NetIPAddress",
    "ip addr": "Get-NetIPAddress",
    "netstat": "Get-NetTCPConnection",
    "traceroute": "Test-NetConnection -TraceRoute",
    "curl": "Invoke-WebRequest",
    "wget": "Invoke-WebRequest",
    "hostname": "hostname",
    "nslookup": "Resolve-DnsName",
    "dig": "Resolve-DnsName",
}

PS_TO_LNX = {
    "Get-ChildItem": "ls",
    "Get-ChildItem -Force": "ls -a",
    "Get-ChildItem | Format-List": "ls -l",
    "Get-ChildItem -Force | Format-List": "ls -la",
    "Remove-Item -Recurse -Force": "rm -rf",
    "Remove-Item -Recurse": "rm -r",
    "Remove-Item -Force": "rm -f",
    "Copy-Item -Recurse": "cp -r",
    "Move-Item": "mv",
    "Select-String -CaseSensitive:$false": "grep -i",
    "Select-String -Recurse": "grep -r",
    "Test-Connection": "ping",
    "Get-NetIPAddress": "ifconfig",
    "Get-NetTCPConnection": "netstat",
    "Test-NetConnection -TraceRoute": "traceroute",
    "Invoke-WebRequest": "curl",
    "Resolve-DnsName": "nslookup",
}
