import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API")

system_prompt = """
You are an AI stock market analyst.

Analyze stock market trends using financial data such as:
- Open
- Close
- High
- Low
- Volume
- Price movement

Give clear and practical insights based on the provided stock statistics.

Your response should include:
1. Overall trend
2. Risk level
3. Momentum analysis
4. Volume analysis
5. Short-term outlook
6. Answer to the user's question

Keep the explanation simple and professional.
"""

def stock_analysis(df, user_question, stock_name="AAPL"):

    client = Groq(api_key=api_key)

    latest_close = df['Close'].iloc[-1]
    latest_open = df['Open'].iloc[-1]
    latest_high = df['High'].iloc[-1]
    latest_low = df['Low'].iloc[-1]
    latest_volume = df['Volume'].iloc[-1]

    period_high = df['High'].max()
    period_low = df['Low'].min()

    first_close = df['Close'].iloc[0]

    price_change = ((latest_close - first_close) / first_close) * 100

    avg_volume = df['Volume'].mean()

    user_prompt = f"""
    Stock: {stock_name}

    Latest Open: ${latest_open:.2f}
    Latest Close: ${latest_close:.2f}
    Latest High: ${latest_high:.2f}
    Latest Low: ${latest_low:.2f}
    Period High: ${period_high:.2f}
    Period Low: ${period_low:.2f}
    Price Change: {price_change:.2f}%
    Latest Volume: {latest_volume:,.0f}
    Average Volume: {avg_volume:,.0f}

    User Question:
    {user_question}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content