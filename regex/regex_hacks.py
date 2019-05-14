
# Multiple conditions to be checked and we are not given how pattern should start, 
# > use 're.search()' and 'multiple regular expressions' with '&&' condition
  
  
  
  
# Checking of repetitions in a pattern

# 1                     # no character should repeat
reg = r"(.).*\1"


# 2                     # not have even 'one' group of 4 or more CONSECUTIVE repeated digits, separotor (-) ignored
reg = r"([0-9])-?\1-?\1-?\1"


# 3                     # not contain more than 'one' ALTERNATING REPETITIVE digit pair.
                        # use of lookaround to avoid next character being captured in match as we can have 'one' pair but not more
                        # if used   reg = r"([0-9])[0-9]\1"   without lookaround, it will not give desired result on '110000' as only 'one' pair found but 'two' exists 
reg = r"([0-9])(?=[0-9]\1)"
len(re.findall(reg, str)) < 2


