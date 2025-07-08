Who Said It? - A Quote Guessing Game
Welcome to "Who Said It?", a simple and fun web-based game where players test their knowledge by guessing the author of a randomly selected famous quote. This project was built to demonstrate core web development and scraping skills using Python and Flask.

How to Play
The rules are simple:

When the game starts, you are presented with a quote.

Your goal is to guess the author of the quote by typing their name and submitting your answer.

You have three lives. For each incorrect guess, you lose a life.

To help you out, hints are provided after incorrect guesses:

After the first incorrect guess, you will receive a hint about the author's birthdate.

After the second incorrect guess, you will receive another hint about the author's birthplace.

The game ends when you guess the author correctly or when you run out of lives.

Features
This project showcases several key features:

Dynamic Content: To ensure a fresh experience every time, the game scrapes quotes and author information directly from the live website http://quotes.toscrape.com when the server starts.

Progressive Hint System: The game provides up to two hints to the player, rewarding them with more information as they take risks.

Lives System: Players have three chances to guess the correct author, adding a simple challenge to the game.

Interactive UI: The game is presented through a clean and simple front-end built with standard HTML and CSS, making it easy and intuitive to play.

Technologies Used
The game is built with a combination of backend and frontend technologies:

Backend:

Python: The core programming language for the application logic.

Flask: A lightweight web framework used to handle web pages, routing, and serving the game to the user.

Web Scraping:

Requests: A Python library used to fetch the HTML content from the quotes website.

BeautifulSoup: A library used to parse the HTML and easily extract the quotes, authors, and hints.

Frontend:

HTML: Provides the structure for the web pages.

CSS: Styles the game for a clean and pleasant user experience.

Setup and Installation
To get this project running on your local machine, please follow the steps below. This will guide you through cloning the repository, setting up an environment, installing the necessary packages, and running the game.

1. Clone the repository:

First, download the project files from GitHub to your computer using the git clone command.

git clone https://github.com/XerXX9/who-said-it.git
cd who-said-it

2. (Recommended) Create and activate a virtual environment:

A virtual environment is a private sandbox for your Python packages, which prevents conflicts with other projects.

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
.\venv\Scripts\activate

3. Install the required dependencies:

The requirements.txt file lists all the Python packages the project needs. This command reads the file and installs them automatically.

pip install -r requirements.txt

4. Run the Flask application:

This command starts the local web server.

flask run

5. Open the game in your browser:

Once the server is running, navigate to http://127.0.0.1:5000 in your web browser to start playing!

