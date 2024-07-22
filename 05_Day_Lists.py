list = [] #1
many =['apple','banana','pineapple','orange','lemon','tomato','lettuce','carrot','onion'] #2
print(len(many)) #3
print(many[0]) #4
print(many[-1]) #4
print(many[4]) #4
mixed_data_types = ['Mohammed Mujahiddin Suhiyini',23,5.6,'Single','Dansoman'] #5
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] #6
print(mixed_data_types) #7
print(it_companies) #8
print(it_companies[0]) #9
print(it_companies[-1]) #9
print(it_companies[3]) #9
it_companies.pop(1)
it_companies.insert(2,"Twitter")
print(it_companies) #10
it_companies.append('Slack')#11
it_companies.append('Instagram')#11
print(it_companies[5])#11
it_companies.insert(5,'Yahoo')#12
print(it_companies[0].upper())#13
print("#;  ".join(it_companies))#14

company = input('Name of company you want to check for: ')
it_companies = [company.upper() for company in it_companies]
if company.upper in it_companies:
    print(f"Yes {company} is present in the list")
else:
    print(f"{company} is not present in the list")
