def calculate_square_corners(center, map_size):
    cx, cy, cz = center
    is_odd = map_size % 2 != 0
    offset = (map_size - 1) // 2 if is_odd else map_size // 2
    
# converge result    corner1 = (cx - offset, cy, cz - offset)
# converge result    corner2 = (cx + offset, cy, cz + offset)

# returns calculated corners
    return cx - offset, cy, cz - offset, cx + offset, cy, cz + offset


def get_center_input():
    try:
        coords = input("Enter the center block's coordinates (x y z): ")
        if len(coords) != 3:
            raise ValueError("Please provide exactly THREE coordinates.")
        return tuple(map(int, coords))
        
    except ValueError as e:    
        print(f"The input is invalid: {e}. Try again.")
        return get_center_input()


# map size
def get_map_size():
    try:
        size = int(input("Enter the map size (example: 9, 300, etc): "))
        if size <= 0:
            raise ValueError("The given map size has to be a positive integer.")
        return size
    
    except ValueError as e:
        print(f"The input is invalid: {e}. Try again.")
        return get_map_size()

# center_block = (-530, 90, -145)
# map_size = 9



if __name__ == "__main__":
    center_block = get_center_input()
    map_size = get_map_size()

    pos1, pos2  = calculate_square_corners(center_block, map_size)

    # output
    print("\nResults:")
    print(f"Pos1: {pos1}") # north
    print(f"Pos2: {pos2}") # south