def show_dataset(data):
    print("\nSales Dataset\n")
    print(data)


def summary(data):
    print("\nSummary")
    print("-" * 30)
    print("Total Sales :", data["Sales"].sum())
    print("Total Profit:", data["Profit"].sum())
    print("Average Sales :", round(data["Sales"].mean(), 2))
    print("Average Profit:", round(data["Profit"].mean(), 2))
    print("Maximum Sales :", data["Sales"].max())
    print("Minimum Sales :", data["Sales"].min())