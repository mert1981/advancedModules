from datetime import datetime 
import locale 

locale.setlocale(locale.LC_ALL,"") #we make our location our current location by typing

now = datetime.now() #prints the current time. 
# now.year we can get the year information by typing.Month,hour

better_now = datetime.ctime(now) #Prints the current time better.

strftime_func = datetime.strftime(now,"%B %Y") #We can also get the data we want by typing the year, month, hour.

second = datetime.timestamp(now) #Converts the current time to seconds

convert_second = datetime.fromtimestamp(second) #Converts seconds to current time


date = datetime(2020,5,17)
difference = now - date #finds the difference between the given date and the current date