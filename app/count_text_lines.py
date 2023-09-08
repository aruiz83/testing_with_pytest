
def count_lines(filename: str) -> int:
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File {filename} not found") from e
