import requests

f = open('./papers.nips.cc_4th_Jan_2020.txt','r')
download_urls = f.readlines()

for url in download_urls:
    # print(url.strip().split('/')[-1])
    paper = requests.get(url.strip()+'.pdf')
    with open("/Users/xucong/Downloads/NIPS2019/"+url.strip().split('/')[-1]+'.pdf',"wb") as code:
        code.write(paper.content)