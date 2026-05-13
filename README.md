# 📈 Real-Time Stock Dashboard

An AI-powered real-time stock analysis dashboard built using Python, Streamlit, Redis, Plotly, and Groq LLaMA 3.3.

This application allows users to fetch live stock market data, visualize trends through interactive charts, cache responses using Redis for better performance, and receive AI-generated market insights in real time.

---

# 🚀 Features

- ✅ Live stock data fetching using `yfinance`
- ✅ Interactive candlestick chart with Plotly
- ✅ Volume analysis visualization
- ✅ Redis caching for faster repeated requests
- ✅ AI-powered stock analysis using Groq LLaMA 3.3
- ✅ Multiple selectable time periods
- ✅ Key stock performance metrics
- ✅ Clean and responsive Streamlit UI

---

# 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Data Source | yfinance |
| Visualization | Plotly |
| Cache | Redis |
| AI Analysis | Groq LLaMA 3.3 |
| Backend Language | Python |

---

# 📸 Screenshots

## Dashboard & Candlestick Chart

![Dashboard](screenshots/Real_time_stock_analysis_Dash_board.png)

---

## Volume Analysis

![Volume](screenshots/barchart_plotly.png)

---

## AI-Powered Analysis

![AI Analysis](screenshots/groq_ai_review.png)

---

## Redis Desktop Manager Cache
![Redis Cache](redis_real_time_stock_analysis.png)

---

# 📂 Project Structure

```bash
stock-dashboard/
│
├── data/
│   └── fetch_stock.py
│
├── cache/
│   └── redis_cache.py
│
├── analysis/
│   └── groq_analysis.py
│
├── app/
│   └── streamlit_app.py
│
├── screenshots/
│
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/MohomedShajith/Real-Time-Stock-Dashboard.git
cd Real-Time-Stock-Dashboard
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv stock_env
stock_env\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv stock_env
source stock_env/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create Environment Variables

Create a `.env` file in the root directory:

```env
API=your_groq_api_key
```

---

## 5️⃣ Start Redis Server

Make sure Redis is installed and running.

```bash
redis-server
```

---

# ▶️ Run the Application

```bash
streamlit run app/streamlit_app.py
```

The app will open in your browser at:

```bash
http://localhost:8501
```

---

# 📊 How the Dashboard Works

1. Enter a stock ticker symbol
2. Choose a time period
3. Click **Fetch Data**
4. View:
   - Live stock metrics
   - Candlestick chart
   - Volume chart
5. Ask the AI assistant questions about the stock

---

# 🧠 AI Stock Analysis

The Groq-powered AI assistant provides:

- Overall market trend
- Momentum analysis
- Risk estimation
- Volume insights
- Short-term outlook
- Custom answers to user questions

---

# ⚡ Redis Caching Flow

```text
User Request
     ↓
Check Redis Cache
     ↓
Cache Hit  → Return Cached Data
Cache Miss → Fetch from yfinance
            ↓
       Store in Redis
            ↓
        Return Data
```

- Cache TTL: **5 Minutes**
- Improves speed and reduces unnecessary API calls

---

# 📈 Supported Time Periods

- 1 Month (`1mo`)
- 3 Months (`3mo`)
- 6 Months (`6mo`)
- 1 Year (`1y`)
- 2 Years (`2y`)

---

# 📌 Supported Stock Tickers

Any valid Yahoo Finance ticker:

| Company | Ticker |
|---|---|
| Apple | AAPL |
| Google | GOOGL |
| Tesla | TSLA |
| Microsoft | MSFT |
| Amazon | AMZN |
| NVIDIA | NVDA |

---

# 🔮 Future Improvements

- 📁 Portfolio tracking
- 🔔 Price alerts
- 📊 Multiple stock comparison
- 📰 News sentiment analysis
- 🤖 LSTM price prediction
- ☁️ Cloud deployment

---

# 👨‍💻 Author

## Mohomed Shajith

GitHub Profile:  
[MohomedShajith GitHub](https://github.com/MohomedShajith?utm_source=chatgpt.com)

Project Repository:  
[Real-Time-Stock-Dashboard Repository](https://github.com/MohomedShajith/Real-Time-Stock-Dashboard?utm_source=chatgpt.com)

---

# ⭐ If You Like This Project

Give this repository a star on GitHub and support the project.

```bash
⭐ Star the repo
🍴 Fork the project
🚀 Build something awesome
```
