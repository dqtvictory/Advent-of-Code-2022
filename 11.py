from common import *
from dataclasses import dataclass
from collections import deque

@dataclass
class Monkey:
	items: Deque[int]
	op: str
	div: int
	true: int
	false: int
	total: int = 0

	def inspect(self) -> int:
		item = self.items.popleft()
		self.total += 1
		return calc_val(item, self.op)

	def add_item(self, val: int):
		self.items.append(val)


calc_val = lambda old, op: eval(op)

def get_monkeys(lines: List[str]) -> List[Monkey]:
	def build_monkey(prev: Tuple[list, List[Monkey]], line: str):
		att, mk = prev
		if "Starting" in line:
			a = deque(map(int, line[16:].split(', ')))
		elif "Operation" in line:
			a = line[17:]
		elif "Test" in line:
			a = int(line[19:])
		elif "true" in line:
			a = int(line[25:])
		elif "false" in line:
			a = int(line[26:])
		else:
			return prev
		att_monkey = att + [a]
		if "false" in line:
			return [], mk + [Monkey(*att_monkey)]
		return att_monkey, mk

	init = [], []	# current monkey's attribute, monkey list
	return Chainable(lines) \
		.map(str.lstrip) \
		.reduce(build_monkey, True, init)[1]

def part1(monkeys: List[Monkey]):
	for _ in range(20):
		for m in monkeys:
			while len(m.items):
				val = m.inspect() // 3
				if (val % m.div) == 0:
					monkeys[m.true].add_item(val)
				else:
					monkeys[m.false].add_item(val)
	l = sorted([m.total for m in monkeys], reverse=True)[:2]
	return l[0] * l[1]

def part2(monkeys: List[Monkey]):
	div = reduce(lambda a, m: a * m.div, monkeys, 1)
	for _ in range(10000):
		for m in monkeys:
			while len(m.items):
				val = m.inspect() % div
				if (val % m.div) == 0:
					monkeys[m.true].add_item(val)
				else:
					monkeys[m.false].add_item(val)
	l = sorted([m.total for m in monkeys], reverse=True)[:2]
	return l[0] * l[1]


if __name__ == '__main__':
	fname = "input.txt" if len(argv) == 1 else argv[1]
	lines = get_lines(fname, rstrip=True)

	monkeys = get_monkeys(lines)
	print("Part 1:", part1(monkeys))

	monkeys = get_monkeys(lines)
	print("Part 2:", part2(monkeys))
