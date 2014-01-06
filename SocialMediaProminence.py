from __future__ import division
import urllib
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

facebook_weight = 0.4;        #Because of the relatively large number of users on FaceBook for each company
twitter_weight = 0.3;
googleplus_weight = 0.3;

def popularity_among_customers(fk,eb,cr,am):
    Players = ('Flipkart', 'EBay', 'Croma', 'Amazon');
    y_pos = np.arange(len(Players))

    scores = [];
    scores.append(fk);
    scores.append(eb);
    scores.append(cr);
    scores.append(am);
    
    print scores
    People_Likability = np.array(scores);
    error = np.zeros(len(Players));
    
    plt.barh(y_pos, People_Likability, xerr=error, align='center', alpha=0.4)
    plt.yticks(y_pos, Players)
    plt.xlabel('Players')
    plt.title('People Likability')
    plt.show();

def like_extract(url):
    proxy = 'http://10.93.0.37:3333';
    fb = urllib.urlopen(url,proxies={'https':proxy})     #Can sometimes have problems due to the lack of https authentication in urllib and urlopen
    fb_lines = fb.readlines();
    ind = fb_lines[60].index("stats fwb\">") + len("stats fwb\">");
    indend = fb_lines[60].index("<",ind);
    t = fb_lines[60][ind:indend];
    
    if "m" in t:
        t = float(t[:-1])*1e9;
    return t;


def plusones_extract(url):
    proxy = 'http://10.93.0.37:3333';
    gp = urllib.urlopen(url,proxies={'https':proxy})     #Can sometimes have problems due to the lack of https authentication in urllib and urlopen
    gp_lines = gp.readlines();
    ind = gp_lines[62].index("<span class=\"Myb j0c\"") + len("<span class=\"Myb j0c\"");
    indend = gp_lines[62].index("<",ind);
    t = gp_lines[62][ind:indend];
    
    return float(t);

def follow_extract(url):
    proxy = 'http://10.93.0.37:3333';
    tw = urllib.urlopen(url,proxies={'https':proxy})     #Can sometimes have problems due to the lack of https authentication in urllib and urlopen
    tw_lines = gp.readlines();
    for l in tw_lines:
        if("Followers" in l):
            ind = l.index("<strong>") + len("<strong>");
            indend = l.index("</strong>");
            t = l[ind:indend];
            t=int(_.join(t.split(",")))
            break;
    
    return t;

if __name__ == "__main__":
    
    fk_url_fb="https://www.facebook.com/flipkart";
    fk_url_gp = "https://plus.google.com/u/0/+flipkart/posts";
    fk_url_tw = "https://twitter.com/Flipkart";

    eb_url_fb="https://www.facebook.com/ebay";
    eb_url_gp = "https://plus.google.com/u/0/+eBay/posts";
    eb_url_tw = "https://twitter.com/ebay";

    cr_url_fb="https://www.facebook.com/CromaRetail";
    cr_url_gp = "https://plus.google.com/116744904644384595704/posts";
    cr_url_tw = "https://twitter.com/cromaretail";

    am_url_fb="https://www.facebook.com/amazon";
    am_url_gp = "https://plus.google.com/u/0/+amazon/posts";
    am_url_tw = "https://twitter.com/Amazon";


    Flipkart_facebook_likes = like_extract(fk_url_fb);          #2357920
    Flipkart_twitter_followers = follow_extract(fk_url_tw);     #99485
    Flipkart_googleplus_ones = plusones_extract(fk_url_gp);     #282934
    
    Ebay_facebook_likes = like_extract(eb_url_fb);              #7009797
    Ebay_twitter_followers = follow_extract(eb_url_tw);         #297589
    Ebay_googleplus_ones = plusones_extract(eb_url_gp);         #439796
    
    Croma_facebook_likes = like_extract(cr_url_fb);             #89303
    Croma_twitter_followers = follow_extract(cr_url_tw);        #10140
    Croma_googleplus_ones = plusones_extract(cr_url_gp);        #308
    
    Amazon_facebook_likes = like_extract(am_url_fb);            #22675230
    Amazon_twitter_followers = follow_extract(am_url_tw);       #887350
    Amazon_googleplus_ones = plusones_extract(am_url_gp);       #433602

    fk = facebook_weight*(Flipkart_facebook_likes)/(Flipkart_facebook_likes+Ebay_facebook_likes+Croma_facebook_likes+Amazon_facebook_likes) +twitter_weight*(Flipkart_twitter_followers)/(Flipkart_twitter_followers+Ebay_twitter_followers+Croma_twitter_followers+Amazon_twitter_followers) + googleplus_weight*(Flipkart_googleplus_ones)/(Flipkart_googleplus_ones+Ebay_googleplus_ones+Croma_googleplus_ones+Amazon_googleplus_ones);
    
    eb = facebook_weight*(Ebay_facebook_likes)/(Flipkart_facebook_likes+Ebay_facebook_likes+Croma_facebook_likes+Amazon_facebook_likes) +twitter_weight*(Ebay_twitter_followers)/(Flipkart_twitter_followers+Ebay_twitter_followers+Croma_twitter_followers+Amazon_twitter_followers) + googleplus_weight*(Ebay_googleplus_ones)/(Flipkart_googleplus_ones+Ebay_googleplus_ones+Croma_googleplus_ones+Amazon_googleplus_ones);
    
    cr = facebook_weight*(Croma_facebook_likes)/(Flipkart_facebook_likes+Ebay_facebook_likes+Croma_facebook_likes+Amazon_facebook_likes) +twitter_weight*(Croma_twitter_followers)/(Flipkart_twitter_followers+Ebay_twitter_followers+Croma_twitter_followers+Amazon_twitter_followers) + googleplus_weight*(Croma_googleplus_ones)/(Flipkart_googleplus_ones+Ebay_googleplus_ones+Croma_googleplus_ones+Amazon_googleplus_ones);
    
    am = facebook_weight*(Croma_facebook_likes)/(Flipkart_facebook_likes+Ebay_facebook_likes+Croma_facebook_likes+Amazon_facebook_likes) +twitter_weight*(Croma_twitter_followers)/(Flipkart_twitter_followers+Ebay_twitter_followers+Croma_twitter_followers+Amazon_twitter_followers) + googleplus_weight*(Croma_googleplus_ones)/(Flipkart_googleplus_ones+Ebay_googleplus_ones+Croma_googleplus_ones+Amazon_googleplus_ones);
    
    popularity_among_customers(fk,eb,cr,am);
