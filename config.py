# ntfy.sh online chat config manager

try:
	with open('config', 'r') as f:
		username = f.readline()
except FileNotFoundError:
	with open('config', 'w') as f:
		username = input('Enter username: ')
		f.write(username)

