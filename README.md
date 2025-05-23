# Elevate-Labs-Internship-Task-8

# Superstore Sales Dashboard Design

## 📊 Objective
Design a clean, interactive dashboard that visualizes sales performance by product category, region, and month. This task demonstrates the ability to work with business datasets and communicate insights visually.

---

## 🗂️ Dataset
We used the [Superstore Dataset from Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final), which contains:

- `Order Date` – Date of purchase
- `Region` – Geographical region
- `Category` – Product category (e.g., Furniture, Technology)
- `Sales` – Sales value
- `Profit` – Profit earned per sale

---

## 🛠 Tools Used
- **Power BI** (you can also use Tableau)
- **Python + Pandas** for data cleaning

---

## Data Cleaning

**Performed in Python (see `data_cleaning.py`):**
- Checked for and handled missing values (none found).
- Removed duplicate rows.
- Renamed columns to lowercase with underscores.
- Converted date columns (`order_date`, `ship_date`) to datetime format.
- Ensured correct data types for numeric columns (`sales`, `profit`, `quantity`, `discount`).
- Saved the cleaned data as `cleaned_superstore.csv`.

---

## 📈 Visuals in the Dashboard
1. **Line Chart**: Sales over months
2. **Bar Chart**: Sales and Profit by region
3. **Donut Chart**: Sales by category
4. **Slicers/Filters**: Region, Category and Order Date

---

## 💡 Key Insights

1. **West region consistently had the highest sales** from Q3 2021 to Q2 2022.
2. **Technology category had the highest profit margins** across all regions.
3. **Furniture sales dropped in Q4 2021**, despite increased marketing efforts.
4. **South region showed steady growth in sales** but had **relatively lower profit margins**.

---

## 📁 Files Included
- `Superstore Sales Dashboard.pbix` – Power BI Dashboard File
- `Superstore Sales Dashboard Insights.pptx` – Slide with summarized insights
- `Superstore Sales Dashboard.pdf` -  Dashboard pdf
- `cleaned_superstore.csv` - Superstore Dataset
- `data_cleaning.py` - Data Cleaning Python Script
- `README.md` – This file

---
