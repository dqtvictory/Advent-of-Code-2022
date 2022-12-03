from common import *


def part1(lines: list[str]):
	total = 0
	for line in lines:
		length = len(line)
		s1 = set(line[: length//2])	# first half
		s2 = set(line[length//2 :])	# second half
		c = s1.intersection(s2).pop()	# common letter
		if c.islower():
			total += ord(c) - ord('a') + 1
		else:
			total += ord(c) - ord('A') + 27
	return total

def part2(lines: list[str]):
	total = 0
	for i, line in enumerate(lines):
		if i % 3 == 0:
			s = set(line)
			continue
		s = s.intersection(set(line))
		if i % 3 == 2:
			c = s.pop()	# common letter in 3 consecutive lines
			if c.islower():
				total += ord(c) - ord('a') + 1
			else:
				total += ord(c) - ord('A') + 27
	return total
	

if __name__ == '__main__':
	fname = "input" if len(argv) == 1 else argv[1]
	lines = get_lines(fname)

	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))
