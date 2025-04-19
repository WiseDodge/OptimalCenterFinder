import pyperclip
import re
from typing import Optional, Tuple

DEBUG = False  # default: False. Set to True for debugging/testing

def calculate_square_corners(center: Tuple[int, int, int], map_size: int) -> Tuple[Tuple[int, int, int], Tuple[int, int, int]]:
    cx, cy, cz = center
    is_odd = map_size % 2 != 0
    offset = (map_size - 1) // 2 if is_odd else map_size // 2

# returns calculated corners
    return (cx - offset, cy, cz - offset), (cx + offset, cy, cz + offset)

def attempt_clipboard_center() -> Optional[Tuple[int, int, int]]:
    try:
        clipboard_txt = pyperclip.paste().strip()
        vals = re.split(r"[\s,]+", clipboard_txt)
        if len(vals) == 3 and all(v.lstrip("-").isdigit() for v in vals):
            return tuple(map(int, vals))
    except Exception as e:
        print(f"Error accessing clipboard: {e}")
    return None

def get_center_input() -> Tuple[int, int, int]:
    retry_count = 0
    clipboard_coords = attempt_clipboard_center()
    clipboard_checked = False

    while retry_count < 5:
        if clipboard_coords and not clipboard_checked:
            print(f"ggs. Auto-detected your coordinates from clipboard: {clipboard_coords}")
            use_clipboard = input("Use these coordinates? (y/n): ").strip().lower()
            clipboard_checked = True
            if use_clipboard == "y":
                return clipboard_coords

        # manual input if clipboard wasn't used
        coords = input("Enter the center block coordinates (x y z or x,y,z), or 'x' to exit: ").replace(",", " ").split()
        if coords == ['x']:
            print("Exiting the program.")
            exit()

        if len(coords) != 3:
            print("Please provide exactly three coordinates (e.g., x y z).")
        elif not all(c.lstrip("-").isdigit() for c in coords):
            print("Invalid input: coordinates must be whole numbers (integers).")
        else:
            try:
                return tuple(map(int, coords))
            except ValueError:
                print("Unexpected error during coordinate parsing.")

        retry_count += 1
        if retry_count >= 3:
            print("Three strikes and you're out! Exiting program.")
            exit()

    # fallback
    print("Error: Could not process the coordinates.")
    exit()

def get_map_size() -> int:
    size_input = input("Enter map size (e.g., 9, 300), or 'x' to exit: ").strip()
    if size_input.lower() == 'x':
        print("Exiting program.")
        exit()

    normalized = size_input.lstrip("-")
    if not normalized.isdigit():
        print("The input is invalid: map size must be a whole number. Try again.")
        return get_map_size()

    size = int(size_input)
    if size <= 0:
        print("The map size must be a positive integer. Try again.")
        return get_map_size()
    return size

def run():
    if DEBUG:
        center_block = (0, 64, 0)
        map_size = 25
        print(f"DEBUG MODE ACTIVE: Using center {center_block} with map size {map_size}")
    else:
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