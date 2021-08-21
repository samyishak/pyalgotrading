

def read_lines(filepath, range=5):
    with open(filepath, 'r') as f:
        for _ in range(range):
            print(f.readline(), end='')
