# Enter your code here. Read input from STDIN. Print output to STDOUT

import string

def is_isomorphic(word1, word2, marked_list, match_list, res):

	if len(word1) != len(word2):
		return (False, [], [], "")		


	for index in range(len(word1)):
		letter1 = ord(word1[index])
		letter2 = ord(word2[index])

		if match_list[letter1] != -1:
			if match_list[letter1] != letter2:
				return (False, [], [], "")

		else :
			if marked_list[letter2]:
				return (False, [], [], "")
			marked_list[letter2] = True
			match_list[letter1] = letter2
			

	res += word2 + " "
	return (True, marked_list, match_list, res)


def words_dfs(word_count, marked, match, res):
	
	if word_count >= len(inp):
		print(res[:-1])
		return True

	inp_word = inp[word_count]
	for test_word in words:
		is_isomorphics, updated_mark, updated_match, updated_res  = is_isomorphic(inp_word, test_word, marked.copy(), match.copy(), res)

		if is_isomorphics:
			if words_dfs(word_count+1, updated_mark, updated_match, updated_res):
				return True

	return False

words = [i.lower() for i in open('dictionary.lst', 'r').read().split()]

inp = input().split()

MAX_CHARS = 256

# to validate one-to-one and onto relation
marked_list = [False for i in range(MAX_CHARS)] 
match_list = [-1 for i in range(MAX_CHARS)]


words_dfs(0, marked_list, match_list, "")
