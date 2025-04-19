import json
import subprocess
from pathlib import Path


def export_vscode_settings():
    # Define the path to the VS Code settings.json file
    settings_json = "Library/Application Support/Code/User/settings.json"
    settings_path = Path.home() / settings_json
    output_settings = Path("vscode.json")
    output_extensions = Path("vscodeextension")

    # Check if the settings.json file exists
    if not settings_path.exists():
        print(f"❌ VS Code settings.json not found at: {settings_path}")
        return

    # Read and write the settings.json content
    try:
        with open(settings_path, "r", encoding="utf-8") as f:
            settings_data = json.load(f)
        with open(output_settings, "w", encoding="utf-8") as f:
            json.dump(settings_data, f, indent=2)
        print(f"✅ VS Code settings exported to {output_settings}")
    except Exception as e:
        print(f"❌ Error reading/writing settings.json: {e}")
        return

    # List installed extensions and write to file
    try:
        result = subprocess.run(
            ["code", "--list-extensions"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        with open(output_extensions, "w", encoding="utf-8") as f:
            f.write(result.stdout)
        print(f"✅ VS Code extensions list saved to {output_extensions}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error listing extensions: {e.stderr.strip()}")
    except FileNotFoundError:
        print("❌ 'code' command not found.")


if __name__ == "__main__":
    export_vscode_settings()
