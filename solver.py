words = [] #the list of words

add_word='' #the word we'll be adding to the list
m=0 #the length of the words in the list of words

print('Type the word you wish to add and press ENTER\nType 0 and press Enter when you\'ve added all the words')
while add_word!='0':
	add_word = input().upper()
	if add_word!='0':
		if len(words)>0:
			if len(add_word)==m:
				words.append(add_word)
				print('added '+add_word)
			else:
				print(add_word,'is not the same length as the other words in this list')
		else:
			words.append(add_word)
			m=len(add_word)	#set the word length
			print('added '+add_word)

eliminated = [] #the list of eliminated words, to be used in future uses

#cycle through the list of active words until there is 1 or 0 contenders left
while len(words)>1:
	n=len(words) #the number of words to choose from

	#sets up the similarity matrix for each word
	sim = [x[:] for x in [[-1] * n] * n]

	for i in range(n):
		for j in range(i+1, n):
			num_sim=0;
			for k in range(m):
				if words[i][k]==words[j][k]:
					num_sim+=1
			sim[i][j]=num_sim
			sim[j][i]=num_sim
		
	print('#\tword\t\t max similarity')	
	for i in range(n):
		print(i+1,')\t',words[i],'\t-\t', max(sim[i]))

	#given a choice and a returned similarity, eliminate all options of a different similarity
	#player picks a word
	choice = int(input("Pick the number corresponding to the word you've chosen: "))-1
	while choice>n-1 or choice <0:
		choice = int(input("Not a valid number: "))-1

	#give them the choice of possible similarity scores
	temp = set(sim[choice])
	temp.remove(-1)
	temp.add(m)
	
	#take in the similarity score
	score = int(input(f'What was the similarty score? {temp} : '))
	while score not in temp:
		score = int(input(f'It has to be one of these: {temp}'))
	
	#exit if the score is the length of the word, otherwise remove all words that aren't valid
	if score==m:
		words = [words[choice]]
	else:	
		for i in range(len(words)-1,-1,-1):
			if sim[choice][i]!=score:
				eliminated.append(words.pop(i))

#After exiting the loop the solution (or lack thereof) will be displayed
if len(words)==1:
	print(words[0],'is the solution... But you knew that already!')
else:
	print('There is no solution possible given the inputs')
