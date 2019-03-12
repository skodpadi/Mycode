#!/usr/bin/env pyhton3

import shutil
import os

os.chdir('/home/student/mycode')

shutil.move('raynor.obj', 'ceph_storage/')
xname = input("What's the new name for kerrigan.obj?")
shutil.move('ceph_storage/kerrigan.obj',('ceph_storage/'+ xname))

