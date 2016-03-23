<h2>Display the times of low tide in your area, and only within your open schedule.</h2>

<hr />
<p>This is my quick solution to display the times of&nbsp;low tide so I know when I could bring my dog out for a walk on the beach. &nbsp;<a href="http://www.jaredlog.com/?p=2261" target="_blank"><span style="color: rgb(150, 152, 150); font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace; font-size: 12px; line-height: 16.8px; white-space: pre;">See my blog post about this.</span></a> &nbsp;Since I can go only&nbsp;in the morning or early evening,&nbsp;this script shows low tides&nbsp;only during these two windows&nbsp;of time.</p>

<p>Thanks to taxpayers&#39; money, NOAA provides annual daily&nbsp;predictions of tides at different spots&nbsp;across the country. &nbsp;You can download your local tides data in XML format at:&nbsp;<a href="http://tidesandcurrents.noaa.gov/tide_predictions.html" target="_blank"><span style="color: rgb(150, 152, 150); font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace; font-size: 12px; line-height: 16.8px; white-space: pre;">http://tidesandcurrents.noaa.gov/tide_predictions.html</span></a></p>

<p>Note: uses lxml and xpath for fast and simple XML processing / filtering</p>

<p>Set your available schedule in the script using 24H format.</p>

<p>My available schedule is 7am - 10:30am and 4:00pm - 7:30pm</p>

<table class="highlight tab-size js-file-line-container" data-tab-size="8" style="box-sizing: border-box; border-collapse: collapse; border-spacing: 0px; tab-size: 8; font-family: Helvetica, arial, nimbussansl, liberationsans, freesans, clean, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; line-height: 18.2px;">
	<tbody style="box-sizing: border-box;">
		<tr style="box-sizing: border-box;">
			<td class="blob-code blob-code-inner js-file-line" id="LC87" style="box-sizing: border-box; padding: 0px 10px; position: relative; vertical-align: top; overflow: visible; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace; font-size: 12px; word-wrap: normal; white-space: pre;">morning_start <span class="pl-k" style="box-sizing: border-box; color: rgb(167, 29, 93);">=</span> time(<span class="pl-c1" style="box-sizing: border-box; color: rgb(0, 134, 179);">7</span>,<span class="pl-c1" style="box-sizing: border-box; color: rgb(0, 134, 179);">0</span>,<span class="pl-c1" style="box-sizing: border-box; color: rgb(0, 134, 179);">0</span>)</td>
		</tr>
		<tr style="box-sizing: border-box;">
			<td class="blob-code blob-code-inner js-file-line" id="LC88" style="box-sizing: border-box; padding: 0px 10px; position: relative; vertical-align: top; overflow: visible; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace; font-size: 12px; word-wrap: normal; white-space: pre;">morning_end <span class="pl-k" style="box-sizing: border-box; color: rgb(167, 29, 93);">=</span> time(<span class="pl-c1" style="box-sizing: border-box; color: rgb(0, 134, 179);">10</span>,<span class="pl-c1" style="box-sizing: border-box; color: rgb(0, 134, 179);">30</span>,<span class="pl-c1" style="box-sizing: border-box; color: rgb(0, 134, 179);">0</span>)</td>
		</tr>
		<tr style="box-sizing: border-box;">
			<td class="blob-code blob-code-inner js-file-line" id="LC89" style="box-sizing: border-box; padding: 0px 10px; position: relative; vertical-align: top; overflow: visible; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace; font-size: 12px; word-wrap: normal; white-space: pre;">evening_start <span class="pl-k" style="box-sizing: border-box; color: rgb(167, 29, 93);">=</span> time(<span class="pl-c1" style="box-sizing: border-box; color: rgb(0, 134, 179);">16</span>,<span class="pl-c1" style="box-sizing: border-box; color: rgb(0, 134, 179);">0</span>,<span class="pl-c1" style="box-sizing: border-box; color: rgb(0, 134, 179);">0</span>)</td>
		</tr>
		<tr style="box-sizing: border-box;">
			<td class="blob-code blob-code-inner js-file-line" id="LC90" style="box-sizing: border-box; padding: 0px 10px; position: relative; vertical-align: top; overflow: visible; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace; font-size: 12px; word-wrap: normal; white-space: pre;">evening_end <span class="pl-k" style="box-sizing: border-box; color: rgb(167, 29, 93);">=</span> time(<span class="pl-c1" style="box-sizing: border-box; color: rgb(0, 134, 179);">19</span>,<span class="pl-c1" style="box-sizing: border-box; color: rgb(0, 134, 179);">30</span>,<span class="pl-c1" style="box-sizing: border-box; color: rgb(0, 134, 179);">0</span>)</td>
		</tr>
	</tbody>
</table>

<p>The script accepts an&nbsp;argument <span style="line-height: 20.8px;">&quot;days deltas&quot;&nbsp;</span>so you can ask for &#39;x&#39; number of days of tide predictions in advance that works within your open schedule.</p>

<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;">&gt; python3 tides.py -d 0 1 2 3 4 5 6 7<br />
Upcoming low tides within your available schedule:</div>

<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;">&nbsp; &nbsp;Today &nbsp;2016/03/22 &nbsp;08:03 AM &nbsp; 0.1<br />
Tomorrow &nbsp;2016/03/23 &nbsp;08:25 AM &nbsp; 0.2<br />
&nbsp; Future &nbsp;2016/03/24 &nbsp;08:46 AM &nbsp; 0.3<br />
&nbsp; Future &nbsp;2016/03/25 &nbsp;09:07 AM &nbsp; 0.4<br />
&nbsp; Future &nbsp;2016/03/26 &nbsp;09:29 AM &nbsp; 0.5<br />
&nbsp; Future &nbsp;2016/03/27 &nbsp;09:52 AM &nbsp; 0.6<br />
&nbsp; Future &nbsp;2016/03/28 &nbsp;10:17 AM &nbsp; 0.7</div>
