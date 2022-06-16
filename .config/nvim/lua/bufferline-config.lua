--vim.opt.termguicolors = true

vim.cmd('nnoremap <A-1> :BufferLineCyclePrev<CR>')
vim.cmd('nnoremap <A-2> :BufferLineCycleNext<CR>')
vim.cmd('nnoremap <A-Tab> :BufferLinePickClose<CR>')

require("bufferline").setup{
options = {
    indicator_icon = '',
    separator_style = {"", ""},
}

}
