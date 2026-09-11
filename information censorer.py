#just a script that censors a data


Menu_choice = 0

persons = [
        ['john','Snow','20','06','2001','123456789','1111222233334444','visa'],
        ['Bruce','Wayne','01','09','1980','098765432','0000999988887777','MasterCard'],
        ['Peter','Parker','20','04','1970','567345234','3333444455556666','Visa']
]

persons_censored = [

]

while Menu_choice != 3:
    print("if you wish to add a person, type 1,")
    print("if you wish to viev a person, type 2,")
    print("in you wish to quit type 3,")
    Menu_choice = input("type a number:")


    if Menu_choice == "2":


        for i, person in enumerate(persons):
            x = i + 1
            print(x, person[0], person[1])
        name_choice = input("choose the name of the person: ")
        index = int(name_choice) - 1



            # First name
        def censor_first_name(person):
            nametemp = person[0]
            nameLenght = len(nametemp)
            cnameLenght = int(nameLenght - 1)
            name_censored_temp = nametemp[0:1]+"X" * cnameLenght
            return(name_censored_temp)

        print("---------------------")

            #surname
        def censor_surname(person):
            surnametemp = person[1]
            snamelenght = len(surnametemp)
            csnamelenght = int(snamelenght - 1)
            surname_censored_temp = surnametemp[0:1]+"X" * csnamelenght
            return(surname_censored_temp)

            # date of birth
        def dob_censored(person):
            dob_temp_full = person[2]+"-"+person[3]+"-"+person[4]
            dob_temp = person[4]
            dob_censored_temp = "XX-XX-"+dob_temp
            return(dob_censored_temp)


            # phone number
        def pn_censored(person):
            phone_temp = person[5]
            phonenumLenght = len(phone_temp)
            cphoneNumLenght = int(phonenumLenght - 3)
            phone_censored_temp = "X" * int(cphoneNumLenght)+phone_temp[-3:]
            return(phone_censored_temp)


            # card type
        def ct_censored(person):
            card_type_temp = person[7]
            return(card_type_temp)


            # card number
        def cc_num_censored(person):
            card_temp = person[6]
            ccnumLenght = len(card_temp)
            cccnumlenght = int(ccnumLenght - 4)
            card_censored_temp = "X" * cccnumlenght+card_temp[-4:]
            return(card_censored_temp)



        for person in persons:
            name_resoult = censor_first_name(person)
            surname_resoult = censor_surname(person)
            dob_resoult = dob_censored(person)
            pn_resoult = pn_censored(person)
            ccnum_resoult = cc_num_censored(person)
            ct_temp = ct_censored(person)
            add = name_resoult,surname_resoult,dob_resoult,pn_resoult,ccnum_resoult,ct_temp
            persons_censored.append(add)

        print(persons_censored[index])
        print("---------------------")


        uncensor = input("if you wish to uncensor the text type Y:")
        affirm_choice = ["Y","y","yes","yup","yeah"]
        if uncensor in affirm_choice:

            print("---------------------")
            print(persons[index][0])
            print(persons[index][1])
            print(persons[index][2]+"-"+persons[index][3]+ "-"+ persons[index][4])
            print(persons[index][5])
            print(str(persons[index][6])+"-"+str(persons[index][7]))
            print("---------------------")

    #addition script
    if Menu_choice == "1":
        info_choice = 100
        # name
        info_choice = 1
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")

        # birthdate
        print("whats your birth date?")
        dayd = input("day:")
        monthd = input("month:")
        year = input("year:")

        # info
        phone_num = input("Enter your Phone number: ")
        credit_card_num = input("Enter your credit card number: ")
        card_type = input("Enter your card type: ")

        persons.append([name,surname,dayd,monthd,year,phone_num,credit_card_num,card_type])

    if Menu_choice == "3":
        break


