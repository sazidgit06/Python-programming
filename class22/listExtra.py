names = ["Milo", "Sarah", "Amaina", "Okia", "Saliba", "Umair"]
# namesWidth = [i for i in names if "o" in i]
namesWidth = [i for i in names if (len(i) > 4)]
print(namesWidth)