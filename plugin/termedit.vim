com! TermRelease if exists('b:termedit') | call rpcnotify(b:termedit, 'release') | endif

let $EDITOR = resolve(expand('<sfile>:h:h')).'/termedit.py'
