# Flipper         | WPI Hackathon 2020
Python web application that finds products to buy from [mercari](https://www.mercari.com) and sell on [ebay](https://www.ebay.com)

# How to run
To run locally you need to run the command "python app.py" inside the flipper directory. Once the server is running, open in your browser "http://localhost:5000/"

# Inspiration
The idea came from videos on social media platform TikTok. There were several people giving advice to flip products from across different websites. We thought about how we could streamline the process and came up with flipper.

# What it does
Flipper allows you to search for items of interest. The application will then find items on ebay and mercari given that search term. It will then give the user profitable suggestions for them to decide if they will want to buy the item.

# How we built it
We built the app using python with flask, along with html and css. Calling the ebay api but also web scraping from both ebay and mercari.

# Challenges we ran into
Database and system desing, api calling, conflicting libraries, scraping permissions.

# Accomplishments that we're proud of
We defined a statistical analysis to decide how to prioritize what calls we made to the ebay api.

# What we learned
We learned how to scrape while confiding with terms of service. Learned the flask library.

# What's next for Flipper
We plan on refining the algorithm and expanding the websites.

## Libraries Used
- Flask
- PyMongo
- BeautifulSoup4
- Numpy
- Urlib
- Bootstrap
- Multiprocessing


