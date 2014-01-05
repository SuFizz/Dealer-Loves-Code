import urllib

def link_fk_actu(product_image):
    Flipkart_query = "http://www.flipkart.com/all-categories/pr?p%5B%5D=sort%3Drelevance&sid=search.flipkart.com&q=";
    print "\n\n\n\n\nLINK FK ACTUAL";
#    print product_image;
    names = [];
    for i in range(3):
        ind = product_image[i].index("data-pid=")+len("data-pid=\"");
        indend = product_image[i].index("data-tracking-products",ind) - 2;
        names.append(Flipkart_query + product_image[i][ind:indend]);
    return names;

def price_fk(product_image):
    print "\n\n\n\n\nPRICE FK";
    print product_image;
    names = [];
    for i in range(3):
        indend = product_image[i].index(";;");
        ind = product_image[i].rfind(";",0,indend-1);
        names.append(product_image[i][ind+1:indend]);
    return names;

def name_fk(product_image):
    print "\n\n\n\n\nNAME FK";
#    print product_image;
    names = [];
    for i in range(3):
        ind = product_image[i].index("alt")+len("alt=\"");
        names.append(product_image[i][ind:].split()[0]);
#        product_image[i][ind:indend]);
    return names;

def link_fk(product_link):
    print "\n\n\n\n\nLINK FK";
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
        print product_image[i];
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

if __name__=="__main__":
    proxy = 'http://10.93.0.37:3333';
    search_query = raw_input("Enter the name to compare : ");
    search_query = search_query.replace(" ","+");


    Flipkart_query = "http://www.flipkart.com/all-categories/pr?p%5B%5D=sort%3Drelevance&sid=search.flipkart.com&q="+search_query;
    Amazon_query = "http://www.amazon.in/s/ref=nb_sb_ss_i_0_8?url=search-alias%3Daps&field-keywords="+search_query;
    Croma_query = "http://www.cromaretail.com/productsearch.aspx?txtSearch="+search_query+"&x=-808&y=-85";
    Ebay_query = "http://www.ebay.in/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0.Xsamsung&_nkw=samsung&_sacat=0&_from=R40"


    Flipkart = urllib.urlopen(Flipkart_query, proxies={'http': proxy})
    Amazon = urllib.urlopen(Amazon_query, proxies={'http': proxy})

    fk_lines = Flipkart.readlines();
    am_lines = Amazon.readlines();
#    cr_lines = Croma.readlines();
#    eb_lines = Ebay.readlines();

    prod_fk =process_fk(fk_lines);#    product_fk,images_fk = 
    
#    product_am,images_am = process_am(am_lines);
#    product_cr,images_cr = process_cr(cr_lines);
#    product_eb,images_eb = process_eb(eb_lines);