import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

df = pd.read_csv('netflix_titles.csv')
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
sns.countplot(x='type', data=df, palette=['#FF6B6B', '#4D96FF'])
plt.title('Movies vs TV Shows')

plt.subplot(2,2,2)
df['year_added'].value_counts().sort_index().plot(kind='line', color='#FF9F1C')
plt.title('Titles Added by Year')

plt.subplot(2,2,3)
df['country'].dropna().str.split(', ').explode().value_counts().head(10).plot(kind='barh', color='#6A4C93')
plt.title('Top 10 Countries')

plt.subplot(2,2,4)
df['listed_in'].dropna().str.split(', ').explode().value_counts().head(10).plot(kind='bar', color='#43AA8B')
plt.title('Top 10 Genres')

plt.tight_layout()
plt.show()
