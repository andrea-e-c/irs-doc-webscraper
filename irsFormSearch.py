from posixpath import dirname
import requests
import json
import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess
from irs_forms.spiders.forms_spider import FormsSpider
import os

# ------ DEFINES SEARCH LIST ------
inputToFind = input("Please enter your search list as a string, separated by commas:" )

# ------ CONVERT INPUT STRING TO LIST ------
toFind = inputToFind.split(", ")

# ------ INITIATE SPIDER TO CONDUCT WEB SEARCH ------
process = CrawlerProcess()
for form in toFind:
    form = form.replace(" ", "+")
    process.crawl(FormsSpider, search=form)
process.start()

# ------ INITIATE PANDAS TO READ CSV OUTPUT BY SPIDER ------
df = pd.read_csv('forms_data.csv')

# ------ CONVERT DATA TO PROPER TYPES ------
df['year'] = pd.to_numeric(
    df['year'], 
    errors='coerce'
).fillna(0).astype('int')

df['form_title'] = df['form_title'].astype(str)

# ------ FUNCTION TO OUTPUT REQUESTED INFORMATION ------
def searchFilesForInfo(formsToFind):
    for form in formsToFind:
        allDocs = df[df["form_number"] == form]
        formNumber = allDocs["form_number"].iloc[0]
        formTitle = allDocs["form_title"].iloc[0]
        formTitle = formTitle.strip("\n\t        \t")
        maxYear = int(allDocs["year"].max())
        minYear = int(allDocs["year"].min())
        result = {
            "form_number": formNumber,
            "form_title":  formTitle,
            "min_year": minYear,
            "max_year": maxYear
        }
        print(json.dumps(result))
searchFilesForInfo(toFind)

# ------ INITIATE PART 2 OF TEST ------
download = input("Would you like to download the PDFs for a specific form? [Y/N]" )
if download == "N" or "n":
    print("Exiting program.")
    exit()
elif download == "Y" or "y":
    formNumber = input("Input form name:" )
    firstYear = input("Start year:" )
    lastYear = input("End year:" )
    firstYear = float(firstYear)
    lastYear = float(lastYear)
    # ------ FUNCTION TO CREATE DIRECTORY AND SAVE PDFS ------
    def saveFilesToSystem():
        forms = df[df["form_number"]== formNumber]
        selectedYears = forms[(forms["year"] >= firstYear) & (forms["year"] <= lastYear)]
        pdfs = selectedYears["link"]
        urls = pdfs.values.tolist()
        folderName = formNumber
        os.mkdir(folderName)
        for url in urls:
            names = url.split('/')
            name = names[-1]
            file_name = f'{name}'
            file = os.path.join(folderName, file_name)
            response = requests.get(url)
            with open(file, 'wb') as doc:
                doc.write(response.content)
    saveFilesToSystem()
