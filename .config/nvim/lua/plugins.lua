vim.cmd[[ packadd packer.nvim ]]

return require('packer').startup(function()

	-- Manejador de paquetes
	use 'wbthomason/packer.nvim'
    
	-- chingadera para el LSP y CMP
	use "williamboman/nvim-lsp-installer"
	use "neovim/nvim-lspconfig"
	use 'hrsh7th/nvim-cmp' -- Autocompletion plugin
    use 'hrsh7th/cmp-nvim-lsp' -- LSP source for nvim-cmp
    use 'saadparwaiz1/cmp_luasnip' -- Snippets source for nvim-cmp
    use 'L3MON4D3/LuaSnip' -- Snippets plugin	
	use "onsails/lspkind.nvim" -- Cmp icons
    use {"ray-x/lsp_signature.nvim"}

    -- Line mamalona
    use {'nvim-lualine/lualine.nvim', requires = { 'kyazdani42/nvim-web-devicons', opt = true }}

    -- Tree files
    use {'kyazdani42/nvim-tree.lua', requires = {'kyazdani42/nvim-web-devicons', opt = true}}
    
    -- Syntax highlighting
    use {'nvim-treesitter/nvim-treesitter', run = ':TSUpdate'} 
    use 'nvim-treesitter/nvim-treesitter-refactor'

    use {'akinsho/bufferline.nvim', tag = "v2.*", requires = {'kyazdani42/nvim-web-devicons', opt= true }}
    use({'noib3/nvim-cokeline', requires = 'kyazdani42/nvim-web-devicons'})

    -- Themes
    use 'voithos/vim-colorpack'
    use 'marko-cerovac/material.nvim'
    use 'rktjmp/lush.nvim'
    use {'MordechaiHadad/nvim-papadark', requires = {'rktjmp/lush.nvim'}}
    use 'rockerBOO/boo-colorscheme-nvim'
    use 'folke/tokyonight.nvim'
    use("themercorp/themer.lua")  --Theme manager
    
    use "windwp/nvim-autopairs"

    use 'nvim-lua/plenary.nvim' 
    use {'nvim-telescope/telescope.nvim', requires = { {'nvim-lua/plenary.nvim'} }}
    
    use {
        "folke/which-key.nvim",
        config = function() require("which-key").setup {}end
    }

    use('lewis6991/gitsigns.nvim')

end)
