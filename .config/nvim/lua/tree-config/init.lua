require('nvim-tree').setup{
    actions = {
        open_file = {
            quit_on_open = true,
        },
    },
    git = {
        ignore = false,
    }
}


vim.cmd('nnoremap <C-n> :NvimTreeToggle<CR>')
