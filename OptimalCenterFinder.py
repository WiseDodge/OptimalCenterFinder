def calculate_square_corners(center, map_size):
    cx, cy, cz = center
    is_odd = map_size % 2 != 0
    offset = (map_size - 1) // 2 if is_odd else map_size // 2
    


# returns calculated corners
    return (cx - offset, cy, cz - offset), (cx + offset, cy, cz + offset)


if __name__ == "__main__":
    try:
        center_block = tuple(map(int, input("Enter the center block's coordinates (x y z or x,y,z):").replace(",", " ").split()))
        map_size = int(input("Enter the map size (example: 9, 300, etc): ").strip())
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        exit()
        

    corner1, corner2 = calculate_square_corners(center_block, map_size)
    center_type = "1-block center" if map_size % 2 != 0 else "2x2 center"


    # output
    print("\n--- Results ---")
    print(f"Center Block Position: {center_block}")
    print(f"For a map size of {map_size}, a {center_type} is recommended for better symmetry.")
    print(f"Opposite Corner 1: {corner1}")
    print(f"Opposite Corner 2: {corner2}")