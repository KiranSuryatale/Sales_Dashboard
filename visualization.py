import matplotlib.pyplot as plt


def sales_chart(data):
    plt.figure(figsize=(10,5))
    plt.plot(data["Month"], data["Sales"], marker="o")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.grid()
    plt.show()


def profit_chart(data):
    plt.figure(figsize=(10,5))
    plt.bar(data["Month"], data["Profit"])
    plt.title("Monthly Profit")
    plt.xlabel("Month")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.grid()
    plt.show()


def sales_profit_chart(data):
    plt.figure(figsize=(10,5))
    plt.plot(data["Month"], data["Sales"], marker="o", label="Sales")
    plt.plot(data["Month"], data["Profit"], marker="s", label="Profit")
    plt.title("Sales vs Profit")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.legend()
    plt.grid()
    plt.show()