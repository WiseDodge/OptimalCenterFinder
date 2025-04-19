import pyperclip
import re

def calculate_square_corners(center, map_size):
    cx, cy, cz = center
    is_odd = map_size % 2 != 0
    offset = (map_size - 1) // 2 if is_odd else map_size // 2

# returns calculated corners
    return (cx - offset, cy, cz - offset), (cx + offset, cy, cz + offset)

def attempt_clipboard_center():
    clipboard_txt = pyperclip.paste().strip()
    vals = re.split(r"[\s,]+", clipboard_txt)
    if len(vals) == 3 and all(v.lstrip("-").isdigit() for v in vals):
        return tuple(map(int, vals))
    return None

def get_center_input():
    retry_count = 0
    while retry_count < 5:
        clipboard_coords = attempt_clipboard_center()
        if clipboard_coords:
            print(f"ggs. Auto-detected your coordinates from clipboard: {clipboard_coords}")
            use_clipboard = input("Use these coordinates? (y/n): ").strip().lower()
            if use_clipboard == "y":
                return clipboard_coords

        # manual input if clipboard wasn't used
        coords = input("Enter the center block coordinates (x y z or x,y,z), or 'x' to exit: ").replace(",", " ").split()
        if coords == ['x']:
            print("Exiting the program.")
            exit()
            
        if len(coords) != 3:
            print("Please provide exactly three coordinates (e.g., x y z).")
        else:
            try:
                return tuple(map(int, coords))
            except ValueError:
                print("Invalid input: coordinates must be integers.")
        
        retry_count += 1
        if retry_count >= 3:
            print("Too many invalid attempts. Exiting program.")
            exit()

    # fallback
    print("Error: Could not process the coordinates.")
    exit()

def get_map_size():
    size_input = input("Enter map size (e.g., 9, 300), or 'x' to exit: ").strip()
    if size_input.lower() == 'x':
        print("Exiting program.")
        exit()
    try:
        size = int(size_input)
        if size <= 0:
            raise ValueError("The map size must be a positive integer.")
        return size
    except ValueError as e:
        print(f"The input is invalid: {e}. Try again.")
        return get_map_size()

def run():
    center_block = get_center_input()
    map_size = get_map_size()

    corner1, corner2 = calculate_square_corners(center_block, map_size)
    center_type = "1-block center" if map_size % 2 != 0 else "2x2 center"


    # output
    print("\n--- Results ---")
    print(f"Center Block Position: {center_block}")
    print(f"For a map size of {map_size}, a {center_type} is recommended for better symmetry.")
    print(f"Opposite Corner 1: {corner1}")
    print(f"Opposite Corner 2: {corner2}")

if __name__ == "__main__":
    run()