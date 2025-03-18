
import requests
import pyfiglet
import shlex
import subprocess
import os
import time

# Verificação de sistema e de login para novos usuários
def instalar_books():
	os.system('pip install pyfiglet')
	os.system('pip install beautifulsoup4')
	os.system('pkg install nmap')
	os.system('pip install requests')
	

with open('login.txt', 'r') as p:
	a = p.read()
if a == 'True':
	print('Ok')

	
else:
	with open('login.txt', 'w') as p:
		p.write('True')
		os.system('clear')
		txt = 'Iremos instalar as bibliotecas, isso pode demorar dependendo da sua internet.'
		for c in txt:
			print(c, end="", flush=True)
			time.sleep(0.1)
		time.sleep(2)
		instalar_books()
		
	with open('onixx.py', 'r') as p:
		linhas = p.readlines()
	linhas.insert(0, '\nimport pyfiglet\n')
	linhas.insert(0, '\nimport requests')
	with open('onixx.py', 'w') as p:
		p.writelines(linhas)
	os.system('python onixx.py')
	


# Daqui pra baixo onde as parada acontece

def clear_():
	sistema = os.name
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
			
def lin():
	print('_'*50)	

def systema(command):
	command = subprocess.run(shlex.split(command), capture_output=True, text=True)
	saida = command.stdout
	return saida
	
	 
	
	
def logo(text):
	os.system('clear')
	text = pyfiglet.figlet_format(text, font='slant')
	print('\033[1;31m', text, '\033[m\033[1;37mconsole\033[m\n')
		
def verify(opc):
	opc = int(opc)
	if opc == 1:
		logo('NMAP')
		ip = input('\033[1;33mDigite o IP:\033[m ')
		clear_()
		logo('NMAP')
		systema(f'nmap {ip}')
		texto_d('\033[1;33mEnter para voltar ao menu\033[m\n')
		input('')
	
	
			
def space():
	print('\n\n\n')	
def show_menu():
	class nmap:
		print('\033[1;31m', pyfiglet.figlet_format('NMAP', font='slant'), '\033[m')
		print('\033[1;33m[01] SCANEAR IP\033[m')
		print('\033[1;33m[02] SCANEAR PORTA\033[m')
		print('\033[1;33m[03] SCANEAR SISTEMA\033[')
		
		
		
		
		

		
				
												
def texto_d(texto):
	for c in texto:
		print(c, end="", flush=True)
		time.sleep(0.1)												
def menu_principal():
	while True:
		text = 'MR.ROBOT'
		text = pyfiglet.figlet_format(text, font='big')
		clear_()
		#print(f'\033[1;34m{text}\033[m\nby: @akycyel')
		show_menu()
		space()
		txt = '\033[1;31mDigite a opção abaixo\033[m\n: '
		texto_d(txt)
		opc = input('')
		if opc == 'sair':
			break
		elif opc == 'reiniciar':
			os.system('python onixx.py')
			break
		else:
			verify(opc)
		
		
		
		
		
		
menu_principal()
	
		
