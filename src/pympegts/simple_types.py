# -*- coding: UTF-8, tab-width: 4 -*-

class shybytes(bytes):
    '''
    Like bytes, but too shy to expose themselves to print() and repr().
    '''
    def __repr__(self):
        return f"{type(self).__name__}[{len(self)}]"

