# ShadowFox Python Internship

This is my work for the ShadowFox Python Developer internship. I finished all three levels between September 1 and 30, 2026. Everything is written in Python 3.12.

## Folders

**Task1_Beginner**

Out of the 9 topics given, I picked variables, numbers, list, if condition and for loop since these felt like the core basics to focus on first. There is one file per topic, and the questions inside each file are separated by comments (Q1, Q2, Q3).

**Task2_Intermediate**

- `web_scraper.py` scrapes the ShadowFox home page using requests and BeautifulSoup. It prints the page title, the h1/h2/h3 headings and the number of links, and saves them to `scraped_data.txt`. If the request fails (no internet, site down) it prints the error instead of crashing.
- `hangman_game.py` was the fun one to build. I added a play again option so you don't have to restart the script every time you want to play.

**Task3_Advance**

For the advanced task I picked the cricket fielding analysis option. `cricket_fielding_analysis.py` holds ball by ball fielding entries for three players (Virat Kohli, MS Dhoni, Ravindra Jadeja) from the RCB vs CSK match played on 18 May 2024 at Chinnaswamy Stadium — I remembered watching that match, so I used it as the base. RCB batted first, so CSK were fielding in the first innings and RCB in the second. The fielding events themselves are made up by me for practice, not the real data from that game. The code counts each player's actions and works out a performance score using the formula and weights given in the task's sample sheet.

It writes two files:
- `fielding_ball_by_ball_data.csv` - the collected data
- `fielding_performance_matrix.csv` - counts and performance score for each player

## Running

Install the libraries first:

```
pip install requests beautifulsoup4 pandas
```

Then run any file, for example:

```
python Task1_Beginner/1_variable.py
python Task2_Intermediate/hangman_game.py
python Task3_Advance/cricket_fielding_analysis.py
```

Some files in Task 1 ask for input (height, weight, city names, etc). The scraper needs an internet connection, and the CSV/txt output files are created in whichever folder you run the script from.
