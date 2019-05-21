
test = {
    "key1":"one",
    "key2":"two",
    "key3":"three"
    }
tt = ""
#tt = "".join(test["key1"]) + "".join(test["key1"])
tt= test["key1"]+test["key1"]
print(tt)