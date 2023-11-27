# Note: time.perf_counter() function is used in this script, not the timeit module. This is because the latter disables the garbage collector, the influence of which should be measured

import numpy as np
import time


def main():
	# Run the benchmark repeatedly, increasing how many times the array it is overwritten
	SHAPE = (100, 100, 3)
	REPEATS = 100

	# With varying numbers of changes to the array (overwrite operations)
	print("###------- Benchmarking with varying numbers of changes to the array (overwrite operations) -------###\n\n")
	array_size = 100			# array size is constant
	for i in range(1, 3):
		n = 10 ** i				# 10, 100, 1_000..
		exec_benchmarks(n, SHAPE, array_size, REPEATS)
	
	# With different array sizes
	print("###------- Benchmarking with different array sizes -------###\n\n")
	n = 100					    # n is constant
	for i in range(1, 4):
		array_size = 10 ** i	# 10, 100, 1_000..
		exec_benchmarks(n, SHAPE, array_size, REPEATS)


def exec_benchmarks(n, shape, array_size, repeats):
	print(f"#-- Benchmarking with n = {n}, shape = {shape}, array length = {array_size}, repeats = {repeats} --#")

	# Naive
	benchmark_naive(10, shape, array_size, repeats)					# Warmup
	t_naive, avg_naive = benchmark_naive(
			n, shape, array_size, repeats)

	print(f"naive = {t_naive}s (mean = {avg_naive})")

	# Overwriting
	benchmark_overwriting(10, shape, array_size, repeats)			# Warmup
	t_overwriting, avg_overwriting = benchmark_overwriting(
			n, shape, array_size, repeats)

	print(f"overwriting = {t_overwriting}s (mean = {avg_overwriting})\n")


def benchmark_naive(n=1000, shape=(100, 100, 3), array_size=10_000, repeats=100):
	times = np.zeros(repeats)

	# Record `repeats` different tests
	for i in range(repeats):
		t0 = time.perf_counter()

		# Create the array
		a = np.full(shape=(*shape, array_size), fill_value=1)

		# Change it `n` times (no overwriting)
		for _ in range(n):
			a = np.zeros_like(a)

		# Stop the time
		t1 = time.perf_counter()
		times[i] = t1 - t0

	# Return the mesured times
	return times.sum(), times.mean()


def benchmark_overwriting(n=1000, shape=(100, 100, 3), array_size=10_000, repeats=100):
	times = np.zeros(repeats)

	# Record `repeats` different tests
	for i in range(repeats):
		t0 = time.perf_counter()

		# Create the array
		a = np.full(shape=(*shape, array_size), fill_value=1)

		# Change it `n` times (through overwriting)
		for _ in range(n):
			a[:] = np.zeros_like(a)

		# Stop the time
		t1 = time.perf_counter()
		times[i] = t1 - t0
	
	# Return the measured times
	return times.sum(), times.mean()


if __name__ == "__main__":
    main()


