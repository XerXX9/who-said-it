# Who Said It? - A Quote Guessing Game

Welcome to **"Who Said It?"**, a simple and fun web-based game where players test their knowledge by guessing the author of a randomly selected famous quote. This project was built to demonstrate core web development and scraping skills using **Python** and **Flask**.

---

## How to Play

The rules are simple:

1. When the game starts, you are presented with a **quote**.
2. Your goal is to **guess the author** of the quote by typing their name and submitting your answer.
3. You have **three lives**. For each incorrect guess, you lose a life.
4. To help you out, **hints** are provided after incorrect guesses:
   - First incorrect guess: Hint about the **author's birthdate**.
   - Second incorrect guess: Hint about the **author's birthplace**.
5. The game ends when you guess the author correctly or run out of lives.

---

## Features

- **Dynamic Content**: Quotes and author information are scraped from [http://quotes.toscrape.com](http://quotes.toscrape.com) when the server starts.
- **Progressive Hint System**: Get up to two hints as you guess incorrectly.
- **Lives System**: You get 3 chances per quote.
- **Interactive UI**: Clean and simple front-end using HTML and CSS.

---

## Technologies Used

### Backend
- **Python**: Core application logic
- **Flask**: Web framework for routing and serving pages

### Web Scraping
- **Requests**: For fetching HTML from the quotes site
- **BeautifulSoup**: For parsing and extracting data from HTML

### Frontend
- **HTML**: Structure
- **CSS**: Styling

---

## Setup and Installation

Follow these steps to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/XerXX9/who-said-it.git
cd who-said-it
```

### 2. (Recommended) Create and activate a virtual environment

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
flask run
```

### 5. Open the game in your browser

Go to [http://127.0.0.1:5000](http://127.0.0.1:5000) and start playing!

---

Enjoy the game and happy guessing!
