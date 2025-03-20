
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
		ip = input('\033[1;33mDigite o IP ou URL:\033[m ')
		clear_()
		logo('NMAP')
		terminal = systema(f'nmap {ip}')
		terminal = terminal.splitlines()
		terminal = terminal[4:]
		print(f'\033[1;34mPORTAS DE {ip} SCANEADAS\033[m 🧐')
		for c in terminal:
			if '/' in c:
				if 'open' in c:
					c = c.replace('open', '\033[1;32mABERTO\033[m😎')
					print('\033[1;35mPORTA =\033[m', c)
				elif 'closed' in c:
					c = c.replace('closed', '\033[1;31mFECHADA\033[m😡')
					print('\033[1;35mPORTA =\033[m', c)
				elif 'filtered' in c:
					c = c.replace('filtered', '\033[1;33mFILTRADA\033[m🤨')
					print('\033[1;35mPORTA =\033[m', c)
					
		
		texto_d('\n\033[1;33mEnter para voltar ao menu\033[m\n')
		input('')
	if opc == 2:
		logo('NMAP')
		ip = input('\033[1;33mDigite o IP ou URL:\033[m ')
		port = input('\033[1;33mDigite a porta:\033[m ')
		logo('NMAP')
		terminal = systema(f'nmap -p {port} {ip}')
		terminal = terminal.splitlines()
		terminal = terminal[4:]
		print(f'\033[1;34mPORTA {port} DE {ip} scaneada.\033[m')	
		for c in terminal:
			if '/' in c:
				if 'open' in c:	
					c = c.replace('open', '\033[1;32mABERTO\033[m😎')
					print('\033[1;35mPORTA =\033[m', c)
				elif 'closed' in c:
					c = c.replace('closed', '\033[1;31mFECHADA\033[m😡')
					print('\033[1;35mPORTA =\033[m', c)
				elif 'filtered' in c:
					c = c.replace('filtered', '\033[1;33mFILTRADA\033[m🤨')
					print('\033[1;35mPORTA =\033[m', c)
				else:
					print(c)
					
		
		texto_d('\n\033[1;33mEnter para voltar ao menu\033[m\n')
		input('')
	if opc == 4:
		logo('NMAP')
		texto_d('\033[1;33mDigite IP [do roteador/modem]:\033[m ')
		ip = input(': ')
		logo('NMAP')
		print('\033[1;33mpingando em ips\033[m', '🤭')
		terminal = systema(f'nmap -sn {ip}/24')
		terminal = terminal.splitlines()
		for c in terminal:
			if '192.168' in c or '10.0' in c:
				c = c.replace('Nmap', '\033[1;35mESSE IP RESPONDEU AO PING:\033[m\033[1;32m')
				c = c.replace('scan', '')
				c = c.replace('report', '')
				c = c.replace('for', '')
				print(c, '🥱')
		texto_d('\n\033[1;33mEnter para voltar ao menu\033[m')
		input('')
		
	
	
	
			
def space():
	print('\n\n\n')	
def show_menu():
	class nmap:
		print('\033[1;31m', pyfiglet.figlet_format('NMAP', font='slant'), '\033[m')
		print('\033[1;33m[01] SCANEAR IP\033[m')
		print('\033[1;33m[02] SCANEAR PORTA\033[m')
		print('\033[1;33m[03] SCANEAR SISTEMA [root]\033[m')
		print('\033[1;33m[04] DESCOBRIR HOST ATIVO NA REDE\033[m')
		#print('\033[1;33m[05] SCANEAMENTO FURTIVO [root]\033[m')
		
		
	
		
		
		
		
		
		
		

		
				
												
def texto_d(texto):
	for c in texto:
		print(c, end="", flush=True)
		time.sleep(0.03)												
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
	
		
