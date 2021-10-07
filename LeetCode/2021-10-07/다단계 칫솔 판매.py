from collections import defaultdict


def create_graph(enroll, referral):
	graph = {}
	for i in range(len(enroll)):
		graph[enroll[i]]=referral[i]
	return graph


def distribute(name, price, amounts, graph):
	if name == '-':
		return
	if price < 10:
		amounts[name] += price
	else:
		amounts[name] += price - price //10
		distribute(graph[name], price//10, amounts, graph)


def solution(enroll, referral, seller, amount):
	graph = create_graph(enroll, referral)
	amounts = defaultdict(int)

	for i in range(len(seller)):
		name = seller[i]
		price = amount[i] * 100
		distribute(name, price, amounts, graph)

	return [amounts[name] for name in enroll]


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
			   ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
			   ["young", "john", "tod", "emily", "mary"],
			   [12, 4, 2, 5, 10]	))