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
</p><p><br>
</p>
<div id="toc" class="toc"><div class="toctitle"><h2>Contents</h2><span class="toctoggle">&nbsp;[<a role="button" tabindex="0" class="togglelink">hide</a>]&nbsp;</span></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#Due_time"><span class="tocnumber">1</span> <span class="toctext">Due time</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#Overview"><span class="tocnumber">2</span> <span class="toctext">Overview</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#File"><span class="tocnumber">3</span> <span class="toctext">File</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#Max_Heaps"><span class="tocnumber">4</span> <span class="toctext">Max Heaps</span></a></li>
<li class="toclevel-1 tocsection-5"><a href="#Lab_discussion_topics"><span class="tocnumber">5</span> <span class="toctext">Lab discussion topics</span></a></li>
<li class="toclevel-1 tocsection-6"><a href="#Rubric"><span class="tocnumber">6</span> <span class="toctext">Rubric</span></a></li>
<li class="toclevel-1 tocsection-7"><a href="#Submission"><span class="tocnumber">7</span> <span class="toctext">Submission</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="Due_time">Due time</span></h2>
<p>This lab is due two weeks from the start of your lab.
</p>
<h2><span class="mw-headline" id="Overview">Overview</span></h2>
<p>In this lab you will make a Hospital simulator.  Patients are arriving at the Hospital with varying degrees of illness. You need to make sure the sickest patients are seen first.
</p>
<h2><span class="mw-headline" id="File">File</span></h2>
<p>The file will have the instructions that describe what is happening at the Hospital.  The Hospital is short-staffed, so only one patient can be seen at a time.
</p>
<table class="wikitable">

<tbody><tr>
<th> Command </th>
<th> Description
</th></tr>
<tr>
<td> ARRIVE &lt;first_name&gt; &lt;last_name&gt; &lt;age&gt; &lt;illness&gt; &lt;severity&gt;</td>
<td> A new patient arrives at the hospital and should placed in line based on their illnesses severity. If there is a tie, then the older patient should be seen first. If there is still a tie, the patient that arrived first should be seen first.
<ul><li>first and last names and illness are independent contiguous string</li>
<li>age is a positive integer</li>
<li>severity is a positive integer between 0-9 inclusively, where 9 is the most severe</li></ul>
</td></tr>
<tr>
<td> NEXT </td>
<td> The receptionist calls the name of the next patient. They will be seen by the doctor soon. Print the patient's information to terminal. The patient isn't treated until the TREAT command is used. Display the patient's information in the following format: <br>
<pre>Name:  
Age: 
Suffers from:
Illness severity: 
</pre>
</td></tr>
<tr>
<td> TREAT </td>
<td> The doctor treats the patient with the highest severity level.  After treatment, the patient can go home.
</td></tr>
<tr>
<td> COUNT </td>
<td> Displays the current count of patients waiting to be seen
</td></tr></tbody></table>
<p>Sample file:
</p>
<pre>ARRIVE John Gibbons 39 sleep_deprivation 2
ARRIVE C.S. Student 19 coffee_overdose 6
ARRIVE Grigori Rasputin 47 everything 9
COUNT
NEXT
TREAT
NEXT
TREAT
COUNT
</pre>
<p>Your program would display something like:
</p>
<pre>There are 3 patients waiting.

Next patient:
     Name: Rasputin, Grigori. 
     Age: 47
     Suffers from: everything
     Illness severity: 9

Next patient:
     Name: Student, C.S. 
     Age: 19
     Suffers from: coffee_overdose
     Illness severity: 6

There is 1 patient waiting.
</pre>
<p>We will test your code with different files. You can assume a given command will be formatted as shown, but we should be able to provide a file with commands in any order we choose.  For example, be able to handle a file that does TREAT when there are no patients.
</p>
<h2><span class="mw-headline" id="Max_Heaps">Max Heaps</span></h2>
<p>I'm not sure why I'm typing this. This lab is about Hospitals, not Heaps. This probably won't be helpful at all. 
</p><p>Or will it!? (It will.)
</p><p>So this lab we will use a Max Heap as a means of implementing a priority queue.  A priority queue is a queue where people can shift towards the front of the queue based on a priority status. 
</p><p>You're Hospital class will act as a priority queue where a patient's order in the queue will be determined by their priority.
</p><p>For this lab you must implement a MaxHeap using a list-based implementation. Then use that MaxHeap to handle all your patient prioritizing in the hospital.
</p><p><b>You must create all classes (minus built-in python list) from scratch. Do not including pre-exisiting heap modules</b>
</p>
<h2><span class="mw-headline" id="Lab_discussion_topics">Lab discussion topics</span></h2>
<p>As a class discuss the following questions:
</p>
<ol><li>How should we represent Patients?</li>
<li>What operators will Patients need overloaded, and how will overloaded operators work?</li>
<li>Is the Doctor something that we need to design a class for? Why or why not?</li>
<li>What role will the MaxHeap play in this lab, if any?</li></ol>
<h2><span class="mw-headline" id="Rubric">Rubric</span></h2>
<ul><li> [10%] Attendance and Lab discussion participation
<ul><li>Participate in lab discussion. Granted, not every student can supply an answer to every question, but every student can get involved in the discussion on some level. Listening, asking questions, seeking clarification, etc.</li></ul></li>
<li> [15%] Class design</li>
<li> [30%] Max-heap list-based implementation</li>
<li> [35%] Hospital Simulation</li>
<li> [10%] Stability
<ul><li> [5%] No unhandled exceptions</li>
<li> [5%] Can stand up to input files with non-sensical command ordering</li></ul></li></ul>
<p><br>
</p>
<h2><span class="mw-headline" id="Submission">Submission</span></h2>
<p>Consult your TA for submission instructions
</p>
<!-- 
NewPP limit report
Cached time: 20221116003610
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.025 seconds
Real time usage: 0.032 seconds
Preprocessor visited node count: 62/1000000
Preprocessor generated node count: 114/1000000
Post‐expand include size: 621/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    2.894      1 -total
100.00%    2.894      1 Template:EECS268
-->
