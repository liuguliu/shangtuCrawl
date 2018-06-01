import json
import time

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(0,26):
    urilist = []
    jsonlist = []
    urifile = open("./data/Alluri/shangtushuju_"+alphabet[i]+".txt",'r',encoding='utf-8')
    jsonfile = open("./jsondata/shangtushuju_"+alphabet[i]+".txt",'r',encoding='utf-8')
    leaveoutfile = open("./data/leaveout/shangtushuju_"+alphabet[i]+".txt",'a+',encoding='utf-8')
    urilines = urifile.readlines()
    jsonlines = jsonfile.readlines()
    for uri in urilines:
        urilist.append(uri)
    for jsonline in jsonlines:
        try:
            jsondata = json.loads(jsonline,encoding='utf-8')
            jsonlist.append(jsondata)
        except:
            continue
    num = 0
    for uri in urilist:
        dottindex = uri.find(',')
        urid = uri[dottindex+1:-1]
        #print(urid)
        #time.sleep(2)
        flag = False
        for person in jsonlist:
            if(person['jsondata']['uri']==urid):
                flag = True
                break;
        if(flag==False):
            leaveoutfile.writelines(uri)
            num=num+1
    print(num)
    leaveoutfile.close()
    jsonfile.close()
    urifile.close()

