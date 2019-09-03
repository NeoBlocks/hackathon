# EUR Hackathon Token
# Created by Thomas Lobker
#
# This is a simple example token contract with a single
# hardcoded admin address and no crowdsale option
#
# Fully compliant with NEP5.1 on the NEO blockchain

# NEO API includes
from boa.interop.Neo.Runtime import GetTrigger, CheckWitness, Notify, Log
from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.Neo.Storage import GetContext, Get, Put, Delete
from boa.interop.Neo.Action import RegisterAction
from boa.interop.Neo.Enumerator import EnumeratorCreate, EnumeratorNext

# Compiler includes
from boa.builtins import concat

# Storage context for local contract
context = GetContext()

# Static administrative address
admin = b'\xae\xe7O\xf1\x02\xbb$CL\xb0\xd5\x17pD\xadx\xc1C\xfa\x90'
burn = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Set notification triggers
OnTransfer = RegisterAction('transfer', 'address', 'to', 'amount')
OnApprove = RegisterAction('approve', 'address', 'to', 'amount')

# Main function
def Main(operation, arguments):

	# Get the contract trigger type
	trigger = GetTrigger()

	# Contract transaction
	if trigger == Verification():

		if CheckWitness(admin):
			return True

		return False

	# Invocation transaction
	elif trigger == Application():

		# Get the name of the token
		if operation == 'name':

			return name(context, arguments)

		# Get the token symbol
		elif operation == 'symbol':

			return symbol(context, arguments)

		# Get the amount of token decimals
		elif operation == 'decimals':

			return decimals(context, arguments)

		# Get the total supply of the token
		elif operation == 'totalSupply':

			return totalSupply(context, arguments)

		# Get the balance of a token address
		elif operation == 'balanceOf':
			# arguments[0] = address

			if len(arguments) != 1:
				print('Invalid number of arguments')
				return False

			return balanceOf(context, arguments)

		# Transfer tokens to another address
		elif operation == 'transfer':
			# arguments[0] = address
			# arguments[1] = to
			# arguments[2] = amount

			if len(arguments) != 3:
				print('Invalid number of arguments')
				return False

			return transfer(context, arguments)

		# Transfer tokens to another address from an allowance
		elif operation == 'transferFrom':
			# arguments[0] = address
			# arguments[1] = to
			# arguments[2] = amount

			if len(arguments) != 3:
				print('Invalid number of arguments')
				return False

			return transferFrom(context, arguments)

		# Set an allowance
		elif operation == 'approve':
			# arguments[0] = address
			# arguments[1] = to
			# arguments[2] = amount

			if len(arguments) != 3:
				print('Invalid number of arguments')
				return False

			return approve(context, arguments)

		# Get the balance of an allowance
		elif operation == 'allowance':
			# arguments[0] = address
			# arguments[1] = to

			if len(arguments) != 2:
				print('Invalid number of arguments')
				return False

			return allowance(context, arguments)

		# Initial initialization of the contract
		elif operation == 'init':

			# Allow only authenticated requests
			if not CheckWitness(admin):
				print('Permission denied')
				return False

			# Only continue if the contract has not been initialized yet
			if Get(context, 'initialized'):
				print('Contract is already initialized')
				return False

			supply = 100000000000000000

			# Update the circulating supply in storage
			Put(context, 'circulating', supply)

			# Update the balance for the administrative user
			Put(context, admin, supply)

			# Send the notification
			OnTransfer(None, admin, supply)

			Put(context, 'initialized', True)

			print('Contract is initialized')
			return True

		# Requested method is not implemented
		print('Invalid operation')
		return False

# Get the name of the token
def name(context, arguments):

	return 'Workshop Euro'

# Get the token symbol
def symbol(context, arguments):

	return 'EUR'

# Get the amount of token decimals
def decimals(context, arguments):

	return 8

# Get the total supply of the token
def totalSupply(context, arguments):

	return Get(context, 'circulating')

# Get the balance of a token address
def balanceOf(context, arguments):

	address = arguments[0]

	# Address has to be 20 bytes
	if len(address) != 20:
		print('Address is incorrect')
		return False

	# Return the balance of the address
	balance = Get(context, address)
	return balance

# Transfer tokens to another address
def transfer(context, arguments):

	address = arguments[0]
	to = arguments[1]
	amount = arguments[2]

	# Allow only authenticated requests
	if not CheckWitness(address):
		print('Permission denied')
		return False

	# To address has to be 20 bytes
	if len(to) != 20:
		print('Address is incorrect')
		return False

	# Allow only a positive amount
	if not amount >= 0:
		print('Amount must be positive')
		return False

	balance = Get(context, address)

	if balance < amount:
		print('Insufficient funds')
		return False

	if address == to:
		return True

	# Calculate the balance for the sender
	if balance == amount:
		Delete(context, address)
	else:
		balance = balance - amount
		Put(context, address, balance)

	# Check if the tokens have been burned
	if to == burn:
		# Reduce supply when tokens are burned
		print('Tokens have been burned')
		supply = Get(context, 'circulating') - amount
		Put(context, 'circulating', supply)
	else:
		# Calculate the balance for the recipient
		balance = Get(context, to) + amount
		Put(context, to, balance)

	# Send the notification
	OnTransfer(address, to, amount)
	return True

# Transfer tokens to another address from an allowance
def transferFrom(context, arguments):

	address = arguments[0]
	to = arguments[1]
	amount = arguments[2]

	# Address has to be 20 bytes
	if len(address) != 20:
		print('Address is incorrect')
		return False

	# To address has to be 20 bytes
	if len(to) != 20:
		print('Address is incorrect')
		return False

	# Allow only a positive amount
	if not amount >= 0:
		print('Amount must be positive')
		return False

	key = concat(address, to)
	allowance = Get(context, key)

	if allowance < amount:
		print('Insufficient funds approved')
		return False

	balance = Get(context, address)

	if balance < amount:
		print('Insufficient funds')
		return False

	if address == to:
		return True

	# Calculate the balance for the sender
	if (balance == amount):
		Delete(context, address)
	else:
		balance = balance - amount
		Put(context, address, balance)

	# Calculate the new allowance
	allowance = allowance - amount

	if allowance == 0:
		Delete(context, key)
	else:
		Put(context, key, allowance)

	# Check if the tokens have been burned
	if to == burn:
		# Reduce supply when tokens are burned
		print('Tokens have been burned')
		supply = Get(context, 'circulating') - amount
		Put(context, 'circulating', supply)
	else:
		# Calculate the balance for the recipient
		balance = Get(context, to) + amount
		Put(context, to, balance)

	# Send the notification
	OnTransfer(address, to, amount)
	return True

# Set an allowance
def approve(context, arguments):

	address = arguments[0]
	to = arguments[1]
	amount = arguments[2]

	# Allow only authenticated requests
	if not CheckWitness(address):
		print('Permission denied')
		return False

	# To address has to be 20 bytes
	if len(to) != 20:
		print('Address is incorrect')
		return False

	# Allow only a positive amount
	if not amount >= 0:
		print('Amount must be positive')
		return False

	# Do not allow more allowance than the current balance
	if not Get(context, address) >= amount:
		print('Insufficient funds')
		return False

	key = concat(address, to)

	if amount == 0:
		Delete(context, key)
	else:
		Put(context, key, amount)

	# Send the notification
	OnApprove(address, to, amount)
	return True

# Get the balance of an allowance
def allowance(context, arguments):

	address = arguments[0]
	to = arguments[1]

	# Address has to be 20 bytes
	if len(address) != 20:
		print('Address is incorrect')
		return False

	# To address has to be 20 bytes
	if len(to) != 20:
		print('Address is incorrect')
		return False

	key = concat(address, to)

	# Return the allowance
	allowance = Get(context, key)
	return allowance
