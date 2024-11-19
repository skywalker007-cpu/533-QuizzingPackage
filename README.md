# Quizzing Python Package Description

## List of Classes

### `Quizzing`

- **Description**: This class is the main class of the package. It is used to create a quiz object.

#### Included Variables

- `questions`: A list of `Question` objects that each element in the list represent one question from the quiz.
- `responses`: A list of `Response` objects that each object represent the student's reponse to the quiz.
- `API_KEY` (str): The API key used to access the OpenAI API for marking the responses.

#### Included Methods

- `__init__(self, questions: List[Question], responses: List[Response], API_KEY: str)`: The constructor method for the `Quizzing` class. It initializes the `questions`, `responses`, and `API_KEY` variables.
- `__str__(self)`: A method that returns a string that list the questions.
- `add_question(self, question: Question)`: A method that adds a `Question` object to the `questions` list. 
**(unable to add a question if the quiz has already started, and will show "quiz is already started, and you cannot add question anymore!" to the user for notification.)**
- `remove_question(self, question: Question)`: A method that removes a `Question` object from the `questions` list. 
**(unable to add a question if the quiz has already started, and will return corresponding string for notification.)**
- `add_response(self, response: Response)`: A method that adds a `Response` object after user reply to the question during the quiz to the `responses` list.
**(unable to add a response if there is no quiz happening, and will return corresponding string for notification.)**
- `take_quiz(self, student_id)`: A method that allows the user to take the quiz and submit responses. 
**(unable to take the quiz if there's no questions, and will return corresponding string for notification.)**
- `mark_quiz(self, student_id, type)`: A method that marks the quiz using the OpenAI API and returns the results *(format - gained score/total score)*. 
**(unable to mark the quiz if the quiz has not been taken, and will return corresponding string for notification.)**
  - `type`: auto(AI) or manual(human)

### `Question`

- **Description**: This class represents a question in the quiz, and data format is following a dictionary format, which is that the question's id is the key, and some subkeys that are having corresponding values such as question text and corresponding correct answer, score, and type of the question.

#### Included Variables

- `question_id`: The ID of the question.
- `question`: The text of the question.
- `answer`: The correct answer to the question.
- `score`: The score of the question.

#### Included Methods

- `__init__(self, question: str, score: int)`: The constructor method for the `Question` class. It initializes the `question` and `score` variables.
- `__str__(self)`: A method that returns a string representation of the question.

#### SubClasses (extend from `Question`)

- `MultipleChoiceQuestion`: A subclass of `Question` that represents a multiple-choice question, and has an additional `options` variable.
  - extra attribute: `options` in the `__init__` function: A list of options for the multiple-choice question.
- `ShortAnswerQuestion`: A subclass of `Question` that represents a short answer question.
  - extra attribute: `notice` in the `__init__` function: A notice for user when they do the short answer question. For example, "Please write your answer in one sentence."
- `TrueFalseQuestion`: A subclass of `Question` that represents a true/false question.
  - extra attribute: `options` in the `__init__` function: A list of options that only contain true/false.

### `Response` 

- **Description**: This class represents a response from a student to a question in the quiz. Moreover, the class format is the dictionary format, which is that the student_id is the key, and their answers as response are the values.

#### Included Variables

- `student_id`: The ID of the student who submitted the response.
- `response`: A list of answers to the questions in the quiz.

#### Included Methods

- `__init__(self, student_id: str, response: List[str])`: The constructor method for the `Response` class. It initializes the `student_id` and `response` variables.
- `__str__(self)`: A method that returns a string representation of the response.
