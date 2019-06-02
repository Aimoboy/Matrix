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

		new_values = []

		for x in range(self.rows):
			new_values.append([None] * other.cols)

		for x in range(len(new_values)):
			for y in range(len(new_values[x])):
				new_values[x][y] = self.values[x][0] * other.values[0][y]
				for z in range(1, self.cols):
					new_values[x][y] = new_values[x][y] + self.values[x][z] * other.values[z][y]

		return Matrix(new_values)
