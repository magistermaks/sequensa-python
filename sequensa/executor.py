
from .native import libsq as native
from .stream import Stream


def default_error_handle(ptr):
    return False


class Executor:

    def __init__(self):
        self.__error = native.SQERRHANDLE(default_error_handle)
        self.__pointer = native.seq_executor_new()

    def __del__(self):
        native.seq_executor_free(self.__pointer)

    def ptr(self):
        return self.__pointer

    def err(self):
        return self.__error

    def set_error_handle(self, handle):
        self.__error = handle

    def execute(self, program):
        program.execute(self)

    def strict_math(self, flag):
        native.seq_executor_strict_math(self.__pointer, flag)

    def results(self):
        return Stream(native.seq_executor_results_stream_ptr(self.__pointer))
