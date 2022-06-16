local awful = require("awful")
local wibox = require("wibox")
local beautiful = require("beautiful")
local shape = require("gears.shape")
local utils = require("config.util.utils")
beautiful.init("~/.config/awesome/themes/marca_theme/theme.lua")

local cmd_usg = "top -b -n 1 | awk '/Cpu/ { print $2 }'"
local cmd_temp = "sensors | awk '/Package id 0:/ { print $4 }' | sed 's/+//'"

local cpu_widget = wibox.widget{
	{
		{
			{
				{
					id = "text",
					font = beautiful.font .. "25",
					markup = '<span foreground="' .. beautiful.fg_urgent .. '"></span> 0%',
					widget = wibox.widget.textbox,
				},
				right = 11,
				left = 5,
				layout = wibox.container.margin,
			},
			shape = function (cr, width, height)
							shape.rounded_rect(cr, width, height, 10) end,
			--shape_border_width = 1.75,
			fg = beautiful.fg_urgent,
			--shape_border_color = "#000000",
			--bg = beautiful.bg_primary .. "40",
			widget = wibox.container.background,
		},
		top = 3,
		bottom = 3,
		right = 4,
		left = 0,
		layout = wibox.container.margin,
	},
	layout = wibox.layout.align.horizontal
}

local cpu_tt = awful.tooltip{
	objects = { cpu_widget },
	mode = "outside",
}

awful.widget.watch("sh -c \"" .. cmd_usg .."\"", 1, 
    function(widget, stdout)
	    local split_stdout = utils.split_str(stdout, "\n")
	    cpu_widget:get_children_by_id("text")[1].markup = '<span foreground="' .. beautiful.fg_urgent .. '"></span> ' .. split_stdout[1] .. '%'
	    cpu_tt.text = "Usg: " .. split_stdout[1] .. ""
    end, 
cpu_widget)

--utils.split_str(split_stdout[1], ".")[1]

return cpu_widget