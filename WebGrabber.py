import os
import subprocess
import socket
import re
def pinguh(host):
        command = ['ping','-c','1',host]
        return subprocess.call(command)
def nmapuh(host):
        nmapOpenArr = []
        nmapRes = "Open Ports:\n"
        nmapRes = ("\u0332".join(nmapRes))
        command = ['nmap','-sS','--open',host]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines = True)
        for line in iter(process.stdout.readline, ""):
                line = line.strip()
                x = '/tcp' in line
                if x:
                        nmapRes = nmapRes + line + "\n"
                        nmapOpenArr.append(line)
        return nmapRes
def wgetuh(host):
        hostC = 'www.' + host + '/'
        wgetArr = []
        command = ['wget','-r','-nd','--delete-after','--spider',hostC]
        process = subprocess.Popen(command, stderr=subprocess.PIPE, universal_newlines = True)
        for line in iter(process.stderr.readline,""):
                line = line.strip()
                x = host + '/' in line
                y = "following" in line
                if x and not y:
                        wgetRes =  line[25:].strip() + "\n"
                        if wgetRes not in wgetArr:
                                wgetArr.append(wgetRes)
        return wgetArr



def getRobots(host):
        robots = ''
        command = ['curl',host]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines = True)
        for line in iter(process.stdout.readline,""):
                line = line.strip()
                robots = robots + line + "\n"
        return robots


def WebGrab(pingee):
        if pinguh(pingee) == 0:
                print("Server is up! Continuing processes...")
                ip = socket.gethostbyname(pingee)
                print (ip)
                nmapPorts = nmapuh(pingee)
                print(nmapPorts)
                x = wgetuh(pingee)
                for urls in x:
                        print(urls)
                if 'https://'+ pingee  in  x:
                        x = getRobots("https://" + pingee + "/robots.txt")
                else:
                        x = getRobots("https://" + pingee + "/robots.txt")
                print('\n Robots under me \n')
                print (x)
        else:
                print("Server is down!")
        return "done"
urls  = input('Please enter in urls seperated by a space (EX: google.com reddit.com): ').strip()
targets = urls.split()
for tar in targets:
        WebGrab(tar)

