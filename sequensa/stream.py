
from .native import libsq as native
from .generic import Generic


class Stream:

    def __init__(self, pointer):
        self.__pointer = pointer

    def size(self):
        return native.seq_stream_size(self.__pointer)

    def get(self, index):
        return Generic(native.seq_stream_generic_ptr(self.__pointer, index))