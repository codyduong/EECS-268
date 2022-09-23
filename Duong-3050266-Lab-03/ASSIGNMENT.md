<table style="padding:0.3em; float:right; margin-left:15px; border:1px solid #A3B1BF; background:#f5faff; text-align:center; font-size:95%; line-height:1.5em;">
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
<li class="toclevel-1 tocsection-2"><a href="#Overview"><span class="tocnumber">2</span> <span class="toctext">Overview</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#Create_and_Test_a_Linked_List"><span class="tocnumber">3</span> <span class="toctext">Create and Test a Linked List</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#Web_Browser_History"><span class="tocnumber">4</span> <span class="toctext">Web Browser History</span></a>
<ul>
<li class="toclevel-2 tocsection-5"><a href="#Reading_the_history_from_file"><span class="tocnumber">4.1</span> <span class="toctext">Reading the history from file</span></a></li>
<li class="toclevel-2 tocsection-6"><a href="#Sample_input_file"><span class="tocnumber">4.2</span> <span class="toctext">Sample input file</span></a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-7"><a href="#Linked_List_requirements"><span class="tocnumber">5</span> <span class="toctext">Linked List requirements</span></a></li>
<li class="toclevel-1 tocsection-8"><a href="#Rubric"><span class="tocnumber">6</span> <span class="toctext">Rubric</span></a></li>
<li class="toclevel-1 tocsection-9"><a href="#Submission_instructions"><span class="tocnumber">7</span> <span class="toctext">Submission instructions</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="Due_time">Due time</span></h2>
<p>This lab is due 1 week from the start of your lab.
</p>
<h2><span class="mw-headline" id="Overview">Overview</span></h2>
<p>I recommend doing this lab in two phases.  First, create and test an implementation of a List.  Second, make an implementation of the Browser, using your LinkedList.
</p>
<h2><span class="mw-headline" id="Create_and_Test_a_Linked_List">Create and Test a Linked List</span></h2>
<p>Make sure to...
</p>
<ol><li> Test each method as you go along</li>
<li> Run your code VERY often (if you write even a simple method, run it and test!)</li>
<li> I recommend writing a helper class to help speed up tests (e.g. a class that automates populating a LinkedList with value</li>
<li> Use the IDLE debugger
<ul><li> The debugger can show you exactly what is happening with your list and help track down reasons for errors or exceptions</li></ul></li></ol>
<p>What not to do...
</p>
<ul><li> Skip testing to try to save time (it doesn't save time in the long run)</li>
<li> Code an entire class or the entire lab before running for the first time</li></ul>
<p>Here's a listing (pun intended) of the methods your LinkedList will have:
</p>
<table class="wikitable">

<tbody><tr>
<th>Method </th>
<th> Description
</th></tr>
<tr>
<td>__init__(self) </td>
<td> Initialize list
</td></tr>
<tr>
<td>length(self) </td>
<td> Return length of the list
</td></tr>
<tr>
<td>insert(self, index, entry) </td>
<td> Insert the entry at the index. Valid indices range from 0 to length inclusively. Inserting at index=0 inserts at the front. Inserting at index=length adds to the back. Each insert increases the length by 1.
</td></tr>
<tr>
<td>remove(self, index) </td>
<td> Removes the entry at the index. Valid indices range from 0 to length-1 inclusively. Each remove decreases the length by 1.
</td></tr>
<tr>
<td>get_entry(self, index) </td>
<td> Return the entry at index, raises a RuntimeError otherwise.
</td></tr>
<tr>
<td>set_entry(self, index, entry) </td>
<td> Sets the entry at index, raises a RuntimeError otherwise. Even if successful, the length remains the same.
</td></tr>
<tr>
<td>clear(self) </td>
<td> Empties the list
</td></tr>
</tbody></table>
<h2><span class="mw-headline" id="Web_Browser_History">Web Browser History</span></h2>
<p>You will create a class that mimics the behavior of your web browser's back button, forward button, and address bar.
</p><p>Here is a listing of methods for the Browser class. 
</p><p>This class can then be used by an Executive class.
</p>
<table class="wikitable">

<tbody><tr>
<th>Method </th>
<th> Description
</th></tr>
<tr>
<td>__init__(self) </td>
<td> Initialize Browser
</td></tr>
<tr>
<td>navigate_to(self, url) </td>
<td> The browser navigate to the given url
</td></tr>
<tr>
<td>forward(self) </td>
<td> If possible, the browser navigates forward in the history otherwise it keeps focus
</td></tr>
<tr>
<td>back(self) </td>
<td> If possible, the browser navigates backwards in the history otherwise it keeps focus
</td></tr>
<tr>
<td>history(self) </td>
<td> Returns a well formatted string (see below) with the current history.
</td></tr>
</tbody></table>
<p><br>
</p>
<h3><span class="mw-headline" id="Reading_the_history_from_file">Reading the history from file</span></h3>
<p>To build up your browser history, you will read in from file. The file name will come in on the command line.  
</p><p>Any given line of the file will contain one of the following entries:
</p>
<table class="wikitable">
<tbody><tr>
<th> File Entry </th>
<th> Description
</th></tr>
<tr>
<td> NAVIGATE &lt;URL&gt;</td>
<td> Navigates the browser to the given URL. NOTE navigating to a URL retains all URLs accessible from going BACK, but any URLs that would have accessible from going FORWARD are now lost
</td></tr>
<tr>
<td> BACK </td>
<td> A command indicating the web browser is redirected to the previous URL in the history. If there is no URL further back, then the browser stays on the current URL.
</td></tr>
<tr>
<td> FORWARD </td>
<td> A command indicating the web browser is redirected to the next URL in the history. If there is no URL that is next, then the browser stays on the current URL.
</td></tr>
<tr>
<td> HISTORY </td>
<td> Prints the current URL history to the screen using the following format: <br>
<pre>Oldest
===========
&lt;URL&gt;
&lt;URL&gt;  &lt;==current (assuming this is the current URL)
&lt;URL&gt; 
===========
Newest
</pre>
</td></tr>
</tbody></table>
<h3><span class="mw-headline" id="Sample_input_file">Sample input file</span></h3>
<pre>NAVIGATE http://google.com
NAVIGATE http://reddit.com
NAVIGATE http://facebook.com
NAVIGATE http://myspace.com
HISTORY
BACK
BACK
HISTORY
FORWARD
FORWARD
FORWARD
FORWARD
HISTORY
BACK
BACK
BACK
NAVIGATE http://ku.edu
FORWARD
HISTORY
BACK
HISTORY
</pre>
<p>Output to screen:
</p>
<pre>Oldest
===========
http://google.com
http://reddit.com
http://facebook.com
http://myspace.com  &lt;==current
===========
Newest

Oldest
===========
http://google.com
http://reddit.com   &lt;==current
http://facebook.com
http://myspace.com 
===========
Newest

Oldest
===========
http://google.com
http://reddit.com
http://facebook.com
http://myspace.com  &lt;==current
===========
Newest

Oldest
===========
http://google.com
http://ku.edu       &lt;==current
===========
Newest

Oldest
===========
http://google.com   &lt;==current
http://ku.edu
===========
Newest
</pre>
<h2><span class="mw-headline" id="Linked_List_requirements">Linked List requirements</span></h2>
<p>Your LinkedList must be made out of your Node class. DO NOT just implement your LinkedList using the existing python lists.
</p><p>If this class was designed to teach you how to make a pizza, the first step isn't order Dominoes and put your name on the box. We're making it from scratch.
</p>
<h2><span class="mw-headline" id="Rubric">Rubric</span></h2>
<ul><li> 10pts Attendance</li>
<li> 20pts List Implementation</li>
<li> 40pts Web Browser Implementation</li>
<li> 10pts Modularity
<ul><li> Sensible class design</li>
<li> Completely object oriented (e.g. your main should invoke some kind of executive class)</li></ul></li>
<li> 10pts Stability
<ul><li>There should be zero unhanded exceptions when provided with a properly formatted file</li></ul></li>
<li> 5pts Comments and documentation: 
<ul><li>docstrings</li>
<li>Author, date, last modified comments at the top of each .py file</li></ul></li></ul>
<h2><span class="mw-headline" id="Submission_instructions">Submission instructions</span></h2>
<p>All .py and input files should be packaged into a zip or tar.gz file and submitted.
</p><p>Consult your TA for additional submission instructions.
</p>
<!-- 
NewPP limit report
Cached time: 20220922181328
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.029 seconds
Real time usage: 0.034 seconds
Preprocessor visited node count: 70/1000000
Preprocessor generated node count: 122/1000000
Post‐expand include size: 621/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    3.034      1 -total
100.00%    3.034      1 Template:EECS268
-->
