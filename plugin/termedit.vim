let $EDITOR = resolve(expand('<sfile>:h:h')) . '/termedit.py'

function! s:term_release()
  if exists('b:termedit')
    call rpcnotify(b:termedit, 'release')
  endif
endfunction
command! TermRelease call s:term_release()
