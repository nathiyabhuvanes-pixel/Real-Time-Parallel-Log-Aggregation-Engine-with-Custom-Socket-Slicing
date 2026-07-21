def sort_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    lines.sort()

    with open(file, 'w') as f:
        f.writelines(lines)