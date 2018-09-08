# binary file writer


def write(path, data):
    with open(path, "wb") as file:
        file.write(data)
