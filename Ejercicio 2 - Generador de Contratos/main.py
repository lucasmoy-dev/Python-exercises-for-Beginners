from datetime import datetime

def replaceText(text):
    filters = [["[COMPANY_NAME]", "Company Name"],
                   ["[EMPLOYEE_NAME]", "Employee Name"],
                   ["[PRICE]", "Price"],
                   ["[CITY]", "City"],
                   ["[COUNTRY]", "Country"]
               ]
    for filter in filters:
        print("What is the " + filter[1] + "?")
        txtInput = input()
        text = text.replace(filter[0], txtInput)

    return text.replace("[CURRENT_DATE]", datetime.today().strftime('%Y-%m-%d'))

contractFile = open("contract.txt", "r")
result = ""


for row in contractFile:
    result += row
result = replaceText(result)

with open("contract_processed.txt", "w") as textFile:
    textFile.write(result)


#  [CURRENT_DATE] [COMPANY_NAME] [EMPLOYEE_NAME] [CITY] [COUNTRY] [PRICE]