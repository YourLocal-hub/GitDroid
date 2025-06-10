# GitHub Kotlin App Maker

This is a simple Kotlin App Maker that sets up the basic structure of a Kotlin project.

## 📁 Included Files

- `configuration.json`: App configurations (name, version, language, file type, etc.)
- `installer.py`: Python script that creates the app and deletes itself and the config

## 🚀 How to Use

1. **Edit `configuration.json`**
   - Set `app_name`, `entry_point`, `version`, `output_type` (e.g., `.apk`), and `language` (`Kotlin` or `Java`).

2. **Run the Installer**
   ```bash
   python installer.py
   ```

3. **Result**
   - A folder named after your app will be created.
   - The Kotlin entry file (e.g., `Main.kt`) will be generated.
   - `installer.py` and `configuration.json` will delete themselves.

## 🛠 Requirements
- Python 3.x
- Kotlin compiler or Android Studio (for building the .apk)

## ✅ Example
With `configuration.json`:
```json
{
    "app_name": "KotlinApp",
    "version": "1.0.0",
    "author": "YourName",
    "description": "A Kotlin app created by GitHub App Maker",
    "entry_point": "Main.kt",
    "language": "Kotlin",
    "output_type": ".apk"
}
```
Run:
```bash
python installer.py
```
