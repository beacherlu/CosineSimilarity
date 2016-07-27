# -*- coding: utf-8 -*-

import os;
import  math;
FILENAME_LIST=[]


def isExclude(filename=''):
    excludelist = ['software','code','.git','System Volume Information']

    for i in excludelist:
        if filename.find(i) !=-1:
            return True;

    return False;


def isInclude(filename=''):
    includelist = ['.pdf']

    for i in includelist:
        if filename.find(i) !=-1:
            return True;

    return False;


def handleName(e = ""):
    while e.find(' ') != -1:
        e = e.replace(' ','\ ')
        print " === "+e
    return e


def readdirlist(dir, fileList):
    l = os.listdir(dir)

    for e in l:
        if isExclude(dir+"/"+e):
            continue;

        if os.path.isdir(dir+"/"+e):
            readdirlist(dir+"/"+e,[])

        if isInclude(e)!=True:
            continue;

        if os.path.isdir(dir+"/"+e):
            print dir+"/"+e
        #exclude
        # if e.find('amap') != -1:
        #     continue;
        if os.path.isfile(dir+"/"+e):
            FILENAME_LIST.append(dir+"/"+e);

    return fileList

def cosAcal(dicA={},dicB={}):
    fenmu = 0.000001
    fenzi = 0;

    tempfenmu=0.000001
    for key in dicA.keys():
        tempfenmu+=dicA[key]*dicA[key]
    fenmu+= math.sqrt(tempfenmu);

    tempfenmu=0.000001
    for key in dicB.keys():
        tempfenmu+=dicB[key]*dicB[key]

    fenmu*=math.sqrt(tempfenmu);

    for key in dicA.keys():
        fenzi+= dicA[key]*dicB[key]

    return fenzi/fenmu

def cosAsame(a='',b=''):
    pass
    dic = {}
    for i in a:
        if not dic.has_key(i):
            dic[i]=0;
    for i in b:
        if not dic.has_key(i):
            dic[i]=0;
    dicA = dic.copy();
    dicB = dic.copy();
    for i in a:
        if dicA.has_key(i):
            dicA[i]+=1;
    for i in b:
        if dicB.has_key(i):
            dicB[i]+=1;
    if cosAcal(dicA,dicB) > 0.98:
        print a+" ---- "+b+" [ "+str(cosAcal(dicA,dicB))+" ]"




if __name__ == '__main__':
    readdirlist(u"D:/",[])
    for l in FILENAME_LIST:
        print l;

    for l in FILENAME_LIST:
        print l.split('/')[len(l.split('/'))-1]


    for i in range(len(FILENAME_LIST)):
        for j in range(i+1,len(FILENAME_LIST)):
            a = FILENAME_LIST[i].split('/')[len(FILENAME_LIST[i].split('/'))-1]
            b = FILENAME_LIST[j].split('/')[len(FILENAME_LIST[j].split('/'))-1]
            cosAsame(a,b)
            break;
    # print u'D://System Volume Information\\*.*'.replace(' ','\ ')
    # l = os.listdir('C:/')
    # print l;