import unittest
from matrix import *

class TestMatrix(unittest.TestCase):
	def test_init(self):
		# Test 1
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m = Matrix(values)
		self.assertEqual(m.rows, 2)
		self.assertEqual(m.cols, 3)

		# Test 2
		values = [
			[1, 2],
			[3, 4],
			[5, 6]]
		m = Matrix(values)
		self.assertEqual(m.rows, 3)
		self.assertEqual(m.cols, 2)

		# Exceptions
		values = [
			[1, 2],
			[3, 4],
			[5, 6, 7]]
		self.assertRaises(ValueError, Matrix, values)

	def test_string(self):
		# Test 1
		values = [
			[1, 2],
			[3, 4]]
		m = Matrix(values)
		self.assertEqual(str(m), "1 2\n3 4\n")

		# Test 2
		values = [
			[10, 2],
			[3, 4]]
		m = Matrix(values)
		self.assertEqual(str(m), "10  2\n 3  4\n")

	def test_mul_matrix_matrix_method(self):
		# Test 1
		values = [
			[1, 2],
			[3, 4]]
		m1 = Matrix(values)
		values = [
			[5, 6],
			[7, 8]]
		m2 = Matrix(values)
		values = [
			[19, 22],
			[43, 50]]
		m3 = Matrix(values)
		self.assertEqual(m1.multiply_matrix_matrix(m2), m3)

		# Test 2
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m1 = Matrix(values)
		values = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]]
		m2 = Matrix(values)
		values = [
			[30, 36, 42],
			[66, 81, 96]]
		m3 = Matrix(values)
		self.assertEqual(m1.multiply_matrix_matrix(m2), m3)

		# Exceptions
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m1 = Matrix(values)
		values = [
			[1, 2],
			[3, 4]]
		m2 = Matrix(values)
		self.assertRaises(ValueError, m1.multiply_matrix_matrix, m2)

	def test_mul_matrix_scalar_method(self):
		# Test 1
		values = [
			[1, 1],
			[1, 1]]
		m1 = Matrix(values)
		values = [
			[5, 5],
			[5, 5]]
		m2 = Matrix(values)
		self.assertEqual(m1.multiply_matrix_scalar(5), m2)

	def test_mul_left(self):
		# Test 1
		values = [
			[1, 2],
			[3, 4]]
		m1 = Matrix(values)
		values = [
			[5, 6],
			[7, 8]]
		m2 = Matrix(values)
		values = [
			[19, 22],
			[43, 50]]
		m3 = Matrix(values)
		self.assertEqual(m1 * m2, m3)

		# Test 2
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m1 = Matrix(values)
		values = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]]
		m2 = Matrix(values)
		values = [
			[30, 36, 42],
			[66, 81, 96]]
		m3 = Matrix(values)
		self.assertEqual(m1 * m2, m3)

		# Test 3
		values = [
			[1, 1, 1],
			[2, 2, 2]]
		m1 = Matrix(values)
		values = [
			[3, 3, 3],
			[6, 6, 6]]
		m2 = Matrix(values)
		self.assertEqual(m1 * 3, m2)

	def test_mul_right(self):
		# Test 1
		values = [
			[1, 2],
			[3, 4]]
		m1 = Matrix(values)
		values = [
			[5, 6],
			[7, 8]]
		m2 = Matrix(values)
		values = [
			[23, 34],
			[31, 46]]
		m3 = Matrix(values)
		self.assertEqual(m2 * m1, m3)

		# Test 2
		values = [
			[1, 1, 1],
			[2, 2, 2]]
		m1 = Matrix(values)
		values = [
			[3, 3, 3],
			[6, 6, 6]]
		m2 = Matrix(values)
		self.assertEqual(3 * m1, m2)

	def test_ero_interchange(self):
		# Test 1
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m1 = Matrix(values)
		m1.ero_interchange(0, 1)
		values = [
			[4, 5, 6],
			[1, 2, 3]]
		m2 = Matrix(values)
		self.assertEqual(m1, m2)

		# Test 2
		values = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]]
		m1 = Matrix(values)
		m1.ero_interchange(0, 1)
		values = [
			[4, 5, 6],
			[1, 2, 3],
			[7, 8, 9]]
		m2 = Matrix(values)
		self.assertEqual(m1, m2)

	def test_ero_scale(self):
		# Test 1
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m1 = Matrix(values)
		m1.ero_scale(0, 3)
		values = [
			[3, 6, 9],
			[4, 5, 6]]
		m2 = Matrix(values)
		self.assertEqual(m1, m2)

	def test_ero_replace(self):
		# Test 1
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m1 = Matrix(values)
		m1.ero_replace(0, 1, 1)
		values = [
			[5, 7, 9],
			[4, 5, 6]]
		m2 = Matrix(values)
		self.assertEqual(m1, m2)

		# Test 2
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m1 = Matrix(values)
		m1.ero_replace(0, 1, 0)
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m2 = Matrix(values)
		self.assertEqual(m1, m2)

		# Test 3
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m1 = Matrix(values)
		m1.ero_replace(0, 1, -1)
		values = [
			[-3, -3, -3],
			[4, 5, 6]]
		m2 = Matrix(values)
		self.assertEqual(m1, m2)
