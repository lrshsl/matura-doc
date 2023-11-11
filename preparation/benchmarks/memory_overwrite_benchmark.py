# Note: time.perf_counter() function is used in this script, not the timeit module. This is because the latter disables the garbage collector, the influence of which should be measured

import numpy as np
import time


def main():
	# Run the benchmark repeatedly, increasing how many times the array it is overwritten
	shape = (200, 200, 100)
	repeats = 100
	for i in range(1, 3):
		n = 10 ** i
		print(f"### Benchmarking with n = {n}, shape = {shape}, repeats = {repeats} ###")

		# Overwriting
		benchmark_overwriting(10, shape, repeats)			# Warmup
		t_overwriting = benchmark_overwriting(n, shape, repeats)

		# Naive
		benchmark_naive(10, shape, repeats)					# Warmup
		t_naive = benchmark_naive(n, shape, repeats)

		print(f"naive = {t_naive}")
		print(f"overwriting = {t_overwriting}\n")


def benchmark_naive(n=1000, shape=(100, 100, 3), repeats=100):
	times = np.zeros(repeats)

	# Record `repeats` different tests
	for i in range(repeats):
		t0 = time.perf_counter()

		# Create the array
		a = np.full(shape=shape, fill_value=1)

		# Change it `n` times (no overwriting)
		for _ in range(n):
			a = np.zeros_like(a)

		# Stop the time
		t1 = time.perf_counter()
		times[i] = t1 - t0

	# Return the average time
	return times.mean()


def benchmark_overwriting(n=1000, shape=(100, 100, 3), repeats=100):
	times = np.zeros(repeats)

	# Record `repeats` different tests
	for i in range(repeats):
		t0 = time.perf_counter()

		# Create the array
		a = np.full(shape=shape, fill_value=1)

		# Change it `n` times (no overwriting)
		for _ in range(n):
			a[:] = np.zeros_like(a)

		# Stop the time
		t1 = time.perf_counter()
		times[i] = t1 - t0
	
	# Return the average time
	return times.mean()


if __name__ == "__main__":
    main()


