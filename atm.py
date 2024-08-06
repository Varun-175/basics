def option_to_be_performed(num):
    bal=5000
    if num==1:
        pin=int(input("\nEnter your four digit pin number: "))
        k=len(str(pin))
        if k==4:
            amount=int(input("\nEnter the amount to be deposited: "))
            if amount<100001:
                print("\nPlace the amount properly inside the CDM machine\n\n*** Processing ***\n\nAmount is: ",amount,"\nChoose the option:")
                a=int(input("\n1.Confirm\n2.Add money\n"))
                bal1=bal+amount
                if a==1:
                    print("\nYour deposit is successful\nWould you want to see your balance\n1.Yes\n2.No")
                    yn=int(input())
                    if yn==1:
                        print("Your available balance is: ",bal1,"\nThank You\nExiting!!")
                    else:
                        print("\nThank You\nExiting!!\n")
                else:
                    am=int(input("\nEnter the amount: "))
                    bal2=bal1+am
                    print("\nYour deposit is successful\nWould you want to see your balance\n1.Yes\n2.No\n")
                    yn1=int(input())
                    if yn1==1:
                        print("\nYour available balance is: ",bal2,"\nThank You\nExiting!!")
                    else:
                        print("\nThank You\nExiting!!\n")
            else:
                print("\nYour deposit limit is only upto 100000\n\nYour transaction is cancelled")
        else:
            print("\n**OOPS**   It is not a valid pin-number!!\n\nYour transaction is cancelled\n")
    elif num==2:
        pin=int(input("\nEnter your four digit pin number: "))
        k=len(str(pin))
        if k==4:
            amount=int(input("\nEnter the amount to be withdrawn: "))
            if (amount<=bal) and (amount>=100):
                if amount%10==0:
                    print("\nPlease wait while your transaction is being processed\n\nPlease collect your cash\n")
                    bal1=bal-amount
                    print("\nYour withdrawal is successful\nWould you want to see your balance\n1.Yes\n2.No\n")
                    yn1=int(input())
                    if yn1==1:
                        print("\nYour available balance is: ",bal1,"\nThank You\nExiting!!")
                    else:
                        print("\nThank You\nExiting!!\n")
                else:
                    print("\nRequested amount cannot be withdrawn\nYour transaction is declained !!\n")
            elif amount>bal:
                print("\n** Insufficient Balance **\n\nYour transaction is cancalled\n")
            else:
                print("\nRequested amount cannot be withdrawn\nLast transaction is declained !!\n")
        else:
            print("\n**OOPS**   It is not a valid pin-number!!\n\nYour transaction is cancelled\n")
    
    elif num==3:
        pin=int(input("\nEnter your four digit pin number: "))
        k=len(str(pin))
        if k==4:
            print("\nChoose your account-type:\n1.Savings\n2.Current\n")
            at=int(input())
            if at==1 or at==2:
                print("\nYour available balance is: \n\nRs: ",bal,"/-")
                print("\nThank You\nExiting!!\n")
            else:
                print("\nYour transaction is cancelled\n\nThank You\n")
        else:
            print("\n**OOPS**   It is not a valid pin-number!!\n\nYour transaction is cancelled\n")

    elif num==4:
        acc_no=int(input("\nPlease enter your 11-digit account number: "))
        acc_no1=int(input("\nRe-enter your account number: "))
        k=len(str(acc_no))
        if k==11 and acc_no==acc_no1:
            mn=int(input("\nEnter your 10-digit mobile number: "))
            mn1=int(input("\nRe-enter your mobile number: "))
            k1=len(str(mn))
            if k1==10 and mn==mn1:
                print("\nSelect the option:\n1.Cardless Deposit\n2.Cardless Withdraw")
                op=int(input())
                if op==1:
                    amount=int(input("\nEnter the amount to be deposited: "))
                    if amount<100001:
                        print("\nPlace the amount properly inside the CDM machine\n\n*** Processing ***\n\nAmount is: ",amount,"\nChoose the option:")
                        a=int(input("1.Confirm\n2.Add money\n"))
                        bal1=bal+amount
                        if a==1:
                            print("\nYour deposit is successful\nWould you want to see your balance\n1.Yes\n2.No")
                            yn=int(input())
                            if yn==1:
                                print("\nYour available balance is: ",bal1,"\nThank You\nExiting!!")
                            else:
                                print("\nThank You\nExiting!!\n")
                        else:
                            am=int(input("\nEnter the amount: "))
                            bal2=bal1+am
                            print("\nYour deposit is successful\nWould you want to see your balance\n1.Yes\n2.No\n")
                            yn1=int(input())
                            if yn1==1:
                                print("\nYour available balance is: ",bal2,"\nThank You\nExiting!!\n")
                            else:
                                print("\nThank You\nExiting!!\n")
                    else:
                        print("\nYour deposit limit is only upto 100000\n\nYour transaction is cancelled\n")
                elif op==2:
                    amount=int(input("\nEnter the amount to be withdrawn: "))
                    if (amount<=bal) and (amount>=100):
                        if amount%10==0:
                            print("\nPlease wait while your transaction is being processed\n\nPlease collect your cash\n")
                            bal1=bal-amount
                            print("\nYour withdrawal is successful\n\nWould you want to see your balance\n1.Yes\n2.No\n")
                            yn1=int(input())
                            if yn1==1:
                                print("\nYour available balance is: ",bal1,"\nThank You\nExiting!!\n")
                            else:
                                print("\nThank You\nExiting!!\n")
                        else:
                            print("\nRequested amount cannot be withdrawn\n\nYour transaction is declained !!\n")
                    elif amount>bal:
                        print("\n** Insufficient Balance **\n\nYour transaction is cancalled\n")
                    else:
                        print("\nRequested amount cannot be withdrawn\n\nLast transaction is declained !!\n")
                else:
                    print("\nYour transaction is cancelled\nThank You\n")
            else:
                print("\n** OOPS **  It,s not a valid mobile number\nYour transaction is cancelled\n")
        else:
            print("\n** OOPS **  It,s not a valid account number\nYour transaction is cancelled\n")

    else:
        print("\nLast transaction is cancelled\n")

print("\nHello ! Welcome to the SBI ATM\n")
print("Choose an option:\n1.Domestic\n2.International\n")
n=int(input())
if n==1 or n==2:
    print("\nChoose an option:\n1.Deposit\n2.Withdraw\n3.Balance Enquiry\n4.Cardless Transactions\n5.Cancel\n")
    num=int(input())
    option_to_be_performed(num)
else:
    print("\nTransaction is cancelled\n")