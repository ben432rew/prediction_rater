def get_input(x, y, string):
    choice = "None"
    while choice.lower() != x and choice.lower() != y:
        print(string)
        choice = input("=>")
    return choice.lower()

def welcome():
    print("\n\n\n\n\n\n\n\n")     
    print("*****************************************************")
    print("Welcome to the StockHotOrNot (rate my fortune teller)")
    print("*****************************************************")       
    print("\n\n\n\n\n\n")

def show_evaluations(results):
    print("Here is percentage of correct predictions:")
    print("-----------------------------------------------------")
    for result in results:
        print("The website {} has a {}% success rate".format(result["website"], round(result["percent"])))
    print("-----------------------------------------------------")        

def show_non_marginal(results):
    print("\nHere are the percentages, but with margins of less than .1 percent discounted:")
    print("-----------------------------------------------------")  
    for result in results:
        print("The website {} has a {}% success rate".format(result["website"], round(result["percent"])))
    print("-----------------------------------------------------")    
    return get_input('y','q', "would you like to see today's predictions?  Press 'Y' to see them, or 'Q' to Quit")

def show_todays(results):
    print("\n\n Here are todays predictions:")
    for r in results:
        print("{} predicts that {} will go {} today".format(r.website, r.symbol, r.prediction))

def show_consistent_winners(results):
    pass    