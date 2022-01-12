#!/usr/bin/python
# import commands
from bs4 import BeautifulSoup
# from urllib3 import urlopen
from urllib.request import urlopen
import sys
if len(sys.argv) == 2 and sys.argv[1] == "autoconf":
    print("yes")
elif len(sys.argv) == 2 and sys.argv[1] == "config":
    print("graph_title Temperature")
    print("graph_vlabel Celsius")
    print("graph_category sensors")
    print("graph_args --base 1000 -l 0")
    print("MeteoSTG.label Meteo STG Petite France")
    print("Temper.label Temperature Cave")
else:
    html = urlopen('https://www.senscritique.com/liste/Disponible_sur_Netflix/2844569')
    soup = BeautifulSoup(html)

    # class list set
    class_list = set()

    notes1 = {notes1.text for notes1 in soup.find_all(class_="erra-global")}
    titles = {titles.text for titles in soup.find_all(class_="elco-anchor")}
    links_number1  = {links.text for links in soup.find_all(class_="eipa-anchor")}
    link  = soup.find(class_="eipa-anchor")
    link = link['href']
    print("Titles : " + str(titles))
    print("Titles len : " + str(len(titles)))
    print("Link : " + str(link))
    links_number = []
    for link_number2 in links_number1:
        link_number2 = int(link_number2.replace("...",""))
        links_number.append(link_number2)
    print("links_number : " + str(links_number))
    notes = []
    links = 0
    for note in notes1:
        note = note.replace("\n","")
        note = note.replace("\t","")
        notes.append(note)
    links_number_max = max(links_number)
    # for link in links1:
    #     # print(link['href'])
    #     link = link['href']
    #     links.append(link)

    print("Note : " + str(notes))
    print("Note len : " + str(len(notes)))
    print("Links : " + str(links_number))
    print("Links len : " + str(len(links_number)))
    print("Links number max : " + str(links_number_max))


    # iterate all tags
    # for title in titles:
    #     print(titles)
    #     # find all element of tag
    #     for i in soup.find_all( title ):
    #         print(i)
    #         # if tag has attribute of class
    #         if i.has_attr( "class" ):
    
    #             if len( i['class'] ) != 0:
    #                 class_list.add(" ".join( i['class']))
    
    # print( class_list )
    
    # # class list set
    # class_list = set()

    # tags = {tag.name for tag in soup.find_all()}
    
    # # iterate all tags
    # for tag in tags:
    
    #     # find all element of tag
    #     for i in soup.find_all( tag ):
    
    #         # if tag has attribute of class
    #         if i.has_attr( "class" ):
    
    #             if len( i['class'] ) != 0:
    #                 class_list.add(" ".join( i['class']))
    
    # print( class_list )