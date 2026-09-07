#just a script that censors a data
    #name
name = input("Enter your name: ")
surname = input("Enter your surname: ")
    #birthdate
print("whats your birth date?")
dayd = input("day:")
monthd = input("month:")
year = input("year:")
    #info
phone_num = input("Enter your Phone number: ")
credit_card_num = input("Enter your credit card number: ")
#card_type =input("Enter your card type: ")

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




