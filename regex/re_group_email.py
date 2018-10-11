import re

s = "kapoor_rakshit@yahoo.co.in"
s2 = "adhish.kapoor@yahoo.co.in"
s3 = "rakshitk.ec.14@nitj.ac.in"
s4 = "rakshit.kapoor2@wipro.com"
s5 = "kapoor-rakshit@github-app.co.us"
s6 = "kapoor@gmail.com"
s7 = "kop@.in"                       # INVALID test-case

reg_pattern = r"(\w+.*)@(\w+.*)\.(\w+.*)"

m = re.match(reg_pattern , s7)       # re.match() expression only matches at the beginning of the string. 

                                     # group()
print("EMAIL ID :" , m.group(0))     # The entire match 
print("USERNAME :" , m.group(1))     # The first parenthesized subgroup.
print("WEBSITE :" , m.group(2))      # The second parenthesized subgroup.
print("DOMAIN :" , m.group(3))       # The third parenthesized subgroup.

print("USERNAME and WEBSITE :" , m.group(1,2))   # Multiple arguments give us a tuple.


print()

                                     # groups()
print(m.groups() if m else -1)       # returns a tuple containing all the subgroups of the match.


print()

                                    # groupdict()
                                    # a dictionary containing all the named subgroups of the match, keyed by the subgroup name
                                    
reg_patterndict = r"(?P<username>\w+.*)@(?P<website>\w+.*)\.(?P<domain>\w+.*)"

mdict = re.match(reg_patterndict, s5)

print(mdict.groupdict())             