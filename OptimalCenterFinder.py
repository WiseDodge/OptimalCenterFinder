def calculate_square_corners(center, map_size):
    cx, cy, cz = center
    is_odd = map_size % 2 != 0
    center_type = "1-block center" if is_odd else "2x2 center"
    
    offset = (map_size - 1) // 2 if is_odd else map_size // 2
    
    corner1 = (cx - offset, cy, cz - offset)
    corner2 = (cx + offset, cy, cz + offset)

    recommendedCenter = f"For a map size of {map_size}, a {center_type} is recommended for improving symmetry."

# returns calculated corners
    return recommendedCenter, corner1, corner2



if __name__ == "__main__":
    print("Enter the center block's coordinates (x y z or x,y,z):")
    center_block = tuple(map(int, input().replace(",", " ").split()))
    
    print("Enter the map size (example: 9, 300, etc): ")
    map_size = int(input().strip())

    recommendedCenter, pos1, pos2  = calculate_square_corners(center_block, map_size)

    # output
    print("\nRecommendation:", recommendedCenter)
    print(f"Corner 1: {pos1}") # north
    print(f"Corner 2: {pos2}") # south