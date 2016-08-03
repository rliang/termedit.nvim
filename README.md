# termedit.nvim
Sets the Neovim host instance as `$EDITOR`.

## Summary
This plugin sets `$EDITOR` to a python script that has the host Neovim instance
open its given arguments. It's useful mostly for `:term`.

The script then blocks until all files opened by the script are closed, or
`:TermRelease` is invoked.

## Commands
* `TermRelease`: When invoked on a buffer opened through this plugin, has the
  script exit without waiting for the buffer to be unloaded.

## Requirements
`python3-neovim`

## Credits
The python script is based on [this script by
@tarruda](https://gist.github.com/tarruda/37f7a3e22996addf8921) and [this
script by
@lahwran](https://github.com/lahwran/dotfiles/blob/master/bin/nvim-inner).
