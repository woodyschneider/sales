from crunchbase import CrunchBase
# may be outdated. switched all code to __init__.py
import doctest
doctest.testfile('README.md', verbose=False)

cb = CrunchBase('erne3k43qk8jv2925mgwdf98')
#company = cb.getCompanyData('Fundly')
'''
print company
print company['name']
print company['total_money_raised']
print company['funding_rounds'][1]['investments']#['financial_org']
'''
#investors = cb.listCompanyInvestors('Fundly')
#print investors

investor_list = ['Andreessen Horowitz', 'Sequoia Capital']
investor_list = ['Kapor Capital'] #this is just to keep it simple


master = {} #dict

for investor in investor_list:
	print "Full List for: " + investor	
	companies = cb.listInvestorPortfolio(investor)
	for company in companies:		
		master[company] = {"company_name": company} # grab the name for this company and begin that company's object'
		print company + " was invested in by " + investor
		master[company]["investor"] = investor #add investor to list
		print "Getting additional info for: " + company + "..."
		try:
			company_data = cb.getCompanyData(company)
			print "	... rectifying details are availible about: " + company
			for key in company_data:
				master[company][key] = company_data[key]
				print "			"+ key
			
		except:
			print "!!! -- Something went wrong when we tried to get extra data for: " + company


## Now let's grab the URL
for company in master:
	print company.name


# print str(master)






