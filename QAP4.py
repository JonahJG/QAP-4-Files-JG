# QAP 4. One Step Insurance Comapny, a program to enter and calculate new insurace policy information
# Author: Jonah Greening                        Date:

import Validate as V
import FormatValues as FV
import datetime
# Open OSICDef.dat file to read the variables

f = open("OSICDef.dat", "r")
NEXT_POLICY_NUM = int(f.readline())
POLICY_DATE = (f.readline())
BASE_RATE = float(f.readline())
ADD_CAR_DISC = float(f.readline())
EXTRA_LIABILITY = float(f.readline())
GLASS_COVER = float(f.readline())
LOANER_CAR = float(f.readline())
HST_RATE = float(f.readline())
PROC_FEE_MON_PAY = float(f.readline())
f.close()

while True:

    while True:
        CusFName = input("Enter the customer's first name: ").title()
        if CusFName == "":
            print("The customer's first name cannot be blank. Please re-enter.")
        elif CusFName.isalpha() == False:
            print("Invalid characters in customer's first name. Please re-enter")
        else:
            break



    while True:

        CusLName = input("Enter the customer's last name: ").title()

        if CusLName == "":
            print("The customer's last name cannot be blank. Please re-enter.")
        elif CusLName.isalpha() == False:
            print("Invalid characters in customer's last name. Please re-enter")
        else:
            break

    StAdd = input("Enter the customer's street address: ")
    City = input("Enter the customer's city: ")
    Prov = input("Enter the customer's province: ")
    PostCode = input("Enter the customer's postal code: ").upper()
    PhoneNum = input("Enter the customer's phone number (##########): ")
    NumCars = int(input("Enter the number of cars on the policy: "))

    while True:
        ExtraLiabRate = 0
        Discount = 0
        ExtraLiability = input("Would the customer like to purchase extra liability? (Y/N): ").upper()
        if ExtraLiability == "":
            print("Field cannot be blank. Please re-enter.")
        elif ExtraLiability != "Y" and ExtraLiability != "N":
            print("Must be Y or N. Please re-enter.")
        elif ExtraLiability == "Y":
            Discount = (BASE_RATE * ADD_CAR_DISC) * NumCars
            ExtraLiabRate = (NumCars * EXTRA_LIABILITY)
            break
        else:
            Discount = 0
            ExtraLiabRate = 0
            break

    while True:
        GlassRate = 0
        Glass = input("Would the customer like optional glass coverage? (Y/N): ").upper()
        if Glass == "":
            print("Field cannot be blank. Please re-enter.")
        elif Glass != "Y" and Glass != "N":
            print("Must be Y or N. Please re-enter.")
        elif Glass == "Y":
            GlassRate = NumCars * GLASS_COVER
            break
        else:
            GlassRate = 0
            break

    while True:
        LoanerCar = input("Will the customer be using a loaner car? (Y/N): ").upper()

        if LoanerCar == "":
            print("Field cannot be blank. Please re-enter.")
        elif LoanerCar != "Y" and LoanerCar != "N":
            print("Must be Y or N. Please re-enter.")
        elif LoanerCar == "Y":
            LoanCarRate = NumCars * LOANER_CAR
            break
        else:
            LoanCarRate = 0
            break

    PolicyNum = NEXT_POLICY_NUM

    Premium = BASE_RATE + Discount
    TotalExtraCosts = ExtraLiabRate + LoanCarRate + GlassRate
    TotalPremium = Premium + TotalExtraCosts
    HST = TotalPremium * HST_RATE
    TotalCost = TotalPremium + HST
    MonthPay = (TotalPremium + PROC_FEE_MON_PAY) / 8
    POLICY_DATE = datetime.datetime.now()



    while True:

        FullOrMon = input("Would the customer like to pay in full, or on a monthly basis? (F/M): ").upper()
        if FullOrMon == "":
            print("Field cannot be blank. Please re-enter.")
        elif FullOrMon != "M" and FullOrMon != "F":
            print("Must be F or M. Please re-enter.")
        elif FullOrMon == "M":
            MonthPay = (TotalPremium + PROC_FEE_MON_PAY) / 8
            break
        else:
            break

    CusName = CusFName + " " + CusLName
    print()
    print("            One Stop Insurance Company")
    print("--------------------------------------------------")
    print(f"Policy number: {NEXT_POLICY_NUM:<4d}-{CusFName[0]}{CusLName[0]}    Policy date: {FV.FDateS(POLICY_DATE)}")
    print()
    print("Customer details:                      Phone:")
    print(f"{CusName:<15s}                        {PhoneNum:<10s}")
    print(f"{StAdd}")
    print(f"{City}, {Prov} {PostCode} ")
    print("--------------------------------------------------")
    print(f"Number of cars on policy:                       {NumCars:>1d}")
    print(f"Extra liability:                                {ExtraLiability:>1s}")
    print(f"Glass coverage:                                 {Glass:>1s}")
    print(f"Loaner car:                                     {LoanerCar:>1s}")
    print(f"Payment option:                                 {FullOrMon:>1s}")
    print("                                         ----------")
    print(f"Premium cost:                            {FV.FDollar2(Premium):>9s}")
    print(f"Extra costs:                             {FV.FDollar2(TotalExtraCosts):>9s}")
    print(f"Total premium cost:                      {FV.FDollar2(TotalPremium):>9s}")
    print("                                         ----------")
    print(f"HST:                                     {FV.FDollar2(HST):>9s}")
    print(f"Total cost:                              {FV.FDollar2(TotalCost):>9s}")
    print("                                         ----------")
    if FullOrMon == "M":
        print(f"Monthly payment:                         {FV.FDollar2(MonthPay):>9s}")
    print("---------------------------------------------------")
    print()


    f = open("Policies.dat", "a")

    f.write("{}, ".format(str(NEXT_POLICY_NUM)))
    f.write("{}, ".format(FV.FDateS(POLICY_DATE)))
    f.write("{}, ".format(CusName))
    f.write("{}, ".format(StAdd))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Prov))
    f.write("{}, ".format(str(NumCars)))
    f.write("{}, ".format(ExtraLiability))
    f.write("{}, ".format(Glass))
    f.write("{}, ".format(LoanerCar))
    f.write("{}, ".format(FullOrMon))
    f.write("{}\n".format(str(TotalPremium)))
    f.close()

    NEXT_POLICY_NUM += 1

    Cont = input("Would you like to make another claim? (Y/N): ").upper()
    if Cont == "N":
        break
    print()
    print("Policy information processed and saved.")


    f = open("OSICDef.dat", "w")

    f.write("{}\n".format(str(NEXT_POLICY_NUM)))
    f.write("{}\n".format(FV.FDateS(POLICY_DATE)))
    f.write("{}\n".format(str(BASE_RATE)))
    f.write("{}\n".format(str(ADD_CAR_DISC)))
    f.write("{}\n".format(str(EXTRA_LIABILITY)))
    f.write("{}\n".format(str(GLASS_COVER)))
    f.write("{}\n".format(str(LOANER_CAR)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(PROC_FEE_MON_PAY)))

    f.close()




