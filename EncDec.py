import pyAesCrypt
import os
import getpass
from os import stat, remove
bufferSize = 64*1024

def encrypt(infile,password):
	with open(infile, 'rb') as fin:
		with open(infile+'.enc','wb') as fout:
				pyAesCrypt.encryptStream(fin,fout,password,bufferSize)
				os.remove(infile)
			
def decrypt(infile,password):
	with open(infile,'rb') as fin:
		encfilesize = stat(infile).st_size
		with open(infile[:-4],'wb') as fout:
				try:
					pyAesCrypt.decryptStream(fin,fout,password,bufferSize,encfilesize)
					os.remove(infile)
					print('Done')
				except ValueError:
					remove(infile[:-4])
					print('Wrong password.....?')
				
def main():
	choice = input('would u like to (E)encrypt or (D)decrypt: ')
	if choice == 'E':
		infile = input('enter file name: ')
		password = getpass.getpass('password: ')
		encrypt(infile,password)
		print('Done')
		
	elif choice == 'D':
		infile = input('enter file name: ')
		password = getpass.getpass('password: ')
		decrypt(infile,password)
	
if __name__ == '__main__':
	main()
