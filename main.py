from data_loader import load_data
from dashboard import *
from visualization import *

data = load_data()

if data is None:
    exit()

while True:

    print("\n" + "=" * 40)
    print("      SALES DASHBOARD")
    print("=" * 40)

    print("1. Show Dataset")
    print("2. Summary")
    print("3. Monthly Sales Chart")
    print("4. Monthly Profit Chart")
    print("5. Sales vs Profit")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_dataset(data)

    elif choice == "2":
        summary(data)

    elif choice == "3":
        sales_chart(data)

    elif choice == "4":
        profit_chart(data)

    elif choice == "5":
        sales_profit_chart(data)

    elif choice == "6":
        print("Thank You...")
        break

    else:
        print("Invalid Choice")