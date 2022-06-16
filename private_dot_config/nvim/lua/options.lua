local options = {
    relativenumber = true,
	--background = "dark",
	smartindent = true,
	tabstop = 4,
	showtabline = 4,
	autoindent = true,
    mouse = "a",
	expandtab = true,
    shiftwidth = 4,
    clipboard = "unnamedplus",
    fileencoding = "utf-8",
    number = true,
    termguicolors = true,
    updatetime = 1000,
}

for k, v in pairs(options) do
	vim.opt[k] = v
end

