class BmpHeader:
    def __init__(self, sizeoffile, sizeofdata,
                 width, height,
                 hdef=12000, vdef=12000,
                 depth=24, compression=0):

        self.signature = bytearray.fromhex('424D')
        self.sizeoffile = bytearray(sizeoffile.to_bytes(4, 'little'))
        self.reserved1 = bytearray(2)
        self.reserved2 = bytearray(2)
        self.startofdata = bytearray((54).to_bytes(4, 'little'))
        self.sizeofinfoheader = bytearray((40).to_bytes(4, 'little'))

        if not width % 2:
            width += 1
        self.width = bytearray(width.to_bytes(4, 'little'))
        self.height = bytearray(height.to_bytes(4, 'little'))
        self.plane = bytearray((1).to_bytes(2, 'little'))

        if depth not in [1, 4, 8, 24]:
            raise ValueError('depth must be 1, 4, 8 or 24 for Bitmap files')
        self.depth = bytearray(depth.to_bytes(2, 'little'))

        if compression not in range(3):
            raise ValueError('compression value must be 0, 1 or 2. 0=none, 1=RLE-8, 2=RLE-4')
        self.compression = bytearray(compression.to_bytes(4, 'little'))
        self.sizeofdata = bytearray(sizeofdata.to_bytes(4, 'little'))
        self.hdef = bytearray(hdef.to_bytes(4, 'little'))
        self.vdef = bytearray(vdef.to_bytes(4, 'little'))
        self.nb_colors = bytearray(4)
        self.important_colors = bytearray(4)
        self.structure = [self.signature,
                          self.sizeoffile,
                          self.reserved1,
                          self.reserved2,
                          self.startofdata,
                          self.sizeofinfoheader,
                          self.width,
                          self.height,
                          self.plane,
                          self.depth,
                          self.compression,
                          self.sizeofdata,
                          self.hdef,
                          self.vdef,
                          self.nb_colors,
                          self.important_colors]

    def __repr__(self):
        reprheader = bytearray()
        for section in self.structure:
            reprheader.extend(section)
        return reprheader

    def __len__(self):
        lenheader = 0
        for section in self.structure:
            lenheader += len(section)
        return lenheader

    def get(self):
        reprheader = bytearray()
        for section in self.structure:
            reprheader.extend(section)
        return reprheader
