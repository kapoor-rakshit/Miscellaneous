import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    single=['one','two','three',"four","five",'six','seven','eight','nine','ten',"eleven","twelve"]
    tn=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    dn=["ten","twenty"]
    
    hr = single[h-1]     #h%12
    mr=""
    if m>30:
        diff = 60-m
        if diff==15:
            mr="quarter"
        odg=diff%10
        diff//=10
        tdg=diff%10
        if tdg==1 and odg!=5 and odg!=0:
            mr=tn[odg-1]
        elif tdg==1 and odg==0:
            mr="ten"
        elif tdg==0:
            mr=single[odg-1]
        elif tdg==2 and odg!=0:
            mr=dn[1]+" "+single[odg-1]
        elif tdg==2 and odg==0:
            mr="twenty"
        if mr=="one":
            return mr+" minute to "+single[h%12]
        elif mr=="quarter":
            return mr+" to "+single[h%12]
        else:
            return mr+" minutes to "+single[h%12]
    else:
        if m==15:
            mr="quarter"
        if m==0:
            mr="o' clock"
        odg=m%10
        m//=10
        tdg=m%10
        if tdg==1 and odg!=5 and odg!=0:
            mr=tn[odg-1]
        elif tdg==1 and odg==0:
            mr="ten"
        elif tdg==0 and odg!=0:
            mr=single[odg-1]
        elif tdg==2 and odg!=0:
            mr=dn[1]+" "+single[odg-1]
        elif tdg==2 and odg==0:
            mr="twenty"
        elif tdg==3:
            mr="half"
        if mr=="one":
            return mr+" minute past "+hr
        elif mr=="quarter":
            return mr+" past "+hr
        elif mr=="o' clock":
            return hr+" "+mr
        elif mr=="half":
            return mr+" past "+hr
        else:
            return mr+" minutes past "+hr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
    
    
