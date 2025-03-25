import pexpect
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
	os.system('pkg install pexpect')
	

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



def texto_d(texto):
	for c in texto:
		print(c, end="", flush=True)
		time.sleep(0.03)
		
def iniciar_telnet(ip, login, password):
	while True:
		router = pexpect.spawn(f'telnet {ip}', timeout=20)
		router.expect('Login:')
		router.sendline(login)
		router.expect('Password:')
		router.sendline(password)
		router.expect('WAP>')
		texto_d('\033[1;32mconectado com sucesso\033[m')
		print('😈')
		time.sleep(2)

		return router

def comandos_telnet(command, router):
	if command == 1:
		router.sendline('set led switch on')
		router.expect('WAP>')
	elif command == 2:
		router.sendline('set led switch off')
		router.expect('WAP>')
	elif command == 3:
		for c in range(0, 40):
			time.sleep(0.1)
			router.sendline('set led switch on')
			router.expect('WAP>')
			time.sleep(0.1)
			router.sendline('set led switch off')
			router.expect('WAP>')
			
			
		
	elif command == 5:
		router.sendline('restore manufactory')
			
		
	
		
	
def fechar_telnet(router):
	router.close()
	print('Conexão encerrada')
	

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
def systema_os(command):
	clear_()
	os.system(command)
	 
	
	
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
	if opc == 10:
		logo('PROTOCOLOS')
		texto_d('\033[1;33mIremos fazer conexão TELNET.\n')
		texto_d('\033[1;33mDigite o IP\033[m: ')
		ip = input('')
		texto_d('\033[1;33mLogin:\033[m ')
		login = input('')
		texto_d('\033[1;33mSenha: \033[m')
		password = input('')
		clear_()
		logo('TELNET')
		router = iniciar_telnet(ip, login, password)
		while True:
			clear_()
			logo('TELNET')
			print('\033[1;33m[1] LIGAR LUZES\033[m 😃')
			print('\033[1;33m[2] DESLIGAR LUZES\033[m 😴')
			print('\033[1;33m[3] MODO PISCA PISCA\033[m 😂')
			print('\033[1;33m[4] REINICIAR MODEM\033[m 😑')
			print('\033[1;33m[5] RESETAR DE FÁBRICA\033[m 😐')
			print('\033[1;33m[6] VER QUEM ESTÁ CONECTADO\033[m 🧐')
			print('\033[1;33m[9] SAIR\033[m 🙂👋')
			user = int(input('\n\033[1;31mOPÇÃO: '))
			if user == 9:
				fechar_telnet(router)
				break
			elif user == 4:
				clear_()
				logo('TELNET')				
				router.sendline('reset')
				texto_d('\033[1;33mEspere o wifi voltar e refaça a conexão para usar os comandos, pois você reiniciou o modem.\033[m')
				texto_d('Aguarde 10 segundos')
				time.sleep(10)
			elif user == 6:
				clear_()
				print('\033[1;31m', pyfiglet.figlet_format('DISPOSITIVOS', font='small'), '\033[m')
				print('    \033[1;34m', pyfiglet.figlet_format('CONECTADOS', font='small'), '\033[m')
				for c in range(1, 120):
					saida = router.before.decode()
					listabase = saida.splitlines()
					if 'success!' in listabase:
						router.sendline('')
						router.expect('WAP>')
					elif '' in listabase:
						router.sendline('')
						router.expect('WAP>')
						
						
					router.sendline(f'get wlan associated laninst 1 wlaninst 1 deviceinst {c}')
					router.expect('WAP>')
					saida = router.before.decode()
					listabase = saida.splitlines()
					lista = []
					for linha in listabase:
						lista.extend(linha.split())
					if len(lista) < 18:
						print('\n\033[1;97m', c - 1, 'DISPOSITIVO ENCONTRADOS\033[m', '🥱')
						break
					nome = lista[24] if len(lista) > 24 else 'Desconhecido'
					ip = lista[18] if len(lista) > 18 else 'Não encontrado'
					mac = lista[15] if len(lista) > 15 else 'Não encontrado'
					print('\033[1;31m_\033[m' * 50)
					print(f'\n\033[1;34mNOME: {nome}\033[m')
					print(f'\033[1;35mIP: {ip}\033[m')
					print(f'\033[1;32mMAC ADDRESS: {mac}\033[m')
					print('\033[1;31m_\033[m' * 50)
        				
        				
        				

						
						
						
				texto_d('\n\033[1;33mENTER PARA VOLTAR AO MENU DO TELNET\033[m')
				input()
			else:
				comandos_telnet(user, router)
			
			
		
	
			
			
			
		
		 
		
	
	
	
			
def space():
	print('\n\n\n')	
def show_menu():
	class nmap:
		print('\033[1;31m', pyfiglet.figlet_format('NMAP', font='slant'), '\033[m')
		print('\033[1;33m[01] SCANEAR IP\033[m',          '\033[1;32m                  [ATIVO]\033[m')
		print('\033[1;33m[02] SCANEAR PORTA\033[m')
		print('\033[1;33m[03] SCANEAR SISTEMA [root]\033[m')
		print('\033[1;33m[04] DESCOBRIR HOST ATIVO NA REDE\033[m')
		#print('\033[1;33m[05] SCANEAMENTO FURTIVO [root]\033[m')
		
	class telnet:
		print('\033[1;31m', pyfiglet.figlet_format('PROTOCOLOS', font='slant'), '\033[m')
		print('\033[1;33m[10] FAZER CONEXÃO TELNET\033[m', '\033[1;32m         [ATIVO]\033[m')
		print('\033[1;33m[11] FAZER CONEXÃO SSH\033[m', '\033[1;31m          [MANUNTENÇÃO]\033[m')
		print('\033[1;33m[12] FAZER CONEXÃO MYSQL\033[m', '\033[1;31m        [MANUNTENÇÃO]\033[m')
		
		
		
		
	
		
		
		
		
		
		
		

		
				
												
												
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
	
		
