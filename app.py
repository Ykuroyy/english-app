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
                "question": "I have ___ studying English for two years.",
                "options": ["been", "be", "being", "was"],
                "answer": 0,
                "explanation": "現在完了進行形では「have been + -ing」を使います。"
            },
            {
                "question": "If it ___ tomorrow, we will stay home.",
                "options": ["rain", "rains", "will rain", "rained"],
                "answer": 1,
                "explanation": "if文の条件節では現在形を使います。"
            },
            {
                "question": "The book ___ by many people.",
                "options": ["reads", "is read", "read", "reading"],
                "answer": 1,
                "explanation": "受動態では「be動詞 + 過去分詞」を使います。"
            },
            {
                "question": "I wish I ___ taller.",
                "options": ["am", "was", "were", "be"],
                "answer": 2,
                "explanation": "仮定法では主語がIでもwereを使います。"
            },
            {
                "question": "She made me ___ my room.",
                "options": ["clean", "to clean", "cleaning", "cleaned"],
                "answer": 0,
                "explanation": "make + 人 + 動詞の原形の形を使います。"
            }
        ],
        "3": [
            {
                "question": "I would rather ___ at home than go out.",
                "options": ["stay", "to stay", "staying", "stayed"],
                "answer": 0,
                "explanation": "would rather + 動詞の原形を使います。"
            },
            {
                "question": "The more you practice, ___ you become.",
                "options": ["good", "better", "the better", "best"],
                "answer": 2,
                "explanation": "「the + 比較級, the + 比較級」の構文です。"
            },
            {
                "question": "I'm looking forward to ___ you again.",
                "options": ["see", "seeing", "saw", "seen"],
                "answer": 1,
                "explanation": "look forward toの後は動名詞（-ing形）が続きます。"
            },
            {
                "question": "Had I known about it, I ___ you.",
                "options": ["would help", "will help", "would have helped", "helped"],
                "answer": 2,
                "explanation": "仮定法過去完了では「would have + 過去分詞」を使います。"
            },
            {
                "question": "It is important that he ___ on time.",
                "options": ["comes", "come", "came", "coming"],
                "answer": 1,
                "explanation": "重要性を表すthat節では動詞の原形を使います。"
            }
        ],
        "4": [
            {
                "question": "Scarcely had I arrived ___ it started raining.",
                "options": ["when", "than", "as", "while"],
                "answer": 0,
                "explanation": "scarcely... whenは「...するやいなや」という意味です。"
            },
            {
                "question": "Not only did he pass the exam, ___ he got the highest score.",
                "options": ["and", "but also", "so", "or"],
                "answer": 1,
                "explanation": "not only... but alsoの構文です。"
            },
            {
                "question": "Little ___ he know what was waiting for him.",
                "options": ["did", "does", "was", "had"],
                "answer": 0,
                "explanation": "否定の副詞littleが文頭にくると倒置が起こります。"
            },
            {
                "question": "I suggest that the meeting ___ postponed.",
                "options": ["is", "be", "was", "were"],
                "answer": 1,
                "explanation": "提案のthat節では動詞の原形（仮定法現在）を使います。"
            },
            {
                "question": "She acted as if she ___ nothing about it.",
                "options": ["knows", "knew", "know", "known"],
                "answer": 1,
                "explanation": "as ifの後は仮定法過去を使います。"
            }
        ],
        "5": [
            {
                "question": "So absorbed ___ in his work that he didn't notice me.",
                "options": ["he was", "was he", "he is", "is he"],
                "answer": 1,
                "explanation": "soが文頭にくると倒置が起こります。"
            },
            {
                "question": "I would sooner die ___ betray my friends.",
                "options": ["than", "rather than", "instead of", "before"],
                "answer": 0,
                "explanation": "would sooner... thanは「...するより...したい」という意味です。"
            },
            {
                "question": "Were it not for your help, I ___ succeeded.",
                "options": ["would not have", "will not have", "had not", "did not"],
                "answer": 0,
                "explanation": "倒置した仮定法過去完了の構文です。"
            },
            {
                "question": "Never before ___ such a beautiful sunset.",
                "options": ["I have seen", "have I seen", "I saw", "did I see"],
                "answer": 1,
                "explanation": "否定語が文頭にくると倒置が起こります。"
            },
            {
                "question": "It is high time we ___ serious about this problem.",
                "options": ["get", "got", "are getting", "will get"],
                "answer": 1,
                "explanation": "It is high time + 仮定法過去の構文です。"
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
                "question": "「achieve」の意味は？",
                "options": ["失敗する", "達成する", "始める", "終わる"],
                "answer": 1,
                "explanation": "achieveは「達成する」という意味です。"
            },
            {
                "question": "「environment」の意味は？",
                "options": ["環境", "娯楽", "教育", "経済"],
                "answer": 0,
                "explanation": "environmentは「環境」という意味です。"
            },
            {
                "question": "「frequently」の意味は？",
                "options": ["めったに", "時々", "頻繁に", "決して"],
                "answer": 2,
                "explanation": "frequentlyは「頻繁に」という意味です。"
            },
            {
                "question": "「ignore」の意味は？",
                "options": ["注意する", "無視する", "理解する", "説明する"],
                "answer": 1,
                "explanation": "ignoreは「無視する」という意味です。"
            },
            {
                "question": "「convenient」の意味は？",
                "options": ["不便な", "便利な", "危険な", "安全な"],
                "answer": 1,
                "explanation": "convenientは「便利な」という意味です。"
            }
        ],
        "3": [
            {
                "question": "「phenomena」の単数形は？",
                "options": ["phenomena", "phenomenon", "phenomen", "phenomenas"],
                "answer": 1,
                "explanation": "phenomenaの単数形はphenomenonです。"
            },
            {
                "question": "「elaborate」の意味は？",
                "options": ["簡単な", "詳細な", "短い", "普通の"],
                "answer": 1,
                "explanation": "elaborateは「詳細な、精巧な」という意味です。"
            },
            {
                "question": "「reluctant」の意味は？",
                "options": ["熱心な", "気が進まない", "興奮した", "満足した"],
                "answer": 1,
                "explanation": "reluctantは「気が進まない、嫌がる」という意味です。"
            },
            {
                "question": "「deteriorate」の意味は？",
                "options": ["改善する", "悪化する", "維持する", "開始する"],
                "answer": 1,
                "explanation": "deteriorateは「悪化する、劣化する」という意味です。"
            },
            {
                "question": "「authentic」の意味は？",
                "options": ["偽の", "本物の", "新しい", "古い"],
                "answer": 1,
                "explanation": "authenticは「本物の、真正な」という意味です。"
            }
        ],
        "4": [
            {
                "question": "「ubiquitous」の意味は？",
                "options": ["珍しい", "どこにでもある", "高価な", "複雑な"],
                "answer": 1,
                "explanation": "ubiquitousは「どこにでもある、遍在する」という意味です。"
            },
            {
                "question": "「meticulous」の意味は？",
                "options": ["大雑把な", "細心な", "速い", "遅い"],
                "answer": 1,
                "explanation": "meticulousは「細心な、綿密な」という意味です。"
            },
            {
                "question": "「ephemeral」の意味は？",
                "options": ["永続的な", "短命な", "大きな", "小さな"],
                "answer": 1,
                "explanation": "ephemeralは「短命な、はかない」という意味です。"
            },
            {
                "question": "「pragmatic」の意味は？",
                "options": ["理想的な", "実用的な", "理論的な", "感情的な"],
                "answer": 1,
                "explanation": "pragmaticは「実用的な、実際的な」という意味です。"
            },
            {
                "question": "「indigenous」の意味は？",
                "options": ["外来の", "土着の", "現代の", "伝統的な"],
                "answer": 1,
                "explanation": "indigenousは「土着の、固有の」という意味です。"
            }
        ],
        "5": [
            {
                "question": "「perspicacious」の意味は？",
                "options": ["鈍い", "洞察力のある", "優しい", "厳しい"],
                "answer": 1,
                "explanation": "perspicaciousは「洞察力のある、鋭い」という意味です。"
            },
            {
                "question": "「magnanimous」の意味は？",
                "options": ["けちな", "寛大な", "怒りっぽい", "悲しい"],
                "answer": 1,
                "explanation": "magnanimousは「寛大な、度量の大きい」という意味です。"
            },
            {
                "question": "「surreptitious」の意味は？",
                "options": ["公然の", "秘密の", "明るい", "暗い"],
                "answer": 1,
                "explanation": "surreptitiousは「秘密の、こっそりした」という意味です。"
            },
            {
                "question": "「vituperative」の意味は？",
                "options": ["賞賛の", "非難の", "中立の", "疑問の"],
                "answer": 1,
                "explanation": "vituperativeは「非難の、痛烈な批判の」という意味です。"
            },
            {
                "question": "「obsequious」の意味は？",
                "options": ["反抗的な", "へつらう", "独立した", "協力的な"],
                "answer": 1,
                "explanation": "obsequiousは「へつらう、卑屈な」という意味です。"
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
                "question": "「1,000,000」を英語で何と言いますか？",
                "options": ["one thousand", "ten thousand", "one hundred thousand", "one million"],
                "answer": 3,
                "explanation": "1,000,000は「one million」です。"
            },
            {
                "question": "「double」の意味は？",
                "options": ["半分", "2倍", "3倍", "4倍"],
                "answer": 1,
                "explanation": "doubleは「2倍」という意味です。"
            }
        ],
        "3": [
            {
                "question": "「dozen」の意味は？",
                "options": ["10個", "12個", "20個", "100個"],
                "answer": 1,
                "explanation": "dozenは「12個、1ダース」という意味です。"
            },
            {
                "question": "「5.25」を英語で何と言いますか？",
                "options": ["five point twenty-five", "five and quarter", "five point two five", "all correct"],
                "answer": 3,
                "explanation": "5.25はすべての表現が正しいです。"
            },
            {
                "question": "「百分率」を英語で何と言いますか？",
                "options": ["percentage", "fraction", "decimal", "ratio"],
                "answer": 0,
                "explanation": "百分率は「percentage」です。"
            },
            {
                "question": "「負の数」を英語で何と言いますか？",
                "options": ["minus number", "negative number", "bad number", "down number"],
                "answer": 1,
                "explanation": "負の数は「negative number」です。"
            },
            {
                "question": "「平方根」を英語で何と言いますか？",
                "options": ["square root", "square number", "root square", "number square"],
                "answer": 0,
                "explanation": "平方根は「square root」です。"
            }
        ],
        "4": [
            {
                "question": "「exponential」の意味は？",
                "options": ["指数の", "対数の", "平方の", "立方の"],
                "answer": 0,
                "explanation": "exponentialは「指数の」という意味です。"
            },
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
                "question": "「asymptote」の意味は？",
                "options": ["対称軸", "漸近線", "接線", "法線"],
                "answer": 1,
                "explanation": "asymptoteは「漸近線」という意味です。"
            },
            {
                "question": "「derivative」の意味は？",
                "options": ["積分", "微分", "極限", "級数"],
                "answer": 1,
                "explanation": "derivativeは「微分」という意味です。"
            }
        ],
        "5": [
            {
                "question": "「infinitesimal」の意味は？",
                "options": ["無限大の", "極小の", "有限の", "整数の"],
                "answer": 1,
                "explanation": "infinitesimalは「極小の、無限小の」という意味です。"
            },
            {
                "question": "「convergence」の意味は？",
                "options": ["発散", "収束", "振動", "回転"],
                "answer": 1,
                "explanation": "convergenceは「収束」という意味です。"
            },
            {
                "question": "「stochastic」の意味は？",
                "options": ["確定的な", "確率的な", "周期的な", "線形的な"],
                "answer": 1,
                "explanation": "stochasticは「確率的な」という意味です。"
            },
            {
                "question": "「permutation」の意味は？",
                "options": ["組み合わせ", "順列", "確率", "統計"],
                "answer": 1,
                "explanation": "permutationは「順列」という意味です。"
            },
            {
                "question": "「eigenvalue」の意味は？",
                "options": ["固有値", "特異値", "最大値", "最小値"],
                "answer": 0,
                "explanation": "eigenvalueは「固有値」という意味です。"
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