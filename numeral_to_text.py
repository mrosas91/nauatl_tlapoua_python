#!/usr/bin/env python3

# prefixes array uses effectively index 1 to store prefixes
prefixes = ['-', 'sem', 'om', 'ex', 'naj', 'makuil', '6', '7', '8', '9', 'matlak']

root_names_to_9 = ['amopouali',  'se', 'ome', 'eyi', 'naui', 'makuili', 'chikuasej', 'chikome', 'chikueyi', 'chiknaui']

root_10 = 'majtlaktli'
root_20 = 'pouali'
root_400 = 'tsontli'
root_8000 = 'xiquipilli'
# root_160000

connector = ' iuan '

def numeral_to_text(numeral):
	return numeral_to_text(numeral, True)

def numeral_to_text(numeral, first_time):
	possible_connector = ''
	if not first_time:
		possible_connector = connector
		if numeral == 0:
			return ''

	if numeral < 10:
		return possible_connector + root_names_to_9[numeral]
	elif numeral <20 :
		return possible_connector + root_10 + numeral_to_text(numeral-10, False)
	elif numeral < 400:
		times_in_20 = numeral // 20
		return possible_connector + prefixes[times_in_20] + root_20 + numeral_to_text(numeral-(times_in_20 * 20), False)
	# elif numeral < 8000 :
	# 	return 'sentsontli'

	else:
		return 'UNKNOWN'
