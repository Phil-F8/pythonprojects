from random import randint, choice


def password_generator(digits_or_chars=5, password_type='all'):
	password = []
	if digits_or_chars > 150: print('The number you entered is too big.')
	if password_type.title() == 'Numbers':
		d = int(digits_or_chars)
		for i in range(d):
			add_digit = randint(0, 9)
			password.append(add_digit)
		for digit in password:
			print(digit, sep='', end='')
	if password_type.title() == 'Letters':
		c = digits_or_chars
		for i in range(c):
			add_char = choice(
				[
					'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
					'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
				]
			)
			password.append(add_char)
		for char in password:
			print(char, sep='', end='')
	if password_type.title() == 'All':
		c = digits_or_chars
		for i in range(c):
			add_char_digit = choice(
				[
					'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
					'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
					'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
					'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
					1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
					'!', '#', '$', '%', '&', '?', '+', '=', '⨝', '£', '∑', '⨹', '§'
				]
			)
			password.append(add_char_digit)
		for char in password:
			print(char, sep='', end='')
