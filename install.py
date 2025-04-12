import os
import subprocess
import time
def verificar_pacotes():
	print('\033[1;37mVERIFICANDO PACOTES\033[m')

	
	pacotes_do_onixx = ['pyfiglet', 'beautifulsoup4', 'nmap', 'requests', 'pexpect']
	terminal = subprocess.run(['pip', 'list'], capture_output=True, text=True)
	for c in range(0, 5):
		time.sleep(1)
		print('\033[1;33mVerificando', pacotes_do_onixx[c], '\033[m')
		if pacotes_do_onixx[c] not in terminal.stdout:
			print('\033[1;31mPacote', pacotes_do_onixx[c], 'não instalado\033[m' )
			os.system('pip install ', pacotes_do_onixx[c])
		else:
			print('\033[1;32mPacote', pacotes_do_onixx[c], 'instalado\033[m')
			
def desinstall():
	os.system('clear')
	os.system('rm -r install.py')
	os.system('python onixx.py')
verificar_pacotes()
desinstall()
