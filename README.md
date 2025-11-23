# 🎮 Telegram XO Game Bot

A simple yet engaging **Tic‑Tac‑Toe (XO)** game built with **Aiogram** for Telegram.  
Players can challenge each other or play against the bot, with support for both **webhook** and **polling** modes.

---

## ✨ Features
- Interactive **XO (Tic‑Tac‑Toe)** gameplay inside Telegram  
- Supports **two‑player mode** or **player vs bot**  
- **Webhook** and **polling** options for deployment  
- **Redis** integration for session and state management  
- **Localization** support with `locales` directory  
- Code quality tools: `isort` and `flake8`  

---

## 📦 Installation

Clone the repository and set up the environment:

```bash
git clone https://github.com/dostontv/x_o_game.git
cd telegram-xo-game
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

🌍 Localization Setup
Create the locales directory and run the following commands:
bash
mkdir locales
make extract
make init
make update
make compile

## 🛠️ Development
Run linting and style checks:
bash
isort .
flake8 .

## 🚀 Usage
Start the bot in polling mode:
bash
python bot.py
Or configure webhook mode for production deployment.

## 📂 Project Structure
```
Code
├── src/              # Main bot source code
├── locales/          # Translation files
├── requirements.txt  # Dependencies
├── Makefile          # Localization commands
└── README.md         # Project documentation
```
