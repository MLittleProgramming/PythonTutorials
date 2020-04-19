text = "MLittleProgramming"
try:
    int(text)
except ValueError:
    print("This type can't be casted")
except:
    print("There was an error of some kind")
else:
    print("There was no error caused")
