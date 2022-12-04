from common import *


score_dic = dict(
	r = 1,
	p = 2,
	s = 3,
)
opponent_dic = dict(
	A = 'r',
	B = 'p',
	C = 's',
)
me_dic = dict(
	X = 'r',
	Y = 'p',
	Z = 's',
)

me_out_dic = dict(
	X = 0,
	Y = 3,
	Z = 6,
)

order_dic = {
	0: "rspr",
	6: "rpsr",
}

def part1(lines: List[str]):
	def score(pair: Tuple[int, int]):
		op, me = pair
		if op == me:
			return 3
		if abs(op - me) == 1:
			return 6 * (op < me)
		return 6 * (op > me)
	
	return sum(
		map(
			lambda pair: pair[1] + score(pair),
			map(
				lambda pair: (score_dic[pair[0]], score_dic[pair[1]]),
				map(
					lambda pair: (opponent_dic[pair[0]], me_dic[pair[1]]),
					map(str.split, lines)
				)
			)
		)
	)

def part2(lines: List[str]):
	def me_score(pair: Tuple[str, int]):
		op, score = pair
		if score == 3:
			return score_dic[op]
		order = order_dic[score]
		return score_dic[order[order.index(op) + 1]]
	
	return sum(
		map(
			lambda pair: pair[1] + me_score(pair),
			map(
				lambda pair: (opponent_dic[pair[0]], me_out_dic[pair[1]]),
				map(str.split, lines)
			)
		)
	)
	

if __name__ == '__main__':
	fname = "input" if len(argv) == 1 else argv[1]
	lines = get_lines(fname)

	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))
