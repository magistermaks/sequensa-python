
from .native import libsq as native


class Generic:

    def __init__(self, pointer):
        self.__pointer = pointer

    def get_long(self):
        return native.seq_generic_number_long(self.__pointer)

