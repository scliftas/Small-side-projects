from lxml import html
import requests, time, os, subprocess

start = time.time()

old = []
count = 0

while True:

    page = requests.get('http://www.bbc.co.uk/news')
    tree = html.fromstring(page.content)
    headlines = tree.xpath("//div[@class='nw-c-top-stories gs-t-news no-touch gs-u-box-size']//h3/text()")
    desc = tree.xpath("//div[@class='nw-c-top-stories gs-t-news no-touch gs-u-box-size']//p/text()")
    heads = []

    for i in headlines:
        r = i.split("\n", 1)[0]
        heads.append(r)

    heads = list(filter(None, heads))
    heads = set(heads)
    os.system('clear')
    time.sleep(0.2)
    print ('Top Headlines:')
    for i in heads:
        print(i)

    keywords = ['Trump', 'May', 'war', 'Putin', 'Russia']

    if count == 1:
        new = list(heads - set(old))
        for i in new:
            if any(word in i for word in keywords):
                pos = headlines.index(i)
                result = desc[pos]
                subprocess.call(['notify-send', i, result])
        print("\nNew headlines: ", len(new))
        if len(new) > 0:
            subprocess.call(['notify-send', "New Headlines"])
    elif count == 0:
        for i in heads:
            if any(word in i for word in keywords):
                pos = headlines.index(i)
                result = desc[pos]
                subprocess.call(['notify-send', i, result])

    time.sleep(60.0 - ((time.time() - start) % 60.0))

    old = []
    old = heads
    count = 1
