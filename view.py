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
    print("Here is the ratio of correct to incorrect predictions:\n")
    for result in results:
        print("The website {} has a {} ratio of correct to incorrect predictions".format(result["website"], result["ratio"]))
    print("\nHere are the ratios, but with margins of less than .1 percent discounted:")
        # for website in websites:


