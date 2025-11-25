import pandas as pd
import matplotlib.pyplot as plt
#load the data
df = pd.read_csv('data/vgsales.csv')
#explore the data
print(df.head())
print(df.info())
print(df.describe())
# Question 1: What are the top 10 best-selling games globally?
top_10_games = df.nlargest(10, 'Global_Sales')[['Name', 'Global_Sales']]
print("\nTop 10 Best-Selling Games:")
print(top_10_games)

plt.figure(figsize=(10, 6))
plt.barh(top_10_games['Name'], top_10_games['Global_Sales'])
plt.xlabel('Global Sales (millions)')
plt.title('Top 10 Best-Selling Video Games')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('top_10_games.png')
plt.close()

# Question 2: Which genre is most popular by total sales?
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
print("\nTotal Sales by Genre:")
print(genre_sales)

plt.figure(figsize=(10, 6))
plt.bar(genre_sales.index, genre_sales.values)
plt.xlabel('Genre')
plt.ylabel('Total Sales (millions)')
plt.title('Video Game Sales by Genre')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_genre.png')
plt.close()

# Question 3: How have game sales changed over time?
# Remove missing years first
df_clean = df.dropna(subset=['Year'])
sales_by_year = df_clean.groupby('Year')['Global_Sales'].sum()
print("\nSales Trend Over Time:")
print(sales_by_year.tail(10))

plt.figure(figsize=(12, 6))
plt.plot(sales_by_year.index, sales_by_year.values, marker='o')
plt.xlabel('Year')
plt.ylabel('Total Sales (millions)')
plt.title('Video Game Sales Over Time')
plt.grid(True)
plt.tight_layout()
plt.savefig('sales_over_time.png')
plt.close()

# Question 4: Which publishers have the most games?
top_publishers = df['Publisher'].value_counts().head(10)
print("\nTop 10 Publishers by Number of Games:")
print(top_publishers)

plt.figure(figsize=(10, 6))
plt.barh(top_publishers.index, top_publishers.values)
plt.xlabel('Number of Games')
plt.title('Top 10 Publishers by Game Count')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('top_publishers.png')
plt.close()

# Question 5: Which region buys the most games?
region_sales = {
    'North America': df['NA_Sales'].sum(),
    'Europe': df['EU_Sales'].sum(),
    'Japan': df['JP_Sales'].sum(),
    'Other': df['Other_Sales'].sum()
}
print("\nTotal Sales by Region:")
for region, sales in region_sales.items():
    print(f"{region}: {sales:.2f} million")

plt.figure(figsize=(8, 8))
plt.pie(region_sales.values(), labels=region_sales.keys(), autopct='%1.1f%%')
plt.title('Video Game Sales by Region')
plt.tight_layout()
plt.savefig('sales_by_region.png')
plt.close()

print("\nAnalysis complete! Check your project folder for the visualizations.")