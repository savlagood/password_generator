import random

char_sets = {
	'uppercase_chars': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
	'lowercase_chars': 'abcdefghijklmnopqrstuvwxyz',
	'numbers': '1234567890',
	'special_symbols': '!@#$%^&*',
	'similar_chars': 'oO0iIlLbdftvu'
}

class LengthException(Exception):
	pass

class ParametersException(Exception):
	pass

def generate_password(
		length=8, first_cap=True, upper_chars=True,
		lower_chars=True, nums=True, spec_symbs=False, sim_chars=True):
	"""
	:param length - length of password
	:param first_cap - first letter of the password be capitalized
	:param upper_chars - using uppercase chars in password
	:param lower_chars - using lowercase chars in password
	:param nums - using numbers in password
	:param spec_symbs - using special symbols in password (such as !@#$%^&*)
	:param sim_chars - using simillar symbols in password
	:return: reliable password
	"""
	possible_params = list()
	possible_params += ['lowercase_chars'] if lower_chars else []
	possible_params += ['uppercase_chars'] if upper_chars else []
	possible_params += ['numbers'] if nums else []
	possible_params += ['special_symbols'] if spec_symbs else []
	possible_params += ['similar_chars'] if sim_chars else []

	if possible_params == []:
		raise ParametersException("All parameters are disabled. Password could not be generated.")

	if length < 1:
		raise LengthException("Length of password less than 1. Password could not be generated.")

	password = str()

	if first_cap:
		password += random.choice(char_sets['uppercase_chars'])
	else:
		password += random.choice(char_sets[random.choice(possible_params)]).lower()

	param_chain = [random.choice(possible_params) for _ in range(length - 1)]

	for parameter in param_chain:
		password += random.choice(char_sets[parameter])
	
	return password

if __name__ == '__main__':
	text = """\t***The Password Generator***
Include:
	1 - first letter is capitalized
	2 - uppercase chars (ABCDEFG...)
	3 - numbers (12345...)
	4 - special symbols (!@#$%...)
	5 - simillar symbols (oO0iI...)

Write numbers without spaces!"""

	print(text)

	raw_params = input()
	length = int(input('Length of password: '))

	parameters = {
		'length': length,
		'first_cap': True if '1' in raw_params else False,
		'upper_chars': True if '2' in raw_params else False,
		'nums': True if '3' in raw_params else False,
		'spec_symbs': True if '4' in raw_params else False,
		'sim_chars': True if '5' in raw_params else False,
	}

	password = generate_password(**parameters)

	print(f"Your new reliable password: {password}")
