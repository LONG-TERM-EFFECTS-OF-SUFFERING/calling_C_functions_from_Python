#include <immintrin.h>


void vector_scalar_multiplication(double* vector, double scalar, int size) {
	// If the vector size is not a multiple of four, we have to calculate
	// that remainder without AVX operations
	int remainder = size % 4;

	for (int i = size - remainder; i < size; i++)
		vector[i] *= scalar;

	// Loop through the vector in 4-element chunks because AVX instructions
	// operate on 256 bits of data at once, which corresponds to a 4
	// double-precision floating-point numbers
	for (int i = 0; i < size - remainder; i += 4) {
		// Load the vector chunk into AVX register
		__m256d vector1 = _mm256_loadu_pd(vector + i);

		// Broadcast the scalar value to all elements of another AVX register
		__m256d vector2 = _mm256_broadcast_sd(&scalar);

		// Perform element-wise multiplication
		__m256d result = _mm256_mul_pd(vector1, vector2);

		// Store the result back to memory
		_mm256_storeu_pd(vector + i, result);
	}
}
