#just a script that censors a data
from censorersupplementary import persons

print("if you wish to add a person, type 1,")
print("if you wish to viev a person, type 2,")
Menu_choice = input("type a number:")

persons = [
    ['john','Snow','20','06','2001','123456789','1111222233334444','visa'],
    ['Bruce','Wayne','01','09','1980','098765432','0000999988887777','MasterCard'],
    ['Peter','Parker','20','04','1970','567345234','3333444455556666','Visa']
]
persons_censored = [

]


if Menu_choice == "1":
    #name
    name = input("Enter your name: ")
    persons.append(name[3:0])
    surname = input("Enter your surname: ")
    persons.append(surname[3:1])

    #birthdate
    print("whats your birth date?")
    dayd = input("day:")
    persons.append(dayd[3:2])
    monthd = input("month:")
    persons.append(monthd[3:3])
    year = input("year:")
    persons.append(year[3:4])
        #info
    phone_num = input("Enter your Phone number: ")
    persons.append(phone_num[3:5])
    credit_card_num = input("Enter your credit card number: ")
    persons.append(credit_card_num[3:6])
    card_type =input("Enter your card type: ")
    persons.append(card_type[3:7])

if Menu_choice == "2":

    print("1=",persons[0][0],persons[0][1])
    name_choice = input("choose the name of the person: ")



    #censoring script
#First name
nameLenght = len(name)
cnameLenght = int(nameLenght-1)
print(name[0:1],"X"*cnameLenght)

#surname
snamelenght = len(surname)
csnamelenght = int(snamelenght-1)
print(surname[0:1],"X"*csnamelenght)

#date of birth
print("XX-XX-",int(year))

phonenumLenght = len(phone_num)
cphoneNumLenght = int(phonenumLenght - 3)
print("X"*int(cphoneNumLenght),int(phone_num[-3:]))

ccnumLenght = len(credit_card_num)
cccnumlenght = int(ccnumLenght - 4)
print("X"*cccnumlenght,int(credit_card_num[-4:]))
print(card_type)




