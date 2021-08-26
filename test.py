import os

os.system("pip3 install requests shodan colorama bs4 html5lib sty alive-progress")   

import sys
from rainbow import *
import time
import requests
import socket
import webbrowser
from json import *
from shodan import Shodan
from requests import *
from colorama import *
from bs4 import BeautifulSoup
import json
from urllib import request
import urllib
import requests
from alive_progress import alive_bar




def help():
    rainbow('''

     ______________________________________________________________________________________________
    |                                                                                              |
    | shodan [IP] - Saca vulnerabilidades/informacion sobre una IP                                 |
    | shodan2 [URL] - Saca vulnerabilidades/informacion sobre una pagina web                       |
    | bannerscrap [URL] - Saca info/banner sobre una pagina web                                    |
    | whois [IP] - Saca informacion sobre una IP [Recon Activo]                                    |
    | bypasscf [URL] - BruteForce a una pagina web [Adivinar subdominios/bypassear el CF]          |
    | nmap [IP/URL] - Saca informacion sobre los puertos de una IP/URL                             |
    | nmapbp [Firewall Bypass] - Script NSE de nmap para Bypassear el WAF                          |
    | reverseip [URL/IP] - Averigua si la IP/URL de una maquina contiene mas maquinas o subdominios|
    | iphistory [URL] - Averigua todas las IPS de una pagina web                                   |
    | httpheader [URL] - Sepa los headers de una pagina web (Parecido a BurpSuite)                 |
    | cls/clear - Limpia la terminal                                                               |
    |______________________________________________________________________________________________|

''')




def banner():
    rainbow('''
                                        Escribe "ls" para los comandos.
                                ▄ •▄  ▄▄▄· ▄▄▌  ▪  .▄▄ · ▄▄▄▄▄▄▄▄ . ▐ ▄ ▪   ▄▄▄· 
                                █▌▄▌▪▐█ ▀█ ██•  ██ ▐█ ▀. •██  ▀▄.▀·•█▌▐███ ▐█ ▀█ 
                                ▐▀▀▄·▄█▀▀█ ██▪  ▐█·▄▀▀▀█▄ ▐█.▪▐▀▀▪▄▐█▐▐▌▐█·▄█▀▀█ 
                                ▐█.█▌▐█ ▪▐▌▐█▌▐▌▐█▌▐█▄▪▐█ ▐█▌·▐█▄▄▌██▐█▌▐█▌▐█ ▪▐▌
                                ·▀  ▀ ▀  ▀ .▀▀▀ ▀▀▀ ▀▀▀▀  ▀▀▀  ▀▀▀ ▀▀ █▪▀▀▀ ▀  ▀ V1.0
                                            Coded by hashes#1843 
''')

def clearscreen():
    if sys.platform.startswith('win32'):
        os.system("cls")
    else:
        print('\e[2J')

clearscreen()

print(Fore.CYAN)

with alive_bar(100, bar='circles') as bar:
    for i in range(100):
        time.sleep(.05)
        bar()

clearscreen()
banner()

while True:
    print(f"{Fore.RED}root{Fore.WHITE}@{Fore.RED}kalistenia:{Fore.WHITE}~# ", end='')
    x = input().split()
    cmd = x[0]


    if cmd == "help":
        help()

    elif cmd == 'clear':
        clearscreen()

    elif cmd == "bypasscf":
        try:

            print()
            subdomains = ["www", "ovh-birdmc", "cpanel", "ads",  "clans", "clanseu", "clanshub", "vote", "vote1", "vote2", "vote3", "vote4", "vote5", "vote6", "vote7", "vote8",  "clanshubeu",  "eudev", "db", "chat", "cvote1", "cvote2", "cvote3", "cvote4", "cvote5", "cvote6", "vpn", "vpn1", "vpn2", "vpn3", "vpn4", "vpn5", "cvote7", "pebg", "oracle", "pe", "sqlstats", "staging", "" "ns-vps", "d", "t", "short", "jar", "iptables", "ufw", "recuperar", "baneados", "imagenes", "samp", "social", "holo", "donaciones", "shoprp", "wow", "multicraft", "mail", "radio3", "radio2", "fr", "teamdub", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "torneo", "serv11", "serv0", "serv10", "serv9", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "appeals", "reports", "translations", "marketing", "staff", "bugs", "rules", "singapore1", "singapore2", "singapore3", "singapore4", "singapore5", "help", "render", "foro", "ts3", "git", "analytics", "coins", "votos", "docker-main", "docker", "main", "server3", "cdn", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "panel", "apolo", "sv3", "sv2", "sv1", "backups", "zeus", "thor", "vps", "web", "dev", "tv", "deposito", "depositos", "extra", "extras", "bungee1", "torneoyt", "hcf", "uhc5", "uhc4", "uhc3", "uhc2", "uhc1", "uhc", "dedicado5", "dedicado4", "dedicado3", "dedicado2", "ded5", "ded4", "ded3", "ded2", "ded1", "ded", "gamehitodrh", "servidor4", "webdisk", "webmail", "monitor", "servidor001", "servidor10", "servidor9", "servidor8", "servidor7", "servidor6", "servidor5", "servidor4", "servidor3", "hvokfcic7sm", "autodiscover", "tauchet", "hg10", "ping", "hg9", "hg8", "hg7", "hg6", "hg5", "hg4", "hg3", "hg2", "hg1", "tienda", "status", "ayuda", "playstation", "xenforo", "home", "job", "firewall", "rank", "mantenimiento", "beta", "pay", "private", "port", "bb", "stor", "mx5",
                           "serieyt", "shop", "jira", "rule", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv7", "serv6", "serv5", "serv", "mcp", "paysafe", "mu", "radio", "donate", "unauthorized",  "vps03", "atlas", "au", "accounts", "account", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "translations", "staff", "help", "render", "git", "analytics", "coins", "votos", "docker-main", "main", "server3", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test" "sv3", "sv2", "sv1",  "vps", "build", "web", "dev", "mc", "play", "sys", "node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10", "node11", "node12", "node13", "node14", "node15", "node16", "node17", "node18", "node19", "node20", "node001", "node002", "node01", "node02", "node003", "sys001", "sys002", "go", "admin", "eggwars", "bedwars", "lobby1", "hub", "builder", "developer", "test1", "forum", "bans", "baneos", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "supports", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeal", "store-assets", "builds", "testing", "server", "pvp", "skywars", "survival", "skyblock", "lobby", "hg", "games", "sys001", "sys002", "node001", "node002", "games001", "games002", "game001", "game002", "game003", "sys001", "us72", "us1", "us2", "us3", "us4", "us5", "goliathdev", "staticassets", "rewards", "rpsrv", "ftp", "ssh", "web", "jobs", "hcf", "grafana", "vote2", "file", "sentry", "enjin", "webserver", "xen", "mco", "monitor", "servidor2", "sadre", "gamehitodrh", "ts"]
            xy = x[1]
            xyy = xy.lower()
            print()
            for ejecutar in subdomains:
                try:
                    ipserver = str(ejecutar)+"."+str(xyy)
                    iphost = socket.gethostbyname(str(ipserver))
                    if iphost.startswith("104."):
                        print("[Bypass CloudFlare] Subdominios encontrados >> " + ""+str(
                            ejecutar)+"."+str(xyy)+" >> "+ "" +str(iphost) + " [CloudFlare]")
                    else:
                        print("[Bypass CloudFlare] Subdominios encontrados >> " + ""+str(
                            ejecutar)+"."+str(xyy)+" >> "+ ""+str(iphost) + " [Bypass]")
                except:
                    pass

        except Exception as e:
            print()
            rainbow("""
        ╔═════════════════════════════╗
        ║ Uso: bypasscf [example.com] ║
        ╚═════════════════════════════╝
				""")
            pass
            print()



    elif cmd == "nmap":
        try:
            target = x[1]
            try:
                os.system("nmap -Pn -sC -sV -vvv --max-retries 3 "+target) #Pueden cambiar el comando de nmap si quieren xd
                print()
            except:
                pass
        except Exception as e:
            print()
            rainbow("""
    ╔═══════════════════════════════════╗
    ║ Uso: nmap [127.0.0.1/example.com] ║
    ╚═══════════════════════════════════╝
					""")    


    elif cmd == "shodan":
        try:
            target = x[1]
            try:
                api = Shodan('EO3OOfPyo4OJprHeADpPCrjMkytAKtIx')
                h = api.host(target)
                print('''

                    Direccion: {}
                    Ciudad: {}
                    ISP: {}
                    ORG: {}
                    Ports: {}
                    Country Code: {}
                    OS: {}
                    Vuln: {}

                '''.format(h['ip_str'],h['city'],h['isp'],h['org'],h['ports'],h['country_code'],h['os'],h['vulns']))
            except:
                pass
                print()

        except Exception as e:
            print()
            rainbow("""
            ╔═════════════════════════╗
            ║ Uso: shodan [127.0.0.1] ║
            ╚═════════════════════════╝
                   """)
            print()


    elif cmd == "whois":
        target = x[1]
        try:
            urlx = (f"https://ipinfo.io/{target}/json")
            response = urllib.request.urlopen(urlx)
            x = response.read()
            j = json.loads(x)
            print("[+] Whois ->: ")
            print(f"IP: {target}")
            print("Ciudad: "+j['city'])
            print("Region: "+j['region'])
            print("Pais: "+j['country'])
            print("Loc: "+j['loc'])
            print("ORG: "+j['org'])
            print("Codigo Postal: "+j['postal'])
            print("Zona de tiempo: "+j['timezone'])

        except Exception as e:
            print()
            rainbow("""
            ╔════════════════════════╗
            ║ Uso: whois [127.0.0.1] ║
            ╚════════════════════════╝
                 """)
            print()

    elif cmd == "tgn":
        webbrowser.open("https://discord.gg/y73vH5E9aw")


    elif cmd == "cls":
        if sys.platform.startswith('win32'):
            os.system("cls")
            banner()

        else:
            os.system("clear")
            banner()

    elif cmd == "":
        help()

    elif cmd == "reverseip":
        target = x[1]
        try:
	        agente= {'User-Agent': 'Firefox'}
	        a = requests.get(f"https://viewdns.info/reverseip/?host={target}&t=1",headers=agente)
	        b = BeautifulSoup(a.text,'html5lib')
	        c = b.find(id="null")
	        d = c.find(border="1")
	        for l in d.find_all("tr"):
		        print("Sitio encontrado: " + l.td.string)
                
        except Exception as e:
            print()
            rainbow("""
            ╔══════════════════════════════╗
            ║ Uso: reverseip [example.com] ║
            ╚══════════════════════════════╝
                 """)
            print()



    elif cmd == "iphistory":
        target = x[1]
        try:
	        agente= {'User-Agent': 'Firefox'}
	        a = requests.get(f"https://viewdns.info/iphistory/?domain={target}&t=1",headers=agente)
	        b = BeautifulSoup(a.text,'html5lib')
	        c = b.find(id="null")
	        d = c.find(border="1")
	        for l in d.find_all("tr"):
		        print("IP encontradas: " + l.td.string)
                
        except Exception as e:
            print()
            rainbow("""
            ╔══════════════════════╗
            ║ Uso: iphistory [URL] ║
            ╚══════════════════════╝
                 """)
            print()


    elif cmd == "httpheader":
        target = x[1]
        try:
            r = requests.get(target)
            cabeceras = dict(r.headers)
            for x in cabeceras:
                print(x + " : " + cabeceras[x])
                print()
        except Exception as e:
            print()
            rainbow("""
            ╔═══════════════════════════════╗
            ║ Uso: httpheader [example.com] ║
            ╚═══════════════════════════════╝
                 """)
            print()
            
    elif cmd == "nmapbp":
        target = x[1]
        try:
            os.system("nmap --script firewall-bypass "+target)
        except Exception as e:
            print()
            rainbow("""
            ╔═════════════════════════════════════╗
            ║ Uso: nmapbp [127.0.0.1/example.com] ║
            ╚═════════════════════════════════════╝
                 """)
            print()

    elif cmd == "ls":
        help()


    elif cmd == "clear":
        if sys.platform.startswith('win32'):
            os.system("cls")
            banner()

        else:
            os.system("clear")
            banner()



    elif cmd == "shodan2":
        target = input("Web: ")
        try:
            api = Shodan('EO3OOfPyo4OJprHeADpPCrjMkytAKtIx')
            print("¡Recuerda poner el sitio web sin HTTP/S!")
            results = api.search(target, page=1, facets=None)
            for h in results['matches']:
                print("Target Encontrado: {}".format(h['ip_str']+ " Port " + str(h['port'])))

        
        except Exception as e:
            print()
            rainbow("""
            ╔════════════════════════════╗
            ║ Uso: shodan2 [example.com] ║
            ╚════════════════════════════╝
                 """)
            print()

    
    elif cmd == "bannerscrap":
        target = x[1]
        try:
            os.system("nmap -sV --script=banner {} ".format(target))
        except Exception as e:
            print()
            rainbow('''
            ╔════════════════════════════════╗
            ║ Uso: bannerscrap [example.com] ║
            ╚════════════════════════════════╝
            ''')
            print()


    else:
        help()




