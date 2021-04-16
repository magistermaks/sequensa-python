
from ctypes import *
libsq = cdll.LoadLibrary('/home/magistermaks/sequensa/libseqapi.so')

libsq.SQNATIVE = CFUNCTYPE(c_void_p, c_void_p)
libsq.SQERRHANDLE = CFUNCTYPE(c_bool, c_void_p)

# Dummy function
libsq.seq_verify.__doc__ = "Dummy function"
libsq.seq_verify.restype = c_int 
libsq.seq_verify.argtypes = []
seq_verify = libsq.seq_verify

# Generic free()
libsq.seq_free.__doc__ = "Generic free()"
libsq.seq_free.restype = None
libsq.seq_free.argtypes = [c_void_p]
seq_free = libsq.seq_free

# Get major version component
libsq.seq_version_major.__doc__ = "Get major version component"
libsq.seq_version_major.restype = c_int 
libsq.seq_version_major.argtypes = []
seq_version_major = libsq.seq_version_major

# Get minor version component
libsq.seq_version_minor.__doc__ = "Get minor version component"
libsq.seq_version_minor.restype = c_int 
libsq.seq_version_minor.argtypes = []
seq_version_minor = libsq.seq_version_minor

# Get path version component
libsq.seq_version_patch.__doc__ = "Get path version component"
libsq.seq_version_patch.restype = c_int 
libsq.seq_version_patch.argtypes = []
seq_version_patch = libsq.seq_version_patch

# Get standard name
libsq.seq_standard.__doc__ = "Get standard name"
libsq.seq_standard.restype = c_char_p 
libsq.seq_standard.argtypes = []
seq_standard = libsq.seq_standard

# Free Compiler object allocated using seq_compiler_new
libsq.seq_compiler_free.__doc__ = "Free Compiler object allocated using seq_compiler_new"
libsq.seq_compiler_free.restype = None
libsq.seq_compiler_free.argtypes = [c_void_p]
seq_compiler_free = libsq.seq_compiler_free

# Create new Compiler object
libsq.seq_compiler_new.__doc__ = "Create new Compiler object"
libsq.seq_compiler_new.restype = c_void_p 
libsq.seq_compiler_new.argtypes = []
seq_compiler_new = libsq.seq_compiler_new

# Free program buffer
libsq.seq_compiler_build_free.__doc__ = "Free program buffer"
libsq.seq_compiler_build_free.restype = None
libsq.seq_compiler_build_free.argtypes = [c_void_p]
seq_compiler_build_free = libsq.seq_compiler_build_free

# Create and populate new program buffer
libsq.seq_compiler_build_new.__doc__ = "Create and populate new program buffer"
libsq.seq_compiler_build_new.restype = c_void_p 
libsq.seq_compiler_build_new.argtypes = [c_void_p, c_char_p, POINTER(c_int)]
seq_compiler_build_new = libsq.seq_compiler_build_new

# create new buffer, it needs to be later freed
libsq.seq_buffer_new.__doc__ = "create new buffer, it needs to be later freed"
libsq.seq_buffer_new.restype = c_void_p 
libsq.seq_buffer_new.argtypes = [c_void_p, c_int]
seq_buffer_new = libsq.seq_buffer_new

# Set compiler optimization flags
libsq.seq_compiler_optimizations.__doc__ = "Set compiler optimization flags"
libsq.seq_compiler_optimizations.restype = None
libsq.seq_compiler_optimizations.argtypes = [c_void_p, c_int]
seq_compiler_optimizations = libsq.seq_compiler_optimizations

# Set Compiler error handle
libsq.seq_compiler_error_handle.__doc__ = "Set Compiler error handle"
libsq.seq_compiler_error_handle.restype = None
libsq.seq_compiler_error_handle.argtypes = [c_void_p, c_void_p]
seq_compiler_error_handle = libsq.seq_compiler_error_handle

# Query error message from any exception
libsq.seq_exception_message.__doc__ = "Query error message from any exception"
libsq.seq_exception_message.restype = c_char_p 
libsq.seq_exception_message.argtypes = [c_void_p]
seq_exception_message = libsq.seq_exception_message

# Query error level from compiler exception
libsq.seq_compiler_error_level.__doc__ = "Query error level from compiler exception"
libsq.seq_compiler_error_level.restype = c_int 
libsq.seq_compiler_error_level.argtypes = [c_void_p]
seq_compiler_error_level = libsq.seq_compiler_error_level

# Decompile given bytecode buffer
libsq.seq_decompile.__doc__ = "Decompile given bytecode buffer"
libsq.seq_decompile.restype = c_void_p 
libsq.seq_decompile.argtypes = [c_void_p, c_int, c_char_p, c_int]
seq_decompile = libsq.seq_decompile

# Free Executor object allocated using seq_executor_new
libsq.seq_executor_free.__doc__ = "Free Executor object allocated using seq_executor_new"
libsq.seq_executor_free.restype = None
libsq.seq_executor_free.argtypes = [c_void_p]
seq_executor_free = libsq.seq_executor_free

# Create new Executor object
libsq.seq_executor_new.__doc__ = "Create new Executor object"
libsq.seq_executor_new.restype = c_void_p 
libsq.seq_executor_new.argtypes = []
seq_executor_new = libsq.seq_executor_new

# Set Executor's strict math flag
libsq.seq_executor_strict_math.__doc__ = "Set Executor's strict math flag"
libsq.seq_executor_strict_math.restype = None
libsq.seq_executor_strict_math.argtypes = [c_void_p, c_bool]
seq_executor_strict_math = libsq.seq_executor_strict_math

# Execute given program
libsq.seq_executor_execute.__doc__ = "Execute given program"
libsq.seq_executor_execute.restype = None
libsq.seq_executor_execute.argtypes = [c_void_p, c_void_p, c_int, c_void_p]
seq_executor_execute = libsq.seq_executor_execute

# Get pointer to the results stream
libsq.seq_executor_results_stream_ptr.__doc__ = "Get pointer to the results stream"
libsq.seq_executor_results_stream_ptr.restype = c_void_p 
libsq.seq_executor_results_stream_ptr.argtypes = [c_void_p]
seq_executor_results_stream_ptr = libsq.seq_executor_results_stream_ptr

# Add native function to executor
libsq.seq_executor_add_native.__doc__ = "Add native function to executor"
libsq.seq_executor_add_native.restype = None
libsq.seq_executor_add_native.argtypes = [c_void_p, c_char_p, c_void_p]
seq_executor_add_native = libsq.seq_executor_add_native

# Get stream size
libsq.seq_stream_size.__doc__ = "Get stream size"
libsq.seq_stream_size.restype = c_int 
libsq.seq_stream_size.argtypes = [c_void_p]
seq_stream_size = libsq.seq_stream_size

# Get a new stream object, for use in native functions
libsq.seq_stream_create.__doc__ = "Get a new stream object, for use in native functions"
libsq.seq_stream_create.restype = c_void_p 
libsq.seq_stream_create.argtypes = []
seq_stream_create = libsq.seq_stream_create

# Free Stream object allocated using seq_stream_create
libsq.seq_stream_free.__doc__ = "Free Stream object allocated using seq_stream_create"
libsq.seq_stream_free.restype = None
libsq.seq_stream_free.argtypes = [c_void_p]
seq_stream_free = libsq.seq_stream_free

# Get generic from stream
libsq.seq_stream_generic_ptr.__doc__ = "Get generic from stream"
libsq.seq_stream_generic_ptr.restype = c_void_p 
libsq.seq_stream_generic_ptr.argtypes = [c_void_p, c_int]
seq_stream_generic_ptr = libsq.seq_stream_generic_ptr

# Clear the stream
libsq.seq_stream_clear.__doc__ = "Clear the stream"
libsq.seq_stream_clear.restype = None
libsq.seq_stream_clear.argtypes = [c_void_p]
seq_stream_clear = libsq.seq_stream_clear

# Append to stream
libsq.seq_stream_add.__doc__ = "Append to stream"
libsq.seq_stream_add.restype = None
libsq.seq_stream_add.argtypes = [c_void_p, c_void_p]
seq_stream_add = libsq.seq_stream_add

# Get data type from generic
libsq.seq_generic_type.__doc__ = "Get data type from generic"
libsq.seq_generic_type.restype = c_int 
libsq.seq_generic_type.argtypes = [c_void_p]
seq_generic_type = libsq.seq_generic_type

# Get anchor from generic
libsq.seq_generic_anchor.__doc__ = "Get anchor from generic"
libsq.seq_generic_anchor.restype = c_int 
libsq.seq_generic_anchor.argtypes = [c_void_p]
seq_generic_anchor = libsq.seq_generic_anchor

# Query long from number generic
libsq.seq_generic_number_long.__doc__ = "Query long from number generic"
libsq.seq_generic_number_long.restype = c_long 
libsq.seq_generic_number_long.argtypes = [c_void_p]
seq_generic_number_long = libsq.seq_generic_number_long

# Query double from number generic
libsq.seq_generic_number_double.__doc__ = "Query double from number generic"
libsq.seq_generic_number_double.restype = c_double 
libsq.seq_generic_number_double.argtypes = [c_void_p]
seq_generic_number_double = libsq.seq_generic_number_double

# Query string from string generic
libsq.seq_generic_string_string.__doc__ = "Query string from string generic"
libsq.seq_generic_string_string.restype = c_char_p 
libsq.seq_generic_string_string.argtypes = [c_void_p]
seq_generic_string_string = libsq.seq_generic_string_string

# Query bool from string generic
libsq.seq_generic_bool_bool.__doc__ = "Query bool from string generic"
libsq.seq_generic_bool_bool.restype = c_bool 
libsq.seq_generic_bool_bool.argtypes = [c_void_p]
seq_generic_bool_bool = libsq.seq_generic_bool_bool

# Create new generic number object
libsq.seq_generic_number_create.__doc__ = "Create new generic number object"
libsq.seq_generic_number_create.restype = c_void_p 
libsq.seq_generic_number_create.argtypes = [c_bool, c_double]
seq_generic_number_create = libsq.seq_generic_number_create

# Create new generic bool object
libsq.seq_generic_bool_create.__doc__ = "Create new generic bool object"
libsq.seq_generic_bool_create.restype = c_void_p 
libsq.seq_generic_bool_create.argtypes = [c_bool, c_bool]
seq_generic_bool_create = libsq.seq_generic_bool_create

# Create new generic string object
libsq.seq_generic_string_create.__doc__ = "Create new generic string object"
libsq.seq_generic_string_create.restype = c_void_p 
libsq.seq_generic_string_create.argtypes = [c_bool, c_char_p]
seq_generic_string_create = libsq.seq_generic_string_create

# Create new generic null object
libsq.seq_generic_null_create.__doc__ = "Create new generic null object"
libsq.seq_generic_null_create.restype = c_void_p 
libsq.seq_generic_null_create.argtypes = [c_bool]
seq_generic_null_create = libsq.seq_generic_null_create


