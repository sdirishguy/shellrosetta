# shellrosetta/autocomplete.sh
# Add this to your ~/.bashrc or ~/.zshrc for tab completion!

_shellrosetta_complete() {
  local cur prev opts lnxflags psflags
  COMPREPLY=()
  cur="${COMP_WORDS[COMP_CWORD]}"
  prev="${COMP_WORDS[COMP_CWORD-1]}"
  opts="ls rm cp mv grep find cat ping ifconfig netstat traceroute curl wget hostname nslookup dig"
  lnxflags="-a -l -h -R -r -f -v"
  psflags="-Force -Recurse -Verbose | Format-List -CaseSensitive:$false"

  if [[ ${COMP_CWORD} -eq 1 ]]; then
    COMPREPLY=( $(compgen -W "lnx2ps ps2lnx" -- "${cur}") )
    return 0
  fi
  if [[ ${COMP_CWORD} -eq 2 ]]; then
    COMPREPLY=( $(compgen -W "${opts}" -- "${cur}") )
    return 0
  fi
  if [[ ${COMP_WORDS[1]} == "lnx2ps" ]]; then
    if [[ ${COMP_WORDS[2]} == "ls" || ${COMP_WORDS[2]} == "rm" || ${COMP_WORDS[2]} == "cp" || ${COMP_WORDS[2]} == "mv" ]]; then
      COMPREPLY=( $(compgen -W "${lnxflags}" -- "${cur}") )
      return 0
    fi
  elif [[ ${COMP_WORDS[1]} == "ps2lnx" ]]; then
    if [[ ${COMP_WORDS[2]} =~ (Get-ChildItem|Remove-Item|Copy-Item|Move-Item|Select-String) ]]; then
      COMPREPLY=( $(compgen -W "${psflags}" -- "${cur}") )
      return 0
    fi
  fi
}
complete -F _shellrosetta_complete lnx2ps
complete -F _shellrosetta_complete ps2lnx
