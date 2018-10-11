
# Reference : https://pythonprogramming.net/regular-expressions-regex-tutorial-python-3/
#           : https://www.regular-expressions.info/lookaround.html

"""
Identifiers:
\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter
\W = anything but a letter
.  = any character, except for a new line
\b = space around whole words
\. = period.    NOTE : Mind use of \(backslash), because . normally means any character.
[] = range, or "variance" , of values written in it

NOTE:
^regex_pattern$ =  use ^ and $ for match at start and end respectively 


Modifiers:
+     = match 1 or MORE repetitions of PRECEEDING
?     = match 0 or 1 repetitions.
*     = match 0 or MORE repetitions
$     = matches at the end of string, eg:- r"123$"  --> 12345..123
^     = matches start of a string,    eg:- r"^123"  --> 123..45123
|     = matches either/or. Example x|y = will match either x or y
[^]   = negated character class [^] matches any character not in square brackets, eg:- [^\d] (No digit match) [^0-9]
[a-z] = hyphen (-) inside a character class specifies a range of characters to match, eg:- [1-5a-qA-Z]


{x}   = returns exactly x consecutive chars anywhere in word(s) of string
{x,}  = returns x or more consecutive chars anywhere in word(s) of string
{x,y} = returns at least x but no more than y consecutive chars anywhere in word(s) of string
  eg :- r"^[a-zA-Z]{40}[0-9]{5}$"  -->  first(used ^) 40 chars alphabets and last(used $) 5 digits

# NOTE : 
# Above will give x chars from a string which is more than x length, along with exact x len
# to get away from these issues use LOOKAROUND
#    Lookahead to match something not-followed / followed by something else
#                          Negative : (?!text) / Positive : (?=u)
#
#    Lookbehind to match something not-preceeded / preceeded by something else
#                          Negative : (?<!text) / Positive : (?<=text)


White Space Charts:
\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = carriage return


re.match  : attempts to match a pattern at the beginning of the string.
re.search : attempts to match the pattern throughout the string until it finds a match
"""



# EXAMPLE : 1
# LOOKAROUND usage
import re

p = "we are here. who 20024024 789 890 9025 raghj))@$)@$"

print(re.findall(r'[A-Za-z]{3,4}',p))

print(re.findall(r'(?<!\d)\d{4}(?!\d)',p))         # returns word with exactly {4} digits



# EXAMPLE : 2
# CHECK for valid DECIMAL values
import re

n = int(input())

while n:
    k = input()
    reg = r"^[+-]?\d*\.\d+$"                      # Number can start with +, - or . symbol , must contain at least 1 decimal value.
    print(bool(re.match(reg, k)))                 # NOTE : use of ^ $
    n=n-1

