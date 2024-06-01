def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    # Get the total amount of questions being asked
    total_question = len(translations)
    # Start score counter at zero
    game_counter = 0

    # Loop over every key/value pair and ask a question
    for keys in translations:
        # The question is the key 
        question = keys
        # The correct answer is the value
        true_answer = translations[keys]
        # The question is stored with the users input in the answer variable
        answer = str(input("What is the Spanish translation for " + question + "? "))

        # If the user was correct add one to their score
        if answer == true_answer:
            print("That is correct!\n")
            game_counter += 1
        # If the user was incorrect give the correct answer
        else:
            print("That is incorrect, the Spanish translation for " + question + " is " + true_answer + ".\n")
    # Once all key/value pairs are looped through, give the user their game score compared with total of questioned asked
    print("You got " + str(game_counter) + "/" + str(total_question) + " words correct, come study again soon!")


        # These were for testing 
        
        # print(question)
        # print(true_answer)
        # print(answer)
        

if __name__ == '__main__':
    main()