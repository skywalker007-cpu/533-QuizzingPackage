# Quizzing Python Package Description

## List of Classes

### `Quizzing`

- **Description**: This class is the main class of the package. It is used to create a quiz object.

#### Included Variables

- `questions`: A list of `Question` objects that are part of the quiz.
- `responses`: A dict of `Response` objects that are part of the quiz.
- `API_KEY` (str): The API key used to access the OpenAI API for marking the responses.

#### Included Methods

- `__init__(self, questions: List[Question], responses: List[Response], API_KEY: str)`: The constructor method for the `Quizzing` class. It initializes the `questions`, `responses`, and `API_KEY` variables.
- `__str__(self)`: A method that returns a string that list the questions.
- `add_question(self, question: Question)`: A method that adds a `Question` object to the `questions` list. (unable to add a question if the quiz has already started)
- `remove_question(self, question: Question)`: A method that removes a `Question` object from the `questions` list. (unable to add a question if the quiz has already started)
- `take_quiz(self, student_id)`: A method that allows the user to take the quiz and submit responses. (unable to take the quiz if there's no questions)
- `mark_quiz(self, student_id, type)`: A method that marks the quiz using the OpenAI API and returns the results. (unable to mark the quiz if the quiz has not been taken)
  - `type`: auto or manual
- `get_results(self, student_id)`: A method that returns the results of the quiz for a specific student. (unable to get results if the quiz has not been taken)

### `Question`

- **Description**: This class represents a question in the quiz.

#### Included Variables

- `question`: The text of the question.
- `score`: The score of the question.
- `type`: The type of the question (multiple-choice, short-answer, true/false).

#### Included Methods

- `__init__(self, question: str, score: int)`: The constructor method for the `Question` class. It initializes the `question` and `score` variables.
- `__str__(self)`: A method that returns a string representation of the question.
- `check_answer_format(self, answer)`: A method that checks the format of the answer based on the type of the question.

#### SubClasses

- `MultipleChoiceQuestion`: A subclass of `Question` that represents a multiple-choice question.
- `ShortAnswerQuestion`: A subclass of `Question` that represents a short answer question.
- `TrueFalseQuestion`: A subclass of `Question` that represents a true/false question.

### `Response`

- **Description**: This class represents a response to a question in the quiz.

#### Included Variables

- `student_id`: The ID of the student who submitted the response.
- `answers`: A list of answers to the questions in the quiz.

#### Included Methods

- `__init__(self, student_id: str, answers: List[str])`: The constructor method for the `Response` class. It initializes the `student_id` and `answers` variables.
- `__str__(self)`: A method that returns a string representation of the response.
