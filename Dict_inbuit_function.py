d={"pen":"kalam","gold":"sona","diamond":"heera","silver":"chandi","list":[1,2,3,4,6]}
print(d.items())             # item built in fuction// return pair of key and values

print(d.keys())              # .keys built in function //return the list of keys of dictionery

d.update({"mine":"mera"})    # update built in funtion// add thepair of key and value at end of dict
print(d)

print(d.get("list"))         # get built in function// return the value of desired key

print(d.values())            # values built in function// return the list of value of dict

print(d.__len__())           # len built in funtion// return the length of dict

d.clear()                    # clear built in funtion // make empty dict
print(d)