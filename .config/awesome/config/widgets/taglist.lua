local awful = require("awful")
local wibox = require("wibox")
local shape = require("gears.shape")
local beautiful = require("beautiful")
beautiful.init("~/.config/awesome/themes/marca_theme/theme.lua")

local taglist_widget = {}

function taglist_widget.get_taglist(s, taglist_b)
    local taglist = awful.widget.taglist {
        screen = s,
        filter = awful.widget.taglist.filter.all,
        style = {
            shape = function(cr, width, height)
                shape.rounded_react(cr, width, height, 30)
            end,
            bg_focus = beautiful.bg_primary,
            fg_occupied = "#850000",
            bg_occupied = "#ffe800"
        },
        layout = {
            spacing = 1,
            spacing_widget = {
                top = 10,
                bottom = 10,
                widget = wibox.container.margin
            },
            layout = wibox.layout.fixed.horizontal
        },
        widget_template = {
            {
				{
					{
						{
							id     = 'text_role',
							widget = wibox.widget.textbox,
						},
						layout = wibox.layout.fixed.horizontal,
					},
					left  = 6,
					right = 6,
					widget = wibox.container.margin
				},			
                --shape_border_width = 1.75,
                --shpae_border_color = "#000000",
				widget = wibox.container.margin,
			},
			top = 5,
			bottom = 5,
			right = 1,
			left = 1,
            --color = beautiful.bg_second,
            --id = "background_role",
            --bg = beautiful.bg_primary,
            widget = wibox.container.background,
		},
        buttons = taglist_b
    }
    return taglist
end

return taglist_widget