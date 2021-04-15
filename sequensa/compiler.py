
from .native import libsq as native
from .program import Program
from ctypes import *


class Compiler:

    def __init__(self):
        self.__pointer = native.seq_compiler_new()

    def __del__(self):
        native.seq_compiler_free(self.__pointer)

    def build(self, code):
        size = c_int()
        buffer = native.seq_compiler_build_new(self.__pointer, code, byref(size))

        if size.value != 0:
            return Program(buffer, size)
        else:
            return None

    def error_handle(self, handle):
        native.seq_compiler_error_handle(self.__pointer, handle)
