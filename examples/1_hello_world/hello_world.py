# Hello World
# Created by Thomas Lobker
#
# This is a simple contract to demonstrate
# how to deploy and invoke a contract

# NEO API includes
from boa.interop.Neo.Runtime import GetTrigger, CheckWitness, Notify, Log
from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.Neo.Storage import GetContext, Get, Put, Delete
from boa.interop.Neo.Action import RegisterAction
from boa.interop.Neo.Enumerator import EnumeratorCreate, EnumeratorNext

# Compiler includes
from boa.builtins import concat

# Main function
def Main(operation, arguments):

	# Get the contract trigger type
	trigger = GetTrigger()

	# Contract transaction
	if trigger == Verification():

		return False

	# Invocation transaction
	elif trigger == Application():

		# User says hello
		if operation == 'hello':

			return greetings(arguments)

		# Requested method is not implemented
		print('Invalid operation')
		return False

# Send some greetings
def greetings(arguments):

	print('Such a beautiful day today')

	return 'Hello World'
