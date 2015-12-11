#baconian-cipher

from utility import normalize

def encrypt(str_input):
<<<<<<< HEAD
    str_input = str_input.lower()
=======
    str_input = normalize(str_input)
>>>>>>> b7c74213098822d84af3422d2fc07d9ab535f386
    bacon_dictionary = {
        "A":"AAAAA","B":"AAAAB","C":"AAABA","D":"AAABB",
        "E":"AABAA","F":"AABAB","G":"AABBA","H":"AABBB",
        "I":"ABAAA","J":"ABAAB","K":"ABABA","L":"ABABB",
        "M":"ABBAA","N":"ABBAB","O":"ABBBA","P":"ABBBB",
        "Q":"BAAAA","R":"BAAAB","S":"BAABA","T":"BAABB",
        "U":"BABAA","V":"BABAB","W":"BABBA","X":"BABBB",
        "Y":"BBAAA","Z":"BBAAB"}
    bring_home_the_bacon = ""
    for eachletter in str_input:
        bring_home_the_bacon += bacon_dictionary[eachletter]
    return bring_home_the_bacon
<<<<<<< HEAD

def decrypt(str_input):
=======
    
def decrypt(str_input):
    str_input = normalize(str_input)
>>>>>>> b7c74213098822d84af3422d2fc07d9ab535f386
    baconlist = chunks_of_bacon(str_input)
    bacon_dictionary = {
        "AAAAA":"A","AAAAB":"B","AAABA":"C","AAABB":"D",
        "AABAA":"E","AABAB":"F","AABBA":"G","AABBB":"H",
        "ABAAA":"I","ABAAB":"J","ABABA":"K","ABABB":"L",
        "ABBAA":"O","ABBAB":"N","ABBBA":"O","ABBBB":"P",
        "BAAAA":"Q","BAAAB":"R","BAABA":"S","BAABB":"T",
        "BABAA":"U","BABAB":"V","BABBA":"W","BABBB":"X",
        "BBAAA":"Y","BBAAB":"Z"}
    bring_home_the_bacon = ""
    for bacon in baconlist:
<<<<<<< HEAD
        bring_home_the_bacon += bacon_dictionary[bacon]
    return bring_home_the_bacon.upper()
=======
        bring_home_the_bacon += bacon_dictionary[bacon]             
    return bring_home_the_bacon
>>>>>>> b7c74213098822d84af3422d2fc07d9ab535f386

def chunks_of_bacon(l):
    return [l[i:i + 5] for i in range(0, len(l), 5)]
