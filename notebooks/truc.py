def map(key, value):
    inter = []
    for word in value.split():
        inter.append((word, 1))
    return inter


def reduce(key, values):
    result = 0
    for c in values:
        result = result + c
    return (key, result)