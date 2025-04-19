def calculate_square_corners(center, map_size):
    cx, cy, cz = center
    is_odd = map_size % 2 != 0
    offset = (map_size - 1) // 2 if is_odd else map_size // 2

# returns calculated corners
    return (cx - offset, cy, cz - offset), (cx + offset, cy, cz + offset)


def get_center_input():
    try:
        coords = input("Enter the center block coordinates (x y z or x,y,z): ").replace(",", " ").split()
        if len(coords) != 3:
            raise ValueError("Please provide exactly three coordinates.")
        return tuple(map(int, coords))
    except ValueError as e:
        print(f"The input is invalid: {e}. Try again.")
        return get_center_input()


def get_map_size():
    try:
        size = int(input("Enter map size (e.g., 9, 300): ").strip())
        if size <= 0:
            raise ValueError("The Map size must be a positive integer.")
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