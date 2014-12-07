def get_input(x, y, string):
    choice = "None"
    while choice.lower() != x and choice.lower() != y:
        print(string)
        choice = input("=>")
    return choice.lower()

def welcome():
    print("\n\n\n\n\n\n\n\n")     
    print("-------------------------------------------")
    print("Welcome to the StockHotOrNot (rate my fortune teller)")
    print("-------------------------------------------")       
    print("\n\n\n\n\n\n\n\n")

def show_evaluations(results):
    print("Here is the ratio of correct to incorrect predictions:")
    for result in results:
        print("The website {} has a {} ratio of correct to incorrect predictions".format(result["website"], result["ratio"]))

    print("Here are the ratios, but only changes of .1 percent or more are counted:")
    # for website in websites:


