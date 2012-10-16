"""Fichier de test TD1"""
import httplib
import sys
import pdb
LOG = False
if (len(sys.argv)>2):
    LOG = True
def logger(myfile, message):
    """logger"""
    if LOG:
        myfile.write(message)


def connection(adresse):
    """connection"""
    pdb.set_trace()
    conn = httplib.HTTPConnection("cache.univ-st-etienne.fr", 3128)
    conn.request("GET", adresse)
    response = conn.getresponse()
    return response
##print r1.status,r1.reason
##data = r1.read()
##print len(data)
##print len(data.split(' '))

RES = connection(sys.argv[1])
FILE = open(sys.argv[2], "w")
logger(FILE, "status:%s\n"%str(RES.status))
DATA = RES.read()
logger(FILE, "longeur:%s\n"%len(DATA))
logger(FILE, "nb des mots:%d\n"%len(DATA.split(' ')))
FILE.close()
##"http://www.python.org/index.html"
