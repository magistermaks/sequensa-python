
from .native import libsq as native


class Program:

    def __init__(self, pointer, size):
        self.__pointer = pointer
        self.__size = size

    def __del__(self):
        native.seq_compiler_build_free(self.__pointer)

    def execute(self, executor):
        native.seq_executor_execute(executor.ptr(), self.__pointer, self.__size)
