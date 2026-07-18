# Sales Dashboard 

The Sales Dashboard Analyzer allows users to visualize sales and profit trends from a CSV dataset through a clean, terminal-based interactive menu. It is an excellent starting point for anyone looking to bridge the gap between data analysis and data visualization using Python.

## 🚀 Features
- **Modular Architecture:** Organized into separate files (data_loader, dashboard, visualization) for clean code management.

- **Statistical Analysis:** Quickly calculate total sales, profit, averages, and extreme values (Max/Min).

- **Data Visualization:** Generate professional charts including:

    - **Line Charts: To track monthly sales trends.

    - **Bar Charts:** To compare monthly profit distribution.

    - **Multi-Series Plotting:** Comparative analysis of Sales vs. Profit in a single view.

    - **Interactive Interface:** A user-friendly command-line menu for seamless navigation.

## 📂 Project Structure
```text
Sales_Dashboard/
│
├── main.py          # Entry point of the application
├── dashboard.py     # Logic for data exploration and statistics
├── data_loader.py   # Handles CSV file loading logic
├── sales_data.py    # Source data file
├── visualization.py # Module for Matplotlib plotting
├── requirements.txt # Project dependencies
└── README.md        # README.md File