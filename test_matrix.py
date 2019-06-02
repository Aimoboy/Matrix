import unittest
from matrix import *

class TestMatrix(unittest.TestCase):
	def test_init(self):
		values = [
			[1, 2, 3],
			[4, 5, 6]]
		m = Matrix(values)
		self.assertEqual(m.rows, 2)
		self.assertEqual(m.cols, 3)

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
		values = [
			[1, 2],
			[3, 4]]
		m = Matrix(values)
		self.assertEqual(str(m), "1 2\n3 4\n")

		values = [
			[10, 2],
			[3, 4]]
		m = Matrix(values)
		self.assertEqual(str(m), "10  2\n 3  4\n")

	def test_mul_matrix_matrix_method(self):
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
