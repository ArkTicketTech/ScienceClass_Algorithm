maxs = 0
maxq = (0,0)
st_neighbors = {}
qs_neighbors = {}
st_list = set()
qs_list = set()
st_sim = {}
qs_sim = {}
new_qs_sim = {}
new_st_sim = {}


def initialize():

		global maxs
		global maxq
		global st_neighbors
		global qs_neighbors
		file = open("sample.txt")
		while 1:
			line = file.readline()
			if not line:
				break

			temp = line.split("\t")

			for i,each in enumerate(temp):
					temp[i] = int(temp[i])
			
			if(not st_neighbors.has_key(temp[0])):
				st_neighbors[temp[0]] = []
				st_sim[(temp[0],temp[0])] = 1

			if(not st_neighbors.has_key((temp[1],temp[2]))):	
				qs_neighbors[(temp[1],temp[2])] = []
				st_sim[((temp[1],temp[2]),(temp[1],temp[2]))] = 1

			st_neighbors[temp[0]] = st_neighbors[temp[0]] + [(temp[1],temp[2])]
			qs_neighbors[(temp[1],temp[2])] = qs_neighbors[(temp[1],temp[2])] + [temp[0]]

			st_list.add(temp[0])
			qs_list.add((temp[1],temp[2]))

			if(maxs<int(temp[0])): maxs = int(temp[0])
			if(maxq<(int(temp[1]),int(temp[2]))): maxq = (int(temp[1]),int(temp[2]))


def simqueryStudent(s1,s2,Converge):
		if s1 == s2 : return 1;
		tmp = Converge / (len(st_neighbors[s1]) * len(st_neighbors[s2]))
		simsum = 0
		for nb1 in st_neighbors[s1]:
				for nb2 in st_neighbors[s2]:
					if st_sim.has_key((nb1,nb2)):
						simsum = simsum + st_sim[(nb1,nb2)]

		if(not qs_neighbors.has_key(s1) or not qs_neighbors.has_key(s2)):
			return 0

		return tmp * simsum 

def simqueryQStep(q1,q2,Converge):
		if q1 == q2 : return 1;
		tmp = Converge / (len(qs_neighbors[q1]) * len(qs_neighbors[q2]))
		simsum = 0

		if(not qs_neighbors.has_key(q1) or not qs_neighbors.has_key(q2)):
			return 0

		for nb1 in qs_neighbors[q1]:
				for nb2 in qs_neighbors[q2]:
					if qs_sim.has_key((nb1,nb2)):
						simsum = simsum + qs_sim[(nb1,nb2)]

		return tmp * simsum 

def simrank(C=0.6, times=10):
		for q1 in qs_list:
			for q2 in qs_list:
				if(q1 == q2):
					new_qs_sim[(q1,q2)] = 1
				else:
					new_qs_sim[(q1,q2)] = simqueryQStep(q1,q2,C)

		for s1 in st_list:
			for s2 in st_list:
				if(s1 == s2):
					new_st_sim[(s1,s2)] = 1
				else:
					new_st_sim[(s1,s2)] = simqueryStudent(s1,s2,C)		

		# qs_sim = new_qs_sim
		# st_sim = new_st_sim


# def simqueryQStep():


def main():
	initialize()

	# print st_list
	# print qs_list

	simrank()

	# print qs_sim
	# print st_sim

	# print st_neighbors[1]

	# print len(st_neighbors['1'])
	# print len(qs_neighbors[('4','1')])
	# print maxs
	# print maxq

main()