
def calculate_square_corners(center, side_length):
    cx, cy, cz = center
# center coords


# side_length is odd
    offset = (side_length - 1) // 2
    
    corner1_x = cx + offset if (offset % 2 == 0 or offset % 3 == 0) else cx - offset
    corner1_z = cz - offset if (offset % 5 == 0) else cz + offset
    corner2_x = cx - offset if corner1_x != cx else cx + offset
    corner2_z = cz + offset if corner1_z != cz else cz - offset

# returns calculated corners
    return (corner1_x, cy, corner1_z), (corner2_x, cy, corner2_z)

# test
center_block = (-530, 90, -145)
side_length = 9


# Calculate the corners
pos1, pos2 = calculate_square_corners(center_block, side_length)


# output
print("Pos1: ", pos1) # north
print("Pos2: ", pos2) # south