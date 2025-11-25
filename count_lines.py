def count_lines(path):
    """Return number of lines in a given file."""
    try:
        with open(path, 'r') as f:
            return sum(1 for _ in f)
    except Exception:
        return -1  # indicates error
