<h2>Display the times of low tide in your area, and only within your open schedule.</h2>

<hr />
<p>Updated: included the Flask web app version.</p>
<p>This is my quick solution to display the times of&nbsp;low tide so I know when I could bring my dog out for a walk on the beach. &nbsp;<a href="http://www.jaredlog.com/?p=2261" target="_blank"><span style="color: rgb(150, 152, 150); font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace; font-size: 12px; line-height: 16.8px; white-space: pre;">See my blog post about this.</span></a> &nbsp;Since I can go only&nbsp;in the morning or early evening,&nbsp;this script shows low tides&nbsp;only during these two windows&nbsp;of time.</p>

<p>Thanks to taxpayers&#39; money, NOAA provides annual daily&nbsp;predictions of tides at different spots&nbsp;across the country. &nbsp;You can download your local tides data in XML format at:&nbsp;<a href="http://tidesandcurrents.noaa.gov/tide_predictions.html" target="_blank"><span style="color: rgb(150, 152, 150); font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace; font-size: 12px; line-height: 16.8px; white-space: pre;">http://tidesandcurrents.noaa.gov/tide_predictions.html</span></a></p>

<p>Note: lxml and xpath is used&nbsp;for fast and simple XML processing / filtering</p>
<p><pre>If using Ubuntu: sudo apt-get install python3-lxml</pre></p>

<p>Set your available schedule using the morning/evenings start/end arguments.</p>

<p><span style="line-height: 1.6;">The script accepts an&nbsp;argument </span><span style="line-height: 20.8px;">--daydeltas&nbsp;</span><span style="line-height: 1.6;">so you can receive &#39;x&#39; number of days worth of tide predictions that are within your open schedule.</span></p>

<pre>
tides.py -xf tides.xml -d 0 1 2 -ms 7:00am -me 10:30am -es 4:00pm -ee 8:30pm

Subject: Low Tides
Upcoming low tides within your available schedule:

<p>&nbsp; &nbsp; &nbsp; Today &nbsp;&nbsp;2016/03/26 &nbsp;09:29 AM &nbsp; 0.5</p>
Tomorrow &nbsp;2016/03/27 &nbsp;09:52 AM &nbsp; 0.6
Future &nbsp; &nbsp; 2016/03/28 &nbsp;10:17 AM &nbsp; 0.7
</pre>

<hr/>
<pre>
python3 tides.py -h
usage: tides.py [-h] [-d N [N ...]] [-xf XMLFILE] [-ms MORNING_START]
                [-me MORNING_END] [-es EVENING_START] [-ee EVENING_END]

Get low tides for your available schedule

optional arguments:
  -h, --help            show this help message and exit
  -d N [N ...], --daydeltas N [N ...]
                        Day deltas to process, i.e. 0 1 2 3 4
  -xf XMLFILE, --xmlfile XMLFILE
                        Your local tides XML file
  -ms MORNING_START, --morning_start MORNING_START
                        Your morning start time.
  -me MORNING_END, --morning_end MORNING_END
                        Your morning end time.
  -es EVENING_START, --evening_start EVENING_START
                        Your evening start time.
  -ee EVENING_END, --evening_end EVENING_END
                        Your evening end time.
</pre>
