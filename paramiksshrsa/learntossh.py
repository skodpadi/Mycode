#!/usr/bin/env python3

## import paramiko so we can talk SSH

import paramiko
import os

## shortcut issuing commands to remote

def sshcommands():
    listcommands = input("Provide list of commands..")
    print(listcommands)
    return listcommands

def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

sshsession = paramiko.SSHClient()

## mykey is our private key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

IPaddressUsername = "none"

while IPaddressUsername != "Done":
    IPaddressUsername = input("Enter IP address and username..")
    sshsession.connect(hostname=IPaddressUsername.split()[0], username=IPaddressUsername.split()[1], pkey=mykey)

#our_commands1 = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]
    our_commands = sshcommands().split(",")
    print(type(our_commands))
    for x in our_commands:
        print(commandissue(x).decode('utf-8'))


