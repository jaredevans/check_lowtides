from flask import Flask
app = Flask(__name__)

import argparse
from lxml import etree
from datetime import datetime, time, date, timedelta

app.debug = True

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def get_tides(day_deltas, root, ms, me, es, ee):
  """Return low tides within morning/evening schedule"""
  lowtides = {}
  for day_delta in day_deltas:
    udate = datetime.now() + timedelta(days=day_delta)
    pdate = udate.strftime("%Y/%m/%d")
    #The xpath to filter xml for a specific date having low tide
    xpathstr=".//data/item[date='" + pdate + "'][highlow='L']"

    for item in root.findall(xpathstr):
      strtime = item.find('time').text
      vtime = datetime.strptime(strtime, '%I:%M %p')
      ptime = time(vtime.hour,vtime.minute,0)

      if time_in_range(ms, me, ptime) or time_in_range(es, ee, ptime) :
        strdate = item.find('date').text + " " + item.find('time').text
        vtimestamp = datetime.strptime(strdate , '%Y/%m/%d %I:%M %p')
        lowtides[vtimestamp] = {}
        if day_delta == 0:
          lowtides[vtimestamp]['day'] = "Today"
        elif day_delta == 1:
          lowtides[vtimestamp]['day'] = "Tomorrow"
        else:
          lowtides[vtimestamp]['day'] = "In " + str(day_delta) + " days"
        lowtides[vtimestamp]['date'] = item.find('date').text
        lowtides[vtimestamp]['time'] = item.find('time').text
        lowtides[vtimestamp]['prediction'] = item.find('predictions_in_ft').text

  return lowtides

def print_tides(day_deltas, root, ms, me, es, ee):
  """Output sorted list of low tides"""
  #Filter out low tides for today=0, tomorrow=1, and future=2,10
  data = ""
  tides = {}
  tides = get_tides(day_deltas, root, ms, me, es, ee)

  if len(tides) > 0 :
    prev_day = ""
    curr_day = ""
    data = "<p>Upcoming tides within your schedule:</p>"
    tides_sorted = iter(sorted(tides.items()))
    data = data + "<pre>"
    for k, v in tides_sorted:
      curr_day = v['day']
      if (prev_day == 'Today') and (curr_day == 'Tomorrow') :
         data = data + "<br>"
      data = data + "{: >8} {: >11} {: >9} {: >5}".format(v['day'], v['date'], v['time'], v['prediction']) + "<br>"
      prev_day = v['day']
    data = data + "</pre>"
  else:
    numdays = len(day_deltas)
    data = data + "No upcoming low tides within next " + str(numdays) + " days."
  return data


@app.route('/lowtides')
def index():
  ms, me, es, ee = ("6:00AM", "9:00AM", "4:00PM", "8:30PM")
  xmlFile = "tides.xml"

  vMorningStart = datetime.strptime(ms, '%I:%M%p')
  morning_start = time(vMorningStart.hour,vMorningStart.minute,0)

  vMorningEnd= datetime.strptime(me, '%I:%M%p')
  morning_end = time(vMorningEnd.hour,vMorningEnd.minute,0)

  vEveningStart = datetime.strptime(es, '%I:%M%p')
  evening_start = time(vEveningStart.hour,vEveningStart.minute,0)

  vEveningEnd= datetime.strptime(ee, '%I:%M%p')
  evening_end = time(vEveningEnd.hour,vEveningEnd.minute,0)

  #Read in the tides data
  tree = etree.parse(xmlFile)

  #Process the tides data
  root = tree.getroot()

  # Display the low tides within your schedule
  daydeltas = (0, 1, 2, 4)
  numdays = len (daydeltas)
  data = "Seeking low tides for the next " + str(numdays) + " days between <p> </p> morning times: " + ms + "-" + me + " <br> evening times: " + es + "-" + ee + "<p> </p>"
  data = data + print_tides(daydeltas, root, morning_start, morning_end, evening_start, evening_end)
  return data 

if __name__ == "__main__":
    app.run()
