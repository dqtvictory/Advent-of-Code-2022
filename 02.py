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

def outcome(op: str, me: str):
	if op == me:
		return 3
	order = "rps"
	op = order.index(op)
	me = order.index(me)
	if abs(op - me) == 1:
		return 6 * (op < me)
	return 6 * (op > me)

def part1(lines: list[str]):
	score = 0
	for line in lines:
		play = line.split()
		opponent, me = opponent_dic[play[0]], me_dic[play[1]]
		score += score_dic[me] + outcome(opponent, me)
	return score

def get_me(op: str, out_score: int):
	if out_score == 3:
		return op
	order = "rpsr" if out_score == 6 else "rspr"
	return order[order.index(op) + 1]

out_dic = dict(
	X = 0,
	Y = 3,
	Z = 6,
)

def part2(lines: list[str]):
	score = 0
	for line in lines:
		play = line.split()
		opponent, out_score = opponent_dic[play[0]], out_dic[play[1]]
		me = get_me(opponent, out_score)
		score += out_score + score_dic[me]
	return score
	

if __name__ == '__main__':
	fname = "input" if len(argv) == 1 else argv[1]
	lines = get_lines(fname)

	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))
