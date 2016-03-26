#!/usr/bin/python3

#Get your annual local tides in xml format:
#http://tidesandcurrents.noaa.gov/tide_predictions.html

import argparse
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
  """Return low tides within morning/evening schedule"""
  lowtides = {}
  for day_delta in day_deltas:
    udate = datetime.now() + timedelta(days=day_delta)
    pdate = udate.strftime("%Y/%m/%d")

##### Custom select dates for troubleshooting, if necessary
#    if day_delta == 0 :
#      pdate="2016/01/22"
#    elif day_delta == 1 :
#      pdate="2016/01/23"
#    elif day_delta == 2 :
#      pdate="2016/01/24"
#    else:
#      pdate="2016/02/03"
#    print(pdate)

    #The xpath to filter xml for a specific date having low tide
    xpathstr=".//data/item[date='" + pdate + "'][highlow='L']"

    for item in root.findall(xpathstr):
      strtime = item.find('time').text
      vtime = datetime.strptime(strtime, '%I:%M %p')
      ptime = time(vtime.hour,vtime.minute,0)

      if time_in_range(morning_start, morning_end, ptime) or time_in_range(evening_start, evening_end, ptime) :
        strdate = item.find('date').text + " " + item.find('time').text
        vtimestamp = datetime.strptime(strdate , '%Y/%m/%d %I:%M %p')
        lowtides[vtimestamp] = {}
        if day_delta == 0:
          lowtides[vtimestamp]['day'] = "Today"
        elif day_delta == 1:
          lowtides[vtimestamp]['day'] = "Tomorrow"
        else:
          lowtides[vtimestamp]['day'] = "Future"
        lowtides[vtimestamp]['date'] = item.find('date').text
        lowtides[vtimestamp]['time'] = item.find('time').text
        lowtides[vtimestamp]['prediction'] = item.find('predictions_in_ft').text

  return lowtides

def print_tides(day_deltas):
  """Output sorted list of low tides"""
  #Filter out low tides for today=0, tomorrow=1, and future=2,10
  tides = {}
  tides = get_tides(day_deltas)

  if len(tides) > 0 :
    prev_day = ""
    curr_day = ""
    print("Upcoming low tides within your available schedule:")
    print (" ")
    # A dictionary doesn't guarantee a sorted order, so need to do this first
    tides_sorted = iter(sorted(tides.items()))
    for k, v in tides_sorted:
      #Prettify the output in aligned columns of text
      curr_day = v['day']
      if (prev_day == 'Today') and (curr_day == 'Tomorrow') :
        print(" ")
      print("{: >8} {: >11} {: >9} {: >5}".format(v['day'], v['date'], v['time'], v['prediction']))
      prev_day = v['day']
  else:
    print("No upcoming low tides within your available schedule.")
    print (" ")
  
  print (" ")

if __name__ == "__main__":
  """Run the script: ./tides.py -d 0 1 2 3"""
  parser = argparse.ArgumentParser(description="Get low tides for your available schedule")
  parser.add_argument("-d" , "--daydeltas", default=["replace this with your default values, 0 1 2 3 4"], metavar='N', type=int, nargs='+', help="Day deltas to process, i.e. 0 1 2 3 4")
  parser.add_argument("-xf" , "--xmlfile", default=["tides.xml"], nargs=1, help="Your local tides XML file")
  parser.add_argument("-ms" , "--morning_start", default=["7:00am"], nargs=1, help="Your morning start time.")
  parser.add_argument("-me" , "--morning_end", default=["10:30am"], nargs=1, help="Your morning end time.")
  parser.add_argument("-es" , "--evening_start", default=["4:00pm"], nargs=1, help="Your evening start time.")
  parser.add_argument("-ee" , "--evening_end", default=["8:30pm"], nargs=1, help="Your evening end time.")
  args = parser.parse_args()

  #Set your available schedule using 24H format
  vMorningStart = datetime.strptime(args.morning_start[0], '%I:%M%p')
  morning_start = time(vMorningStart.hour,vMorningStart.minute,0)

  vMorningEnd= datetime.strptime(args.morning_end[0], '%I:%M%p')
  morning_end = time(vMorningEnd.hour,vMorningEnd.minute,0)

  vEveningStart = datetime.strptime(args.evening_start[0], '%I:%M%p')
  evening_start = time(vEveningStart.hour,vEveningStart.minute,0)

  vEveningEnd= datetime.strptime(args.evening_end[0], '%I:%M%p')
  evening_end = time(vEveningEnd.hour,vEveningEnd.minute,0)

  xmlFile = args.xmlfile[0] 

  #Read in the tides data
  tree = etree.parse(xmlFile)

  #Process the tides data
  root = tree.getroot()

  # Display the low tides within your schedule
  print("Subject: Low Tides")
  print_tides(args.daydeltas)
