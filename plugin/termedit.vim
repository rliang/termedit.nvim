let s:python = executable('python3') ? 'python3' : 'python'
let s:script = resolve(expand('<sfile>:h:h')) . '/termedit.py'
let $EDITOR = s:python . ' ' . s:script

function! s:term_release()
  if exists('b:termedit')
    call rpcnotify(b:termedit, 'release')
  endif
endfunction
command! TermRelease call s:term_release()
