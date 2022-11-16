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
<li class="toclevel-1 tocsection-1"><a href="#Due_Date"><span class="tocnumber">1</span> <span class="toctext">Due Date</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#Overview"><span class="tocnumber">2</span> <span class="toctext">Overview</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#Pokemon_File"><span class="tocnumber">3</span> <span class="toctext">Pokemon File</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#Requirements"><span class="tocnumber">4</span> <span class="toctext">Requirements</span></a></li>
<li class="toclevel-1 tocsection-5"><a href="#Binary_Search_Tree_Overview"><span class="tocnumber">5</span> <span class="toctext">Binary Search Tree Overview</span></a></li>
<li class="toclevel-1 tocsection-6"><a href="#Phase_1"><span class="tocnumber">6</span> <span class="toctext">Phase 1</span></a></li>
<li class="toclevel-1 tocsection-7"><a href="#Implementation_Details"><span class="tocnumber">7</span> <span class="toctext">Implementation Details</span></a></li>
<li class="toclevel-1 tocsection-8"><a href="#Rubric"><span class="tocnumber">8</span> <span class="toctext">Rubric</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="Due_Date">Due Date</span></h2>
<p>This lab is due one week from the start of your lab.
</p>
<h2><span class="mw-headline" id="Overview">Overview</span></h2>
<p>The next two labs will use Binary Search Trees. For this lab we will only implement adding, searching, and traversing a BST. The next lab is when we'll implement other methods like removal and copy.  We'll cover more BST topics in lecture this week.
</p><p>Phase 1:
</p>
<ul><li>Adding to a BST</li>
<li>Searching a BST</li>
<li>Visiting a BST in pre, in, and post orders</li></ul>
<p>Phase 2:
</p>
<ul><li>Coming in next lab...</li></ul>
<h2><span class="mw-headline" id="Pokemon_File">Pokemon File</span></h2>
<p>You can download a sample file <a rel="nofollow" class="external text" href="https://github.com/jwgibbo/public_html/blob/master/eecs268/2022fall/labs/lab07/pokemon.txt">here</a>.
Each line is organized in the following manner (white-space delimited):
</p>
<pre>&lt;american pokemon name&gt; &lt;pokedex number&gt; &lt;japanese pokemon name&gt;
</pre>
<table class="wikitable">
<tbody><tr>
<th> American Name
</th>
<td> What the pokemon is called in the U.S.A.
</td></tr>
<tr>
<th> pokedex number
</th>
<td> A number associated with a particular pokemon. Think of it as a pokemon's SSN
</td></tr>
<tr>
<th> Japanese pokemon name
</th>
<td> What the pokemon is called in Japan
</td></tr></tbody></table>
<p>Example entries:
</p>
<pre>Abra	63	Casey
Aerodactyl	142	Ptera
Alakazam	65	Foodin
Arbok	24	Arbok
Arcanine	59	Windie
Articuno	144	Freezer
Beedrill	15	Spear
Bellsprout	69	Madatsubomi
Blastoise	9	Kamex
Bulbasaur	1	Fushigidane
</pre>
<h2><span class="mw-headline" id="Requirements">Requirements</span></h2>
<p>This lab and the next lab will involve implementing and using a <b>node-based implementation of a Binary Search Tree</b> (you cannot use built-in dicts like in 168).  The table lists the functionality that  you can accomplish by loading the Pokedex entries into a single Binary Search Tree.  <b>Only do the requirements for phase 1 even if you know how to accomplish other tasks (e.g. removal)</b>
</p><p>Notes:
</p>
<ul><li>The user will provide the name of an input file formatted in the way described above</li>
<li>Using that file, create and load a BST full of Pokemon</li>
<li>Until the user wants to quit, let them use your pokedex in the ways listed in the table below:
<ul><li> The table list the menus labels and desired outcomes, but you will need to use the BinarySearchTree method that accomplishes the task</li>
<li> Example: If the user wants to <strong>Search</strong> you will need to call the <strong>search(key)</strong> method from the BinarySearchTree and see whether it produces a result or raises an exception to verify if the Pokemon is in the BST</li></ul></li></ul>
<h2><span class="mw-headline" id="Binary_Search_Tree_Overview">Binary Search Tree Overview</span></h2>
<ul><li>BSTs are binary trees (so you can use your binary nodes we made in class)</li>
<li>They have rules for adding:
<ul><li>If a subtree is empty, add new value</li>
<li>If it's non-empty compare new value to value in current node
<ul><li>If new value is less than current node's value, add to left subtree</li>
<li>If new value is greater than current node's value, add to right subtree</li></ul></li>
<li>No duplicates allowed (raise exceptions should this occur, but keep your program crashing!)</li></ul></li>
<li>Searching should take advantage of the rules for adding
<ul><li>Example if I'm looking for 10 and I'm on a node with 20, I should search 20's left subtree</li></ul></li></ul>
<p><br>
Recall our three traversal orders:
</p>
<table class="wikitable">
<tbody><tr>
<th> Pre order </th>
<th> In order </th>
<th> Post order
</th></tr>
<tr>
<td>1)Visit<br>2)Traverse LST<br>3)Traverse RST </td>
<td> 1)Traverse LST<br>2)Visit<br>3)Traverse RST </td>
<td> 1)Traverse LST<br>2)Traverse RST<br>3)Visit
</td></tr>
</tbody></table>
<h2><span class="mw-headline" id="Phase_1">Phase 1</span></h2>
<table class="wikitable">
<tbody><tr>
<th> Search
</th>
<td> Given pokedex number (id) print all information (US name, Japanese name, pokedex number) to the user
</td></tr>
<tr>
<th> Add
</th>
<td> Prompt the user for a new Pokemon name (US), then new Japanese name and Pokedex number and add the entry to the tree. <b>Duplicates should not be allowed.</b> Make your add method throw an exception (std::runtime_error) if a duplicate is attempted to be added.
</td></tr>
<tr>
<th> Print
</th>
<td> Prompt the user for the following:
<ul><li> Traversal order; The user can choose for the pokedex to be written in in, pre, or post order. </li></ul>
</td></tr>
<tr>
<th> Quit
</th>
<td> Exits the program
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Implementation_Details">Implementation Details</span></h2>
<ul><li>We ask that you BST distinguish between the type of object is in the tree and the type used to search; an ItemType and a KeyType
<ul><li>The ItemType would be the type returned from a search</li>
<li>The KeyType would be the type that you can search on</li>
<li>For example, if I search for the Pokemon with ID 25 I should get back the whole entry for that word when I search.</li></ul></li>
<li>The BST should only use the default comparison operators, and <strong>not be coupled</strong> to the methods of any specific class
<ul><li>Overload the needed comparison operators for your class</li>
<li>We will order them numerically based on their pokedex number</li>
<li>A helpful function your Pokemon's operator overloads could use is <a rel="nofollow" class="external text" href="https://docs.python.org/3/library/functions.html#isinstance">isinstance</a> (e.g. isinstance(5, int) returns True)</li></ul></li>
<li>You'll notice that the traversal functions take a function as a parameter. Essentially, you're passing a function that will be called on each entry in the BST. 
<ul><li>The function will belong to a class/module other than the BST</li></ul></li></ul>
<p><br>
Example of passing functions as parameters and using them.
</p>
<pre>def everything_is_awesome(something):
    print(something, "is awesome!")

def call_func_on_something(func, something):
    func(something)

def main():
    user_input = input("Hey user, what's on your mind?: ")
    call_func_on_something(everything_is_awesome, user_input) #note we just say the name of the function, no () or params

main()
</pre>
<p>Sample run:
</p>
<pre>Hey user, what's on your mind?: 
pudding
pudding is awesome!
</pre>
<h2><span class="mw-headline" id="Rubric">Rubric</span></h2>
<ul><li> 10% Attendance</li>
<li> 60% Pokedex Interaction
<ul><li> 20% Searching</li>
<li> 20% Adding entry</li>
<li> 20% Correct traversal orders</li></ul></li>
<li> 10% Terminal output
<ul><li> 10% well formatted output</li></ul></li>
<li> 10% Program stability</li>
<li> 5% Logical user interface</li>
<li> 5% Needed Operators overloaded</li></ul>

<!-- 
NewPP limit report
Cached time: 20221116200058
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.029 seconds
Real time usage: 0.036 seconds
Preprocessor visited node count: 75/1000000
Preprocessor generated node count: 138/1000000
Post‐expand include size: 621/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    2.929      1 -total
100.00%    2.929      1 Template:EECS268
-->
