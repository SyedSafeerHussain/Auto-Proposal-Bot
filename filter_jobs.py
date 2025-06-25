import pandas as pd
import os
folder_path=os.path.dirname(os.path.abspath(__file__))
csv_path=os.path.join(folder_path,'filtered_jobs.csv')
# 1️⃣ Define your relevant skills/keywords for filtering
keywords = [
    "web scraping", "selenium", "python", "automation",
    "api", "beautifulsoup", "scrapy", "bot", "twilio",
    "chrome extension", "data mining", "email automation"
]

# 2️⃣ Load your existing scraped data (jobs.csv)
df = pd.read_csv("jobs.csv")

# 3️⃣ Combine job title + description for keyword matching
df['combined'] = (df['Job Title'].fillna('') + " " + df['Job Description'].fillna('')).str.lower()

# 4️⃣ Filter rows where any keyword is found
filtered_df = df[df['combined'].apply(lambda x: any(k in x for k in keywords))]

# 5️⃣ Save filtered jobs to new CSV file
filtered_df.to_csv("filtered_jobs.csv", index=False)
print(f"✅ {len(filtered_df)} relevant jobs saved to filtered_jobs.csv")
