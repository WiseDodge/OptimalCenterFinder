# OptimalCenterFinder 🗺️

**OptimalCenterFinder** is a Python script that calculates the opposing corners of a square map, given a center coordinate and map size. It’s particularly useful for tools like **WorldEdit**, **Schematica**, and precise **map positioning**. The program supports both odd and even map sizes (1-block vs 2×2 centers), and it allows for auto-detection of coordinates from your clipboard or manual input.

## ✨ Core Features

- **Clipboard Auto-Detection**: Automatically detects center coordinates if they’re copied to your clipboard.
- **Manual Input**: Enter coordinates manually if clipboard auto-detection isn't available.
- **Map Size Handling**: Supports odd (1-block center) and even (2x2 center) map sizes.
- **User-Friendly CLI**: Prompts with clear instructions and retries on invalid input.
- **Debug Mode**: Easily test with hardcoded values for debugging.

## 🛠️ System Requirements

- **Python 3.6+**  
- **`pyperclip` module**: For clipboard access.

Install the required package with:

```bash
pip install pyperclip
```

## 📥 Installation

1. Clone or download the repository to your local machine.
2. Install the required Python dependencies using the command above.
3. Run the script directly using Python:

```bash
python OptimalCenterFinder.py
```

## 🔧 Usage

1. **Run the script**:  
   Start by running the Python script from your terminal. It will guide you through entering coordinates and map size.

2. **Enter the center block coordinates**:  
   - Automatically detected from clipboard content if in the format `x y z`.  
   - Optionally, you can manually input coordinates if clipboard data is unavailable.

   Example of manual input:
   ```txt
   Enter the center block coordinates (x y z or x,y,z), or 'x' to exit:
   ```

   Example of clipboard auto-detection:
   ```txt
   ggs. Auto-detected your coordinates from clipboard: (30, 60, 90)
   Use these coordinates? (y/n): y
   ```

3. **Enter map size**:  
   The map size must be a positive integer. Example: `9` for a 9x9 map. The program also accounts for odd and even sized maps.

   Example:
   ```txt
   Enter map size (e.g., 9, 300), or 'x' to exit: 120
   ```

4. **Output**:  
   The program will calculate and display the opposite corners of the square, based on the given center and map size.

   Example output:
   ```txt
   --- Results ---
   Center Block Position: (30, 60, 90)
   For a map size of 120, a 2x2 center is recommended for better symmetry.
   Opposite Corner 1: (-30, 60, 30)
   Opposite Corner 2: (90, 60, 150)
   ```

5. **Exit**:  
   You can type `x` to exit at any point.

## 🧑‍💻 Development and Debugging w/ Debug Mode

### **Activating Debug Mode**

To run the script in debug mode (useful for testing), set the `DEBUG` flag to `True` in the script:

```python
DEBUG = True
```

This will bypass user input and automatically use a hardcoded center (`(0, 64, 0)`) and map size (`25`).

### Example Debug Output

```txt
DEBUG MODE ACTIVE: Using center (0, 64, 0) with map size 25
```

## 💡 Configuration Tips

- **Change the center block and map size directly**: If you know the coordinates and map size ahead of time, you can modify them directly in the code (instead of relying on user input).
- **Handling invalid input**: The program will give you up to 3 attempts to input valid coordinates before exiting. If you need more flexibility, consider modifying the `retry_count` logic.

## 📝 Potential Enhancements

- **Cuboid Mapping Support**: Extend functionality to support cuboid maps (allowing for y-axis expansion).
- **Command-Line Arguments**: Enable the script to accept map size and center as arguments instead of interactive input.
- **Clipboard Output**: Copy the calculated corners back to the clipboard for easy pasting elsewhere.
- **Minecraft Integration**: Future versions could allow integration with Minecraft server tools (like WorldEdit).

---

## 📝 **Development & Contribution**

Feel free to fork, modify, or contribute to the development of the script. Contributions such as adding support for 3D cuboid mapping or further enhancing the CLI interaction are encouraged.

---

## 📜 **License**

MIT License – Open-source, free for modification and redistribution.

---