myDict = {"miller": "killer the one who  works in the work"}


my_dict = dict()

print(my_dict)

eng_sp = dict(one= "uno", two = "dos", three = "tres" )
print(eng_sp)

eng_sp2 = {"one":"uno", "two": "dos", "three": "tres"}
print(eng_sp2)


eng_sp3 = [("one", "uno"), ("two","dos"),("three","tres")]
print(eng_sp3)

engspLst = dict(eng_sp3)
print(engspLst)


eng_sp2["one"] = "onos"

print(eng_sp2)


def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
traverseDict(eng_sp2)


val = eng_sp2.pop("one")
print(val)
print(eng_sp2)
