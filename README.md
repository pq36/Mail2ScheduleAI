# Mail2ScheduleAI 📬➡️📅

Mail2ScheduleAI is an **AI-powered automation system** that reads Gmail messages and converts them into **structured scheduled tasks** using **LangChain and Google Gemini**.

The project demonstrates how **Large Language Models (LLMs)** can automate real-world workflows by transforming unstructured email content into actionable schedules.

---

# 🚀 Features

* 📧 Read emails using the **Gmail API**
* 🤖 Extract tasks using **Gemini LLM**
* 🧠 Intelligent message understanding
* 📅 Convert messages into **structured schedule tasks**
* ⚡ Built with **LangChain agents**
* 🔐 Secure API keys using `.env`

---

# 🧠 How It Works

```
Gmail Inbox
     │
     ▼
Gmail API Reader
     │
     ▼
LangChain Agent
     │
     ▼
Gemini LLM
     │
     ▼
Task Extraction
     │
     ▼
Structured Schedule Tasks
```

---

# 📁 Project Structure

```
Mail2ScheduleAI/
│
├── agents/
│   └── schedule_agent.py
│
├── models/
│   └── task_model.py
│
├── utils/
│   ├── gemini_client.py
│   └── gmail_reader.py
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/pq36/Mail2ScheduleAI.git
cd Mail2ScheduleAI
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

# 🔑 Environment Setup

Create `.env` file in the root folder.

```
GOOGLE_API_KEY=your_gemini_api_key
```

---

# 📧 Gmail API Setup

1. Open **Google Cloud Console**
2. Enable **Gmail API**
3. Create **OAuth credentials**
4. Download `credentials.json`
5. Place it in the project root

---

# ▶️ Run the Project

```
python app.py
```

The program will:

1. Authenticate Gmail
2. Fetch recent emails
3. Send messages to Gemini
4. Extract tasks and scheduling information

---

# 📊 Example

### Email Message

```
Hi Meghana,

Please finish the Azure pipeline report by tomorrow at 5 PM.
Also schedule a team meeting on Friday at 10 AM.
```

### Extracted Tasks

```
[
  {
    "task": "Finish Azure pipeline report",
    "date": "Tomorrow",
    "time": "5 PM"
  },
  {
    "task": "Team meeting",
    "date": "Friday",
    "time": "10 AM"
  }
]
```

---

# 🛠 Technologies Used

* Python
* LangChain
* Google Gemini API
* Gmail API
* Pydantic
* python-dotenv

---

# 🔮 Future Improvements

* Google Calendar event creation
* Real-time email monitoring
* Task dashboard UI
* MongoDB task storage
* Notification system

---

# 👩‍💻 Author

Meghana
AI / ML and Full Stack Developer interested in building **AI agents and automation systems**.

---
