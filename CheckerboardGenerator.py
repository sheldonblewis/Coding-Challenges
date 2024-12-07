
"""
numRow, represents the number of rows in the pattern.
numColumn, represents the number of columns in the pattern.
"""
def funcPrint(numRow, numColumn):
	result_lines = []
	for r in range(numRow):
		line_chars = []
		for c in range(numColumn):
			if (r + c) % 2 == 0:
				line_chars.append('#')
			else:
				line_chars.append('$')
		result_lines.append("".join(line_chars))

	return "\n".join(result_lines)

def main():
	#input for numRow
	numRow = int(input())
	
	#input for numColumn
	numColumn = int(input())
	
	
	result = funcPrint(numRow, numColumn)
	print(result)	

if __name__ == "__main__":
	main()
