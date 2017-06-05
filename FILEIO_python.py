import os
#Using Python's built-in open('filename','accessmode','buffering') function. This function creates a file object
#w+ opens for read and write mode but overwrites existing file and creates if not exists
#r+ opens for read and write
fileptr=open('test.txt',"w+")

"""Once a file is opened and you have one file object.
file.closed	    Returns true if file is closed, false otherwise.
file.mode	    Returns access mode with which file was opened.
file.name	    Returns name of the file.
file.softspace	Returns false if space explicitly required with print, true otherwise."""
print(fileptr.closed)
print(fileptr.mode)
print(fileptr.softspace)
print(fileptr.name)

"""The write() method writes any string to an open file. 
It is important to note that Python strings can have binary data and not just text.
The write() method does not add a newline character ('\n') to the end of the string"""
a="Hello this is my python.\nMy file handling\nusing Python3\n"
fileptr.write(a)
a="Check to overwrite or will continue\n\nGreat it continues to append untill fileptr is closed\n"
fileptr.write(a)

"""The read() method reads a string from an open file. 
It is important to note that Python strings can have binary data. apart from text data.
Here, passed parameter is the number of bytes to be read from the opened file. 
This method starts reading from the beginning of the file and if count exceeds,then it reads until the end of file.

The tell() method tells you the current position within the file; ie. the next read or write will occur at that many bytes from the beginning of the file.
The seek(offset,from) method changes the current file position. 
The offset argument indicates the number of bytes to be moved. 
The from argument specifies the reference position from where the bytes are to be moved.
If from is set to 0, it means use the beginning of the file as the reference position and 
1 means use the current position as the reference position and 
if it is set to 2 then the end of the file would be taken as the reference position."""
fileptr.seek(0,0)
position=fileptr.tell()
print("Start reading from position:",position)
st=fileptr.read(26)
print(st)

"""Python automatically closes a file when the reference object of a file is reassigned to another file. 
It is a good practice to use the close() method to close a file."""
fileptr.close()
print(fileptr.closed)

#get words in a newline, from a file which are ending with <anything here>
for line in open("testfile.txt"):
	for word in line.split():
		if word.endswith("ion"):
			print(word)

#Some Py hacks
os.rename('test.py','flasktest.py')    #rename(currentname,newname)
print(os.getcwd())                     #get_current_working _directory
os.remove('abc.text')                  #deletes a file
os.mkdir("newfolder")                  #new directory created
os.rmdir("newfolder")                  #deletes the directory.Before removing a directory,all the contents in it should be removed.
os.chdir("/home/newfolder")            #moves to specified directory and make it current dirctory 
