## Functions detail
- #### Question Module
    - ##### question class (parant class of other three classes and child class of `UserDict` class)
        - __init__ function with parameter such as `quesiton id, question text, question answer and question score`(constructor)
        - __str__ function for printint out question in certain format(print function)
        - __eq__ function for comparing if there are two identical question objects(compare function)
    - ##### multiple_choice class (child class of quesetion class) 
        - __init__ function with extra parameter which is `options` in this case.
        - __str__ function for printing the question with possible options in the following.
    - ##### short_answer_question class (child class of question class)
        - __init__ function with extra parameter which is `notion` in this case.
        - __str__ function for printing the question with specific note about answering the question for users during the quiz.
    - ##### true_false_question class (child class of question class)
        - __init__ function with extra parameter which is `options` in this case.
        - __str__ function for printing the question with only two options which are `True` and `False`.

---

- #### Response Module
    - ##### response class (simple class that store student's response)
        - __init__ function with parameter such as `student id and response list`(constructor)
        - __str__ function for printing out the response in certain format(print function)
        - __repr__ function for better *comprehenstion* for development purpose.
---

- #### Quiz Module
    - ##### quiz class
        - __init__ function with parameter such as `quiz title, quiz total score and questions dictionary and responses dictionary`(constructor)
        - __str__ function for printing out the quiz in certain format(print function)
        - __eq__ function for comparing if there are two `identical quiz objects`(compare function)
        - __clone__ function that simply `clone` a quiz object from an existed one.
        - __add-questions__ function that add `a question object or a list of the objects` to the specific quiz.
        - __remove-questions__ function that remove a question or list of it from the specific quiz with question id/ids. In other words, we will handle with both `one single id or a id list`.
        - __add-responses__ function that add `a response or list of it` to the specific quiz for taking the quiz or just add it directly as option. In other words, the `take_quiz` function will be used in this function to enable the quiz happen.
        - __take-quiz__ function that take student id as paramter and begin to ask the question store in the quiz and also store the `user input` to a new `response object`. Finally the response object will be store in the `responses dictionary`.
        - __mark-quiz__ function that store student's mark about the quiz into a marks dictionary.
        - __get-responses__ function that return student's response about the quiz with the calculated score they get.

---

- #### Marker Module
    - ##### marker class
        - __init__ function which is just for `placeholder` initialization.
        - __mark__ function that return student's mark about the quiz by comparing therir `response` during the quiz session with the **pre-set answer** in the `quiz` object.
        - _validate-inputs_ function is used to check the `validity of user's response in format` before marking the quiz.