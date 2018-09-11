#create this program with a Boolean function bird_available()
#has parameter that takes the name of a type of bird
#for this exercise the variable bird_types = 'crow robin parrot eagle sandpiper hawk pigeon'
#return True or False (we are making a Boolean function)
#call the function using the name of a bird type from user input
#print a sentence that indicates the availability of the type of bird checked
# [ ] create function bird_available

# [ ] user input

# [ ] call bird_available

# [ ] print availability status

def bird_avaliable():
    bird_type ='crow, robin, parrot'
    bird =input("enter name of bird")
    return(bird.lower() in bird_type)
bird_d = bird_avaliable()
print(bird_d)