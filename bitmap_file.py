import binary

import bitmap_header
import bitmap_data


class BmpFile:
    def __init__(self, data, width, height, filename='0000.bmp'):
        self.data = bitmap_data.BmpData(data)
        sizeofdata = len(self.data)
        sizeoffile = sizeofdata + 54             # 54 is the size of the header
        self.header = bitmap_header.BmpHeader(sizeoffile, sizeofdata, width, height)
        self.filename = filename

    def write(self):
        binary.write(self.filename, self.header.get() + self.data.get())
