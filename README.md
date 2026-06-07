# Customer Behavior Analysis Dashboard

## 📌 Project Overview

This project analyzes customer shopping behavior data and provides actionable insights through an interactive Power BI dashboard.

The project follows a complete data analytics workflow:

1. Data Collection (CSV Dataset)
2. Data Cleaning & Transformation using Python
3. Data Storage in MySQL Database
4. Data Analysis using SQL
5. Interactive Visualization using Power BI

The objective is to understand customer purchasing patterns, demographics, product preferences, payment behavior, and sales performance.

---

## 🚀 Technologies Used

### Programming & Data Processing
- Python
- Pandas
- SQLAlchemy
- PyMySQL

### Database
- MySQL
- MySQL Workbench

### Visualization
- Power BI

---

## 📂 Project Structure

```text
Customer-Behavior-Analysis/
│
├── customer_shopping_behavior.csv
├── retail_consumers_data.sql
├── eda_of_data.py
├── Customer_Behavior_Dashboard.pbix
├── screenshots/
│   ├── dashboard_overview.png
│   ├── customer_demographics.png
│   └── sales_analysis.png
│
└── README.md
```

---

## 📊 Dataset Features

The dataset contains customer purchase information including:

| Column | Description |
|----------|------------|
| Customer ID | Unique Customer Identifier |
| Age | Customer Age |
| Gender | Customer Gender |
| Item Purchased | Purchased Product |
| Category | Product Category |
| Purchase Amount | Purchase Amount in USD |
| Location | Customer Location |
| Size | Product Size |
| Color | Product Color |
| Season | Purchase Season |
| Review Rating | Product Rating |
| Subscription Status | Subscription Membership |
| Shipping Type | Delivery Method |
| Discount Applied | Discount Usage |
| Previous Purchases | Historical Purchases |
| Payment Method | Payment Mode |
| Frequency of Purchases | Purchase Frequency |

---

## 🔄 Data Processing Workflow

### Step 1: Load Dataset

```python
df = pd.read_csv('customer_shopping_behavior.csv')
```

### Step 2: Handle Missing Values

Missing review ratings are replaced using category-wise median values.

```python
df['Review Rating'] = df.groupby('Category')['Review Rating'] \
                        .transform(lambda x: x.fillna(x.median()))
```

### Step 3: Feature Engineering

Created a new column:

```python
Age Group
```

Categories:

- Young Adult
- Adult
- Middle-aged
- Senior

```python
df['age_group'] = pd.qcut(df['age'],
                          q=4,
                          labels=['Young Adult',
                                  'Adult',
                                  'Middle-aged',
                                  'Senior'])
```

### Step 4: Remove Unnecessary Columns

```python
df.drop('promo_code_used', axis=1)
```

### Step 5: Load Data into MySQL

Using SQLAlchemy:

```python
engine = create_engine(
"mysql+pymysql://username:password@localhost:3306/retail_consumer_data"
)
```

```python
df.to_sql(
    "customer_purchases",
    engine,
    if_exists="replace",
    index=False
)
```

---

## 🗄️ Database Design

Database:

```sql
retail_consumer_data
```

Table:

```sql
customer_purchases
```

The cleaned dataset is stored in MySQL for querying and reporting.

---

## 📈 Power BI Dashboard

The Power BI dashboard provides insights into:

### Customer Demographics
- Age Distribution
- Gender Distribution
- Age Group Analysis

### Sales Analysis
- Total Revenue
- Average Purchase Value
- Sales by Category

### Customer Behavior
- Purchase Frequency
- Subscription Analysis
- Previous Purchases

### Product Insights
- Best Selling Categories
- Product Ratings
- Seasonal Trends

### Payment Analysis
- Payment Method Distribution
- Shipping Type Preferences

---

## 🔍 Key Business Insights

### Customer Insights
- Identify high-value customer segments.
- Understand purchasing habits across age groups.

### Product Insights
- Discover top-performing product categories.
- Analyze customer ratings and preferences.

### Marketing Insights
- Evaluate impact of discounts.
- Compare subscriber vs non-subscriber behavior.

### Sales Insights
- Track revenue trends.
- Analyze seasonal purchasing patterns.

---

## 📸 Dashboard Preview

Add screenshots here:

```text
screenshots/dashboard_overview.png
screenshots/customer_demographics.png
screenshots/sales_analysis.png
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/yourusername/customer-behavior-analysis.git
```

### Install Dependencies

```bash
pip install pandas
pip install sqlalchemy
pip install pymysql
```

### Configure MySQL

Create database:

```sql
CREATE DATABASE retail_consumer_data;
```

### Run ETL Script

```bash
python eda_of_data.py
```

### Open Dashboard

Open:

```text
Customer_Behavior_Dashboard.pbix
```

in Power BI Desktop.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Data Cleaning using Pandas
- Feature Engineering
- MySQL Database Integration
- SQL Querying
- Power BI Dashboard Development
- End-to-End Data Analytics Workflow

---

## 👨‍💻 Author

Shailesh Panghate

### Skills Demonstrated

- Python
- SQL
- MySQL
- Power BI
- Data Cleaning
- Data Visualization
- Business Analytics

---

## ⭐ Future Improvements

- Customer Segmentation using Clustering
- Predictive Purchase Analysis
- Sales Forecasting
- Customer Lifetime Value Analysis
- Real-time Dashboard Integration
