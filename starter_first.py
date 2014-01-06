import urllib
import twython

def Crowd_twitter(query):
    consumer_key = '*****';
    consumer_secret = '*****';
    access_token = '******';
    access_token_secret = '******';

    client_args = {'proxies': {'https': 'http://10.93.0.37:3333'}}

    t = twython.Twython(app_key=consumer_key, 
            app_secret=consumer_secret, 
            oauth_token=access_token, 
            oauth_token_secret=access_token_secret,
            client_args = client_args)

#    query=raw_input("What do you want to search for?");
#    query.replace(" ","+");
    output = t.search(q=query, result_type='popular', count=10)          #purposely restricted to 10 users to protect from Spamming the Twitter server which could cause blacklisting of our server

    #print output;

    aggregater = []
    for i in range(10):
        aggregater.append(output[u'statuses'][i][u'text']);

    happy = open("positive-words.txt",'r')
    sad = open("negative-words.txt",'r')
    ha = happy.readlines()
    sa = sad.readlines()
    happy.close()
    sad.close()

    for i in range(len(ha)):
        ha[i]=ha[i].rstrip()

    for i in range(len(sa)):
        sa[i]=sa[i].rstrip()

    #Put basic sentiment analysis on tweet
    posi = 0;
    negi = 0;
    for i in range(10):
        for j in range(len(ha)):
            if(ha[j] in aggregater[i]):
                posi += 1;
        for j in range(len(sa)):
            if(sa[j] in aggregater[i]):
                negi += 1;

    #print "<!DOCTYPE html>\n<html>\n<title>Crowd likes!</title>"
    if posi > negi:
        return "<h1>CROWD LOVES IT!!:-)</h1>"
    elif posi<negi:
        return "<h1>CROWD DOESN'T LIKE IT!! :-( </h1>"
    else:
        return "<h1>CROWD CAN'T DECIDE :-| !!</h1>"


def buildwebpage(product_fk,product_cr,product_am,product_eb,search_query):
#            return images,links,names,prices
    print "<!DOCTYPE html>\n<html>";
    print "\n<h1><em><ul>WELCOME TO DEALERSITE - ONE STOP FOR ALL YOUR SHOPPING</ul></em></h1>\n<body>"

    print "<h1>THIS IS WHAT THE CROWD THINKS OF "+search_query+":</h1>"
    print Crowd_twitter(search_query)

    print "\n<h1>AMAZON</h1>";
    for i in range(3):
        print "\n<h2>"+product_am[2][i]+"</h2>"
        print "<img border=\"0\" src=\""+product_am[0][i]+"\" alt=\"Amazon\">"
        print "<a href=\""+product_am[1][i]+"\">CLICK THIS TO TAKE YOU TO AMAZONS PAGE TO BUY THE PRODUCT</a>"
        print "\n<p>PRICE : Rs."+product_am[3][i]+"</p>";

    print "\n<h1>EBAY</h1>";    
    for i in range(3):
        print "\n<h2>"+product_eb[2][i]+"</h2>"
        print "<img border=\"0\" src=\""+product_eb[0][i]+"\" alt=\"EBay\">"
        print "<a href=\""+product_eb[1][i]+"\">CLICK THIS TO TAKE YOU TO EBAYS PAGE TO BUY THE PRODUCT</a>"
        print "\n<p>PRICE : Rs."+product_eb[3][i]+"</p>";

    print "\n<h1>FLIPKART</h1>";
    for i in range(3):
        print "\n<h2>"+product_fk[2][i]+"</h2>"
        print "<img border=\"0\" src=\""+product_fk[0][i]+"\" alt=\"Flipkart\">"
        print "<a href=\""+product_fk[1][i]+"\">CLICK THIS TO TAKE YOU TO FLIPKARTS PAGE TO BUY THE PRODUCT</a>"
        print "\n<p>PRICE : Rs."+product_fk[3][i]+"</p>";


    print "\n<h1>CROMA RETAIL</h1>";
    for i in range(3):
        print "\n<h2>"+product_cr[2][i]+"</h2>"
        print "<img border=\"0\" src=\""+product_cr[0][i]+"\" alt=\"CROMA\">"
        print "<a href=\""+product_cr[1][i]+"\">CLICK THIS TO TAKE YOU TO CROMA PAGE TO BUY THE PRODUCT</a>"
        print "\n<p>PRICE : "+product_cr[3][i]+"</p>";

    print "<a href=\"/comparison.html\"><em><b>CLICK HERE FOR A COMPARISON OF DIFFERENT BRANDS</b></em></a>"
#    print "<a href=\"/crowd.html\">CLICK HERE FOR WHAT THE CROWD THINKS OF THE PRODUCT</a>"
    print "</body>\n</html>"

def link_fk_actu(product_image):
    Flipkart_query = "http://www.flipkart.com/all-categories/pr?p%5B%5D=sort%3Drelevance&sid=search.flipkart.com&q=";
#    print "\n\n\n\n\nLINK FK ACTUAL";
#    print product_image;
    names = [];
    for i in range(3):
        ind = product_image[i].index("data-pid=")+len("data-pid=\"");
        indend = product_image[i].index("data-tracking-products",ind) - 2;
        names.append(Flipkart_query + product_image[i][ind:indend]);
    return names;

def price_fk(product_image):
#    print "\n\n\n\n\nPRICE FK";
#    print product_image;
    names = [];
    for i in range(3):
        indend = product_image[i].index(";;");
        ind = product_image[i].rfind(";",0,indend-1);
        names.append(product_image[i][ind+1:indend]);
    return names;

def name_fk(product_image):
#    print "\n\n\n\n\nNAME FK";
#    print product_image;
    names = [];
    for i in range(3):
        ind = product_image[i].index("alt")+len("alt=\"");
        names.append(product_image[i][ind:].split()[0]);
#        product_image[i][ind:indend]);
    return names;

def link_fk(product_link):
#    print "\n\n\n\n\nLINK FK";
#    print product_link;
    beg_string = "www.flipkart.com";
    links = [];
    for i in range(3):
        ind = product_link[i].index("a href=")+len("a href=\"");
        indend = product_link[i].index("class") - 2;
        links.append(beg_string+product_link[i][ind:indend]);
    return links;


def image_fk(product_image):
    img = [];
    counter = 0;
    for i in range(len(product_image)):
#        print product_image[i];
        try:
            ind = product_image[i].index("data-src")+len("data-src=\"");
            ind_end1 = 10000;
            ind_end2 = 10000;
            try:
                ind_end1 = product_image[i].index("\"",ind);
            except ValueError:
                ind_end2 = product_image[i].index("\'",ind);
            if ind_end2 < ind_end1:
                ind_end = ind_end2;
            else:
                ind_end = ind_end1;
            img.append(product_image[i][ind:ind_end]);
            ++counter;
        except ValueError:
            ind = product_image[i].index("src=")+len("src=\"");

            ind_end1 = 10000;
            ind_end2 = 10000;
            try:
                ind_end1 = product_image[i].index("\"",ind);
            except ValueError:
                ind_end2 = product_image[i].index("\'",ind);
            if ind_end2 < ind_end1:
                ind_end = ind_end2;
            else:
                ind_end = ind_end1;

            img.append(product_image[i][ind:ind_end]);
            ++counter;
        if counter == 3:
            break;
    return img[:3];


def process_fk(fk_lines):
    product_image = [];
    product_name = [];
    product_otherone = [];
    flag = 0;
    counter = 0;
    prev_line = "";
    linenum = 0;

    for l in fk_lines:
#        print l;
#        if "<div class=\'product" in l:
#            flag = 1;
        linenum += 1;
        if "<div class='product" in l:
            product_name.append(l);
            flag = 1;
            
#        if flag == 0 and "<img src=" in l:
#            flag =1;
#            continue;

        if flag == 1 and "<img src=" in l:
            product_image.append(l);
            product_otherone.append(prev_line);
            ++counter;
            if(counter==12):
                break;
            flag = 0;
        prev_line = l;

    product_image = product_image[1:11];
    product_name = product_name[1:11];
    product_otherone = product_otherone[0:10];
    
    if(len(product_name)>=10):
        teer = link_fk_actu(product_name);
    else:
        teer = link_fk(product_otherone);
    
    return image_fk(product_image),teer,name_fk(product_image),price_fk(product_name);

#####################################################################################################



def process_am(am_lines):
#    print am_lines;
    links = [];
    images = [];
    names = [];
    prices = [];
    flag = 0;
    counter = 0;
    
#urllib has a very strange behaviour when retrieving webpages - The server hands out slightly difficult code to parse.
    flag = 0;
    for l in am_lines:
#        print 1;
        try:
            if ("<div id=\"srProductTitle" in l) and ("<a href=\"" in l) and ("src=\"" in l) and ("<br clear=\"all\" />" in l):
#                print l;
    #            break;
                ind =l.index("<a href=\"")+len("<a href=\"");
    #            print ind;
                indend = l.index("\"",ind+1);
                links.append(l[ind:indend]);
    #            i += 1;

                ind =l.index("src=\"")+len("src=\"");
                indend = l.index("\"",ind);
                images.append(l[ind:indend]);
    #            i+=1;
                
                ind =l.index("<br clear=\"all\" />")+len("<br clear=\"all\" />");
                indend = l.index("</a",ind);
                names.append(l[ind:indend]);
                
                flag = 1;
#                print links,images,names;

#            for j in range(10):             #generally keep going and stop when you find the necessary key word
#                i += 1;
            if ("<div class=\"newPrice\">" in l) or ("<div class=\"usedPrice\">" in l):
                if flag == 1:
#                    print flag;
                    indend =l.index("</span></span></div>");
                    ind = l.rfind("</span>",0,indend) + len("</span>");
                    prices.append(l[ind:indend]);
    #                    flag = 1;
                    counter +=1;
                    flag = 0;

        except ValueError:
            continue;
#                break;
#                if flag ==1:
#                    break;
        if counter == 3:
            break;

    return images,links,names,prices;

###########################################################################################################

def process_cr(cr_lines):
    links = [];
    images = [];
    names = [];
    prices = [];
    flag = 0;
    counter = 0;
    
#urllib has a very strange behaviour when retrieving webpages - The server hands out slightly difficult code to parse.
    flag = 0;
    base = "http://www.cromaretail.com"
    for l in cr_lines:
#        print l;
        try:
            if ("<article><a title=" in l) and ("href" in l) and ("<img src=\"" in l):
#                print l;
                ind =l.index("<article><a title=")+len("<article><a title=\"");
                indend = l.index("\"",ind+1);
                names.append(l[ind:indend]);

                ind =l.index("href=\"")+len("href=\"");
                indend = l.index("\"",ind+1);
                links.append(base+"/"+l[ind:indend]);
                
                ind =l.index("<img src=\"")+len("<img src=\"");
                indend = l.index("\"",ind+1);
                images.append(base+l[ind:indend]);
                flag =1;
            if ("</span>" in l) and flag ==1:
                ind =l.index("</span>")+len("</span>");
                indend = l.index("<",ind+1);
                prices.append(l[ind:indend]);
                counter += 1;
                flag =0;
        except ValueError:
            continue;
        if counter == 3:
            break;

    return images,links,names,prices;

#######################################################################################################################

def process_eb(eb_lines):
    links = [];
    images = [];
    names = [];
    prices = [];
    flag = 0;
    counter = 0;
    
#urllib has a very strange behaviour when retrieving webpages - The server hands out slightly difficult code to parse.


    for i in range(len(eb_lines)):
#        print l;
        l = eb_lines[i];
        try:
            if (" class=\"lv-1st\"></a>" in l):

                Link = eb_lines[i+12];
                Image = eb_lines[i+14];
                Name = eb_lines[i+14];
                Price = eb_lines[i+45];
#                print Link,Image,Name,Price,"\n\n\n=======================\n\n\n";

                ind =Link.index("<a href=\"")+len("<a href=\"");
                indend = Link.index("\"",ind+1);
                links.append(Link[ind:indend]);
                
                ind =Image.index("src=")+len("src=\"");
                indend = Image.index("class",ind+1);
                images.append(Image[ind:indend-2]);
                
                ind =Name.index("alt=")+len("alt=\"");
                indend = Name.index(" />",ind+1);
                names.append(Name[ind:indend-1]);
                
                ind =Price.index("</b>")+len("</b>");
                indend = Price.index("<",ind+1);
                prices.append(Price[ind:indend]);
                counter += 1;
                i += 50;
        except ValueError:
            continue;
        if counter == 3:
#            print images,"\n\n\n=======================\n\n\n",links,"\n\n\n=======================\n\n\n",names,"\n\n\n=======================\n\n\n",prices;
            return images,links,names,prices;
#            break;

if __name__=="__main__":
    proxy = 'http://10.93.0.37:3333';
    search_query = raw_input("Enter the name to compare : ");
    search_query = search_query.replace(" ","+");


    Flipkart_query = "http://www.flipkart.com/all-categories/pr?p%5B%5D=sort%3Drelevance&sid=search.flipkart.com&q="+search_query;
    Amazon_query = "http://www.amazon.in/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords="+search_query+"&rh=i%3Aaps%2Ck%3A"+search_query;
    Croma_query = "http://www.cromaretail.com/productsearch.aspx?txtSearch="+search_query+"&x=-808&y=-85";
    Ebay_query = "http://www.ebay.in/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0.X"+search_query+"&_nkw="+search_query+"&_sacat=0&_from=R40";


    Flipkart = urllib.urlopen(Flipkart_query, proxies={'http': proxy})
    Amazon = urllib.urlopen(Amazon_query, proxies={'http': proxy})
    Croma = urllib.urlopen(Croma_query, proxies={'http': proxy})
    Ebay = urllib.urlopen(Ebay_query, proxies={'http': proxy})

    fk_lines = Flipkart.readlines();
    am_lines = Amazon.readlines();
    cr_lines = Croma.readlines();
    eb_lines = Ebay.readlines();

    product_fk = process_fk(fk_lines);    
    product_am = process_am(am_lines);
    product_cr = process_cr(cr_lines);
    product_eb = process_eb(eb_lines);
    
    buildwebpage(product_fk,product_cr,product_am,product_eb,search_query);
#    Crowd_twitter();
