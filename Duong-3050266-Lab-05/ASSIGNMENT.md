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
<li class="toclevel-1 tocsection-2"><a href="#Lab_conduct"><span class="tocnumber">2</span> <span class="toctext">Lab conduct</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#Overview"><span class="tocnumber">3</span> <span class="toctext">Overview</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#File_Format"><span class="tocnumber">4</span> <span class="toctext">File Format</span></a></li>
<li class="toclevel-1 tocsection-5"><a href="#Blob_Moving_Rules"><span class="tocnumber">5</span> <span class="toctext">Blob Moving Rules</span></a></li>
<li class="toclevel-1 tocsection-6"><a href="#Output"><span class="tocnumber">6</span> <span class="toctext">Output</span></a></li>
<li class="toclevel-1 tocsection-7"><a href="#Additional_Requirements"><span class="tocnumber">7</span> <span class="toctext">Additional Requirements</span></a></li>
<li class="toclevel-1 tocsection-8"><a href="#Emailing_Your_Submission"><span class="tocnumber">8</span> <span class="toctext">Emailing Your Submission</span></a></li>
<li class="toclevel-1 tocsection-9"><a href="#Rubric"><span class="tocnumber">9</span> <span class="toctext">Rubric</span></a></li>
<li class="toclevel-1 tocsection-10"><a href="#Sample_Runs"><span class="tocnumber">10</span> <span class="toctext">Sample Runs</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="Due_time">Due time</span></h2>
<p>This lab is due <strike>one week</strike> <b>two weeks</b> from the start of your lab.
</p>
<h2><span class="mw-headline" id="Lab_conduct">Lab conduct</span></h2>
<ul><li>Do not use any unauthorized aid, such sites like rentacoder or chegg to obtain answers</li>
<li>Do not use code provided by another student</li>
<li>Do not reuse code (by you or anyone) from prior semesters</li>
<li>If you need help, seek it from:
<ul><li>Your lab TA.</li>
<li>Me, Dr. Gibbons, my email is jwgibbo@ku.edu / jwgibbo@gmail.com</li></ul></li>
<li>If equipment you don't own (e.g. cycle servers) needs attention or you're having account issues put in a <a rel="nofollow" class="external text" href="https://tsc.ku.edu/request-support-engineering-tsc">ticket!</a></li></ul>
<h2><span class="mw-headline" id="Overview">Overview</span></h2>
<p><a rel="nofollow" class="external text" href="https://www.youtube.com/watch?v=ejtPJc-fDZ8">Beware of the Blob!</a>
</p><p>In this lab, the Blob is loose and you will figure out with parts of the city will and won't be consumed.
</p><p>You'll be given a file with a map of the city and the starting point of the Blob. Your program will use recursion and backtracking to figure how far the Blob will spread.
</p><p>NOTE: This is different from the Maze Walking we've been working on in lecture in that you aren't trying to find a single path to an exit; you want to see all the spaces The Blob can reach.
</p>
<h2><span class="mw-headline" id="File_Format">File Format</span></h2>
<pre>&lt;numRows&gt; &lt;numCols&gt;
&lt;Blob startRow&gt; &lt;Blob startCol&gt;
&lt;map characters&gt;
</pre>
<ul><li>Num rows and columns indicate the maps dimensions</li>
<li>Start row and column are where Blob begins</li>
<li>The row and columns coordinates range from 0 to (numRows-1) and 0 to (numCols-1)</li>
<li>The top left of the map would be considered 0,0</li></ul>
<p>The map consists of:
</p>
<ul><li> Streets represented by capital 'S'
<ul><li>The Blob <b>can only move through streets and sewers</b></li></ul></li>
<li> People represented by capital 'P'</li>
<li> Buildings are represented by '#'</li>
<li> Sewers are represented by '@'
<ul><li>You will need to do some pre-processing on the file to find the locations of all sewers before your Blob simulation begins</li>
<li>All sewers are considered adjacent </li></ul></li></ul>
<p>A file is invalid and the program should end with an error message if...
</p>
<ul><li>if file doesn't exist</li>
<li>if numRows are less than 1</li>
<li>if numCols are less than 1</li>
<li>if start position is not within range</li></ul>
<p>You may assume the map characters match the parameters given above.
</p>
<h2><span class="mw-headline" id="Blob_Moving_Rules">Blob Moving Rules</span></h2>
<ul><li> The Blob starts at the start position</li>
<li> The Blob only spreads orthogonally (up, right, down, or left) not diagonally
<ul><li>See special rules of sewers </li></ul></li>
<li> You must check for valid directions to spread in the order: up, right, down, left</li>
<li> You cannot spread through the Buildings
<ul><li>See special rules of sewers</li></ul></li>
<li>People
<ul><li>People work just like streets, except they add the "People Eaten Total"</li></ul></li>
<li>Sewers
<ul><li> If the Blob is on a sewer space, and has tried to spread in all other directions, it will spread into the sewer, which allows it to move to all connected sewer spaces one at a time</li>
<li>Once the Blob moves through a sewer it continues to move as normal</li></ul></li></ul>
<h2><span class="mw-headline" id="Output">Output</span></h2>
<p>After receiving a file from the command-line you will output to where the Blob spread. As the Blob spreads, you will marks its path with 'B's. <b>You must keep the sewers as '@' in the output</b>. Below the blob-filled map you will also print a count of "Total Eaten"
</p><p>I've provided a few examples below.
</p>
<h2><span class="mw-headline" id="Additional_Requirements">Additional Requirements</span></h2>
<p>Do not use a stack object to solve the problem; use recursion.
</p>
<h2><span class="mw-headline" id="Emailing_Your_Submission">Emailing Your Submission</span></h2>
<p>Once you have created the tarball with your submission files, email it to your TA.  The email subject line <strong>must</strong> look like "[EECS 268] <i>SubmissionName</i>":
</p>
<dl><dd>[EECS 268] Lab 0#</dd></dl>
<p>Note that the subject should be <i>exactly</i> like the line above.  Do not leave out any of the spaces, or the bracket characters ("[" and "]").  In the body of your email, include your name and student ID.
</p>
<h2><span class="mw-headline" id="Rubric">Rubric</span></h2>
<ul><li> 10% Attendance</li>
<li> 70% Correctly spreads the Blob
<ul><li> 45% Blob spreads through streets</li>
<li> 10% Number of people eaten properly counted</li>
<li> 15% Blob spreads into sewers then continue moving as normal</li></ul></li>
<li> 15% Code design</li>
<li> 5% Code style and documentation</li></ul>
<h2><span class="mw-headline" id="Sample_Runs">Sample Runs</span></h2>
<p>Input file 1
</p>
<pre>4 4
0 2
##S#
#PS#
##S#
SPP#
</pre>
<p>Output 1
</p>
<pre>##B#
#BB#
##B#
BBB#
Total eaten: 3
</pre>
<p>Input file 2
</p>
<pre>8 8
0 0
PSSSSSS#
######S#
@SSSSSP#
########
###S####
@SSS#SS#
#S####S#
###PPPSP
</pre>
<p>Output 2
</p>
<pre>8 8
0 0
BBBBBBB#
######B#
@BBBBBB#
########
###B####
@BBB#SS#
#B####S#
###PPPSP
Total eaten: 2
</pre>

<!-- 
NewPP limit report
Cached time: 20221004183409
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.027 seconds
Real time usage: 0.033 seconds
Preprocessor visited node count: 69/1000000
Preprocessor generated node count: 166/1000000
Post‐expand include size: 620/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    2.975      1 -total
100.00%    2.975      1 Template:EECS268
-->
