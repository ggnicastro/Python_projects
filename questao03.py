__author__ = 'kaihami'
#date = raw_input("Inform the date in day, Hours:min:seconds ")
date = "1, 0:0:0"
day = date.split(",")
day2sec = int(day[0])*24*60*60
hour_min_sec = str(day[1]).split(":")
hour2sec = int(hour_min_sec[0])*60*60
min2sec = int(hour_min_sec[1])*60
sec2sec = int(hour_min_sec[2])
totalsec = day2sec + hour2sec + min2sec + sec2sec
print "The total time in second is", totalsec