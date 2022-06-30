require("themer").setup({
    colorscheme = "papa_dark",
    transparent = true,
    enable_installer = true,
    remaps = {
        palette = {
            papa_dark = {}
        },
        highlights = {
            papa_dark = {
                base = {
                    Keyword = { fg = "#32ae85"},
                    Function = {fg = "#e5e9f0"},
                    Normal = {fg = "#afcca4", bg = "#00000000"},
                    TabLineFill = { fg = "#262626", bg = "#000000" },
                },
                plugins = {
                    treesitter = {
                        TSKeywordFunction = { fg = "#32ae85"},
                        TSKeyword = { fg = "#32ae85"},
                        --TSFunction = { link = "Function"},
                    }
                }
            },
        },
    },
})
