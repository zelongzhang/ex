def mirror(word):
	mirrored_word = word
	for letter in reversed(word):
		mirrored_word+=letter
	return mirrored_word


def remove_letter(letter,word):
	newstr = ''.join(word.split(letter))
	return newstr

while True:
	print(mirror(str(input('Enter a string to be mirrored\n'))))
	print(remove_letter(str(input('Enter a word\n')),(input('Enter a letter to remove\n'))))