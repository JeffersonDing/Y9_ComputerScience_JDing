import random
word = []
for i in range(0,5):
	word.append(random.choice(open('English_noun.txt').readlines()).strip('\n'))
print(' '.join(word))