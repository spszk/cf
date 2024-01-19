import pandas

vowels = "aeiou"
temp_list = []

# last name
surname = input("What is your last name? ")
cf_surname = ""
for i in range(len(surname)):
    if surname[i].lower() in vowels:
        temp_list.append(i)
    elif surname[i] == " ":
        pass
    else:
        cf_surname += surname[i].upper()
if len(cf_surname) > 3:
    cf_surname = cf_surname[0:3]
elif len(cf_surname) < 3:
    i = 0
    while len(cf_surname) < 3 and i < len(temp_list):
        cf_surname += surname[temp_list[i]].upper()
        i += 1
    while len(cf_surname) < 3:
        cf_surname += "X"
temp_list.clear()

# name
name = input("What is your name? ")
cf_name = ""
for i in range(len(name)):
    if name[i].lower() in vowels:
        temp_list.append(i)
    elif name[i] == " ":
        pass
    else:
        cf_name += name[i].upper()
if len(cf_name) > 3:
    cf_name = cf_name[0] + cf_name[2:4]
elif len(cf_name) < 3:
    i = 0
    while len(cf_name) < 3 and i < len(temp_list):
        cf_name += name[temp_list[i]].upper()
        i += 1
    while len(cf_name) < 3:
        cf_name += "X"
temp_list.clear()

# date and sex
sex = input("What's your sex? F or M?")
birth = input("When were you born? DDMMYYYY")
months = "ABCDEHLMPRST"
cf_day = 0
cf_month = ""
cf_year = 0

if sex != "F" and sex != "f" and sex != "M" and sex != "m":
    sex = input("Sex not valid. What's your sex? ")
elif sex == "F" or sex == "f":
    cf_day += 40

while len(birth) > 8 or len(birth) < 8:
    birth = input("Date format not valid. When were you born? DDMMYYYY ")
cf_day += int(birth[0:2])
cf_month = months[int(birth[2:4]) - 1]
cf_year = birth[6:8]

# city
city = input("Where were you born? ").upper()
data = pandas.read_csv("city_codes.csv")
cf_city = data[data.Ente_Denominazione == city].Codice

# control
cf_data = cf_surname + cf_name + cf_year + cf_month + str(cf_day) + cf_city.to_string(index=False)
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
