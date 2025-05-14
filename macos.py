import subprocess
import Quartz # type: ignore


def get_display_info():
    # Get main display ID
    main_display = Quartz.CGMainDisplayID() # type: ignore

    # Native resolution (actual physical pixels)
    native_width = Quartz.CGDisplayPixelsWide(main_display) # type: ignore
    native_height = Quartz.CGDisplayPixelsHigh(main_display) # type: ignore
    native_resolution = f"{native_width}x{native_height}"

    # Current (scaled) resolution
    current_mode = Quartz.CGDisplayCopyDisplayMode(main_display) # type: ignore
    current_width = Quartz.CGDisplayModeGetWidth(current_mode) # type: ignore
    current_height = Quartz.CGDisplayModeGetHeight(current_mode) # type: ignore
    current_resolution = f"{current_width}x{current_height}"

    return native_resolution, current_resolution


def get_color_theme():
    try:
        theme_output = subprocess.check_output(
            ["defaults", "read", "-g", "AppleInterfaceStyle"],
            text=True
        ).strip()
        return "Dark" if theme_output == "Dark" else "Light"
    except subprocess.CalledProcessError:
        return "Light"  # If key doesn't exist, it's Light mode


# Run
native_res, current_res = get_display_info()
color_theme = get_color_theme()

# Prepare content
output_lines = [
    f"Actual (Native) Resolution: {native_res}",
    f"Current (Scaled) Resolution: {current_res}",
    f"Color Theme: {color_theme}"
]

# Write to file
with open("macos.txt", "w") as file:
    for line in output_lines:
        file.write(line + "\n")

print("Display info written to macos.txt")
