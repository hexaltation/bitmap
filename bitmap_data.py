class BmpData:
    def __init__(self, data):
        if not isinstance(data, bytearray):
            raise TypeError('Data type of constructor argument must be bytearray')
        self.data = data

    def __repr__(self):
        return self.data

    def __len__(self):
        return len(self.data)

    def get(self):
        return self.data
