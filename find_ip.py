from sys import argv
from socket import gethostbyname, gaierror, getnameinfo, gethostbyaddr
from os import system
from termcolor import colored
from re import search


def get_ips(name):
    ip_list = []
    ips = ""
    for i in range(0, 10):
        ip_list.append(colored(gethostbyname(name), "green"))
        ip_list = list(set(ip_list))
    for ip in ip_list:
        ips += ip + ", "
    return ips[:-2]

argv.pop(0)
n = len(argv)
system("cls||clear")
for domain_name in argv:
    domain_name = domain_name.replace("https://", "")
    domain_name = domain_name.replace("http://", "")
    try:
        search('[a-zA-Z]', domain_name).group(0)
        print(domain_name, " --> ", get_ips(domain_name))
    except gaierror:
        print(domain_name, " --> ", colored("Invalid host", "red"))
    except AttributeError:
        try:
            print(domain_name, " --> ", colored(getnameinfo((domain_name, 0), 0)[0], "green"))
        except AttributeError:
            print(domain_name, " --> ", colored("Invalid ip", "red"))
