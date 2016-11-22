#Some explanations about DEBUG and runprodserver

otree: problem with "Emot Questionnaire Panas + Mauss, n=1"
debug		| server				|result
on			| runserver				|no problem
on			| runprodserver *		|problem
off			| runserver				|no problem
off			| runprodserver *		|problem	
			
			
*(always use: otree collectstatic)

##How to set debug=False locally.
	only replace or mute the traditional code:
		if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
		DEBUG = False
		else:
		DEBUG = True
	with:
		DEBUG = False

##How to run the production server. Usually it is complemented with DEBUG=False
	But you can also use it with the traditional code
	1.- otree resetdb
	2.- otree collectstatic
	3.- otree runprodserver

