from common import *


class Folder:
	flat_fs = dict()	# caching folder's size

	def __init__(self, name, parent):
		self.p: Folder	= parent
		self.sz: int	= 0		# total files size
		self.sub: Dict[str, Folder] = dict()	# subfolders
		self.path = self.__full_path(name)
		Folder.flat_fs[self] = -1

	def __hash__(self) -> int:
		return hash(self.path)

	def __eq__(self, o: object) -> bool:
		return isinstance(o, self.__class__) and o.path == self.path

	def __full_path(self, name: str):
		if name == '/':
			return name
		return self.p.path + name + '/'

	def size(self) -> int:
		total = Folder.flat_fs[self]
		if total == -1:
			total = sum(map(lambda f: self.sub[f].size(), self.sub.keys())) + self.sz
			Folder.flat_fs[self] = total
		return total

	def mkdir(self, name: str):
		self.sub[name] = Folder(name, self)
	
	def touch(self, size):
		self.sz += size
	
	def cd(self, name: str):
		return self.sub[name]


def build_fs(lines: List[str]) -> Folder:
	root = Folder("/", None)
	cur = root
	for line in lines[1:]:
		line = line.split()
		if line[1] == 'cd':
			f = line[2]
			if f == "..":
				cur = cur.p
			else:
				cur = cur.cd(f)
		elif line[0] == "dir":
			cur.mkdir(line[1])
		elif line[0].isnumeric():
			cur.touch(int(line[0]))
	return root

def part1(lines: List[str]):
	build_fs(lines)
	lim = 100000
	return Chainable(Folder.flat_fs.keys()) \
		.map(lambda f: f.size()) \
		.filter(lambda sz: sz <= lim) \
		.reduce(lambda a, b: a + b)

def part2(lines: List[str]):
	fs = build_fs(lines)
	goal = 30000000 - 70000000 + fs.size()
	return Chainable(Folder.flat_fs.keys()) \
		.map(lambda f: f.size()) \
		.filter(lambda sz: sz >= goal) \
		.reduce(min)


if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname, False)

	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))
