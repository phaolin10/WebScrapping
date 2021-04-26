from re import match
from flask import Flask, json, request, jsonify
from bs4 import BeautifulSoup
from string import punctuation
from collections import Counter
import requests
app = Flask(__name__)


@app.route('/')
def show_all():
    return "asdfasdf"


@app.route('/frequency', methods=['GET', 'POST'])
def Frequency():
    if request.method == 'POST':
        data = request.get_json()
        r = requests.get(data['url'])
        source = BeautifulSoup(r.content, "html.parser")
        words = source.find().text
        punct = str.maketrans('', '', punctuation)
        words = words.translate(punct)
        words = words.split()
        words_count = Counter(words)
        for word in words_count.most_common(100):
            print(word)
        print(data['url'])
        return jsonify(words_count.most_common(1000))
    elif request.method == 'GET':
        print("burda")
        return "abcde"


@app.route('/keywords', methods=['GET', 'POST'])
def Keywords():
    if request.method == 'POST':
        lastList = []
        data = request.get_json()
        r = requests.get(data['url'])
        source = BeautifulSoup(r.content, "html.parser")
        words = source.find().text
        punct = str.maketrans('', '', punctuation)
        words = words.translate(punct)
        words = words.split()
        words_count = Counter(words)
        for kelime1 in words_count.most_common(10):
            if(kelime1[0] != "ve" and kelime1 != "ayrıca" and kelime1[0] != "fakat"
                and kelime1[0] != "ancak" and kelime1[0] != "ama" and kelime1[0] != "veya" and kelime1[0] != "yahut"
                and kelime1[0] != "lakin" and kelime1[0] != "veyahut" and kelime1[0] != "ki" and kelime1[0] != "halbuki"
                and kelime1[0] != "çünkü" and kelime1[0] != "de" and kelime1[0] != "ile" and kelime1[0] != "hem"
                and kelime1[0] != "ister" and kelime1[0] != "gerek" and kelime1[0] != "ne" and kelime1[0] != "ya"
                and kelime1[0] != "âdeta" and kelime1[0] != "belki" and kelime1[0] != "bari" and kelime1[0] != "binaenaleyh"
                and kelime1[0] != "eğer" and kelime1[0] != "hâlbuki" and kelime1[0] != "hatta" and kelime1[0] != "hazır"
                and kelime1[0] != "hele" and kelime1[0] != "illa" and kelime1[0] != "illâ" and kelime1[0] != "illaki"
                and kelime1[0] != "keşke" and kelime1[0] != "keza" and kelime1[0] != "lâkin" and kelime1[0] != "madem"
                and kelime1[0] != "mademki" and kelime1[0] != "mamafih" and kelime1[0] != "meğerki" and kelime1[0] != "ne"
                and kelime1[0] != "nasıl" and kelime1[0] != "neden" and kelime1[0] != "niçin" and kelime1[0] != "niye"
                and kelime1[0] != "nitekim" and kelime1[0] != "oysaki" and kelime1[0] != "öyle" and kelime1[0] != "sanki"
                and kelime1[0] != "şayet" and kelime1[0] != "şöyle" and kelime1[0] != "tâ" and kelime1[0] != "üstelik"
                and kelime1[0] != "yalnız" and kelime1[0] != "yani" and kelime1[0] != "yeter" and kelime1[0] != "yoksa"
                and kelime1[0] != "zaten" and kelime1[0] != "zati" and kelime1[0] != "bile" and kelime1[0] != "dahî"
                and kelime1[0] != "değil" and kelime1[0] != "ise" and kelime1[0] != "ya" and kelime1[0] != "gibi"):
                    lastList.append(kelime1)
        return jsonify(lastList)
    elif request.method == 'GET':
        print("burda")
        return "abcde"


@app.route('/similarity', methods=['GET', 'POST'])
def Similarity():
    if request.method == 'POST':
        data = request.get_json()
        i = 0
        j = 0
        List1Word = []
        List1Count = []
        List1Last = []
        Url1TotalCount = 0
        List2Word = []
        List2Count = []
        List2Last = []
        Url2TotalCount = 0

        html_text1 = requests.get(data['url']).text 
        soup1 = BeautifulSoup(html_text1, 'html.parser')
        kelimeler1 = soup1.find().text
        noktalama1 = str.maketrans('', '', punctuation) 
        kelimeler1 = kelimeler1.translate(noktalama1) 
        kelimeler1 = kelimeler1.split()
        kelime_say1 = Counter(kelimeler1)
        print(type(kelime_say1), '\n')
        for kelime1 in kelime_say1.most_common(10): 

            if(kelime1[0] != "ve" and kelime1[0] != "bir" and kelime1 != "ayrıca" and kelime1[0] != "fakat"
            and kelime1[0] != "ancak" and kelime1[0] != "ama" and kelime1[0] != "veya" and kelime1[0] != "yahut"
            and kelime1[0] != "lakin" and kelime1[0] != "veyahut" and kelime1[0] != "ki" and kelime1[0] != "halbuki"
            and kelime1[0] != "çünkü" and kelime1[0] != "de" and kelime1[0] != "ile" and kelime1[0] != "hem"
            and kelime1[0] != "ister" and kelime1[0] != "gerek" and kelime1[0] != "ne" and kelime1[0] != "ya"
            and kelime1[0] != "âdeta" and kelime1[0] != "belki" and kelime1[0] != "bari" and kelime1[0] != "binaenaleyh"
            and kelime1[0] != "eğer" and kelime1[0] != "hâlbuki" and kelime1[0] != "hatta" and kelime1[0] != "hazır"
            and kelime1[0] != "hele" and kelime1[0] != "illa" and kelime1[0] != "illâ" and kelime1[0] != "illaki"
            and kelime1[0] != "keşke" and kelime1[0] != "keza" and kelime1[0] != "lâkin" and kelime1[0] != "madem"
            and kelime1[0] != "mademki" and kelime1[0] != "mamafih" and kelime1[0] != "meğerki" and kelime1[0] != "ne"
            and kelime1[0] != "nasıl" and kelime1[0] != "neden" and kelime1[0] != "niçin" and kelime1[0] != "niye"
            and kelime1[0] != "nitekim" and kelime1[0] != "oysaki" and kelime1[0] != "öyle" and kelime1[0] != "sanki"
            and kelime1[0] != "şayet" and kelime1[0] != "şöyle" and kelime1[0] != "tâ" and kelime1[0] != "üstelik"
            and kelime1[0] != "yalnız" and kelime1[0] != "yani" and kelime1[0] != "yeter" and kelime1[0] != "yoksa"
            and kelime1[0] != "zaten" and kelime1[0] != "zati" and kelime1[0] != "bile" and kelime1[0] != "dahî"
            and kelime1[0] != "değil" and kelime1[0] != "ise" and kelime1[0] != "ya" and kelime1[0] != "gibi"
            and kelime1[0] != "değil" and kelime1[0] != "ise" and kelime1[0] != "ya" and kelime1[0] != "gibi"):
                List1Word.append(kelime1[0]) 
                List1Count.append(kelime1[1])
                List1Last.append(kelime1)
                # print("({0} , {1})".format(List1Word[i], List1Count[i]))
                i = i+1


        html_text2 = requests.get(data['urlOne']).text
        soup2 = BeautifulSoup(html_text2, 'html.parser')
        kelimeler2 = soup2.find().text
        noktalama2 = str.maketrans('', '', punctuation)
        kelimeler2 = kelimeler2.translate(noktalama2)
        kelimeler2 = kelimeler2.split()
        kelime_say2 = Counter(kelimeler2)
        print("aaaaaa",kelime_say2.most_common(10))
        print(type(kelime_say2), '\n')
        for kelime2 in kelime_say2.most_common(10):
            if(kelime2[0] != "ve" and kelime2[0] != "bir" and kelime2 != "ayrıca" and kelime2[0] != "fakat"
            and kelime2[0] != "ancak" and kelime2[0] != "ama" and kelime2[0] != "veya" and kelime2[0] != "yahut"
            and kelime2[0] != "lakin" and kelime2[0] != "veyahut" and kelime2[0] != "ki" and kelime2[0] != "halbuki"
            and kelime2[0] != "çünkü" and kelime2[0] != "de" and kelime2[0] != "ile" and kelime2[0] != "hem"
            and kelime2[0] != "ister" and kelime2[0] != "gerek" and kelime2[0] != "ne" and kelime2[0] != "ya"
            and kelime2[0] != "âdeta" and kelime2[0] != "belki" and kelime2[0] != "bari" and kelime2[0] != "binaenaleyh"
            and kelime2[0] != "eğer" and kelime2[0] != "hâlbuki" and kelime2[0] != "hatta" and kelime2[0] != "hazır"
            and kelime2[0] != "hele" and kelime2[0] != "illa" and kelime2[0] != "illâ" and kelime2[0] != "illaki"
            and kelime2[0] != "keşke" and kelime2[0] != "keza" and kelime2[0] != "lâkin" and kelime2[0] != "madem"
            and kelime2[0] != "mademki" and kelime2[0] != "mamafih" and kelime2[0] != "meğerki" and kelime2[0] != "ne"
            and kelime2[0] != "nasıl" and kelime2[0] != "neden" and kelime2[0] != "niçin" and kelime2[0] != "niye"
            and kelime2[0] != "nitekim" and kelime2[0] != "oysaki" and kelime2[0] != "öyle" and kelime2[0] != "sanki"
            and kelime2[0] != "şayet" and kelime2[0] != "şöyle" and kelime2[0] != "tâ" and kelime2[0] != "üstelik"
            and kelime2[0] != "yalnız" and kelime2[0] != "yani" and kelime2[0] != "yeter" and kelime2[0] != "yoksa"
            and kelime2[0] != "zaten" and kelime2[0] != "zati" and kelime2[0] != "bile" and kelime2[0] != "dahî"
            and kelime2[0] != "değil" and kelime2[0] != "ise" and kelime2[0] != "ya" and kelime2[0] != "gibi"
            and kelime2[0] != "değil" and kelime2[0] != "ise" and kelime2[0] != "ya" and kelime2[0] != "gibi"):

                List2Word.append(kelime2[0])
                List2Count.append(kelime2[1])
                List2Last.append(kelime2)
                # print("({0} , {1})".format(List2Word[j], List2Count[j]))
                j = j+1


        for kelime1 in kelime_say1.most_common(100000000):
            Url1TotalCount = Url1TotalCount + kelime1[1]

        print(Url1TotalCount)

        for kelime2 in kelime_say2.most_common(100000000):
            Url2TotalCount = Url2TotalCount + kelime2[1]

        print(Url2TotalCount)


        print("Benzerlik oranı:")
        print("------------------------------------------------------------------")
        print("1. URL    -    2. URL")
        print("---------------------")
        totalSameWords = 0
        for x in range(len(List1Word)):
            for y in range(len(List2Word)):
                if(List1Word[x] == List2Word[y]):
                    totalSameWords = totalSameWords+1
        matchListRatio = []
        matchList = []
        WordSameRatio = 0
        for x in range(len(List1Word)):
            for y in range(len(List2Word)):
                if(List1Word[x] == List2Word[y]):
                    if(List1Count[x] > List2Count[y]):
                        WordSameRatio = (List2Count[y]/List1Count[x])*100
                    elif(List1Count[x] < List2Count[y]):
                        WordSameRatio = (List1Count[x]/List2Count[y])*100
                    else:
                        WordSameRatio = 100
                    print("({0} , {1})   -   ({2} , {3}) - > Benzerlik Oranı: % {4}".format(
                        List1Word[x], List1Count[x], List2Word[y], List2Count[y], (round(WordSameRatio, 2))))
                    matchList.append([List1Word[x],List1Count[x],List2Count[y],(round(WordSameRatio, 2))])
                    
        WordSameRatio = 0
        Total1 = 0
        Total2 = 0
        for x in range(len(List1Word)):
            for y in range(len(List2Word)):
                if(List1Word[x] == List2Word[y]):
                    if(Url1TotalCount < Url2TotalCount):
                        Total1 = Total1+List1Count[x]
                        WordSameRatio = (Total1/Url2TotalCount)*100
                    elif(Url1TotalCount > Url2TotalCount):
                        Total2 = Total2+List2Count[y]
                        WordSameRatio = (Total2/Url1TotalCount)*100
                    else:
                        WordSameRatio = 100

        matchListRatio.append([(round(WordSameRatio, 2))])
        print(matchListRatio)
        print("Benzerlik Oranı: % {0}".format((round(WordSameRatio, 2))))
    return jsonify({'matchList': matchList, 'matchRatio' : matchListRatio , 'keywordsUrl':List1Last , 'keywordsUrl1':List2Last})            

@app.route('/semanticAnalysis', methods=['GET', 'POST'])
def semanticAnalysis():
    data = request.get_json()
    semanticWords = []
    lastList = []
    matchSemanticWords = []
    inWebsiteSemanticWords = []
    openTxt(semanticWords)
    sendRequest(data['url'],lastList)
    d1 = [item[0] for item in semanticWords]
    d2 = [item[1] for item in semanticWords]
    d3 = [item[0] for item in lastList]
    findSemanticWords(d1,d2,d3,matchSemanticWords)
    print(matchSemanticWords)
    return jsonify( matchSemanticWords)

def openTxt(semanticWords):
    with open("kelime-esanlamlisi.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            line = line.split("\t")
            semanticWords.append(line)


def sendRequest(url,lastList):
    try:
        r = requests.get(url)
        source = BeautifulSoup(r.content, "html.parser")
        words = source.find().text
        punct = str.maketrans('', '', punctuation)
        words = words.translate(punct)
        words = words.split()
        words_count = Counter(words)
        for kelime1 in words_count.most_common(10):
            if(kelime1[0] != "ve" and kelime1 != "ayrıca" and kelime1[0] != "fakat"
                    and kelime1[0] != "ancak" and kelime1[0] != "ama" and kelime1[0] != "veya" and kelime1[0] != "yahut"
                    and kelime1[0] != "lakin" and kelime1[0] != "veyahut" and kelime1[0] != "ki" and kelime1[0] != "halbuki"
                    and kelime1[0] != "çünkü" and kelime1[0] != "de" and kelime1[0] != "ile" and kelime1[0] != "hem"
                    and kelime1[0] != "ister" and kelime1[0] != "gerek" and kelime1[0] != "ne" and kelime1[0] != "ya"
                    and kelime1[0] != "âdeta" and kelime1[0] != "belki" and kelime1[0] != "bari" and kelime1[0] != "binaenaleyh"
                    and kelime1[0] != "eğer" and kelime1[0] != "hâlbuki" and kelime1[0] != "hatta" and kelime1[0] != "hazır"
                    and kelime1[0] != "hele" and kelime1[0] != "illa" and kelime1[0] != "illâ" and kelime1[0] != "illaki"
                    and kelime1[0] != "keşke" and kelime1[0] != "keza" and kelime1[0] != "lâkin" and kelime1[0] != "madem"
                    and kelime1[0] != "mademki" and kelime1[0] != "mamafih" and kelime1[0] != "meğerki" and kelime1[0] != "ne"
                    and kelime1[0] != "nasıl" and kelime1[0] != "neden" and kelime1[0] != "niçin" and kelime1[0] != "niye"
                    and kelime1[0] != "nitekim" and kelime1[0] != "oysaki" and kelime1[0] != "öyle" and kelime1[0] != "sanki"
                    and kelime1[0] != "şayet" and kelime1[0] != "şöyle" and kelime1[0] != "tâ" and kelime1[0] != "üstelik"
                    and kelime1[0] != "yalnız" and kelime1[0] != "yani" and kelime1[0] != "yeter" and kelime1[0] != "yoksa"
                    and kelime1[0] != "zaten" and kelime1[0] != "zati" and kelime1[0] != "bile" and kelime1[0] != "dahî"
                    and kelime1[0] != "değil" and kelime1[0] != "ise" and kelime1[0] != "ya" and kelime1[0] != "gibi"):
                lastList.append(kelime1)

    except:
        print("hatalı url")

def findSemanticWords(d1,d2,d3,matchSemanticWords):
    for x in range(len(d1)):
        for y in range(len(d3)):
            if(d1[x] == d3[y]):
                matchSemanticWords.append([d1[x],d2[x]])



    
app.run()
