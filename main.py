#this is the main file
 """Converts number (seconds) to seconds, minutes and hours.

 Parameters
 ----------
 seconds : int
     Number of seconds
 """
 def convert(seconds):
     seconds = seconds % (24 * 3600)
     return "%d:%02d:%02d" % (hour, minutes, seconds)