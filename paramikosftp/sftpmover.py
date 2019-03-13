#!/usr/bin/env python3

##Moving file with SFTP

import paramiko
import os

## where to connect to

t = paramiko.Transport("10.10.2.3", 22) ## IP and host

## how to connect
t.connect(username="bender", password="alta3")

### Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/home/student/filestocopy/"):
    if not os.path.isdir("/home/student/filestocopy/"+x):
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)

## close the connection
sftp.close()
