def prompt_str(text=str, case_insensitive=False):
    print(text)
    user_input = input("(Enter any string.) ")
    if case_insensitive:
        return user_input.lower()
    return user_input