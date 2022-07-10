if !has('python3')
  echo "Error: Required vim compiled with +python3"
  finish
endif

if exists('g:plugin_loaded')
  finish
 endif

" Get the path of this script
let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

" Execute python and add the path of ../python to the system path so
" that we can import python libraries
python3 << EOF
import sys
from os.path import normpath, join
import vim

plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)

import document as dc
EOF


function! Document(func_name, ident_lvl, params)
	" Call python, to access VimL variables, we need to use
	" vim.eval() and as parameter we send the name of the
	" variable in vim
	python3 dc.document_func(vim.eval('a:func_name'), vim.eval('a:ident_lvl'), vim.eval('a:params'))
endfunction

let g:plugin_loaded = 1

" Convert a given function into a Vim command
command! -nargs=* Document call Document(<f-args>)
