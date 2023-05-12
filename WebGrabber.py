import os
import subprocess
import socket

def pinguh(host):
        command = ['ping','-c','1',host]
        return subprocess.call(command)
def nmapuh(host):
        nmapRes = "Open Ports:\n"
        nmapRes = ("\u0332".join(nmapRes))
        command = ['nmap','-sS','--open',host]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines = True)
        for line in iter(process.stdout.readline, ""):
                line = line.strip()
                x = '/tcp' in line
                if x:
                        nmapRes = nmapRes + line + "\n"
        return nmapRes
def wgetuh(host):
        hostComplete = 'www.' + host + '/'
        wgetArr = []
        command = ['wget','-r','-nd','--delete-after','--spider',hostC]
        process = subprocess.Popen(command, stderr=subprocess.PIPE, universal_newlines = True)
        for line in iter(process.stderr.readline,""):
                line = line.strip()
                x = hostC in line
                y = "following" in line
                if x and not y:
                        wgetRes =  line[25:].strip() + "\n"
                        if wgetRes not in wgetArr:
                                wgetArr.append(wgetRes)
        return wgetArr

pingee = input("Enter Domain: ").strip()

if pinguh(pingee) == 0:
        print("Server is up! Continuing processes...")
        ip = socket.gethostbyname(pingee)
        print (ip)
        nmapPorts = nmapuh(pingee)
        print(nmapPorts)
        x = wgetuh(pingee)
        nmapHeader = "Open Ports:\n"
        nmapHeader = ("\u0332".join(nmapRes))
        print (nmapHeader + '\n')
        for urls in x:
                print(urls)
else:
        print("Server is down!")

