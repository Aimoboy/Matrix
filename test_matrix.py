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

	def test_mul_elements(self):
		# Test 1
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m1 = Matrix(values)
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m2 = Matrix(values)
		m3 = m1.multiply_elements(m2)
		values = [
			[1, 4, 9],
			[16, 25, 36]]
		m_result = Matrix(values)
		self.assertEqual(m3, m_result)
