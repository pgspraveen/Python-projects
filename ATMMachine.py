print("Welcome to ATM")
def ATM():
    chance=3
    while chance>0:
        pin = int(input("Enter your pin: "))
    
        accounts = {
            1234: 50000,
            3456: 60000,
            5678: 70000,
            7890: 80000
        }
    
        if pin in accounts:
            print("1. Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
        
            option = int(input("Enter your option: "))
        
            if option == 1:
                print("Balance:", accounts[pin])
            elif option == 2:
                amount = int(input("Enter amount to deposit: "))
                accounts[pin] += amount
                print("Deposit successful. Total amount:", accounts[pin])
            elif option == 3:
                amount = int(input("Enter amount to withdraw: "))
                if amount > accounts[pin]:
                    print("Insufficient balance.")
                else:
                    accounts[pin] -= amount
                    print("Withdrawal successful. Remaining amount:", accounts[pin])
            elif option == 4:
                print("Exiting...")
            else:
                print("Invalid option.")
        else:
            print("Invalid PIN. You have", chance-1, "chances remaining.")
            chance -= 1
    
    if chance == 0:
        print("Too many incorrect attempts. Exiting...")
            
ATM()
