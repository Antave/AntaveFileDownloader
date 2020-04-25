import os
import subprocess

#initializes the variables
downloadFile = raw_input("Enter Download URL: ")
extension = raw_input("Enter Download Extension (ex: .zip, .png, .exe,): ")

#determines the size of the download
process = subprocess.Popen(["curl", "-L", "-I", downloadFile], stdout=subprocess.PIPE)
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

#initializes some variables
startPacket = 0
endPacket = 10000000
repeat = " & "
downloadCommand = "echo \"Starting Download\" & "
repeatAmount = (fileSize / 10000000) + 1

#repeats for all download streams
for x in range(repeatAmount):
	if x == repeatAmount - 1:
		endPacket = fileSize
		repeat = " & wait"

	if x == 1:
		startPacket += 1

	downloadCommand += "curl -r " + str(startPacket) + "-" + str(endPacket) + " -o Block" + str(x) + ".bin " + downloadFile + repeat
	startPacket += 10000000
	endPacket += 10000000

#executes download for all streams
os.system(downloadCommand)

#finishes up download and performs a checksum with existing files with same extension
os.system("cat Block*.bin > output" + extension)
os.system("echo \"Download Complete!\"")
os.system("rm Block*.bin")
os.system("cksum *" + extension)
