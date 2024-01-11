#!/usr/bin/python3

keystone_file = open("/home/student/os-code/labs/attemptlogin/keystone.common.wsgi","r")
keystone_file_lines=keystone_file.readlines()

loginfail = 0
for line in keystone_file_lines:
	if "- - - - -] Authorization failed" in line:
		loginfail += 1
print('The number of failed login attempts is', loginfail)
keystone_file.close()
