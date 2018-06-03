#**********************************************
#PYTHON 3
#
#LIST FIRST
star = [3,9,11,13,15,17,17,17,19,19,19]
space = [8,5,4,3,2,1,1,1,0,0,0]

# LIST SECOND
rev_star = list(reversed(star))
rev_space = list(reversed(space))

#LIST THIRD
step_star = [star,rev_star]
step_space = [space,rev_space]

# LOOPING
for p in range(2): #LOOPING BETWEEN SETS

	for i in range(11):# FOR SPACES
		for j in range(step_space[p][i]):
			print(' ',end=' ')
			
		for k in range(step_star[p][i]):#FOR STARS
			print('*',end=' ')
			
		print()# NEW LINE
#***********************************************	
	