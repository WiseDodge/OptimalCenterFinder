def calculate_square_corners(center, map_size):
    cx, cy, cz = center


# odd/even -> for symmetry
    is_odd = map_size % 2 != 0
    offset = (map_size - 1) // 2 if is_odd else map_size // 2
    
    corner1 = (cx - offset, cy, cz - offset)
    corner2 = (cx + offset, cy, cz + offset)

# returns calculated corners
    return corner1, corner2

# test
center_block = (-530, 90, -145)
map_size = 9


# Calculate the corners
pos1, pos2 = calculate_square_corners(center_block, map_size)


# output
print("Pos1: ", pos1) # north
print("Pos2: ", pos2) # south