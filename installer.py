import os
import json

def main():
    with open("configuration.json", "r") as f:
        config = json.load(f)

    app_dir = config["app_name"]
    os.makedirs(app_dir, exist_ok=True)

    # Create entry Kotlin file
    with open(os.path.join(app_dir, config["entry_point"]), "w") as f:
        f.write(f"// Entry point for {config['app_name']}\n")
        f.write(f"// Version: {config['version']}\n")
        f.write(f"// Author: {config['author']}\n")
        f.write("fun main() {\n    println(\"App started successfully!\")\n}\n")

    # Cleanup
    os.remove("configuration.json")
    os.remove("installer.py")
    print(f"Kotlin App '{config['app_name']}' created and installer cleaned up.")

if __name__ == "__main__":
    main()
