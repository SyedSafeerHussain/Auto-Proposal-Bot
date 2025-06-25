import pandas as pd
from dotenv import load_dotenv
import os
from twilio.rest import Client
# Step: Load environment variables from .env file
load_dotenv()
# Step: Get variables from .env file
account_sid=os.getenv("ACCOUNT_SID")
auth_token=os.getenv("AUTH_TOKEN")
twilio_number=os.getenv("TWILIO_NUMBER")
your_whatsapp=os.getenv("MY_NUMBER")
# Twilio client setup
clint=Client(account_sid,auth_token)
df=pd.read_csv('filtered_jobs.csv')
# Send WhatsApp message for each job
for index, row in df.iterrows():
    title=row['Job Title']
    link=row['link']
    price=row['price']
    message_body = f"""📢 *New Job Found!*
💼 Title: {title}
💰 Budget: {price}
🔗 Link: {link}
"""
message=clint.messages.create(
    from_=twilio_number,
    body=message_body,
    to=your_whatsapp
)
print(f"✅ Sent: {title}")