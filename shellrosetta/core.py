# shellrosetta/core.py

import shlex
import re
from .mappings import (
    LS_FLAGS_MAP, RM_FLAGS_MAP, CP_FLAGS_MAP, MV_FLAGS_MAP,
    GREP_FLAGS_MAP, FIND_FLAGS_MAP, CAT_FLAGS_MAP,
    NETWORK_CMD_MAP, PS_TO_LNX
)

def extract_flags_and_targets(args):
    """Split arguments into flags and targets (paths/files)."""
    flags = []
    targets = []
    for arg in args:
        if arg.startswith('-'):
            flags.append(arg)
        else:
            targets.append(arg)
    return flags, targets

def translate_ls(args):
    flags, targets = extract_flags_and_targets(args)
    flagkey = "".join(sorted(flags))
    flags_out = LS_FLAGS_MAP.get(flagkey, None)
    base = "Get-ChildItem"
    out = base
    if flags_out:
        out += f" {flags_out}"
    if targets:
        out += " " + " ".join(targets)
    if not flags_out and flags:
        out += f" # [No direct PowerShell equivalent for flags: {', '.join(flags)}]"
    return out.strip()

def translate_rm(args):
    flags, targets = extract_flags_and_targets(args)
    flagkey = "".join(sorted(flags))
    flags_out = RM_FLAGS_MAP.get(flagkey, None)
    base = "Remove-Item"
    out = base
    if flags_out:
        out += f" {flags_out}"
    if targets:
        out += " " + " ".join(targets)
    if not flags_out and flags:
        out += f" # [No direct PowerShell equivalent for flags: {', '.join(flags)}]"
    return out.strip()

def translate_cp(args):
    flags, targets = extract_flags_and_targets(args)
    flagkey = "".join(sorted(flags))
    flags_out = CP_FLAGS_MAP.get(flagkey, None)
    base = "Copy-Item"
    out = base
    if flags_out:
        out += f" {flags_out}"
    if targets:
        out += " " + " ".join(targets)
    if not flags_out and flags:
        out += f" # [No direct PowerShell equivalent for flags: {', '.join(flags)}]"
    return out.strip()

def translate_mv(args):
    flags, targets = extract_flags_and_targets(args)
    flagkey = "".join(sorted(flags))
    flags_out = MV_FLAGS_MAP.get(flagkey, None)
    base = "Move-Item"
    out = base
    if flags_out:
        out += f" {flags_out}"
    if targets:
        out += " " + " ".join(targets)
    if not flags_out and flags:
        out += f" # [No direct PowerShell equivalent for flags: {', '.join(flags)}]"
    return out.strip()

def translate_grep(args):
    flags, targets = extract_flags_and_targets(args)
    flagkey = "".join(sorted(flags))
    flags_out = GREP_FLAGS_MAP.get(flagkey, None)
    base = "Select-String"
    out = base
    if flags_out:
        out += f" {flags_out}"
    if targets:
        out += " " + " ".join(targets)
    if not flags_out and flags:
        out += f" # [No direct PowerShell equivalent for flags: {', '.join(flags)}]"
    return out.strip()

def translate_find(args):
    flags, targets = extract_flags_and_targets(args)
    base = "Get-ChildItem -Recurse"
    out = base
    if "-name" in flags:
        try:
            idx = args.index("-name")
            pattern = args[idx + 1] if idx + 1 < len(args) else ""
            out += f' -Filter "{pattern}"'
        except Exception:
            pass
    if targets:
        out += " " + " ".join(targets)
    return out.strip()

def translate_cat(args):
    flags, targets = extract_flags_and_targets(args)
    base = "Get-Content"
    out = base
    if targets:
        out += " " + " ".join(targets)
    if "-n" in flags:
        out += " # [No direct PowerShell equivalent for line numbers]"
    return out.strip()

def translate_network(cmd, args):
    base = NETWORK_CMD_MAP.get(cmd, None)
    if not base:
        return f"# [No PowerShell equivalent for networking command: {cmd}]"
    if args:
        return f"{base} {' '.join(args)}"
    return base

def generic_translate(cmd, args):
    return f"# [No translation available for '{cmd}' with args '{' '.join(args)}']"

def lnx2ps(command):
    stages = [stage.strip() for stage in command.split('|')]
    translated = []
    for stage in stages:
        if not stage:
            continue
        tokens = shlex.split(stage)
        if not tokens:
            continue
        cmd, *args = tokens
        cmd_lc = cmd.lower()
        if cmd_lc == "ls":
            t = translate_ls(args)
        elif cmd_lc == "rm":
            t = translate_rm(args)
        elif cmd_lc == "cp":
            t = translate_cp(args)
        elif cmd_lc == "mv":
            t = translate_mv(args)
        elif cmd_lc == "grep":
            t = translate_grep(args)
        elif cmd_lc == "find":
            t = translate_find(args)
        elif cmd_lc == "cat":
            t = translate_cat(args)
        elif cmd_lc in NETWORK_CMD_MAP:
            t = translate_network(cmd_lc, args)
        else:
            t = generic_translate(cmd, args)
        translated.append(t)
    return " | ".join(translated)

def ps2lnx(command):
    stages = [stage.strip() for stage in command.split('|')]
    translated = []
    for stage in stages:
        norm_stage = re.sub(r'\s+', ' ', stage)
        found = PS_TO_LNX.get(norm_stage, None)
        if found:
            translated.append(found)
        else:
            first_word = stage.split()[0]
            match = [k for k in PS_TO_LNX if k.startswith(first_word)]
            if match:
                translated.append(PS_TO_LNX[match[0]])
            else:
                translated.append(f"# [No Linux equivalent for: {stage}]")
    return " | ".join(translated)
