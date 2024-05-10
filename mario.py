from cs50 import get_int

# Get height from user
while True:
    height = get_int("Height: ")
    if height in range(1, 9):
        break

# Print pyramid of height
for i in range(height):

    # Calculate number of spaces needed per row
    spaces = (height - i - 1)

    # Calculate the number of hashes needed per row
    blocks = i + 1

    # Create a string for each row of the pyramid
    row = (" " * spaces + "#" * blocks)

    # Print the row
    print(row)
