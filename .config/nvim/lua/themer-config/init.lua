require("themer").setup({
    colorscheme = "papa_dark",
    transparent = true,
    enable_installer = true,
    remaps = {
        palette = {
            papa_dark = {
                fg = "#ff0000"
            }
        },
        highlights = {
            papa_dark = {
                base = {
                    Keyword = { fg = "#32ae85"},
                    Function = {fg = "#e5e9f0"},
                    Normal = {fg = "#afcca4", bg = "#00000000"},
                    TabLineFill = { fg = "#262626", bg = "#000000" },
                    StatusLine = { fg = "#262626", bg = "#262626"},
                    StatusLineNC = { fg = "#262626", bg = "#262626"},
                    -- Esta esta de pureba
                    VertSplit = { bg="#262626"},
                },
                plugins = {
                    treesitter = {
                        TSKeywordFunction = { fg = "#32ae85"},
                        TSKeyword = { fg = "#32ae85"},
                        --TSFunction = { link = "Function"},
                    },
                    gitsigns = {
                        GitSignsAdd = { fg = "#c487b9"},
                        GitSignsChange = { fg = "#d4d198", bg="#00000000"},
                        GitSignsDelete = { bg = "#d94848" },
                    },
                }
            },
        },
    },
})
