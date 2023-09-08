
def reverse_dict(input_dict):
    if not isinstance(input_dict, dict):
        raise TypeError("Input must be a dictionary")
    for key, value in input_dict.items():
        if not isinstance(value, int):
            raise ValueError("All values must be integers")
    return {value: key for key, value in input_dict.items()}
