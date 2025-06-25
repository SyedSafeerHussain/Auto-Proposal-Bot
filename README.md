# 🤖 Auto Proposal Bot (PeoplePerHour Scraper)

The **Auto Proposal Bot** is a smart freelance job monitoring tool that scrapes job listings from [PeoplePerHour](https://www.peopleperhour.com/freelance-jobs), filters them using relevant keywords, and sends real-time WhatsApp alerts via Twilio. It's built for freelancers who want to apply quickly and stay ahead of the competition.

---

## 🚀 Features

- 🔍 Scrapes real-time freelance jobs from PeoplePerHour
- ✅ Accepts cookie prompts automatically
- 🔑 Searches using 20+ smart keywords
- 📂 Saves all job results into `jobs.csv`
- 🧠 Filters only matching jobs into `filtered_jobs.csv`
- 📩 Sends matched jobs via WhatsApp using Twilio API
- 🛡️ Credentials are stored securely using `.env`

---

## 🧰 Technologies Used

- Python 3
- Selenium
- Twilio API
- Pandas
- dotenv

---



🗂️ Project Structure
Auto_Proposal_Bot/
│
├── jobs.csv               # All scraped job data
├── filtered_jobs.csv      # Filtered job results
├── main.py                # Scraping + filtering logic
├── notifier.py            # WhatsApp notification logic
├── .env                   # (Not pushed) Contains Twilio secrets
└── README.md              # Project overview

🔐 .env File Format
TWILIO_SID=your_account_sid
TWILIO_AUTH=your_auth_token
TWILIO_FROM=whatsapp:+14155238886
TWILIO_TO=whatsapp:+923XXXXXXXXX

📢 *New Job Found!*
💼 Title: Web Scraping Expert Needed
💰 Budget: $200
🔗 Link: https://www.peopleperhour.com/job-link
✨ Future Plans
Add scheduling (e.g., run daily via cron)

Support more freelance websites (Upwork, Freelancer, Fiverr)

Telegram or Email notification support

Web-based dashboard for easier control
