A Python Scrapy Project by David Gottlieb

BLOG POST: https://nycdatascience.com/blog/student-works/finding-the-best-gluten-free-metro-areas-and-restaurants-with-scrapy/

FindMeGlutenFree.com is a go-to website in the gluten free / celiac community. The platform works as a Yelp-like user-based restaurant search engine, except one that is meant only for restaurants with gluten-free offerings. This focus makes it much easier to find restaurants that are safe (and delicious!) for users who are on a gluten-free / celiac diet. By scraping this website, one can determine which metropolitan areas have the best gluten free scenes – which is useful when considering which city to accept a new job in, thinking of where to vacation, or discovering a region’s most popular gluten free foods. Since this website has a strong emphasis on celiac food safety standards of restaurants, I also look at which cities and restaurants types are generally rated more celiac-friendly, as well as the size and strength of the celiac community on the platform. As someone with several celiac family members, this web scraping project gives me a chance to generate insights that I can use to help protect my family. 

-----------------
--- DIRECTORY ---
-----------------
JUPYTER NOTEBOOK (PYTHON) FOR CLEANING & VISUALIZATIONS:\
FindMeGF Scraping Code Final with Comments.ipynb

SCRAPY FILES: \
SPIDER SCRAPER TO CRAWL AND COLLECT DATA: spiders/findmegf_long_spider.py\
ITEMS TO SCRAPE: items.py \
PIPELINE FUNCTION TO WRITE ITEMS TO CSV: pipelines.py \
SPIDER MIDDLEWARE MODELS: middlewares.py \
SCRAPING SETTINGS: settings.py \
OTHER SCRAPY FILES: \_\_init\_\_.py, \_\_pycache\_\_ folder


CSV FILES:\
• ORIGINAL SCRAPED DATASET: findmegflong.csv\
• CLEANED, EXPANDED, & DUMMIFIED DATASET: gf_data_all_tags.csv\
• SUMMARY STATS BY METRO AREA: gf_full_stats_metro.csv\
• LIST OF ALL RESTAURANT TYPE TAGS:  gf_rest_tags.csv\
• LIST OF ALL FOOD TYPE TAGS: gf_food_tags.csv\

VISUALIZATIONS: \
• Restaurant_Experience_by_Metro.png\
• Top_10_Restaurant_Type_Tags_by_Metro.png\
• Percentage_of_Reviews_by_Metro.png\
• Restaurant_Reviews_by_Metro_Boxplot.png\
• Celiac_Friendliness_by_Metro.png\
• Celiac_Friendliness_by_Restaurant_Type_Tags.png\
• User_Engagement_by_Restaurant_Type_Tags.png\
• Most_Popular_GF_Foods_WordMap.png\
• Dedicated_Fryers_by_Metro.png (not in blog post)\
• User_Engagement_by_Restaurant_Type_Tags.png (not in blog post)