local is_picking_focus = require("cokeline/mappings").is_picking_focus
local is_picking_close = require("cokeline/mappings").is_picking_close
local get_hex = require("cokeline/utils").get_hex

local red = vim.g.terminal_color_1
local yellow = vim.g.terminal_color_4
local space = {text = " "}
local dark = "#262626"
local text = get_hex("Comment", "#ffffff") -- Textos de los tab no focuseados
local grey = "#263e26"--"#262626" --get_hex("ColorColumn", "bg")
local light = get_hex("Comment", "bg")
local high = "#608b4e"

require("cokeline").setup(
    {
        default_hl = {
            fg = function(buffer)
                if buffer.is_focused then
                    return dark
                end
                return text
            end,
            bg = function(buffer)
                if buffer.is_focused then
                    return high
                end
                return grey
            end
        },
        components = {
            {
                text = function(buffer)
                    if buffer.index ~= 1 then
                        return ""
                    end
                    return ""
                end,
                bg = function(buffer)
                    if buffer.is_focused then
                        return high
                    end
                    return grey
                end,
                fg = dark
            },
            space,
            {
                text = function(buffer)
                    if is_picking_focus() or is_picking_close() then
                        return buffer.pick_letter .. " "
                    end

                    return buffer.devicon.icon
                end,
                fg = function(buffer)
                    if is_picking_focus() then
                        return yellow
                    end
                    if is_picking_close() then
                        return red
                    end

                    if buffer.is_focused then
                        --return dark
                        return buffer.devicon.color
                    else
                        return light
                    end
                end,
                style = function(_)
                    return (is_picking_focus() or is_picking_close()) and "italic,bold" or nil
                end
            },
            {
                text = function(buffer)
                    return buffer.unique_prefix .. buffer.filename .. " "
                end,
                style = function(buffer)
                    return buffer.is_focused and "bold" or nil
                end
            },
            { -- Inicia Parte modificada
                text = function(buffer)
                    return buffer.is_modified and '● ' or ' '
                end,
                fg = function(buffer)
                    if buffer.is_focused then
                        return dark
                    end
                end,
                delete_buffer_on_left_click = true,
            }, -- Termina parte modificada
            {
                text = "",
                fg = function(buffer)
                    if buffer.is_focused then
                        return high
                    end
                    return grey
                end,
                bg = dark
            }
        }
    }
)


-- Mapping
local map = vim.api.nvim_set_keymap

map('', '<A-1>',   '<Plug>(cokeline-focus-prev)',  { silent = true })
map('', '<A-2>',     '<Plug>(cokeline-focus-next)',  { silent = true })
map('n', '<Leader>p', '<Plug>(cokeline-switch-prev)', { silent = true })
map('n', '<Leader>n', '<Plug>(cokeline-switch-next)', { silent = true })
map('', '<A-Tab>', '<Plug>(cokeline-pick-close)', { silent = true })

for i = 1,9 do
  map('n', ('<F%s>'):format(i),      ('<Plug>(cokeline-focus-%s)'):format(i),  { silent = true })
  map('n', ('<Leader>%s'):format(i), ('<Plug>(cokeline-switch-%s)'):format(i), { silent = true })
end

