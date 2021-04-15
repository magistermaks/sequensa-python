
from .native import libsq as native
from .stream import Stream


class Executor:

    def __init__(self):
        self.__pointer = native.seq_executor_new()

    def __del__(self):
        native.seq_executor_free(self.__pointer)

    def ptr(self):
        return self.__pointer

    def execute(self, program):
        program.execute(self)

    def results(self):
        return Stream(native.seq_executor_results_stream_ptr(self.__pointer))
