#!/usr/bin/python
import re, urllib
try:
    import urllib.request
except:
    pass

strona = 'http://hyipexplorer.com'

def get_blocks():
    global blok

    pat = re.compile(r'<b><font color="r+.*?<tr><td colspan="7" style="padding:2px;border-top: 2px solid #C40000;">+', re.I|re.M)
    print ('Searching: ' + strona)
    try:
        u = urllib.urlopen(strona)
    except:
        u = urllib.request.urlopen(strona)
    text = u.read()
    text = text.replace("\n", "")
    blok = re.findall(pat, text)

    print 'jest ' + str(len(blok)) + ' hyipow na stronie glownej'


def get_titles():
    global tytuly
    tytuly = []
    pat = re.compile(r'<b><font color="r+.*?</b>+', re.I|re.M)
    for i in range(len(blok)):
        tytul = re.findall(pat, str(blok[i]))
        t = re.search(r'([A-Z0-9]+)</font>(.+)<', tytul[0], re.I|re.M)
        t = t.group(1)+t.group(2)
        tytuly.append(t)
    print 'jest ' + str(len(tytuly)) + ' tytulow hyipow'


def get_urls():
    global urls
    urls = []
    for i in range(len(blok)):
        t = re.search(r'border="0" /><a  href="(.*?)">program+', blok[i])
        if t == None:
            t = re.search(r'underline" href="(.*?)">program+', blok[i])
        t = t.group(1)
        urls.append(t)
    print 'jest ' + str(len(urls)) + ' linkow do hyipow'

def get_hyip_page(i):
    site = 'http://hyipexplorer.com' + urls[i]
    try:
        u = urllib.urlopen(site)
    except:
        u = urllib.request.urlopen(site)
    text = u.read()
    if not text == None:
        print 'url ' + str(i+1) + ' OK'

def get_status():
    global status
    status = []
    for i in range(len(blok)):
        t = re.search(r'color:#00B300;">(\w+)</span>', blok[i])
        if t == None:
            t = re.search(r'color:#9E9E9E;">(\w+)</a>', blok[i])
            if t == None:
                t = re.search(r'color:#FF8000;">(\w+)</a>', blok[i])
        t = t.group(1)
        status.append(t)
    print 'jest ' + str(len(status)) + ' statosow hyipow'

def get_days():
    global days
    days = []    
    for i in range(len(blok)):
        t = re.search(r'listed for (\d+) days', blok[i])
        if t == None:
            t = re.search(r'listed for (\d+) day', blok[i])
        t = t.group(1)
        days.append(t)
    print 'jest ' + str(len(status)) + ' wartosci dni kontrolowania hyipow'


get_blocks()
get_titles()
get_urls()
get_status()
get_days()
#for i in range(len(urls)):
#    get_hyip_page(i)
hyips = []
for i in range(len(blok)):
    bufor = []
    bufor.append(tytuly[i])
    bufor.append(urls[i])
    bufor.append(status[i])
    bufor.append(days[i])
    hyips.append(bufor)

