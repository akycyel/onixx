import pexpect
import requests
import pyfiglet
import shlex
import subprocess
import os
import time

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
def animacao1():


	skull = """
       ______
    .-'      `-.
   /            \\
  |              |
  |,  .-.  .-.  ,|
  | )(_o/  \o_)( |
  |/     /\     \|
  (_     ^^     _)
   \__|IIIIII|__/
    | \IIIIII/ |
    \          /
     `--------`
"""
	skull_open = """
       ______
    .-'      `-.
   /            \\
  |              |
  |,  .-.  .-.  ,|
  | )(_o/  \o_)( |
  |/     /\     \|
  (_     ^^     _)
   \__|IIIIII|__/
    |  |    |  |
    |  |----|  |
    \  '----'  /
     `--------`
"""

	
	for c in range(0, 6):
		os.system('clear')
		print('\033[1;31mstarting onixx\033[m')
		print('\033[1;32m', skull, '\033[m')
		time.sleep(0.1)
		os.system('clear')
		print('\033[1;31mstarting onixx\033[m')
		print('\033[1;32m', skull_open, '\033[m')
		time.sleep(0.1)


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
	elif opc == 2:
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
	elif opc == 3:
		logo('SCANNER')
		texto_d('DIGITE O IP: ')
		ip = input('')
		logo('SCANNER')
		terminal = systema(f'nmap -O {ip}')
		print(terminal)
		input('ENTER')
	elif opc == 4:
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
	elif opc == 5:
		logo('FURTIVO')
		texto_d('\033[1;33mDIGITE O IP:\033[m ')
		ip = input('')
		logo('FURTIVO')
		terminal = systema(f'nmap -Pn {ip}').splitlines()
		terminal = terminal[4:]
		print('\033[1;31mscaneamento furtivo em', ip, '\033[m')
		for c in terminal:
			if '/' in c:
				if 'open' in c:	
					c = c.replace('open', '\033[1;32mABERTO\033[m😎')
					print('\033[1;35mPORTA =\033[m', c)
				elif 'closed' in c:
					c = c.replace('closed', '\033[1;31mFECHADA\033[m😡')
					print('\033[1;35mPORTA =\033[m', c)
				elif 'filtered' in c:
					c = c.replace('filtered', '\033[1;33mFIREWALL ATIVO\033[m🤨')
					print('\033[1;35mPORTA =\033[m', c)
				else:
					print(c)
				
		texto_d('\n\033[1;33mENTER PARA VOLTAR\033[m')
		input()
	elif opc == 6:
		logo('SYN ACK')
		ip = input('\033[mDIGITE O IP:\033[m ')
		logo('SYN ACK')
		terminal = systema(f'nmap -sS {ip}').splitlines()
		terminal = terminal[4:]
		for c in terminal:
			if '/' in c:
				if 'open' in c:	
					c = c.replace('open', '\033[1;32mABERTO\033[m😎')
					print('\033[1;35mPORTA =\033[m', c)
				elif 'closed' in c:
					c = c.replace('closed', '\033[1;31mFECHADA\033[m😡')
					print('\033[1;35mPORTA =\033[m', c)
				elif 'filtered' in c:
					c = c.replace('filtered', '\033[1;33mFIREWALL ATIVO\033[m🤨')
					print('\033[1;35mPORTA =\033[m', c)
				else:
					print(c)
		texto_d('\033[1;33mENTER PARA VOLTAR\033[m')
		input()
	elif opc == 7:
		logo('SCANNER')
		texto_d('\033[1;33mURL DO SITE:\033[m ')
		url = input('')
		logo('SCANNER')
		terminal = systema(f'ping -c 1 {url}').splitlines()
		terminal = terminal[1]
		ip = terminal.replace('PING', '')
		ip = ip.replace('64', '')
		ip = ip.replace('bytes', '')
		ip = ip.replace('from', '')
		print('\033[1;33m[RESULTADO ABAIXO]\033[m')
		print('\n\033[1;35m', ip)
		texto_d('\n\033[1;33mENTER PARA VOLTAR\033[m')
		input('')
	elif opc == 8:
		logo('SCANNER')
		ip = input('DIGITE O IP: ')
		logo('INFORMACOES')
		url = f'http://ip-api.com/json/{ip}'
		url = requests.get(url).json()
		print('_' * 50)
		print('\033[1;35mPaís:\033[m', url.get('country'))
		print('\033[1;35mCidade:\033[m', url.get('city'))
		print('\033[1;35mCEP:\033[m', url.get('zip'))
		print('\033[1;35mEstado:\033[m', url.get('regionName'))
		print('\033[1;35mSigla do país:\033[m', url.get('countryCode'))
		print('\033[1;35mSigla do estado:\033[m', url.get('region')) 
		print('\033[1;35mProvedor:\033[m', url.get('isp'))
		LAT = url.get('lat')
		LONG = url.get('lon')
		link = f'https://www.google.com/maps?q={LAT},{LONG}'
		print('\033[1;35mLink da localização (não exata):\033[m', link)
		print('_' * 50)

		
		
		
		
		input('')
		
	elif opc == 10:
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

	elif opc == 17:
		def ataque(ip, protocolo, porta, usuario):
			if protocolo == 1:
				protocolo = 'ssh'
				terminal = subprocess.Popen(['hydra', '-l', usuario, '-P', 'senhas.txt', f'{protocolo}://{ip}:{porta}'])
				logo('HYDRA')
				print('\033[1;33mProcesso começou\033[m')
				terminal.wait()
				texto_d('\033[1;33mo processo encerrou\033[m\n')
				print('\033[1;33mENTER PARA VOLTAR AO MENU\033[m')
				input('')
			elif protocolo == 2:
				protocolo = 'telnet'
				terminal = subprocess.Popen(['hydra', '-l', usuario, '-P', 'senhas.txt', f'{protocolo}://{ip}:{porta}'])
				logo('HYDRA')
				print('\033[1;33mProcesso começou\033[m')
				terminal.wait()
				texto_d('\033[1;33mo processo encerrou\033[m\n')
				print('\033[1;33mENTER PARA VOLTAR AO MENU\033[m')
			elif protocolo == 3:
				protocolo = 'mysql'
				terminal = subprocess.Popen(['hydra', '-l', usuario, '-P', 'senhas.txt', f'{protocolo}://{ip}:{porta}'])
				logo('HYDRA')
				print('\033[1;33mProcesso começou\033[m')
				terminal.wait()
				texto_d('\033[1;33mo processo encerrou\033[m\n')
				print('\033[1;33mENTER PARA VOLTAR AO MENU\033[m')
				
					
					
					
		logo('HYDRA')
		ip = input('DIGITE O IP: ')
		logo('HYDRA')
		texto_d('\033[1;37mprecisamos de algumas informações para o ataque\033[m')
		print('\n\n\033[1;33m[1] SSH\033[m')
		print('\033[1;34m[2] TELNET\033[m')
		print('\033[1;35m[3] MYSQL\033[m\n')
		texto_d('\033[1;31mESCOLHA QUAL USARÁ:\033[m ')
		protocolo = int(input(''))
		texto_d('\n\033[1;37mNÚMERO DA PORTA: \033[m')
		porta = input('')
		logo('HYDRA')
		texto_d('\033[1;33mNOME DE USUÁRIO: ')
		usuario = input('')
		ataque(ip, protocolo, porta, usuario)
	elif opc in [25, 26, 27]:
		logo('OPENCV')
		opc = opc
		texto_d('\033[1;33mCole o nome da imagem:\033[m ')
		caminho = input('')
		subprocess.run(['python', 'detect.py', str(opc), str(caminho)])
		input('')

		
		
		
				
			 
			
			
			
		
		
			
			
		
	
			
			
			
		
		 
		
	
	
	
			
def space():
	print('\n\n\n')	
def show_menu():
	
	class info:
		#print(pyfiglet.figlet_format('BEM VINDO', font='small'))
		print('\033[1;32mwellcome to onixx\033[m', '🕵️‍♂️')
		destino = subprocess.run(['pwd'], capture_output=True, text=True)
		destino = destino.stdout.strip()
		ip = subprocess.run(['curl', 'ifconfig.me'], capture_output=True, text=True)
		ip = ip.stdout.strip()
		url = f'http://ip-api.com/json/{ip}'
		url = requests.get(url).json()
		usuario = subprocess.run(['whoami'], capture_output=True, text=True)
		cidade = url.get('city')
		estado = url.get('country')
		usuario = usuario.stdout.strip()
		print('\033[1;37mUSUARIO:\033[m\033[1;35m', usuario)
		print('\033[1;37mIP:\033[m\033[1;35m', ip, '\033[m')
		print(f'\033[1;37mCidade:\033[m \033[1;35m{cidade}\033[m')
		print('\033[1;37mPWD:\033[m\033[1;35m', destino, '\033[m')
		print('\033[1;37mBY:\033[m\033[1;35m @akycyel\033[', '🤖')
		 
		
	class nmap:
		print('\n\n\033[1;31m', pyfiglet.figlet_format('SCANNER', font='slant'), '\033[m')
		print('\033[1;33m[\033[1;32m01\033[1;33m] SCANEAR IP\033[m')
		print('\033[1;33m[\033[1;32m02\033[1;33m] SCANEAR PORTA\033[m')
		print('\033[1;33m[\033[1;32m03\033[1;33m] SCANEAR SISTEMA [OFF]\033[m')
		print('\033[1;33m[\033[1;32m04\033[1;33m] DESCOBRIR HOST ATIVO NA REDE\033[m')
		print('\033[1;33m[\033[1;32m05\033[1;33m] SCAN FURTIVO \033[m')
		print('\033[1;33m[\033[1;32m06\033[1;33m] SCANEAMENTO COM [SYN ACK RST] \033[1;35m(root)\033[m')
		print('\033[1;33m[\033[1;32m07\033[1;33m] DESCOBRIR IP DE SITE\033[m')
		print('\033[1;33m[\033[1;32m08\033[1;33m] CONSULTAR IP\033[m')
		
	class protocolos:
		print('\033[1;31m', pyfiglet.figlet_format('PROTOCOLOS', font='slant'), '\033[m')
		print('\033[1;33m[\033[1;32m10\033[1;33m] FAZER CONEXÃO TELNET\033[m')
		print('\033[1;33m[\033[1;32m11\033[1;33m] FAZER CONEXÃO SSH\033[m')
		print('\033[1;33m[\033[1;32m12\033[1;33m] FAZER CONEXÃO MYSQL\033[m')
	class ataques:
		print('\033[1;31m', pyfiglet.figlet_format('ATACKs', font='slant'), '\033[m')
		print('\033[1;33m[\033[1;32m17\033[1;33m] QUEBRA DE SENHA\033[m')
		print('\033[1;33m[\033[1;32m18\033[1;33m] QUEBRA DE USUÁRIO E SENHA\033[m')
		
	class detecoes:
		print('\033[1;31m', pyfiglet.figlet_format('OPENCV', font='slant'), '\033[m')
		print('\033[1;33m[\033[1;32m25\033[1;33m] DETECTAR ROSTOS EM UMA FOTO\033[m')
		print('\033[1;33m[\033[1;32m26\033[1;33m] EXTRAIR E SALVAR ROSTO DE UMA IMAGEM\033[m')
		print('\033[1;33m[\033[1;32m27\033[1;33m] DETECTAR ROSTOS EM CAMERA\033[m')
		
		
		
		
		
		
	
		
		
		
		
		
		
		

		
				
												
												
def menu_principal():
	while True:
		disponiveis = ['1', '2', '3', '4', '5', '6', '7', '8', '10', '11', '12', '17', '18', '25', '26']
		text = 'MR.ROBOT'
		text = pyfiglet.figlet_format(text, font='big')
		clear_()
		#print(f'\033[1;34m{text}\033[m\nby: @akycyel')
		animacao1()
		clear_()
		show_menu()
		space()
		texto_d('\033[1;32mESCOLHA UMA OPÇÃO:\033[m ')
		opc = input('')
		if opc == 'sair':
			clear_()
			texto_d('\033[1;37mAté logo...💗️\033[m')
			break
		elif opc == 'reiniciar':
			os.system('python onixx.py')
			break
		elif opc in disponiveis:
			verify(opc)
		else:
			clear_()
			print(f'\033[1;31mEssa opção \033[m\033[1;33m[{opc}]\033[m\033[1;31m não existe\033[m')
			time.sleep(3)
		
		
		
		
menu_principal()
	
		
