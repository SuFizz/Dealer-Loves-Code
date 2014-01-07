Dealer-Loves-Code
=================

Crawl different websites such as FlipKart, Amazon, EBay, Croma, etc to get the best deals on products

A simple crawler to crawl through different websites and allow the user to make a choice with regard to the different options available with regard to the Delivery dates, Price, other features etc - as might be important.

This is done as part of the Hackathon being run by PayPal in IITM during Shaastra 2014.

"Untitled Document 1" and "Untitled Document 2" were created only for the purposes of debugging

DealSite - leverages the content on different e commerce websites along with the power of the Social media such as aggregating mood about certain products from the social media space to build a recommender system to suggest better products to users along with other capabilities such as which particular e commerce portal in itself is more trusted among different users. This should allow the user to make a better choice among the products that he is buying to optimize on the different products and also ease the process of getting best value for money - POWER TO THE USER. !!


TO use the program:

1. Run starter_first.py
2. This prompts you to enter the Search Query.
3. Now, the code generates the html code.
4. Copy, paste this into an empty file - _.html
5. Now, just click on the html file to open the web page
6. Also, to generate the Social Media thing - run SocialMediaProminence.py
7. Again repeat the process from 3-4 and name it as comparison.html
8. We are all set!!



Simple Explanation of Product:

USER ENTERS A SEARCH QUERY
========>
App searches for product in FlipKart, EBay, Amazon, Croma Retail
========>
App searches for the relevance among different social media for FlipKart, EBay, Amazon, Croma (comparing with FaceBook and Google+ posts and Tweets to get the best idea about how good each of the companies does in comparison to each other)
========>
App does Sentiment Analysis on Tweets to get the best idea of the crowd about the search query
========>
App generates complete HTML page in standard HTML5 format.
========>
User seamlessly buys his best product - TOTAL POWER TO THE USER!
        ^_^
