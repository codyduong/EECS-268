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
<li class="toclevel-1 tocsection-1"><a href="#NOTICE"><span class="tocnumber">1</span> <span class="toctext">NOTICE</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#Due_time"><span class="tocnumber">2</span> <span class="toctext">Due time</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#Overview"><span class="tocnumber">3</span> <span class="toctext">Overview</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#Exercise_1:_Recursive_Power_Function"><span class="tocnumber">4</span> <span class="toctext">Exercise 1: Recursive Power Function</span></a></li>
<li class="toclevel-1 tocsection-5"><a href="#Exercise_2:_Outbreak_Returns"><span class="tocnumber">5</span> <span class="toctext">Exercise 2:  Outbreak Returns</span></a></li>
<li class="toclevel-1 tocsection-6"><a href="#Exercise_3:_Good_Old_Fibonacci"><span class="tocnumber">6</span> <span class="toctext">Exercise 3: Good Old Fibonacci</span></a></li>
<li class="toclevel-1 tocsection-7"><a href="#Rubric"><span class="tocnumber">7</span> <span class="toctext">Rubric</span></a></li>
<li class="toclevel-1 tocsection-8"><a href="#Emailing_Your_Submission"><span class="tocnumber">8</span> <span class="toctext">Emailing Your Submission</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="NOTICE">NOTICE</span></h2>
<p>The majority of these problem are classic recursive problems with lots of solutions online. Do yourself a favor, and DO NOT go seeking solutions. Instead, seek help from our staff. Your better off figuring it out on your own steam, maybe with some guidance from us. Also, looking up a solution and turning it in as your own is still cheating.
</p>
<h2><span class="mw-headline" id="Due_time">Due time</span></h2>
<p>This lab is due 1 week from the start of your lab.
</p>
<h2><span class="mw-headline" id="Overview">Overview</span></h2>
<p>This lab will consist of several independent exercises (one .py per exercise) that <b>must all use recursion</b> to solve various problems.
</p>
<h2><span class="mw-headline" id="Exercise_1:_Recursive_Power_Function">Exercise 1: Recursive Power Function</span></h2>
<p>Create a program that takes in a base and exponent for the user. If the input is valid, it prints the answer of the base taken to the power given. You must require the user to give ints for both the base and the exponent. Also, the exponent must be zero or larger.
</p><p>Sample runs:
</p>
<pre>Enter a base: 2
Enter a power: 3
Answer: 8
</pre>
<pre>Enter a base: 256
Enter a power: 1
Answer: 256
</pre>
<pre>Enter a base: 256
Enter a power: 0
Answer: 1
</pre>
<pre>Enter a base: -1
Enter a power: 3
Answer: -1
</pre>
<pre>Enter a base: 2 
Enter a power: -1
Sorry, your exponent must be zero or larger.
Enter a power: -1
Sorry, your exponent must be zero or larger.
Enter a power: -1
Sorry, your exponent must be zero or larger.
Enter a power: -1
Sorry, your exponent must be zero or larger.
Enter a power: -1
Sorry, your exponent must be zero or larger.
Enter a power: 10
Answer: 1024
</pre>
<p><br>
</p>
<h2><span class="mw-headline" id="Exercise_2:_Outbreak_Returns">Exercise 2:  Outbreak Returns</span></h2>
<p>Flu season is upon us and the number of people getting sick is growing.  
</p>
<ul><li>On day 1, there was only 6 people had the flu</li>
<li>On day 2, it jumped to 20. </li>
<li>On day 3, there were 75</li>
<li>Every day since, the number of people who have the flu is equal to the last 3 days combined</li></ul>
<p>You will make a program that will ask the user for what day they want a count of people with the flu for. Then display the amount. You must use recursion to solve the calculation of infected for a given day. Assume the user will input a valid day.
</p><p>Sample runs:
</p>
<pre>OUTBREAK!
What day do you want a sick count for?: 1
Total people with flu: 6
</pre>
<pre>OUTBREAK!
What day do you want a sick count for?: 2
Total people with flu: 20
</pre>
<pre>OUTBREAK!
What day do you want a sick count for?: 3
Total people with flu: 75
</pre>
<pre>OUTBREAK!
What day do you want a sick count for?: 4
Total people with flu: 101
</pre>
<pre>OUTBREAK!
What day do you want a sick count for?: 5
Total people with flu: 196
</pre>
<pre>OUTBREAK!
What day do you want a sick count for?: 0
Invalid day
</pre>
<h2><span class="mw-headline" id="Exercise_3:_Good_Old_Fibonacci">Exercise 3: Good Old Fibonacci</span></h2>
<p>The Fibonacci sequence is a famous numerical series in which every number (after the first two) is the sum of the previous two numbers added together. The sequence is defined as...
</p><p>F<sub>0</sub>=0 
</p><p>F<sub>1</sub>=1
</p><p>F<sub>i</sub>=F<sub>i-1</sub> + F<sub>i-2</sub>
</p><p>For your reference, here are the first few numbers in the Fibonacci sequence:
</p><p>0,1,1,2,3,5,8,13,21,34,55,89
</p><p>Create a program that takes an integer and a mode from the user. The mode will indicate one of two options:
</p>
<ul><li>-i mode
<ul><li>Short for "ith" where the user wants to know the ith Fibonacci number (note the lowest valid would be zero)</li></ul></li>
<li>-v mode
<ul><li>Short for "verify" where the user wants to know if the number given is in the Fibonacci sequence</li></ul></li></ul>
<p>Example runs:
</p>
<pre>Enter mode and value: -i 2
1
</pre>
<pre>Enter mode and value: -i 8
21
</pre>
<pre>Enter mode and value: -i 36
14930352
</pre>
<pre>Enter mode and value: -v 7
7 is not in the sequence
</pre>
<pre>Enter mode and value: -v 75025
75025 is in the sequence
</pre>
<p><br>
</p>
<h2><span class="mw-headline" id="Rubric">Rubric</span></h2>
<p>Your solutions must be recursive. <b>Any solutions that do not use recursion will receive a zero.</b>
</p>
<ul><li> [10pts] Attendance</li>
<li> [15pts] Exercise 1</li>
<li> [25pts] Exercise 2</li>
<li> [35pts] Exercise 3
<ul><li>[15pts] -i mode</li>
<li>[20pts] -v mode</li></ul></li>
<li> [5pts] Clean output</li>
<li> [5pts] Zero unhandled exceptions</li>
<li> [5pts] Documentation</li></ul>
<h2><span class="mw-headline" id="Emailing_Your_Submission">Emailing Your Submission</span></h2>
<p>Once you have created the zip/tarball with your submission files, submit it to your TA.
</p>
<!-- 
NewPP limit report
Cached time: 20220925192403
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.029 seconds
Real time usage: 0.034 seconds
Preprocessor visited node count: 184/1000000
Preprocessor generated node count: 378/1000000
Post‐expand include size: 620/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    3.006      1 -total
100.00%    3.006      1 Template:EECS268
-->
