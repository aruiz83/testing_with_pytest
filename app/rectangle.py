
def validate_rectangle_args(width, height):
    if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')


def area(width, height):
    """Calculate the area of a rectangle given its width and height."""
    validate_rectangle_args(width, height)
    return width * height


def perimeter(width, height):
    """Calculate the perimeter of a rectangle given its width and height."""
    validate_rectangle_args(width, height)
    return 2 * (width + height)
