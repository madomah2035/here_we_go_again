def ask():
    answer_to_question = input(
        "What is the answer to the great question of Life, the Universe and Everything? ").strip().capitalize().lower()
    if check_ans(answer_to_question):
        print("Yes")
    else:
        print("No")


def check_ans(answer_to_question):
    match answer_to_question:
        case "42" | "Forty - two" | "forty - two" | "Forty-two" | "forty-two":
            return True
        case _:
            return False


ask()

