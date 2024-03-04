# Quizzler

---

A trivia game in which you get asked 10 right-or-wrong questions with no specific category, the number 
of questions and their category are adjustable, and we get this data from Open Trivia API.

![quizzler_screenshot](https://github.com/Abdelrahman-Elsaudy/Quizzler/assets/158151388/a13ee632-27fb-4d09-a324-7eb6e3266345)

---

## Applied Skills:

---
**1 Object Oriented Programming**

Creating several coding pages that interact together to form the game:
- Data: The one responsible for extracting the required data and filtering them. 
- Quiz Brain: A class in which the score is calculated, the programs iterates over the questions and checks whether the 
provided answer by the user is correct or not.
- UI: The one interacts with Quiz Brain and provides the user-interface experience through Tkinter module.
- Main: to call UI.

**2. API Requests**

- Making _API_ calls to [Open Trivia API](https://opentdb.com/api.php) with the required parameters 
to get the questions and their answers as Json data type.
- Manipulating the data to display the questions consequently and compare the correct answer to the provided answer by the user.

**3. GUI with Tkinter Module**

- Creating a nice user-interface experience where the questions are displayed and the user gets interactive buttons to answer.
- The screen changes its color for an instance indicating whether their answer was correct or not.
- Their score is calculated and displayed.

---

## About The Project:

---

- The number of questions, their type and category are determined by the API parameters we choose, here I chose 10 boolean questions with no specific category:
```
AMOUNT = 10

parameters = {
    "amount": AMOUNT,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
```

- This code is written as OOP so `data` is imported in `quiz_brain` and `quiz_brian` is imported in `ui` and `ui` is imported 
on `main`, so on `main` there is only two lines of code:
```
from ui import Interface

interface = Interface()
```

---
