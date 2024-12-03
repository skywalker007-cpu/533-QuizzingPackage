from Quizzes.quiz import Quiz
import Objects.question as question


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

    quiz_2 = Quiz("quiz_2", [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9])
    # removing question test
    quiz_2.remove_questions(3)
    quiz_2.remove_questions([1, 9, 8, 7, 5, 2, 4])
    # adding question test
    quiz_2.add_questions(Q7)
    
    quiz_3 = quiz_2.clone()
    
    # take quiz test
    quiz_2.add_responses()
    quiz_3.add_responses()

    # get mark test
    quiz_2.mark_quiz()
    quiz_3.mark_quiz()

    # get the responses test
    quiz_2.get_responses()
    quiz_3.get_responses()

    # print the output for testing
    print(quiz_2)
    print(quiz_3)

if __name__ == "__main__":
    main()
