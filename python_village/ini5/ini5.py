def even_numbered_lines(in_file, out_file):
    """Returns the even numbered lines of a file."""
    with open(in_file, 'r') as f:
        out = [line for i, line in enumerate(f) if i % 2 == 1]
    with open(out_file, 'w') as f:
        for line in out:
            f.write(line)

if __name__ == '__main__':
    even_numbered_lines('ini5_in.txt', 'ini5_out.txt')