<div class="mw-parser-output"><table style="padding:0.3em; float:right; margin-left:15px; border:1px solid #A3B1BF; background:#f5faff; text-align:center; font-size:95%; line-height:1.5em;">
<tbody><tr>
<th style="background:#cee0f2; padding:0.3em; text-align:center;">Navigation
</th></tr>
<tr>
<td><a href="/ittc_wiki/index.php/EECS268" title="EECS268">Home</a>
</td></tr>
<tr>
<td style="padding:0.1em; font-size:0.9em; background-color:#cee0f2;">Information
</td></tr>
<tr>
<td>
<p><a href="/ittc_wiki/index.php/EECS268:Syllabus" title="EECS268:Syllabus">Syllabus</a><br>
<a href="/ittc_wiki/index.php/EECS268:Schedule" title="EECS268:Schedule">Schedule</a><br>
<a href="/ittc_wiki/index.php/EECS268:video-lectures" title="EECS268:video-lectures">Lecture Archive</a><br>
</p>
</td></tr>
<tr>
<td style="padding:0.1em; font-size:0.9em; background-color:#cee0f2;">Classwork
</td></tr>
<tr>
<td>
<p><a href="/ittc_wiki/index.php/EECS268:Labs" title="EECS268:Labs">Labs</a><br>
<a href="/ittc_wiki/index.php/EECS268:Submission" title="EECS268:Submission">Submitting Work</a><br>
</p>
</td></tr></tbody></table>
<p><br>
</p>
<div id="toc" class="toc"><div class="toctitle"><h2>Contents</h2><span class="toctoggle">&nbsp;[<a role="button" tabindex="0" class="togglelink">hide</a>]&nbsp;</span></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#Due_time"><span class="tocnumber">1</span> <span class="toctext">Due time</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#Lab_conduct"><span class="tocnumber">2</span> <span class="toctext">Lab conduct</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#Overview"><span class="tocnumber">3</span> <span class="toctext">Overview</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#Timing_a_block_of_code"><span class="tocnumber">4</span> <span class="toctext">Timing a block of code</span></a></li>
<li class="toclevel-1 tocsection-5"><a href="#Requirements"><span class="tocnumber">5</span> <span class="toctext">Requirements</span></a>
<ul>
<li class="toclevel-2 tocsection-6"><a href="#Data_sets"><span class="tocnumber">5.1</span> <span class="toctext">Data sets</span></a></li>
<li class="toclevel-2 tocsection-7"><a href="#Operations_to_time"><span class="tocnumber">5.2</span> <span class="toctext">Operations to time</span></a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-8"><a href="#Plotting"><span class="tocnumber">6</span> <span class="toctext">Plotting</span></a></li>
<li class="toclevel-1 tocsection-9"><a href="#Rubric"><span class="tocnumber">7</span> <span class="toctext">Rubric</span></a></li>
<li class="toclevel-1 tocsection-10"><a href="#Submission_instructions"><span class="tocnumber">8</span> <span class="toctext">Submission instructions</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="Due_time">Due time</span></h2>
<p>This lab is due one week from the start of your lab.
</p>
<h2><span class="mw-headline" id="Lab_conduct">Lab conduct</span></h2>
<ul><li>Do not use any unauthorized aid, such sites like rentacoder or chegg to obtain answers</li>
<li>Do not use code provided by another student</li>
<li>Do not reuse code (by you or anyone) from prior semesters</li>
<li>If you need help, seek it from:
<ul><li>Your lab TA.</li>
<li>ACM Tutoring</li>
<li>Me, Dr. Gibbons, my email is jwgibbo@ku.edu / jwgibbo@gmail.com</li></ul></li>
<li>If equipment you don't own (e.g. cycle servers) needs attention or you're having account issues put in a <a rel="nofollow" class="external text" href="https://tsc.ku.edu/request-support-engineering-tsc">ticket!</a></li></ul>
<p><br>
</p>
<h2><span class="mw-headline" id="Overview">Overview</span></h2>
<p>In this lab we will time various methods from the data structures we've made so far, save those times, and plot them to see if they match the theoretical expectations.
</p>
<h2><span class="mw-headline" id="Timing_a_block_of_code">Timing a block of code</span></h2>
<p>To handle the timing we'll be wanting to track the time our process spent in the CPU (as oppose to clock-on-the-wall time).
</p><p>Luckily, python's time module can easily help with this. But you should know that the timing code will perform different on different platforms. If you're running the timing code on linux use <b>time.process_time_ns()</b> but if you're running the timing code on Windows use <b>time.perf_counter_ns()</b>. Just note that perf_counter_ns is "clock on the wall time" but it's currently the best built-in option for Windows.  
</p><p>Here's an example of timing a loop that has one-hundred million iterations.
</p>
<pre>import time

def nanosec_to_sec(ns):
    BILLION = 1000000000
    return ns/BILLION

print("Beginning the timing code...")
num_iterations = 100000000 #one hundred million
start_time = time.process_time_ns() #Remember to use perf_counter_ns if running on windows

#loop that does nothing but repeat, hence the _ variable and the keyword pass
#which just means do nothing
for _ in range(num_iterations):
    pass

end_time = time.process_time_ns()

print("Total time in ns: ", end_time-start_time)
print("Total time in sec: ", nanosec_to_sec(end_time-start_time))
</pre>
<p>Notes on time.process_time_ns():
</p>
<ul><li> It returns an int that represents the current number of nanosecond the process has spent in the CPU</li>
<li> If you want seconds, you'll need to convert it, like I did in the example</li></ul>
<h2><span class="mw-headline" id="Requirements">Requirements</span></h2>
<p>You will time several methods from Stacks, Queues, and Lists using several values for n (size of the data structure)
</p>
<h3><span class="mw-headline" id="Data_sets">Data sets</span></h3>
<p>You will fill each data structure with an increasing number of elements and record a time for each.  For each method, start with a data size of 1000 then increase by 1000, recording another time, and repeat until you've reached 100,000 elements
</p><p>For example. Let's say I want to time Pop for a Stack. I would do the following:
</p>
<ol><li>Fill a stack with 1000 elements</li>
<li>Record time to perform a single pop with that size stack</li>
<li>Fill a stack with 2000 elements</li>
<li>Record a time to perform a single pop with that size stack</li>
<li>Repeat these steps, increasing the size by 1000 each time until I've recorded a time for a stack with 100,000 elements in it</li></ol>
<h3><span class="mw-headline" id="Operations_to_time">Operations to time</span></h3>
<table class="wikitable">

<tbody><tr>
<th> Operation
</th></tr>
<tr>
<td> Popping a single item from a stack
</td></tr>
<tr>
<td> Popping all items from a stack
</td></tr>
<tr>
<td> Queue's enqueue
</td></tr>
<tr>
<td> Linked List get_entry at specifically index 0
</td></tr>
<tr>
<td> Linked List get_entry at specifically the last index
</td></tr>
<tr>
<td> Printing all elements in a LinkedList using get_entry
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Plotting">Plotting</span></h2>
<p>In addition to your code, you will submit graphs (e.g. excel graphs) of the data you've collected. One graph for each operation. You're not required to generate the graphs with python; only collect the data with python.
</p>
<h2><span class="mw-headline" id="Rubric">Rubric</span></h2>
<ul><li>[10pts] Attendance</li>
<li>[10pts] No crashing or unhandled exceptions</li>
<li>[5pts] Code design (no giant mains!)</li>
<li>[5pts] Documentation</li>
<li>[10pts] Pop single item data</li>
<li>[10pts] Pop all items data</li>
<li>[10pts] Enqueue data</li>
<li>[10pts] get_entry at index 0 data</li>
<li>[15pts] get_entry at last index data</li>
<li>[15pts] printing entire list using get_entry data</li></ul>
<h2><span class="mw-headline" id="Submission_instructions">Submission instructions</span></h2>
<p>Send a tarball/zip with all .py files and plots (e.g. excel file)
</p>
<!-- 
NewPP limit report
Cached time: 20221022162655
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.026 seconds
Real time usage: 0.031 seconds
Preprocessor visited node count: 56/1000000
Preprocessor generated node count: 86/1000000
Post‐expand include size: 621/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    2.954      1 -total
100.00%    2.954      1 Template:EECS268
-->
</div>
<!-- Saved in parser cache with key wikidb-ittc_:pcache:idhash:2897-0!canonical and timestamp 20221022162655 and revision id 24037
 -->
