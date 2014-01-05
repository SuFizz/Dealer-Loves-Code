import urllib

#def process_fk(fk_lines):
    #I need to search till I find the div element like this : <div class='product


if __name__=="__main__":
    proxy = 'http://10.93.0.37:3333';
    search_query = raw_input("Enter the name to compare : ");
    search_query = search_query.replace(" ","+");


    Flipkart_query = "http://www.flipkart.com/all-categories/pr?p%5B%5D=sort%3Drelevance&sid=search.flipkart.com&q="+search_query;
    Amazon_query = "http://www.amazon.in/s/ref=nb_sb_ss_i_0_8?url=search-alias%3Daps&field-keywords="+search_query;
    Infibeam_query = "http://www.infibeam.com/search?q="+search_query;
    Jabong_query = "http://www.jabong.com/find/west/?q="+search_query;
    Jewelskart_query = "http://www.jewelskart.com/catalogsearch/result/?cat=0&q="+search_query+"#cat=0&q="+search_query+"&oos_searchable=Yes&gan_data=true";
    Landmark_query = "http://www.landmarkonthenet.com/search/?q="+search_query;
    Lenskart_query = "http://www.lenskart.com/catalogsearch/result/?cat=0&q="+search_query+"#cat=0&q="+search_query+"&oos_searchable=Yes&gan_data=true";
    Myntra_query = "http://www.myntra.com/"+search_query+"?userQuery=true";
    Naaptol_query = "http://www.naaptol.com/search.html?type=srch_catlg&kw="+search_query;
    Croma_query = "http://www.cromaretail.com/productsearch.aspx?txtSearch="+search_query+"&x=-808&y=-85";
    Ebay_query = "http://www.ebay.in/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0.Xsamsung&_nkw=samsung&_sacat=0&_from=R40"
    Homeshop18_query = "http://www.homeshop18.com/"+search_query+"/search:"+search_query;


    Flipkart = urllib.urlopen(Flipkart_query, proxies={'http': proxy})
    Amazon = urllib.urlopen(Amazon_query, proxies={'http': proxy})
    Croma = urllib.urlopen(Croma_query, proxies={'http': proxy})
    Ebay = urllib.urlopen(Ebay_query, proxies={'http': proxy})
    Infibeam = urllib.urlopen(Infibeam_query, proxies={'http': proxy})
    Jabong = urllib.urlopen(Jabong_query, proxies={'http': proxy})
    Jewelskart = urllib.urlopen(Jewelskart_query, proxies={'http': proxy})
    Landmark = urllib.urlopen(Landmark_query, proxies={'http': proxy})
    Myntra = urllib.urlopen(Myntra_query, proxies={'http': proxy})
    Naaptol = urllib.urlopen(Naaptol_query, proxies={'http': proxy})
    Homeshop18 = urllib.urlopen(Homeshop18_query, proxies={'http': proxy})
    Lenskart = urllib.urlopen(Lenskart_query, proxies={'http': proxy})

    fk_lines = Flipkart.readlines();
    am_lines = Amazon.readlines();
    ib_lines = Infibeam.readlines();
    ja_lines = Jabong.readlines();
    jk_lines = Jewelskart.readlines();
    lm_lines = Landmark.readlines();
    my_lines = Myntra.readlines();
    na_lines = Naaptol.readlines();
    cr_lines = Croma.readlines();
    eb_lines = Ebay.readlines();
    hs_lines = Homeshop18.readlines();
    lk_lines = Lenskart.readlines();


#    product_fk,images_fk = process_fk(fk_lines);
#    product_am,images_am = process_am(am_lines);
#    product_ib,images_ib = process_ib(ib_lines);
#    product_ja,images_ja = process_ja(ja_lines);
#    product_jk,images_jk = process_jk(jk_lines);
#    product_lm,images_lm = process_lm(lm_lines);
#    product_my,images_my = process_my(my_lines);
#    product_na,images_na = process_na(na_lines);
#    product_cr,images_cr = process_cr(cr_lines);
#    product_eb,images_eb = process_eb(eb_lines);
#    product_hs,images_hs = process_hs(hs_lines);
#    product_lk,images_lk = process_lk(lk_lines);   
