#!/usr/bin/python3
from lxml import etree
import pprint
from datetime import datetime, time, date, timedelta

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def get_tides(day_deltas):
  lowtides = {}
  for day_delta in day_deltas:
    udate = datetime.now() + timedelta(days=day_delta)
    pdate = udate.strftime("%Y/%m/%d")

##### Code for troubleshooting dates
#    if day_delta == 0 :
#      pdate="2016/01/22"
#    elif day_delta == 1 :
#      pdate="2016/01/23"
#    elif day_delta == 2 :
#      pdate="2016/01/24"
#    else:
#      pdate="2016/02/03"
#    print(pdate)

    xpathstr=".//data/item[date='" + pdate + "'][highlow='L']"

    for i in root.findall(xpathstr):
      itime = i.find('time').text
      t = datetime.strptime(itime, '%I:%M %p')
      ptime = time(t.hour,t.minute,0)

      if time_in_range(morning_start, morning_end, ptime) or time_in_range(evening_start, evening_end, ptime) :
        dt = i.find('date').text + " " + i.find('time').text
        timestamp = datetime.strptime(dt , '%Y/%m/%d %I:%M %p')
        lowtides[timestamp] = {}
        if day_delta == 0:
          lowtides[timestamp]['tt'] = "Today"
        elif day_delta == 1:
          lowtides[timestamp]['tt'] = "Tomorrow"
        else:
          lowtides[timestamp]['tt'] = "Future"
        lowtides[timestamp]['date'] = i.find('date').text
        lowtides[timestamp]['time'] = i.find('time').text
        lowtides[timestamp]['pred'] = i.find('predictions_in_ft').text

  return lowtides


#Set your available schedule using 24H format
morning_start = time(7,0,0)
morning_end = time(10,30,0)
evening_start = time(16,0,0)
evening_end = time(19,30,0)

#Read in the tides data
tree = etree.parse('tides.xml')

#Process the tides
root = tree.getroot()

#Filter out low tides for today=0, tomorrow=1, and future=2,10
day_deltas=[0,1,2,5]
tides = {}
tides = get_tides(day_deltas)

if len(tides) > 0 :
  print("Upcoming low tides within your available schedule:")
  print (" ")
  # A dictionary doesn't guarantee a sorted order, so need to do this first
  tides_sorted = iter(sorted(tides.items()))
  for k, v in tides_sorted:
    #Prettify the output in aligned columns of text
    print("{: >8} {: >11} {: >9} {: >5}".format(v['tt'], v['date'], v['time'], v['pred']))
else:
  print("No upcoming low tides within your available schedule.")
  print (" ")

print (" ")
