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

    total_question = len(translations)

    game_counter = 0

    for keys in translations:

        question = keys
        true_answer = translations[keys]
        answer = str(input("What is the Spanish translation for " + question + "? "))

        if answer == true_answer:
            print("That is correct!\n")
            game_counter += 1
        else:
            print("That is incorrect, the Spanish translation for " + question + " is " + true_answer + ".\n")

    print("You got " + str(game_counter) + "/" + str(total_question) + " words correct, come study again soon!")

        # print(question)
        # print(true_answer)
        # print(answer)
        

if __name__ == '__main__':
    main()