This program uses Python 3.9.8

This program uses Scrapy to scrape information from the IRS Prior Year Products page.
It then uses Pandas to analyze the data and return the desired information.
Finally, the program uses Python's Requests Library to get specified PDFs for a given year range.


Required libraries:
Requests:
"pip3 install requests"
Scrapy
"pip3 install Scrapy"
Pandas
"pip3 install pandas"


To Run the Program:
Make sure you are in the "pinwheel" directory.
Open the file named "irsFormSearch.py".
Run the file.
You will be prompted in the command linee to enter your search list. Please input the names of the forms you would like to search for,
separated by a comma and then a space.
    * Ex: Form W-2, Form 1099-A
The program will crawl the IRS Prior Year website and output a CSV of all the returned search data.
It will then go through the CSV file and return the requested JSON data in the command line.
Next, you will be asked in the command line if you would like to download a range of forms.
Input "Y" to continue or "N" to quit.
If you continue, you will be prompted to input the form number, the first year in the range, and then the last year in the range.
The PDFs for your requested files will save to a folder in the "pinwheel" directory.



NOTES:
I come from a Javascript background, so I recognize that there are some flaws in my methodology that stem from being new to Python.
Areas I would improve given more time:
    1. A more streamlined crawler that immediately returns the desired information in the requested format,
    instead of having to go through another function after the website has been crawled.
    2. Error handling throughout the program to make the process more user friendly.
    3. The ability to jump to downloading forms without crawling the web if the necessary data has already been extracted.

THOUGHT PROCESS
The IRS Prior Year Products website sends its search requirement to the database by updating the url parameters.
Therefore, I wanted to create a crawler that takes a list of forms to search, updates the url for each form, and returns the response information.
The search process requires specificity in the returned data - if the search requests information on a Form W-2, it should not receive information on the Form W-2P.
The IRS Prior Year Products website does not offer this specificity in its search, so the returned data must be parsed.
I wrote a function to handle evaluating the returned data, and only output the specified information from the test requirements.
The second part of the test requests that a user may input a specific form and a range of years, and it downloads the PDFs to the computer.
So that the user may know if the form exists and what years are available for download, I wanted to make this second function conditional to the first function
having already run.
It would then anyalyze data that has already been provided by the crawler, and download the forms for the range of years.

The data would flow as such:
    Initiate crawler with search list --> 
    Receive search result data --> 
    Analyze data --> 
    Return specified data in json form -->
    Ask user if they would like to download any of the seached forms --> 
    If yes, have user input desired form and year range --> 
    Download files.