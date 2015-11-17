#!/usr/bin/env python3

import os
import sys
import neovim

files = {os.path.abspath(arg) for arg in sys.argv[1:]}
if not files:
    sys.exit(1)

addr = os.environ.get('NVIM_LISTEN_ADDRESS', None)
if not addr:
    os.execvp('nvim', files)

nvim = neovim.attach('socket', path=addr)
tbuf = nvim.current.buffer

for fname in files:
    nvim.command('drop {}'.format(fname))
    nvim.command('autocmd BufUnload <buffer> silent! call rpcnotify({}, "m")'
            .format(nvim.channel_id))

while files:
    try:
        nvim.session.next_message()
    except:
        pass
    files.pop()

nvim.current.buffer = tbuf
nvim.input('i')
