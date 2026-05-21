from search_terms import interventions, outcomes, populations
from menu import menu
from enums import Category
from pyperclip import copy

def main():
   
    terms_included = []
    menu_options = ["Add intervention", "Add outcome", "Add population",]
    
    while True:
        
        match menu(options=menu_options, menu_text="What would you like to do?"):
            case "Add intervention":
                category = interventions
            case "Add outcome":
                category = outcomes
            case "Add population":
                category = populations
            case "Generate search":
                break
        
        choice: Category | str = menu(options=list(category) + ["Go back"], menu_text="What would you like to add?")
        if choice == "Go back":
            continue

        terms_included.append(category[choice])

        if "Generate search" not in menu_options:
            menu_options.append("Generate search")
    

    search_text = ""
    for iter in range(len(terms_included)):
        search_term_clusters = terms_included[iter]
        print(search_term_clusters)

        search_text += "("
        
        for iter2 in range(len(search_term_clusters)):
            search_text += ('("' + search_term_clusters[iter2] + '")')
            if iter2 != len(search_term_clusters) - 1:
                search_text += " OR "

        search_text += ")"

        
        if iter != len(terms_included) - 1:
            search_text += " AND "
    
    print(search_text)

    if menu(options=["Yes", "No"], menu_text="Would you like to copy your search to clipboard?") == "Yes":
        copy(search_text)
        print("Search text copied to clipboard!")
     

if __name__ == "__main__":
    main()
