import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('customer_shopping_behavior.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())

# filling null values(ratings) by grouping of categories
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

print(df.isnull().sum())

print(df.columns)
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)


# create column  age_grooup
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)

print(df[['age', 'age_group']].head(10))

df = df.drop('promo_code_used' , axis = 1)

# Create Engine
engine = create_engine(
    f"mysql+pymysql://root:ShaileshP%40107@localhost:3306/retail_consumer_data"
)


# Load Data
df.to_sql(
    "customer_purchases",
    engine,
    if_exists="replace",
    index=False
)

print(f"{len(df)} records inserted successfully!")

# Verify
result = pd.read_sql(
    "SELECT * FROM customer_purchases LIMIT 5",
    engine
)

print("Results : ", result)