import edgar
edgar = edgar.Edgar()
possible_companies = edgar.findCompanyName("Cisco System")
print(possible_companies)

#get Oracle Corp's last 5 form 10-K's
company = edgar.Company("Oracle Corp", "0001341439")
tree = company.getAllFilings(filingType = "10-K")
docs = edgar.getDocuments(tree, noOfDocuments=5)
#docs is an array of strings, each one is the full text doc

#SIC CODES
url = "https://www.sec.gov/info/edgar/siccodes.htm"
#Developer page
#https://www.sec.gov/developer
