
import names  # random name ko get kiya
import random  # random data lene ke liye
import csv
import pandas as pd  #dataframe

namesi = []
emails = []
addreses = []
salaries = []
companyes=[]
no_of_records = 100

print("----------------------name & email-----------------------")
for i in range(no_of_records):
    name = names.get_full_name()   # Returns the first_name plus the last_name, with a space in between
    namesi.append(name)
    email = name.replace(" ","")+"@gmail.com"  #concent 
    emails.append(email)




print("----------------------address-----------------------")

for j in range(no_of_records):
    addresi = ['indore','khategaon','dewas','harda','ujjain','bhopal','shihor']
    addres = random.choice(addresi)

    # addres= random_address.real_random_address_by_state('CA')
    # addreses.append(addres['city'])
    addreses.append(addres)
    # print(addres['city'])

print("----------------------salary-----------------------")
 
# li = ""
for i in range(0,no_of_records):
    sal = random.randint(10000,99999)
    salaries.append(sal)


for j in range(no_of_records):
    comp = ['zecdata','wipro','infosys','tcs']
    company = random.choice(comp)
    companyes.append(company)

fields = ['Name', 'email', 'address', 'salary','company']

rows = []

for i in range(0,no_of_records):
    # print("name :", namesi[i] , "email :", emails[i], "address :" , addreses[i] , "salary :", salaries[i])
    rows.append([namesi[i],emails[i],addreses[i] ,salaries[i],companyes[i]])

print(rows)

filename = "aartiiiicsv.csv"
with open(filename, 'w') as csvfile:  #automatically connecation close  ho jata hai with open se
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields) # fields ki row create
    csvwriter.writerows(rows) # csv ki row create

print("Successfully")
