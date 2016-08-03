#!/usr/bin/env python3

import os
import sys
import neovim

files = [os.path.abspath(arg) for arg in sys.argv[1:]]
if not files:
    sys.exit(1)

addr = os.environ.get('NVIM_LISTEN_ADDRESS', None)
if not addr:
    os.execvp('nvim', files)

nvim = neovim.attach('socket', path=addr)
cid, cbuf = (nvim.channel_id, nvim.current.buffer)

files = [nvim.eval('fnameescape("{}")'.format(f)) for f in files]
for f in files:
    nvim.command('drop {}'.format(f))
    nvim.command('au BufUnload <buffer> sil! call rpcnotify({}, "unload", "{}")'.format(cid, f))
    nvim.current.buffer.vars['termedit'] = cid

while files:
    msg = nvim.next_message()
    if not msg:
        break
    ev, key, args = msg
    if ev is not 'notification':
        break
    if key == 'release':
        break
    if key == 'unload':
        files = [f for f in files if f not in args]

nvim.current.buffer = cbuf
