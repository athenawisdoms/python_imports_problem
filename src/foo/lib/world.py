from foo import DATA_DIR

def world():
    with open(f'{DATA_DIR}/test.dat') as f:
        name = f.readline()
        return "world, " + name
