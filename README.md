# Quiz Python Package Description 

**Group members: Zetian Zhao(skywalker007-cpu), Haoxiang Xu**

## [Table of Contents](#table-of-contents)

[![Build Status](https://app.travis-ci.com/skywalker007-cpu/533-QuizzingPackage.svg?token=WAveNzXdfMUy8gZvWNvY&branch=main)](https://app.travis-ci.com/skywalker007-cpu/533-QuizzingPackage)

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [List of Classes](#list-of-classes)
  - [Quiz](#quiz)
  - [Question](#question)
  - [Response](#response)

<a name="description"></a>

## Description

The Quiz Python package is a package that allows users to create quizzes and take them. The package includes three classes: `Quiz`, `Question`, and `Response`. The `Quiz` class is the main class of the package and is used to create a quiz object. The `Question` class represents a question in the quiz, and the `Response` class represents a response from a student to a question in the quiz. The package also includes three subclasses of the `Question` class: `MultipleChoiceQuestion`, `ShortAnswerQuestion`, and `TrueFalseQuestion`.

<a name="installation"></a>

## Installation

To install the Quizzing package, you can use the following command:

```bash
pip install git+
```

<a name="usage"></a>

## Usage

- Import the Quizzing package:

  ```python
  from quizzing import Quizzing
  ```

- Create a quiz object:

  ```python
  quiz = Quiz()
  # OR
  quiz = Quiz(questions, responses, API_KEY)
  ```

  - `questions` Optional (List[Question]): A dictionary of `Question` objects that represent the questions in the quiz.
  - `responses` Optional (List[Response]): A dictionary of `Response` objects that represent the responses to the quiz.
  - `API_KEY` Optional (str): The API key used to access the OpenAI API for marking the responses.

<a name="list-of-classes"></a>

## List of Classes

<a name="quiz"></a>

### `Quiz`

- **Description**: This class is the main class of the package. It is used to create a quiz object. The class has a list of `Question` objects and a dictionary of `Response` objects. The class also has a method to take the quiz and submit responses, and a method to mark the quiz using the OpenAI API.

#### Included Variables

- `questions`: A nested dictionary of `Question` objects that each key-value pair represent the question ID and the question object.
- `responses`: A dictionary of `Response` objects that each key-value pair represent the student ID and their response to the quiz.
- `API_KEY` (str): The API key used to access the OpenAI API for marking the responses.

#### Included Methods

- `__init__(self, questions: List[Question], responses: dict[str, Response], API_KEY: str)`: The constructor method for the `Quiz` class. It initializes the `questions`, `responses`, and `API_KEY` variables.
- `__str__(self)`: A method that returns a string that list the questions.
- `add_question(self, question: Question)`: A method that adds a `Question` object to the `questions` list.
  **(unable to add a question if the quiz has already started, and will show "quiz is already started, and you cannot add question anymore!" to the user for notification.)**
- `remove_question(self, question: Question)`: A method that removes a `Question` object from the `questions` list.
  **(unable to add a question if the quiz has already started, and will return corresponding string for notification.)**
- `add_response(self, response: Response)`: A method that adds a `Response` object after user reply to the question during the quiz to the `responses` list.
  **(unable to add a response if there is no quiz happening, and will return corresponding string for notification.)**
- `take_quiz(self, student_id)`: A method that allows the user to take the quiz and submit responses.
  **(unable to take the quiz if there's no questions, and will return corresponding string for notification.)**
- `mark_quiz(self, student_id, type)`: A method that marks the quiz using the OpenAI API and returns the results _(format - gained score/total score)_.
  **(unable to mark the quiz if the quiz has not been taken, and will return corresponding string for notification.)**
  - `type`: auto(AI) or manual(human)

<a name="question"></a>

### `Question`

- **Description**: This class represents a question in the quiz, and data format is following a dictionary format, which the values are question id, question text, correct answer, score, and type of the question with corresponding key.

#### Included Variables

- `question_id`: The ID of the question.
- `description`: The text of the question.
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

- **Description**: This class represents a response from a student to a question in the quiz. 

#### Included Variable

- `student_id`: The ID of the student who submitted the response.
- `response`: a JSON format object that contains the student's response to the question.

#### Included Methods

- `__init__(self, student_id: str, response: List[str])`: The constructor method for the `Response` class. It initializes the `student_id` and `response` variables.
- `__str__(self)`: A method that returns a string representation of the response.
