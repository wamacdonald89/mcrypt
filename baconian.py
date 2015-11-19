#baconian-cipher

import string

def baconize(str_input):
    str_input = str_input.lower()
    bacon_dictionary = {
        "a":"AAAAA","b":"AAAAB","c":"AAABA","d":"AAABB",
        "e":"AABAA","f":"AABAB","g":"AABBA","h":"AABBB",
        "i":"ABAAA","j":"ABAAB","k":"ABABA","l":"ABABB",
        "m":"ABBAA","n":"ABBAB","o":"ABBBA","p":"ABBBB",
        "q":"BAAAA","r":"BAAAB","s":"BAABA","t":"BAABB",
        "u":"BABAA","v":"BABAB","w":"BABBA","x":"BABBB",
        "y":"BBAAA","z":"BBAAB"}
    bring_home_the_bacon = ""
    for eachletter in str_input:
        bring_home_the_bacon += bacon_dictionary[eachletter]
    return bring_home_the_bacon
    
def de_baconize(str_input):
    baconlist = chunks_of_bacon(str_input)
    bacon_dictionary = {
        "AAAAA":"a","AAAAB":"b","AAABA":"c","AAABB":"d",
        "AABAA":"e","AABAB":"f","AABBA":"g","AABBB":"h",
        "ABAAA":"i","ABAAB":"j","ABABA":"k","ABABB":"l",
        "ABBAA":"m","ABBAB":"n","ABBBA":"o","ABBBB":"p",
        "BAAAA":"q","BAAAB":"r","BAABA":"s","BAABB":"t",
        "BABAA":"u","BABAB":"v","BABBA":"w","BABBB":"x",
        "BBAAA":"y","BBAAB":"z"}
    bring_home_the_bacon = ""
    for bacon in baconlist:
        bring_home_the_bacon += bacon_dictionary[bacon]             
    return bring_home_the_bacon.upper()

def chunks_of_bacon(l):
    return [l[i:i + 5] for i in range(0, len(l), 5)]
