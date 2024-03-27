import pandas
from datetime import datetime

vowels = "aeiou"
temp_list = []

# last name
surname = input("What is your last name? ")

temp_list = [letter.upper() for letter in surname if letter.lower() not in vowels]
temp_list.extend([letter.upper() for letter in surname if letter.lower() in vowels])
while len(temp_list) < 3:
    if [] in temp_list:
        temp_list.pop(temp_list.index([]))
    temp_list.append('X')

cf_surname = "".join(temp_list[:3])
temp_list.clear()


# name
name = input("What is your name? ")
temp_list = [letter.upper() for letter in name if letter.lower() not in vowels]
temp_list.extend([letter.upper() for letter in name if letter.lower() in vowels])
temp_list = list(filter(lambda l: l.isalnum(), temp_list))

while len(temp_list) < 3:
    temp_list.append('X')

cf_name = "".join([temp_list[0], temp_list[2], temp_list[3]])
temp_list.clear()


# date and sex
sex = input("What's your sex? F or M? ")
while sex != "F" and sex != "f" and sex != "M" and sex != "m":
    sex = input("Sex not valid. What's your sex? ")

birth = datetime.strptime(input("When were you born? DD-MM-YYYY "), '%d-%m-%Y')
while birth == ValueError:
    birth = datetime.strptime(input("Invalid date. When were you born? DD-MM-YYYY "), '%d-%m-%Y')

months = "ABCDEHLMPRST"
cf_day = birth.day
cf_month = months[birth.month - 1]
cf_year = datetime.strftime(birth, '%y')

if sex == "F" or sex == "f":
    cf_day += 40

# city
city = input("Where were you born? If you were born outside of Italy, just type the country. ").upper()
data = pandas.read_csv("city_codes.csv")
cf_city = data[data.Ente_Denominazione == city].Codice
while cf_city.to_string(index=False) == "Series([], )":
    cf_city= input("Invalid birthplace. Where were you born? ")

# control
cf_data = cf_surname + cf_name + str(cf_year) + cf_month + str(cf_day) + cf_city.to_string(index=False)
odds = pandas.read_csv("odds.csv")
evens = pandas.read_csv("evens.csv")
codify = pandas.read_csv("codify.csv")
temp_list = [[], []]
sum = 0
for i in range(len(cf_data)):
    if i % 2 == 0: # temp_list[0] has odds, temp_list[1] has evens
        temp_list[0].append(cf_data[i])
    else:
        temp_list[1].append(cf_data[i])
for i in range(len(temp_list[0])):
    value = odds[odds.Character == temp_list[0][i]].Value
    sum += int(value.to_string(index=False))
for i in range(len(temp_list[1])):
    value = evens[evens.Character == temp_list[1][i]].Value
    sum += int(value.to_string(index=False))
control = codify[codify.Num == sum % 26].Code

# result
cf = cf_data + control.to_string(index=False)
print(cf)
