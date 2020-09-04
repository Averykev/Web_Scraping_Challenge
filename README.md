# Web_Scraping_Challenge
Web Scraping Challenge

1.)  MISSION TO MARS - PYTHON CODE

	a.)  For this section of the challenge I originally used a lot of "for loops" to get everything to work.  For example, in the Mars News section I had to loop through 
	two different blocks of html code because I was unable to get the "paragraph" from the same block of code as the "title."  However, during office hours I was able to
	get some help from both the TA and the instructor and they helped me to run two different "soup.find" queries in the same line of code.  Once I did that I was able
	to pull the news title and paragraph much easier.  Originally I wasn't able to get this to work because once I was running a "soup.find" it was returning a "list"
	and I wasn't able to run another "soup.find" against a list.

	b.)  In the JPL Featured Image section I was able to find some documentation online that showed how to use "click_link_by_partial_text"  This was very helpful
	because the example that we did in class used "browser.links.find_by_partial_text()" and that was not working for this webpage.  Once I got to the correct page
	it was easy to just use Beautiful Soup to find the block of html code needed...pull the url...and concatenate it to the base url.

	c.)  The Mars Facts table was the easiest part of this section...seeing as it was pretty much a line for line example from when we pulled a table from a webpage
	in class.  I was able to review that section and get this pretty quickly.  The main difference was I had to set the index to the measurement column so that it would
	match the example of what our table was supposed to look like.

	d.)  Finally, the Mars Hemispheres section was pretty tough.  I orignally tried going through and pulling all of the titles and partial url's from the larger block
	of html code.  However, when I was doing that and struggling...I realized that the information I needed was all in four separate blocks of html code and they all were
	a different "<div class="item">".  So, then I was able to use a "for loop" again and go through each one of those 4 sections to pull out all of the information that I
	needed.  The only thing different here was that I actually "visited" each browser inside of the for loop.  So, when I run it you can actually see it visiting all four 
	pages and pulling the info that I need.  I also concatenate everything inside the "for loop" and then I append it to a list of dictionaries that I use later.


2.)  MISSION TO MARS - SCRAPE_MARS.py

	a.)  For this section I pretty much just took my code from the above python code that I wrote and made the adjustments that I needed to in order to make it run 
	without errors.  The main thing I needed to do was change some of the indentation and pull out some of the print statements.


3.)  MISSION TO MARS - APP.py

	a.)  For this section I went back and re-watched the 3rd class of the "web scraping" section again and tried to relearn everything from the Costa Rica example.  
	Once I went through that I was able to write the code for the app.py since the examples were very close to what we are trying to do.  I made the necessary changes
	in order to make everything work...but the idea was generally the same.  I added a collection and it was ready to go. 

	b.)  I set up a connection to mongo...created a "/" route and a "/scrape" route and then I rendered my index.html file so I could pass the information through 
	that I needed to.  I set the variable for the data to "mars" which I then use on the index.html to pull all of the information over.


4.)  MISSION TO MARS - INDEX.html

	a.)  For this section I used bootstrap to pull in a jumbotron, cards, and different container sections in order to block off everything similar to the way it was 
	done on the instructions for the challenge.  The main thing here is for the Mars Hemisphere titles and images I used a loop inside the HTML code using {%%}...since
	the information was actually in a list of dictionaries...and then I filled in the titles and image urls with the cards from bootsrap.  


