import os
import subprocess

#downloadFile = "https://antave.com/onewebmedia/Drive-By_Alpha_2.7.apk"
#downloadFile = "https://download141.uploadhaven.com/1/application/zip/Oezi6X1nTpVwpzpOP0wtciNkBurMwMl0QbDRI28U.zip?key=An4NDatyQCvDh2HOVmW4Kg&expire=1587797054&filename=DOOM.Eternal.Deluxe.Edition.zip"
downloadFile = "http://download1583.mediafire.com/a40ljfnhtagg/0mxww72t6dwl0i8/Server.zip"
process = subprocess.Popen(["curl", "-s", "-L", "-I", downloadFile], stdout=subprocess.PIPE)
stdout = process.communicate()[0]
print 'STDOUT:{}'.format(stdout) 

character = stdout[stdout.lower().find('content-length: ') + 16:stdout.lower().find('content-length: ') + 17]
numberIndex = 1

#finds the content length and sets it to 'fileSize'
while str(character).isdigit() == True:
	character = stdout[stdout.lower().find('content-length: ') + 16:stdout.lower().find('content-length: ') + 16 + numberIndex]
	numberIndex += 1
fileSize = int(character)

print fileSize

startPacket = 0
endPacket = 10000000
repeatAmount = (fileSize / 10000000) + 1

for x in range(repeatAmount):
	if x == repeatAmount:
		endPacket = fileSize

	if x == 1:
		startPacket += 1

	os.system("curl -r " + str(startPacket) + "-" + str(endPacket) + " -o Block" + str(x) + ".bin " + downloadFile)
	startPacket += 10000000
	endPacket += 10000000


#os.system("curl -s -L -I https://antave.com/onewebmedia/Drive-By_Alpha_2.7.apk | gawk -v IGNORECASE=1 '/^Content-Length/ { print $2 }'");
