'''
    Author : Naveen
    Disclaimer : Only for Educational and Practice purpose only
'''
class add:
    def add_to_list(add_item):
        details.append(add_item)

class add_converts:
    def to_lower(to_lower):
        details.append(to_lower.lower())
    def to_cap(to_cap):
        details.append(to_cap.capitalize())
    def to_upper(to_upper):
        details.append(to_upper.upper())
    def convert_a(convert_a):
        if 'a' in convert_a:
            # details.append(convert_a.replace("a", "@"))
            details.append(convert_a.lower().replace("a", "@"))
            details.append(convert_a.capitalize().replace("a", "@"))
            details.append(convert_a.upper().replace("A", "@"))
    def convert_s(convert_s):
        if 's' in convert_s:
            # details.append(convert_s.replace("s", "$"))
            details.append(convert_s.lower().replace("s", "$"))
            details.append(convert_s.capitalize().replace("s", "$"))
            details.append(convert_s.upper().replace("S", "$"))
    def convert_as(convert_as):
        if "a" and "s" in convert_as:
            details.append(convert_as.lower().replace('a', "@").replace('s', '$'))
            details.append(convert_as.capitalize().replace('a', "@").replace('s', '$').replace('S', "$"))
            details.append(convert_as.upper().replace('A', "@").replace('S', '$'))

class add_ends:
    def ends_numbers():
        for i in range(len(details)):
            # print(i + "123")
            details.append(details[i] + "123")
            details.append(details[i] + "1234")
            details.append(details[i] + "@123")
            details.append(details[i] + "@1234")
            details.append(details[i] + "$123")
            details.append(details[i] + "$1234")
            details.append(details[i] + "#123")
            details.append(details[i] + "#1234")
            details.append(details[i] + "*123")
            details.append(details[i] + "*1234")
        
                
details = []

print("\n------------------------------")
print(" Bruteforce Wordlist Generator")
print("------------------------------\n")


victim_name = str(input("[+] Enter Victim's Name : ")).lower()
if victim_name != "":
    add_converts.to_lower(victim_name)   #details.append(victim_name)
    add_converts.to_upper(victim_name)
    add_converts.to_cap(victim_name)
    add_converts.convert_a(victim_name)
    add_converts.convert_s(victim_name)
    add_converts.convert_as(victim_name)
    add_ends.ends_numbers()

victim_DOB = str(input("\n[+] Enter Victim's Birth year : "))
if victim_DOB != "":
    add.add_to_list(victim_DOB);

victim_fav_person = str(input("\n[+] Enter Victim's Fav Person Name : "))
if victim_fav_person != "":
    add_converts.to_lower(victim_fav_person)   #details.append(victim_name)
    add_converts.to_upper(victim_fav_person)
    add_converts.to_cap(victim_fav_person)
    add_converts.convert_a(victim_fav_person)
    add_converts.convert_s(victim_fav_person)
    add_converts.convert_as(victim_fav_person)

victim_fav_person_dob = str(input("\n[+] Enter Victim's Fav Person Birth year : "))
if victim_fav_person_dob != "":
    add.add_to_list(victim_fav_person_dob)

victim_phone_number = str(input("\n[+] Enter Victim's Phone Number : "))
if victim_phone_number != "":
    add.add_to_list(victim_fav_person_dob)
    add.add_to_list(victim_phone_number[:6])
    add.add_to_list(victim_phone_number[6:])
    add.add_to_list(victim_phone_number[-3:-1])
    add.add_to_list(victim_phone_number[-4:-1])

line_1 = [] # Creating a empty list for storaging data
line_2 = [] # Creating a empty list for storaging data

for i in range(len(details)):
    line_1.append(details[i])   # Adding the data in line_1

    for j in range(len(details)):
        line_2.append(details[i] + details[j])  # Adding the data in line_2

file = open('list.txt', 'w')    # to save in file 
for i in line_1:
    file.write(i + "\n")    # adding the words in file
for i in line_2:
    file.write(i + "\n")    # adding the words in file
file.close()

print("")
print(len(line_1) + len(line_2), "lines are generated")
