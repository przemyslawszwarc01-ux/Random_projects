persons = [
    ['john','Snow','20','06','2001','123456789','1111222233334444','visa'],
    ['Bruce','Wayne','01','09','1980','098765432','0000999988887777','MasterCard'],
    ['Peter','Parker','20','04','1970','567345234','3333444455556666','Visa']
]

persons_censored = [

]

print("1=", persons[0][0], persons[0][1])
name_choice = input("choose the name of the person: ")

if name_choice == "1":
    nametemp = persons[0][0]
    # First name
    nameLenght = len(nametemp)
    cnameLenght = int(nameLenght - 1)
    name_censored_temp = nametemp[0:1]+"X" * cnameLenght
    print(name_censored_temp)
    persons_censored.append(name_censored_temp)
    #surname
    surnametemp = persons[0][1]
    snamelenght = len(surnametemp)
    csnamelenght = int(snamelenght - 1)
    surname_censored_temp = surnametemp[0:1]+"X" * csnamelenght
    print(surname_censored_temp)
    persons_censored.append(surname_censored_temp)
    # date of birth
    dob_temp_full = persons[0][2]+"-"+persons[0][3]+"-"+persons[0][4]
    dob_temp = persons[0][4]
    dob_censored_temp = "XX-XX-"+dob_temp
    persons_censored.append(dob_censored_temp)
    print(dob_censored_temp)
    # phone number
    phone_temp = persons[0][5]
    phonenumLenght = len(phone_temp)
    cphoneNumLenght = int(phonenumLenght - 3)
    phone_censored_temp = "X" * int(cphoneNumLenght)+phone_temp[-3:]
    persons_censored.append(phone_censored_temp)
    print(phone_censored_temp)
    # card type
    cart_type_temp = persons[0][7]
    persons_censored.append(cart_type_temp)
    # card number
    card_temp = persons[0][6]
    ccnumLenght = len(card_temp)
    cccnumlenght = int(ccnumLenght - 4)
    card_censored_temp = "X" * cccnumlenght+card_temp[-4:]
    print(card_censored_temp, cart_type_temp)

    uncensor = input("if you wish to uncensor the text type Y:")
    if uncensor == "Y":
        print(nametemp)
        print(surnametemp)
        print(dob_temp_full)
        print(phone_temp)
        print(str(card_temp)+"-"+str(card_censored_temp))






