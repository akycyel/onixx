
import requests
import pyfiglet
import os
import time


def instalar_books():
	os.system('pip install pyfiglet')
	os.system('pip install beautifulsoup4')
	os.system('pkg install nmap')
	os.system('pip install requests')
	
def clear_():
	sistema = os.name
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

if os.path.exists('login.txt'):
	print('Ok')
	
else:
	with open('login.txt', 'w') as p:
		p.write('True')
		clear_()
		txt = 'Iremos instalar as bibliotecas, isso pode demorar dependendo da sua internet.'
		for c in txt:
			print(c, end="", flush=True)
			time.sleep(0.1)
		time.sleep(2)
		instalar_books()
		p.write('\nLivros instalados')
	with open('onixx.py', 'r') as p:
		linhas = p.readlines()
	linhas.insert(0, '\nimport pyfiglet')
	linhas.insert(0, '\nimport requests')
	with open('onixx.py', 'w') as p:
		p.writelines(linhas)
	os.system('python onixx.py')
		
		
		
def verify(opc):
	opc = int(opc)
	if opc == 1:
		print('funcionando')
def space():
	print('\n\n\n')	
def show_menu():
	class nmap:
		print('----------NMAP---------')
		print('[01] SCANEAR IP')
		print('[02] SCANEAR PORTA')
		print('[03] SCANEAR SISTEMA')
		

		
				
						
								
def texto_d(texto):
	for c in texto:
		print(c, end="", flush=True)
		time.sleep(0.1)												
def menu_principal():
	while True:
		text = 'MR.ROBOT'
		text = pyfiglet.figlet_format(text)
		clear_()
		print(f'\033[1;34m{text}\033[m\nby: @akycyel')
		show_menu()
		space()
		txt = '\033[1;31mDigite a opção abaixo\033[m\n: '
		texto_d(txt)
		opc = input('')
		if opc == 'sair':
			break
		else:
			verify(opc)
		
		
		
		
		
		
menu_principal()
	
		
