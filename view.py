def get_input(x, y, string):
    choice = "None"
    while choice.lower() != x and choice.lower() != y:
        print(string)
        choice = input("=>")
    return choice.lower()

def welcome():
    print("\n\n\n\n\n\n\n\n")     
    print("-------------------------------------------")
    print("Welcome to the Fortune Teller Evaluator")
    print("-------------------------------------------")       
    print("\n\n\n\n\n\n\n\n")

def show_evaluations(websites):
    print("Here is the ratio of correct to incorrect predictions:")
    for website in websites:

    print("Here are the ratios, but only changes of .1 percent or more are counted:")
    for website in websites:


