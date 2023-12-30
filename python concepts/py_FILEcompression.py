import gzip

testtxt = b"Testing file compression for WIPROPJP yeah thats true"

print(len(testtxt))

with gzip.open('compressedfile.gz','wb') as fileptr:
	fileptr.write(testtxt)

with gzip.open('compressedfile.gz','rb') as fileptr:
	print(fileptr.read())

print(len(open("compressedfile.gz",'rb').read()))



# how to GZIP compress an existing file:

import gzip
import shutil
with open('/home/joe/file.txt', 'rb') as f_in:
    with gzip.open('/home/joe/file.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)