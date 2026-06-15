# 📰 Aravot News Classifier Bot

An end-to-end NLP project that automatically collects Armenian news articles from Aravot, trains a machine learning model, and classifies incoming news as either Sports or Politics through a Telegram bot.

---

## 🚀 Features

- Automated news collection from Aravot
- Sports and Politics dataset generation
- Text preprocessing and feature extraction using TF-IDF
- Machine Learning classification
- Telegram Bot integration
- Fast real-time predictions
- Fully written in Python

---

## 🏗 Project Structure

```text
aravot-news-classifier-bot/
│
├── scraper.py
├── train.py
├── bot.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── data/
│   └── news_dataset.csv
│
└── models/
    └── news_classifier.pkl
```

---

## ⚙️ Technologies Used

- Python
- BeautifulSoup4
- aiohttp
- Pandas
- Scikit-Learn
- Joblib
- Python Telegram Bot
- TF-IDF Vectorization

---

## 📊 Machine Learning Pipeline

### Dataset Creation

The scraper automatically collects articles from:

- Sports category
- Politics category

and builds a labeled dataset.

### Text Vectorization

TF-IDF is used to transform Armenian news text into numerical features.

### Classification

The classifier learns to distinguish between:

- 🏆 Sports News
- 🏛 Politics News

---

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/aravot-news-classifier-bot.git

cd aravot-news-classifier-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

---

## 📥 Build Dataset

Run the scraper:

```bash
python scraper.py
```

Output:

```text
news_dataset.csv
```

---

## 🤖 Train Model

```bash
python train.py
```

Output:

```text
news_classifier.pkl
```

---

## 💬 Run Telegram Bot

```bash
python bot.py
```

---

## 📱 Example

User sends:

```text
Հայաստանի հավաքականը հաղթեց մրցակցին 3-1 հաշվով։
```

Bot replies:

```text
🏆 Sports News
```

---

User sends:

```text
Ազգային ժողովում քննարկվեց նոր օրենքի նախագիծը։
```

Bot replies:

```text
🏛 Politics News
```

---

## 📈 Future Improvements

- XLM-RoBERTa Fine-Tuning
- Multi-class Classification
- News Summarization
- Automatic Daily Retraining
- Docker Deployment
- Web Dashboard

---

## 🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Smbat Simonyan

GitHub:
https://github.com/SmbatSimonyan
