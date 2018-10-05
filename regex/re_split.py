
""" The re.split() expression splits the string by occurrence of a pattern. """


import re

s = "1,000,000.00"

reg_pattern = r"[.,]"                        # split the string on every occurrence of a dot and on every occurrence of a comma

print("\n".join(re.split(reg_pattern , s)))