
# REFERENCE : https://www.geeksforgeeks.org/python-strings-encode-method/
#           : https://www.geeksforgeeks.org/python-strings-decode-method/


# encode()
# encodes strings with the specified encoded scheme
# encoding :  Specifies the encoding to be performed.
# error    :  Decides how to handle the errors if they occur, e.g ‘strict’ raises Unicode error in case of exception and 
#            ‘ignore’ ignores the errors occurred.

from encodings.aliases import aliases
import base64

# 1
for k,v in aliases.items():
	print(k,v)


# 2
strval = "geeksforgeeks"
encstrval = base64.b64encode(strval.encode(encoding='utf8', errors='strict'))
print(encstrval)



# decode()
# accepts the encoding of the encoding string to decode it and returns the original string.
# encoding :  Specifies the encoding on the basis of which decoding has to be performed.
# error    :  Decides how to handle the errors if they occur, e.g ‘strict’ raises Unicode error in case of exception and 
#            ‘ignore’ ignores the errors occurred.

# 3
print(base64.b64decode(encstrval.decode(encoding='utf8', errors='strict')))

