import urllib

if __name__=="__main__":
	proxy = 'http://10.93.0.37:3333';
	search_query = raw_input("Enter the name to compare");

	Flipkart_query = "http://www.flipkart.com/search?q="+search_query+"&as=off&as-show=on&otracker=start";              #Flipkart - make it in terms of +###+###+
	Amazon_query = "http://www.amazon.in/s/ref=nb_sb_ss_i_0_8?url=search-alias%3Daps&field-keywords="+search_query;     #Amazon - make it in terms of +###+###+
	Infibeam_query = "http://www.infibeam.com/search?q="+search_query;
	Jabong_query = "http://www.jabong.com/find/west/?q="+search_query;
    Jewelskart_query = "http://www.jewelskart.com/catalogsearch/result/?cat=0&q="+search_query+"#cat=0&q="+search_query+"&oos_searchable=Yes&gan_data=true";
#    Koovs_query = "http://www.koovs.com/"+search_query;        because this dude wants -#####-######-#### which is stupid
    Landmark_query = "http://www.landmarkonthenet.com/search/?q="+search_query;
    Lenskart_query = "http://www.lenskart.com/catalogsearch/result/?cat=0&q="+search_query+"#cat=0&q="+search_query+"&oos_searchable=Yes&gan_data=true";
    Myntra_query = "http://www.myntra.com/"+search_query+"?userQuery=true";
    Naaptol_query = "http://www.naaptol.com/search.html?type=srch_catlg&kw="+search_query;
    Croma_query = "http://www.cromaretail.com/productsearch.aspx?txtSearch="+search_query+"&x=-808&y=-85";
    Ebay_query = "http://www.ebay.in/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0.Xsamsung&_nkw=samsung&_sacat=0&_from=R40"
    Homeshop18_query = "http://www.homeshop18.com/"+search_query+"/search:"+search_query;

	Flipkart = urllib.urlopen(Flipkart_query, proxies={'http': proxy})
	Amazon = urllib.urlopen(Amazon_query, proxies={'http': proxy})
	Infibeam = urllib.urlopen(Infibeam_query, proxies={'http': proxy})
	Jabong = urllib.urlopen(Jabong_query, proxies={'http': proxy})
	Jewelskart = urllib.urlopen(Jewelskart_query, proxies={'http': proxy})
	Landmark = urllib.urlopen(Landmark_query, proxies={'http': proxy})
	Myntra = urllib.urlopen(Myntra_query, proxies={'http': proxy})
	Naaptol = urllib.urlopen(Naaptol_query, proxies={'http': proxy})
	Croma = urllib.urlopen(Croma_query, proxies={'http': proxy})
	Ebay = urllib.urlopen(Ebay_query, proxies={'http': proxy})
	Homeshop18 = urllib.urlopen(Homeshop18_query, proxies={'http': proxy})

    filelines = esult.readlines();
