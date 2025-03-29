
def draw_pyramid(height):
    for i in range(height):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (height - i - 1)
        print(spaces + stars)

# Calling the function with height 5
draw_pyramid(5)
