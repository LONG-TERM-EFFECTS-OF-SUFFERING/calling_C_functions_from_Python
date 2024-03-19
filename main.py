import ctypes
import timeit
import numpy as np


n = 1000000
repetitions = 10
T_s = 0
T_numpy = 0
T_avx_python = 0
T_avx_numpy = 0


def python_array_without_library(n):
	x = 2
	v = [i for i in range(1, n + 1)]

	for i in range(n):
		v[i] = v[i] * x

	# print(v)

times = timeit.repeat(stmt="python_array_without_library(n)", number=repetitions, globals=globals())
average_time = sum(times) / repetitions
T_s = average_time

# ---------------------------------------------------------------------------- #

def numpy_array_without_library(n):
	x = 2
	v = np.array(range(1, n + 1))

	for i in range(n):
		v[i] = v[i] * x

	# print(v)

times = timeit.repeat(stmt="numpy_array_without_library(n)", number=repetitions, globals=globals())
average_time = sum(times) / repetitions
T_numpy = average_time

# ---------------------------------------------------------------------------- #

def python_array_with_library(n):
	lib = ctypes.CDLL("./scalar_multiplication_lib.so")
	lib.vector_scalar_multiplication.restype = None
	lib.vector_scalar_multiplication.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.c_int]

	x = 2
	v = [i for i in range(1, n + 1)]
	c_v = (ctypes.c_double * (n))(*v)

	lib.vector_scalar_multiplication(c_v, x, n)

	# print(list(c_v))

times = timeit.repeat(stmt="python_array_with_library(n)", number=repetitions, globals=globals())
average_time = sum(times) / repetitions
T_avx_p = average_time

# ---------------------------------------------------------------------------- #

def numpy_array_with_library(n):
	lib = ctypes.CDLL("./scalar_multiplication_lib.so")
	lib.vector_scalar_multiplication.restype = None
	lib.vector_scalar_multiplication.argtypes = [
		np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),
		ctypes.c_double,
		ctypes.c_int
	]

	x = 2
	v = np.array(range(1, n + 1), dtype=np.float64)

	lib.vector_scalar_multiplication(v, x, n - 1)

	# print(v)

times = timeit.repeat(stmt="numpy_array_with_library(n)", number=repetitions, globals=globals())
average_time = sum(times) / repetitions
T_avx_n = average_time

# ---------------------------------------------------------------------------- #

print(f"T_s: {T_s}")
print(f"T_numpy: {T_numpy}")
print(f"T_avx_p: {T_avx_p}")
print(f"T_avx_n: {T_avx_n}")

print(f"Speedup_numpy: {T_s / T_numpy}")
print(f"Speedup_avx_p: {T_s / T_avx_p}")
print(f"Speedup_avx_n: {T_s / T_avx_n}")
