# REFERENCE : https://www.w3schools.com/python/python_datetime.asp
#           : https://www.tutorialspoint.com/python/time_strptime.htm
#           : https://www.tutorialspoint.com/python/time_strftime.htm


# TICKs
# function time.time() returns the current system time in ticks since 12:00am, January 1, 1970(epoch).

import time                            # This is required to include time module.
ticks = time.time()



# time.localtime([secs])
# To translate a time instant from a seconds since the epoch floating-point value into a time-tuple, with all nine items.

import time
waqt = time.localtime(time.time())     # If secs is not provided or None, the current time as returned by time.time() is used.
                                       # time.struct_time(tm_year=2013, tm_mon=7, tm_mday=17, tm_hour=21, tm_min=26, tm_sec=3, tm_wday=2, tm_yday=198, tm_isdst=0)
waqt[0]                                # 2013
waqt.tm_mon                            # 7



# time.asctime([tupletime])
# Accepts a time-tuple and returns a readable 24-character string

import time
localtime = time.asctime(time.localtime(time.time()))    # 'Wed May 15 11:32:45 2019'
            time.asctime()                               # If tuple is not provided or None, the current time-tuple as returned by time.time() is used.



# time.gmtime([secs])
# Accepts an instant expressed in seconds since the epoch and returns a time-tuple t with the UTC time. Note : t.tm_isdst is always 0

time.gmtime()                    # If secs is not provided or None, the current time as returned by time.time() is used.
time.gmtime(time.time())         # time.struct_time(tm_year=2019, tm_mon=5, tm_mday=15, tm_hour=7, tm_min=11, tm_sec=46, tm_wday=2, tm_yday=135, tm_isdst=0)



# time.mktime(tupletime)
# Accepts an instant expressed as a time-tuple in local time and returns a floating-point value with the instant expressed in seconds since the epoch.

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime(t)



# time.strftime(fmt[,tupletime])
# Accepts an instant expressed as a time-tuple by localtime() or gmtime() and returns a string representing the instant as specified by string fmt.
"""
%a	Weekday, short version	                      Wed	
%A	Weekday, full version	                        Wednesday	
%w	Weekday as a number 0-6, 0 is Monday	        2
%d	Day of month 01-31	                          31	
%b	Month name, short version	                    Dec	
%B	Month name, full version	                    December	
%m	Month as a number 01-12	                      12	
%y	Year, short version, without century	        18	
%Y	Year, full version	                          2018	
%H	Hour 00-23	                                  17	
%I	Hour 00-12	                                  05	
%p	AM/PM	                                        PM	
%M	Minute 00-59	                                41	
%S	Second 00-59	                                08	
%f	Microsecond 000000-999999	                    548513	
%z	UTC offset	                                  +0100	
%Z	Timezone	                                    CST	
%j	Day number of year 001-366	                  365		
%c	Local version of date and time	              Mon Dec 31 17:41:00 2018	
%x	Local version of date	                        12/31/18	
%X	Local version of time	                        17:41:00	
%%	A % character	                                %
"""
# 1
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

# 2
import time
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
print time.strftime("%b %d %Y %H:%M:%S", t)                     # Feb 17 2009 17:03:38



# time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
# Parses str according to format string fmt and returns the instant in time-tuple format.

import time
struct_time_tuple = time.strptime("30 Nov 00", "%d %b %y")       # (2000, 11, 30, 0, 0, 0, 3, 335, -1)



# time.sleep(secs)
# Suspends the calling thread for secs seconds.



# time.timezone
# offset in seconds of the local time zone (without DST) from UTC (>0 in the Americas; <=0 in most of Europe, Asia, Africa).
# OUTPUT : -19800



# time.tzname
# a pair of locale-dependent strings, which are the names of the local time zone without and with DST, respectively.
# OUTPUT : ('India Standard Time', 'India Daylight Time')



# CALENDAR module

# calendar.calendar(year,w=2,l=1,c=6)
# multiline string with a calendar for 'year' formatted into three columns separated by c spaces.
# w is the width in characters of each date; each line has length 21*w+18+2*c.
# l is the number of lines for each week.

import calendar
cal = calendar.calendar(2019)



# calendar.month(year,month,w=2,l=3)
# multiline string with calendar for 'month' of 'year'
# w is the width in characters of each date; each line has length 7*w+6.
# l is the number of lines for each week.

import calendar
cal = calendar.month(1995, 7)



# calendar.isleap(year)
# Returns True if year is a leap year; otherwise, False.



# calendar.leapdays(y1,y2)
# Returns the total number of leap days in the years within range(y1,y2) ie y2 is not included



# calendar.firstweekday()                  # 0 (Monday) to 6 (Sunday)



# calendar.setfirstweekday([CODE])         # 0 (Monday) to 6 (Sunday)

