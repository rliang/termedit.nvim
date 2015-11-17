# termedit.nvim
Sets the Neovim host instance as $EDITOR. 

## Summary
This plugin sets '$EDITOR' to a python script that has the host Neovim instance
open its given arguments. It's useful mostly for `:term`.

The script blocks until all given files are closed. Then, the active buffer at
the time the script was spawned will be switched back to.  The script can also
just be terminated with `^c` as usual.

## Requirements
`python3-neovim`

## Credits
The python script is based on [this script by
@tarruda](https://gist.github.com/tarruda/37f7a3e22996addf8921) and [this
script by
@lahwran](https://github.com/lahwran/dotfiles/blob/master/bin/nvim-inner).
