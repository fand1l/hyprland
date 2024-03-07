# Hyprland Waybar
This is my configuration for hyprland waybar
![Screenshot](https://github.com/fand1l/hyprland.waybar/raw/main/screenshot.png)

## Requirements

## yay
```
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

## Packages (yay)
```
hyprland
waybar
pavucontrol
pamixer
```

## Files
Description of the files

### config
The configuration file for Waybar. It stores information about the position of the panel and the modules used.

### modules.json
Information about modules and their configuration is stored here

### style.css
Styles for Waybar are stored here

### scripts/waybar-wttr
![ChrisTitusTech](https://github.com/ChrisTitusTech/hyprland-titus/tree/main/dotconfig/waybar/scripts) script to get weather for the waybar of the custom/weather module
