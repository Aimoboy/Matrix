import copy

class Matrix:
	def __init__(self, values):
		"""
		Summary:
		Initialize a matrix.

		Parameters:
		values (list of lists): The values for the matrix.
		"""

		self.values = values
		self.rows, self.cols = self.check_values()

	def __eq__(self, other):
		"""
		Summary:
		Check if two matrices are equal.

		Parameters:
		self (Matrix): This matrix.
		other (Matrix): The other matrix.

		Returns:
		True if they are equal else false.
		"""

		if self.rows != other.rows or self.cols != other.cols:
			return False

		equal = True

		for x in range(len(self.values)):
			for y in range(len(self.values[x])):
				if self.values[x][y] != other.values[x][y]:
					equal = False

		return equal

	def __str__(self):
		"""
		Summary:
		Generate string that represents the matrix.

		Returns:
		A string that represents the matrix.
		"""

		# Find length of largest element
		largest_element = 0

		for x in range(len(self.values)):
			for y in range(len(self.values[x])):
				length = len(str(self.values[x][y]))
				if length > largest_element:
					largest_element = length

		# Generate string
		output = ""
		for x in range(len(self.values)):
			for y in range(len(self.values[x])):
				# Spaces before element
				for z in range(largest_element - len(str(self.values[x][y]))):
					output = output + " "

				# Element
				output = output + str(self.values[x][y])

				# Space or newline at end
				if y + 1 == len(self.values[x]):
					output = output + "\n"
				else:
					output = output + " "

		return output

	def __mul__(self, other):
		"""
		Summary:
		Overload the matrix multiplication.

		Returns:
		Returns the product of self and other.
		"""

		if type(other) is Matrix:
			return self.multiply_matrix_matrix(other)
		elif type(other) is int:
			return self.multiply_matrix_scalar(other)
		else:
			return NotImplemented()

	def __rmul__(self, other):
		"""
		Summary:
		Overload the matrix multiplication.

		Returns:
		Returns the product of self and other.
		"""
		if type(other) is Matrix:
			return other.multiply_matrix_matrix(self)
		elif type(other) is int:
			return self.multiply_matrix_scalar(other)
		else:
			return NotImplemented()

	def check_values(self):
		"""
		Summary:
		Check if the given values are valid for a matrix.

		Returns:
		A tuple (rows, cols).
		"""

		valid = True
		line_length = len(self.values[0])

		for x in range(len(self.values)):
			length = len(self.values[x])
			if length != line_length:
				valid = False

		if not valid:
			raise ValueError("Values do not form a square.")

		return (len(self.values), line_length)

	def generate_empty_values(self, rows, cols):
		"""
		Summary:
		Generate empty values of the given size.

		Parameters:
		rows (int): The number of rows.
		cols (int): The number of columns.

		Returns:
		Empty set of values.
		"""

		values = []

		for x in range(rows):
			values.append([None] * cols)

		return values

	def multiply_matrix_matrix(self, other):
		"""
		Summary:
		Calculate the product of two matrices.

		Parameters:
		self (Matrix): This matrix.
		other (Matrix): The other matrix.

		Returns:
		The product of the two matrices.
		"""

		if self.cols != other.rows:
			raise ValueError("Matrices not correct sizes for multiplication.")

		new_values = self.generate_empty_values(self.rows, other.cols)

		for x in range(len(new_values)):
			for y in range(len(new_values[x])):
				new_values[x][y] = self.values[x][0] * other.values[0][y]
				for z in range(1, self.cols):
					new_values[x][y] = new_values[x][y] + self.values[x][z] * other.values[z][y]

		return Matrix(new_values)

	def multiply_matrix_scalar(self, s):
		new_values = self.generate_empty_values(self.rows, self.cols)

		for x in range(self.rows):
			for y in range(self.cols):
				new_values[x][y] = self.values[x][y] * s

		return Matrix(new_values)

	def copy(self):
		"""
		Summary:
		Copy the matrix.

		Returns:
		A copy of the matrix.
		"""

		new_values = copy.deepcopy(self.values)

		return Matrix(new_values)

	def ero_interchange(self, i, j):
		"""
		Summary:
		Swap the i'th and j'th rows.

		Parameters:
		i (int): The first row.
		j (int): The second row.
		"""

		temp = self.values[i]
		self.values[i] = self.values[j]
		self.values[j] = temp

	def ero_scale(self, i, s):
		"""
		Summary:
		Scale each element in the i'th row with s.

		Parameters:
		i (int): The row.
		s (unknown): The scalar.
		"""

		for x in range(self.cols):
			self.values[i][x] = self.values[i][x] * s

	def ero_replace(self, i, j, s):
		"""
		Summary:
		Add every element in the j'th row scaled by s to the i'th row.

		Parameters:
		i (int): The row that is being added to.
		j (int): The row that is added unto the other.
		s (unknown): The scalar.
		"""

		for x in range(self.cols):
			self.values[i][x] = self.values[i][x] + self.values[j][x] * s
