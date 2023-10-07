print("Welcome")
print("   to")
print("Piggy Bank ATM")
print("Insert your card")
print("Please wait your card is being processed...")
print("Select your language preference:")
print("1. English")
print("2. Hindi")
print("3. Urdu")
print("Select a no. from above languages.")
select=int(input())
if select==1:
  print("Menu:")
  print("1. Withdrawal")
  print("2. Deposit")
  print("3. Balance")
  print("4. Change pin")
  print("Select a no. from above menu.")
  menu=int(input())
  if menu==1:
    print("Enter amount")
    amount=int(input())
    if amount>0 and amount<=20000:
      print("Enter pin")
      pin=int(input())
      if pin>999 and pin<10000:
        print("XXXX")
        print("Wait! Your transaction is being processed...")
        print(f"Transaction complete, your remaining balance is {20000-amount}.")
        print("Please collect Your money")
        print("Remove your card")
        print("Print receipt:")
        print("(Y/N)")
        receipt=input()
        receipt=receipt.upper()
        if receipt=="Y":
          print("Collect receipt")
          print("Thankyou for using ATM")
        elif receipt=="N":
          print("Thankyou for using ATM")  
        else:
          print()
      else:
          print("Invalid pin, please remove your card and try again.")
    else:
      print("Insufficient balance! Thankyou, please remove your card.")
  elif menu==2:
    print("Enter amount")
    amount=int(input())
    if amount>0:
      print("Enter pin")
      pin=int(input())
      if pin>999 and pin<10000:
        print("XXXX")
        print("Wait! Your transaction is being processed...")
        print(f"Transaction complete, Your balance is {20000+amount}.")
        print("Remove your card")
        print("Print receipt:")
        print("(Y/N)")
        receipt=input()
        receipt=receipt.upper()
        if receipt=="Y":
          print("Collect receipt")
          print("Thankyou for using ATM")
        elif receipt=="N":
          print("Thankyou for using ATM")
        else:
          print()  
      else:
        print("Invalid pin, please remove your card and try again.")
    else:
      print("Insufficient amount, please remove your card.")
  elif menu==3:
    print("Enter pin")
    pin=int(input())
    if pin>999 and pin<10000:
      print("XXXX")
      print("Wait! Your transaction is being processed...")
      print("Transaction complete, Your balance is 20,000.")
      print("Remove your card")
      print("Print receipt:")
      print("(Y/N)")
      receipt=input()
      receipt=receipt.upper()
      if receipt=="Y":
        print("Collect receipt")
        print("Thankyou for using ATM")
      elif receipt=="N":
        print("Thankyou for using ATM")
      else:
        print()
    else:
      print("Invalid pin, please remove your card and try again.")
  elif menu==4:
    print("Enter pin")
    pin=int(input())
    if pin>999 and pin<10000:
      print("XXXX")
      print("Enter phone no.")
      phone_no=int(input())
      if phone_no>999999999 and phone_no<10000000000:
        phone_no=str(phone_no)
        print(f"An OTP means a temporary 6 digit One Time Password has been sent to you via SMS on this no. (91 XXX-XXX-{phone_no[6:]}) that is valid only for one time.")
        print("Enter OTP:")
        otp=int(input())
        Otp=str(otp)
        if otp>0 and otp<1000000 and len(Otp)==6:
          print("XXXXXX")
          print("Enter new pin.")
          new_pin=int(input())
          if new_pin!=pin:
            if new_pin>999 and new_pin<10000:
              print("XXXX")
              print("Confirm pin")
              confirm_pin=int(input())
              if new_pin==confirm_pin:
                print("XXXX")
                print("Pin successfully changed")
                print("Remove your card")
                print("Thankyou for using ATM")
              else:
                print("Incorrect pin, please enter same pin")
            else:
              print("Invalid new_pin! Pin must be 4 digit and no leading zeroes.")
              print("Please try again.")
          else:
            print("Choose a new pin and try again.")

        else:
          print("Incorrect OTP, please try again.")
      else:
        print("Invalid phone no. please try again.")        
    else:
      print("Invalid pin, please remove your card and try again.")
  else:
    print("Invalid option, please remove your card and try again.")
elif select==2 or select==3:
  print("We sincerely regret the inconvenience caused to you. We are working on it")
else:
  print("Invalid option, please remove your card and try again.")