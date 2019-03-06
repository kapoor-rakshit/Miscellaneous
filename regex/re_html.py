
# EXAMPLE 1
# detect various tags used in an HTML document

import re

reg = r"(?i)<\s*(\w+).*?>"       # NOTE : the plus, the star and the repetition using curly braces are greedy.
                                 #        That is, the plus, the star and the repetition using curly braces causes the regex engine to repeat the preceding token as often as possible. 
                                 #        Only if that causes the entire regex to fail, will the regex engine backtrack. 
                                 #        That is, it will go back to the plus, the star and the repetition using curly braces, 
                                 #        make it give up the last iteration, and proceed with the remainder of the regex.
                                 #        fix is to make the plus, the star and the repetition using curly braces lazy instead of greedy. 
                                 # Lazy quantifiers are sometimes also called "ungreedy" or "reluctant". Eg: use of '?'
                                 # if not used ?, it will not match '<p>' tag in example : <a><p></p></a> but only '<a>'

n = int(input())
ans = []
while n:
    a = input()
    l = re.findall(reg, a)
    ans.extend(l)
    n-=1

print(*sorted(set(ans)), sep=";")



# EXAMPLE 2
# 
