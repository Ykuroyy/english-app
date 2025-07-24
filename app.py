from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)

quiz_data = {
    "grammar": {
        "1": [
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
        "2": [
            {
                "question": "I ___ playing tennis for three hours.",
                "options": ["am", "have been", "was", "will be"],
                "answer": 1,
                "explanation": "「〜時間ずっと」は現在完了進行形を使います。"
            },
            {
                "question": "She is ___ than her sister.",
                "options": ["tall", "taller", "tallest", "more tall"],
                "answer": 1,
                "explanation": "2つを比べる時は比較級を使います。"
            },
            {
                "question": "This is the ___ book I have ever read.",
                "options": ["interesting", "more interesting", "most interesting", "interestinger"],
                "answer": 2,
                "explanation": "「今まで〜した中で一番」は最上級を使います。"
            },
            {
                "question": "I want ___ a doctor when I grow up.",
                "options": ["become", "to become", "becoming", "became"],
                "answer": 1,
                "explanation": "want + to不定詞の形を使います。"
            },
            {
                "question": "If it ___ tomorrow, we will go to the park.",
                "options": ["doesn't rain", "won't rain", "didn't rain", "isn't rain"],
                "answer": 0,
                "explanation": "if文の条件節では現在形を使います。"
            }
        ],
        "3": [
            {
                "question": "I have ___ finished my homework.",
                "options": ["yet", "already", "still", "ever"],
                "answer": 1,
                "explanation": "「もう〜した」はalreadyを使います。"
            },
            {
                "question": "This book ___ by my teacher last year.",
                "options": ["wrote", "was written", "is written", "has written"],
                "answer": 1,
                "explanation": "受動態の過去形は「was/were + 過去分詞」です。"
            },
            {
                "question": "I'm looking forward to ___ you again.",
                "options": ["see", "seeing", "saw", "seen"],
                "answer": 1,
                "explanation": "look forward toの後は動名詞（-ing形）が続きます。"
            },
            {
                "question": "She asked me ___ I liked the movie.",
                "options": ["that", "if", "what", "why"],
                "answer": 1,
                "explanation": "「〜かどうか」を尋ねる間接疑問文ではifを使います。"
            },
            {
                "question": "I wish I ___ speak English better.",
                "options": ["can", "could", "will", "would"],
                "answer": 1,
                "explanation": "I wish + 仮定法過去でcouldを使います。"
            }
        ],
        "4": [
            {
                "question": "I have never seen such a beautiful sunset ___ in my life.",
                "options": ["like", "as", "than", "so"],
                "answer": 1,
                "explanation": "such... asで「そのような〜」を表します。"
            },
            {
                "question": "The more you study, ___ your English will become.",
                "options": ["good", "better", "the better", "best"],
                "answer": 2,
                "explanation": "「the + 比較級, the + 比較級」で「〜すればするほど」を表します。"
            },
            {
                "question": "I would rather ___ at home than go out in this rain.",
                "options": ["stay", "to stay", "staying", "stayed"],
                "answer": 0,
                "explanation": "would rather + 動詞の原形を使います。"
            },
            {
                "question": "If I ___ you, I would accept the offer.",
                "options": ["am", "was", "were", "will be"],
                "answer": 2,
                "explanation": "仮定法過去では主語がIでもwereを使います。"
            },
            {
                "question": "It is important that everyone ___ the rules.",
                "options": ["follows", "follow", "followed", "following"],
                "answer": 1,
                "explanation": "重要性を表すthat節では動詞の原形を使います。"
            }
        ],
        "5": [
            {
                "question": "If I ___ studied harder, I would have passed the exam.",
                "options": ["have", "had", "has", "would have"],
                "answer": 1,
                "explanation": "仮定法過去完了の条件節では過去完了形を使います。"
            },
            {
                "question": "Not only ___ English, but he also speaks French.",
                "options": ["he speaks", "does he speak", "he spoke", "did he speak"],
                "answer": 1,
                "explanation": "not onlyが文頭にくると倒置が起こります。"
            },
            {
                "question": "I wish I ___ to the party last night.",
                "options": ["went", "had gone", "have gone", "go"],
                "answer": 1,
                "explanation": "過去の後悔を表すI wishの後は過去完了形を使います。"
            },
            {
                "question": "He speaks English as if he ___ a native speaker.",
                "options": ["is", "was", "were", "has been"],
                "answer": 2,
                "explanation": "as ifの後の仮定法過去ではwereを使います。"
            },
            {
                "question": "Without your help, I ___ completed the project.",
                "options": ["couldn't have", "can't have", "wouldn't", "won't have"],
                "answer": 0,
                "explanation": "過去の仮定を表すcouldn't haveを使います。"
            }
        ]
    },
    "vocabulary": {
        "1": [
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
        "2": [
            {
                "question": "「important」の意味は？",
                "options": ["簡単な", "重要な", "楽しい", "難しい"],
                "answer": 1,
                "explanation": "importantは「重要な」という意味です。"
            },
            {
                "question": "「different」の意味は？",
                "options": ["同じ", "違う", "近い", "遠い"],
                "answer": 1,
                "explanation": "differentは「違う」という意味です。"
            },
            {
                "question": "「favorite」の意味は？",
                "options": ["嫌いな", "お気に入りの", "普通の", "特別な"],
                "answer": 1,
                "explanation": "favoriteは「お気に入りの」という意味です。"
            },
            {
                "question": "「expensive」の意味は？",
                "options": ["安い", "高い", "古い", "新しい"],
                "answer": 1,
                "explanation": "expensiveは「高い」という意味です。"
            },
            {
                "question": "「possible」の意味は？",
                "options": ["不可能な", "可能な", "確実な", "危険な"],
                "answer": 1,
                "explanation": "possibleは「可能な」という意味です。"
            }
        ],
        "3": [
            {
                "question": "「comfortable」の意味は？",
                "options": ["不快な", "快適な", "忙しい", "静かな"],
                "answer": 1,
                "explanation": "comfortableは「快適な」という意味です。"
            },
            {
                "question": "「popular」の意味は？",
                "options": ["人気のない", "人気のある", "古い", "新しい"],
                "answer": 1,
                "explanation": "popularは「人気のある」という意味です。"
            },
            {
                "question": "「necessary」の意味は？",
                "options": ["不要な", "必要な", "簡単な", "困難な"],
                "answer": 1,
                "explanation": "necessaryは「必要な」という意味です。"
            },
            {
                "question": "「similar」の意味は？",
                "options": ["違う", "似ている", "遠い", "近い"],
                "answer": 1,
                "explanation": "similarは「似ている」という意味です。"
            },
            {
                "question": "「discover」の意味は？",
                "options": ["隠す", "発見する", "忘れる", "覚える"],
                "answer": 1,
                "explanation": "discoverは「発見する」という意味です。"
            }
        ],
        "4": [
            {
                "question": "「abundant」の意味は？",
                "options": ["不足した", "豊富な", "普通の", "少ない"],
                "answer": 1,
                "explanation": "abundantは「豊富な」という意味です。"
            },
            {
                "question": "「significant」の意味は？",
                "options": ["重要でない", "重要な", "小さな", "簡単な"],
                "answer": 1,
                "explanation": "significantは「重要な、意味のある」という意味です。"
            },
            {
                "question": "「contemporary」の意味は？",
                "options": ["古い", "現代の", "未来の", "過去の"],
                "answer": 1,
                "explanation": "contemporaryは「現代の、同時代の」という意味です。"
            },
            {
                "question": "「inevitable」の意味は？",
                "options": ["避けられる", "避けられない", "可能な", "不可能な"],
                "answer": 1,
                "explanation": "inevitableは「避けられない」という意味です。"
            },
            {
                "question": "「comprehensive」の意味は？",
                "options": ["部分的な", "包括的な", "狭い", "限定的な"],
                "answer": 1,
                "explanation": "comprehensiveは「包括的な、総合的な」という意味です。"
            }
        ],
        "5": [
            {
                "question": "「sophisticated」の意味は？",
                "options": ["単純な", "洗練された", "古い", "新しい"],
                "answer": 1,
                "explanation": "sophisticatedは「洗練された、高度な」という意味です。"
            },
            {
                "question": "「arbitrary」の意味は？",
                "options": ["規則的な", "恣意的な", "論理的な", "合理的な"],
                "answer": 1,
                "explanation": "arbitraryは「恣意的な、独断的な」という意味です。"
            },
            {
                "question": "「redundant」の意味は？",
                "options": ["必要な", "余分な", "不足した", "適切な"],
                "answer": 1,
                "explanation": "redundantは「余分な、冗長な」という意味です。"
            },
            {
                "question": "「ambiguous」の意味は？",
                "options": ["明確な", "曖昧な", "正確な", "具体的な"],
                "answer": 1,
                "explanation": "ambiguousは「曖昧な、多義的な」という意味です。"
            },
            {
                "question": "「presumptuous」の意味は？",
                "options": ["謙虚な", "厚かましい", "丁寧な", "親切な"],
                "answer": 1,
                "explanation": "presumptuousは「厚かましい、生意気な」という意味です。"
            }
        ]
    },
    "numbers": {
        "1": [
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
        ],
        "2": [
            {
                "question": "「20」を英語で何と言いますか？",
                "options": ["twelve", "twenty", "thirty", "forty"],
                "answer": 1,
                "explanation": "20は英語でtwentyです。"
            },
            {
                "question": "「2番目」を英語で何と言いますか？",
                "options": ["two", "second", "twice", "double"],
                "answer": 1,
                "explanation": "2番目は英語でsecondです。"
            },
            {
                "question": "「half」の意味は？",
                "options": ["全部", "半分", "4分の1", "3分の1"],
                "answer": 1,
                "explanation": "halfは「半分」という意味です。"
            },
            {
                "question": "「12」を英語で何と言いますか？",
                "options": ["ten", "eleven", "twelve", "thirteen"],
                "answer": 2,
                "explanation": "12は英語でtwelveです。"
            },
            {
                "question": "「90」を英語で何と言いますか？",
                "options": ["nineteen", "ninety", "nine hundred", "nine thousand"],
                "answer": 1,
                "explanation": "90は英語でninetyです。"
            }
        ],
        "3": [
            {
                "question": "「0.5」を英語で何と言いますか？",
                "options": ["zero point five", "half", "one half", "all correct"],
                "answer": 3,
                "explanation": "0.5は「zero point five」「half」「one half」すべて正しいです。"
            },
            {
                "question": "「3/4」を英語で何と言いますか？",
                "options": ["three four", "three fourths", "three of four", "third fourth"],
                "answer": 1,
                "explanation": "3/4は「three fourths」または「three quarters」です。"
            },
            {
                "question": "「21st」を英語で何と言いますか？",
                "options": ["twenty-one", "twenty-first", "twenty-onest", "twenty-ones"],
                "answer": 1,
                "explanation": "21番目は「twenty-first」です。"
            },
            {
                "question": "「double」の意味は？",
                "options": ["半分", "2倍", "3倍", "4倍"],
                "answer": 1,
                "explanation": "doubleは「2倍」という意味です。"
            },
            {
                "question": "「dozen」の意味は？",
                "options": ["10個", "12個", "20個", "100個"],
                "answer": 1,
                "explanation": "dozenは「12個、1ダース」という意味です。"
            }
        ],
        "4": [
            {
                "question": "「percentage」の意味は？",
                "options": ["分数", "百分率", "少数", "整数"],
                "answer": 1,
                "explanation": "percentageは「百分率、パーセント」という意味です。"
            },
            {
                "question": "「fraction」の意味は？",
                "options": ["分数", "小数", "整数", "負数"],
                "answer": 0,
                "explanation": "fractionは「分数」という意味です。"
            },
            {
                "question": "「multiply」の意味は？",
                "options": ["足す", "引く", "掛ける", "割る"],
                "answer": 2,
                "explanation": "multiplyは「掛ける」という意味です。"
            },
            {
                "question": "「diameter」の意味は？",
                "options": ["半径", "直径", "円周", "面積"],
                "answer": 1,
                "explanation": "diameterは「直径」という意味です。"
            },
            {
                "question": "「equation」の意味は？",
                "options": ["関数", "方程式", "図形", "角度"],
                "answer": 1,
                "explanation": "equationは「方程式」という意味です。"
            }
        ],
        "5": [
            {
                "question": "「logarithm」の意味は？",
                "options": ["指数", "対数", "分数", "小数"],
                "answer": 1,
                "explanation": "logarithmは「対数」という意味です。"
            },
            {
                "question": "「coefficient」の意味は？",
                "options": ["変数", "係数", "定数", "関数"],
                "answer": 1,
                "explanation": "coefficientは「係数」という意味です。"
            },
            {
                "question": "「polynomial」の意味は？",
                "options": ["一次式", "多項式", "指数式", "三角関数"],
                "answer": 1,
                "explanation": "polynomialは「多項式」という意味です。"
            },
            {
                "question": "「derivative」の意味は？",
                "options": ["積分", "微分", "極限", "級数"],
                "answer": 1,
                "explanation": "derivativeは「微分」という意味です。"
            },
            {
                "question": "「integral」の意味は？",
                "options": ["微分", "積分", "極限", "関数"],
                "answer": 1,
                "explanation": "integralは「積分」という意味です。"
            }
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/quiz/<category>/<level>')
def get_quiz(category, level):
    if category in quiz_data and level in quiz_data[category]:
        questions = random.sample(quiz_data[category][level], min(5, len(quiz_data[category][level])))
        return jsonify(questions)
    return jsonify([])

@app.route('/api/categories')
def get_categories():
    return jsonify(list(quiz_data.keys()))

@app.route('/api/levels/<category>')
def get_levels(category):
    if category in quiz_data:
        return jsonify(list(quiz_data[category].keys()))
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)