#create Allergy check code
greeting ="This is allergey test"
print(greeting)
inp_test = input("enter food categories eaten in last 24 hours: ").lower()
#print(inp_test)
#print("You have eaten in last 24 hours " + inp_test)
print("It is","dairy" in inp_test, "that", '"',inp_test,'"','contains "dairy"')
print("It is","seafood" in inp_test, "that", '"',inp_test,'"','contains "seafood"')
print("It is","nuts" in inp_test, "that", '"',inp_test,'"','contains "nuts"')
print("It is","chocolate" in inp_test, "that", '"',inp_test,'"','contains "chocolate"')
#print("Its true that", inp_test,'cantains "seafood"', "seafood" in inp_test)
#print('"Its true that seafood, dairy, nuts and chocolate cake" cantains "dairy"', "dairy" in inp_test)
#print('"its ture that seafood, dairy, nuts and chocolate cake" cantains "seafood"', "seafood" in inp_test)
#print('"its ture that seafood, dairy, nuts and chocolate cake" cantains "nuts"', "nuts" in inp_test)