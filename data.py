import requests
import html

AMOUNT = 10

parameters = {
    "amount": AMOUNT,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
raw_data = response.json()["results"]

data = []
for item in raw_data:
    question = {
        "text": html.unescape(item["question"]),
        "correct_answer": item["correct_answer"]
    }
    data.append(question)
