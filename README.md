# Telegram Webhook Bot for Railway

This bot receives alerts from TradingView and sends them to Telegram using a webhook.

## ✅ How to Deploy on Railway

1. Fork or upload this repo to your GitHub account.
2. Go to [https://railway.app](https://railway.app) and create a free account.
3. Click **New Project** → **Deploy from GitHub Repo**
4. Select this repository.
5. Configure:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python main.py`

6. Railway will give you a public URL like:
   ```
   https://your-bot.up.railway.app
   ```

7. Set Telegram webhook:

```
https://api.telegram.org/bot<your_token>/setWebhook?url=https://your-bot.up.railway.app/webhook
```

## 📈 TradingView JSON Example

```
{
  "pair": "EUR/USD",
  "action": "BUY",
  "timeframe": "1m",
  "entry": "1.07345",
  "confidence": "High"
}
```

Created by @AWMR05 for Railway Hosting
