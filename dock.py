import plistlib
import os


def get_dock_items():
    # Path to the Dock preferences file
    list_path = '~/Library/Preferences/com.apple.dock.plist'
    dock_plist_path = os.path.expanduser(list_path)

    # Read the plist file
    with open(dock_plist_path, 'rb') as f:
        plist_data = plistlib.load(f)

    # Initialize an empty list to store the Dock items
    dock_items = []

    # Extract persistent apps (apps pinned to the Dock)
    persistent_apps = plist_data.get('persistent-apps', [])
    for app in persistent_apps:
        if 'tile-data' in app:
            # Try to get the file-label (app name)
            file_label = app['tile-data'].get('file-label', None)
            if file_label:
                dock_items.append(file_label)

    # Extract persistent others (folders, files, etc.)
    persistent_others = plist_data.get('persistent-others', [])
    for other in persistent_others:
        if 'tile-data' in other:
            # Try to get the file-label (name of the folder/file)
            file_label = other['tile-data'].get('file-label', None)
            if file_label:
                dock_items.append(file_label)
            else:
                # If no file-label
                # Use the last part of the file URL as the name
                file_data = other['tile-data'].get('file-data', {})
                file_url = file_data.get('_CFURLString', '')
                if file_url:
                    dock_items.append(file_url.split('/')[-1])

    return dock_items


def main():
    # Get the list of Dock items
    dock_items = get_dock_items()

    # Write the items to a file named 'dock.txt' with a heading
    with open('dock', 'w') as file:
        # Write heading first
        file.write('Applications')
        file.write('\n\n\n')
        file.write('Finder\n')

        # Write the list of Dock items
        for item in dock_items:
            file.write(item + '\n')  # Each item in a new line

        file.write("Bin" + '\n')


if __name__ == '__main__':
    main()
