def load_level(filename):
    filename = 'maps/' + filename
    with open(filename, 'r') as file:
        level_map = [line.strip() for line in file]
    max_width = max(map(len, level_map))
    level_map = list(map(lambda x: x.ljust(max_width, '.'), level_map))
    return level_map
