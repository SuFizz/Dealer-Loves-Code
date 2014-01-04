import urllib

if __name__=="__main__":
	proxy = 'http://10.93.0.37:3333';
	search_query = raw_input("Enter the name to compare");

	Flipkart_query = "http://www.flipkart.com/search?q="+search_query+"&as=off&as-show=on&otracker=start";
	Amazon_query = "http://www.amazon.com/s/ref=nb_sb_noss/190-8560217-0234733?url=search-alias%3Daps&field-keywords="+search_query;
	Infibeam_query = "http://www.infibeam.com/search?q="+search_query;
	Jabong_query = "http://www.jabong.com/find/west/?q="+search_query;


	FlipKart = urllib.urlopen("http://.ycombinator.com/", proxies={'https': proxy})
        

        filelines = esult.readlines();
