" We should not try to execute this plugin if there is no python3 availabe
" as the logic for this logic is wrote in python
if !has('python3')
  echo "Error: Required vim compiled with +python3"
  finish
endif

" Only load this plugin once
"if exists('g:plugin_loaded')
"  finish
" endif

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

function! Header(func_name, ident_lvl)
	" Call python, to access VimL variables, we need to use
	" vim.eval() and as parameter we send the name of the
	" variable in vim
	python3 dc.write_header(vim.eval('a:func_name'), vim.eval('a:ident_lvl'))

endfunction

function! Constants()
	" Call python, to access VimL variables, we need to use
	" vim.eval() and as parameter we send the name of the
	" variable in vim
	python3 dc.constants()

endfunction

function! Globals()
	" Call python, to access VimL variables, we need to use
	" vim.eval() and as parameter we send the name of the
	" variable in vim
	python3 dc.globals()

endfunction

function! Functions()
	" Call python, to access VimL variables, we need to use
	" vim.eval() and as parameter we send the name of the
	" variable in vim
	python3 dc.functions()

endfunction

function! Classes()
	" Call python, to access VimL variables, we need to use
	" vim.eval() and as parameter we send the name of the
	" variable in vim
	python3 dc.classes()

endfunction


" Keep track that the plugin was already loaded
let g:plugin_loaded = 1

" Convert a given function into a Vim command
command! -nargs=* Document call Document(<f-args>)
command! -nargs=* Header call Header(<f-args>)
command! -nargs=0 Constants call Constants()
command! -nargs=0 Globals call Globals()
command! -nargs=0 Functions call Functions()
command! -nargs=0 Classes call Classes()
