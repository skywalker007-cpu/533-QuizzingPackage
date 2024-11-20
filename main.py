from quiz import Quiz
import question


def main():
    Q1 = question.MultipleChoice(1, "What is the capital of France?", "Paris", 1,
                                 ["Paris", "London", "Berlin", "Madrid"])
    Q2 = question.ShortAnswerQuestion(2, "What is the capital of France?", "Paris", 1, "Please answer in one word")
    Q3 = question.TrueFalseQuestion(3, "Is Paris the capital of France?", "True", 1, ["True", "False"])
    Q4 = question.MultipleChoice(4, "What is the capital of France?", "Paris", 1,
                                 ["Paris", "London", "Berlin", "Madrid"])
    Q5 = question.ShortAnswerQuestion(5, "What is the capital of France?", "Paris", 1, "Please answer in one word")
    Q6 = question.TrueFalseQuestion(6, "Is Paris the capital of France?", "True", 1, ["True", "False"])
    Q7 = question.MultipleChoice(7, "What is the capital of France?", "Paris", 1,
                                 ["Paris", "London", "Berlin", "Madrid"])
    Q8 = question.ShortAnswerQuestion(8, "What is the capital of France?", "Paris", 1, "Please answer in one word")
    Q9 = question.TrueFalseQuestion(9, "Is Paris the capital of France?", "True", 1, ["True", "False"])

    quiz_1 = Quiz()

    quiz_1.add(Q1)
    quiz_1.add(Q2)
    quiz_1.add(Q3)
    quiz_1.add([Q4, Q5, Q6, Q7])
    quiz_1.add({8: Q8, 9: Q9})

    quiz_2 = Quiz([Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9])
    quiz_2.remove(3)
    quiz_2.remove([1, 9, 8, 7, 5, 2, 4])

    print(quiz_1)
    print(quiz_2)
    quiz_1.take_quiz("123456789")
    print(quiz_1)


if __name__ == "__main__":
    main()
