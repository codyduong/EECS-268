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
<li class="toclevel-1 tocsection-3"><a href="#Pokemon_File"><span class="tocnumber">3</span> <span class="toctext">Pokemon File</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#Requirements"><span class="tocnumber">4</span> <span class="toctext">Requirements</span></a>
<ul>
<li class="toclevel-2 tocsection-5"><a href="#Phase_1"><span class="tocnumber">4.1</span> <span class="toctext">Phase 1</span></a></li>
<li class="toclevel-2 tocsection-6"><a href="#Phase_2"><span class="tocnumber">4.2</span> <span class="toctext">Phase 2</span></a></li>
<li class="toclevel-2 tocsection-7"><a href="#Implementation_Details"><span class="tocnumber">4.3</span> <span class="toctext">Implementation Details</span></a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-8"><a href="#Rubric"><span class="tocnumber">5</span> <span class="toctext">Rubric</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="Due_time">Due time</span></h2>
<ul><li>Due <strike>a week</strike> two weeks from the start of your lab</li></ul>
<h2><span class="mw-headline" id="Overview">Overview</span></h2>
<p>In this lab you will make a Pokemon translator that will allow users to look up a Pokemon by it's pokedex number and retrieve its American and Japanese names.  You read in the Pokemon's number, American name and their corresponding Japanese translation from a file.  Then, you will allow the user to query your Pokemon index or "Pokedex".
</p>
<h2><span class="mw-headline" id="Pokemon_File">Pokemon File</span></h2>
<p>You will use the same data file from the previous lab.
The file is a tab-separated value file (.tsv). Each line is organized in the following manner:
</p>
<pre>&lt;american pokemon name&gt; &lt;pokedex number&gt; &lt;japanese pokemon name&gt;
</pre>
<p>Where entries are seperated by tabs, but remember that tabs are whitespace too!
</p>
<table class="wikitable">
<tbody><tr>
<th> American Name
</th>
<td> What the pokemon is called in the U.S.A.
</td></tr>
<tr>
<th> pokedex number
</th>
<td> A number associated with a particular pokemon. Think of it as a unique identifier for a pokemon.
</td></tr>
<tr>
<th> Japanese pokemon name
</th>
<td> What the pokemon is called in Japan
</td></tr></tbody></table>
<p><br>
Example entries:
</p>
<pre>Ekans	23	Arbo
Arbok	24	Arbok
Seaking	119	Azumao
Mr. Mime	122	Barrierd
Weedle	13	Beedle
Lickitung	108	Beroringa
Grimer	88	Betbeter
Muk	89	Betbeton
Voltorb	100	Biriridama
Magmar	126	Boober
Flareon	136	Booster
Butterfree	12	Butterfree
Abra	63	Casey
Caterpie	10	Caterpie
Kakuna	14	Cocoon
Magnemite	81	Coil
</pre>
<h2><span class="mw-headline" id="Requirements">Requirements</span></h2>
<p>Since I've seen a lot of students still in the habit of coding EVERYTHING then compiling, I've broken this lab up into phases. But! You should still compile very often! Use the debugger built into IDLE. 
</p><p>I recommend compiling and testing after you add every method (at the the very least).
</p><p>Notes:
</p>
<ul><li>The user will provide the name of an input file formatted in the way described above from the terminal</li>
<li>Using that file, create and load a BST full of Pokemon</li>
<li>Until the user wants to quit, let them use your application in the ways listed in the table below:
<ul><li> The table list the menus labels and desired outcomes, but you will need to use the BinarySearchTree method that accomplishes the task</li></ul></li></ul>
<p><br>
</p>
<h3><span class="mw-headline" id="Phase_1">Phase 1</span></h3>
<p>This should already be done from previous lab, but it still needs to be functional for this lab.
</p>
<table class="wikitable">
<tbody><tr>
<th> Search
</th>
<td> Give a pokemon's pokedex number, retrieve it's US and JPN translations.
</td></tr>
<tr>
<th> Print
</th>
<td> Prompt the user for the following:
<ul><li> Traversal order; The user can choose for the BST to be written in in, pre, or post order. </li></ul>
</td></tr>
</tbody></table>
<h3><span class="mw-headline" id="Phase_2">Phase 2</span></h3>
<table class="wikitable">
<tbody><tr>
<th> Copy
</th>
<td>
<ul><li>Add a method to your BST called copy, which creates a deep copy of the BST.  </li>
<li>A deep copy is identical to the original, but is completely separate. Kind of like a clone; after the cloning should a change occur in one, it does NOT affect the other.</li>
<li>The user can only select this option once. If the user tries to make multiple copies, issue a message stating that ta copy already exists </li>
<li>Once the user makes a copy, ask the user which tree they wish to use each subsequent time they request an Add, Search, or Remove operation</li>
<li>Once a copy is made, you'll need to prompt the user to determine which tree the are interacting with before each action (e.g. search, remove, etc)</li></ul>
</td></tr>
<tr>
<th> Add
</th>
<td> Prompt the user for a new Pokemon name (US), the new Japanese name and Pokedex number and add the entry to the tree. <b>Duplicates should not be allowed.</b> Make your add method raise an exception  if a duplicated is attempted to be added, but your program should not crash. I've listed this in phase 2 because something that is now possible if for a Pokemon to be placed in the tree, then removed, then added again. This is a valid sequence of actions.
</td></tr>
<tr>
<th> Remove
</th>
<td> Given a pokedex number, remove that entry from the BST. When removing, you should choose the maximum value from the target's LST as the replacement candidate (see lecture notes).
</td></tr>
<tr>
<th> Quit
</th>
<td> Exits the program.
</td></tr></tbody></table>
<h3><span class="mw-headline" id="Implementation_Details">Implementation Details</span></h3>
<ul><li>Your BST will utilize two types: an ItemType and a KeyType
<ul><li>The ItemType would be the type returned from a search</li>
<li>The KeyType would be the type that you can search on <b>OR how to choose an entry to remove</b></li>
<li>For example, if I search for 25 I should get back the whole entry for that pokemon when I search.</li></ul></li>
<li>The BST should only use the default comparison operators, and <strong>not be coupled</strong> to the methods of any specific class
<ul><li>Overload the needed comparison operators for your class</li>
<li>We will order them numerically based on their pokedex number</li>
<li>A helpful function your Pokemon's operator overloads could use is <a rel="nofollow" class="external text" href="https://docs.python.org/3/library/functions.html#isinstance">isinstance</a> (e.g. isinstance(5, int) returns True)</li></ul></li>
<li>You'll notice that the traversal functions take a function as a parameter. Essentially, you're passing a function that will be called on each entry in the BST. 
<ul><li>The function will belong to a class/module other than the BST</li></ul></li>
<li> If a copy is made and edits are performed, the original should remain unchanged.</li></ul>
<p><br>
</p>
<h2><span class="mw-headline" id="Rubric">Rubric</span></h2>
<ul><li> 10% Attendance</li>
<li> 65% Pokedex Interaction
<ul><li> 5% Searching</li>
<li> 5% Adding entry</li>
<li> 5% Correct traversal orders</li>
<li> 20% Copying</li>
<li> 30% Removal</li></ul></li>
<li> 10% Terminal output
<ul><li> 10% well formatted output</li></ul></li>
<li> 10% Program stability</li>
<li> 5% Needed Operators overloaded</li></ul>

<!-- 
NewPP limit report
Cached time: 20221116013613
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.027 seconds
Real time usage: 0.032 seconds
Preprocessor visited node count: 57/1000000
Preprocessor generated node count: 98/1000000
Post‐expand include size: 621/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    2.899      1 -total
100.00%    2.899      1 Template:EECS268
-->
