#!/usr/bin/env python3

prefixes = ['sem', 'om', 'ex', 'nau', 'makuil']

root_names_to_9 = ['amopouali',  'se', 'ome', 'eyi', 'naui', 'makuilli', 'chikuase', 'chikome', 'chikueyi', 'chiknaui']

root_10 = 'majtlactli'
root_20 = 'poualli'
root_400 = 'tsontli'
# root_8000
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
		return root_10 + numeral_to_text(numeral-10, False)
	
	else:
		return 'UNKNOWN'
