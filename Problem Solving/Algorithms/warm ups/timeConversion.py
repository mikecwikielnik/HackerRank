import datetime     # hi! so important! 

def timeConversion(s):
   t=datetime.datetime.strptime(s, "%I:%M:%S%p")
   return datetime.datetime.strftime(t, "%H:%M:%S")