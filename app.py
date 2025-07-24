from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)

quiz_data = {
    "grammar": [
        {
            "question": "I ___ to school every day.",
            "options": ["go", "goes", "going", "went"],
            "answer": 0,
            "explanation": "I, you, we, theyの場合は動詞の原形を使います。"
        },
        {
            "question": "She ___ a student.",
            "options": ["am", "is", "are", "be"],
            "answer": 1,
            "explanation": "三人称単数（he, she, it）の場合はisを使います。"
        },
        {
            "question": "They ___ playing soccer now.",
            "options": ["is", "am", "are", "was"],
            "answer": 2,
            "explanation": "複数形の主語にはareを使います。"
        },
        {
            "question": "I ___ my homework yesterday.",
            "options": ["do", "did", "does", "doing"],
            "answer": 1,
            "explanation": "yesterdayは過去を表すので、過去形didを使います。"
        },
        {
            "question": "He ___ speak English very well.",
            "options": ["can", "cans", "could to", "can to"],
            "answer": 0,
            "explanation": "助動詞canの後は動詞の原形が続きます。"
        }
    ],
    "vocabulary": [
        {
            "question": "「図書館」を英語で何と言いますか？",
            "options": ["library", "book store", "school", "museum"],
            "answer": 0,
            "explanation": "図書館は英語でlibraryです。"
        },
        {
            "question": "「beautiful」の意味は？",
            "options": ["醜い", "美しい", "大きい", "小さい"],
            "answer": 1,
            "explanation": "beautifulは「美しい」という意味です。"
        },
        {
            "question": "「朝食」を英語で何と言いますか？",
            "options": ["lunch", "dinner", "breakfast", "supper"],
            "answer": 2,
            "explanation": "朝食は英語でbreakfastです。"
        },
        {
            "question": "「happy」の反対語は？",
            "options": ["sad", "angry", "excited", "tired"],
            "answer": 0,
            "explanation": "happyの反対語はsad（悲しい）です。"
        },
        {
            "question": "「月曜日」を英語で何と言いますか？",
            "options": ["Sunday", "Monday", "Tuesday", "Friday"],
            "answer": 1,
            "explanation": "月曜日は英語でMondayです。"
        }
    ],
    "numbers": [
        {
            "question": "「15」を英語で何と言いますか？",
            "options": ["thirteen", "fourteen", "fifteen", "sixteen"],
            "answer": 2,
            "explanation": "15は英語でfifteenです。"
        },
        {
            "question": "「100」を英語で何と言いますか？",
            "options": ["one hundred", "one thousand", "ten", "one hundread"],
            "answer": 0,
            "explanation": "100は英語でone hundredです。"
        },
        {
            "question": "「3番目」を英語で何と言いますか？",
            "options": ["three", "third", "thirth", "tree"],
            "answer": 1,
            "explanation": "3番目は英語でthirdです。"
        },
        {
            "question": "「50」を英語で何と言いますか？",
            "options": ["fifteen", "fifty", "five", "fivety"],
            "answer": 1,
            "explanation": "50は英語でfiftyです。"
        },
        {
            "question": "「1,000」を英語で何と言いますか？",
            "options": ["one hundred", "ten thousand", "one thousand", "one million"],
            "answer": 2,
            "explanation": "1,000は英語でone thousandです。"
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/quiz/<category>')
def get_quiz(category):
    if category in quiz_data:
        questions = random.sample(quiz_data[category], min(5, len(quiz_data[category])))
        return jsonify(questions)
    return jsonify([])

@app.route('/api/categories')
def get_categories():
    return jsonify(list(quiz_data.keys()))

if __name__ == '__main__':
    app.run(debug=True)