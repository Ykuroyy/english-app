let currentQuiz = [];
let currentQuestionIndex = 0;
let score = 0;
let selectedCategory = '';
let selectedLevel = '';

const startScreen = document.getElementById('start-screen');
const levelScreen = document.getElementById('level-screen');
const quizScreen = document.getElementById('quiz-screen');
const resultScreen = document.getElementById('result-screen');
const questionEl = document.getElementById('question');
const optionsEl = document.getElementById('options');
const feedbackEl = document.getElementById('feedback');
const nextBtn = document.getElementById('next-btn');
const scoreEl = document.getElementById('score');
const currentQuestionEl = document.getElementById('current-question');
const totalQuestionsEl = document.getElementById('total-questions');
const finalScoreEl = document.getElementById('final-score');
const finalTotalEl = document.getElementById('final-total');
const resultMessageEl = document.getElementById('result-message');

document.querySelectorAll('.category-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        selectedCategory = e.target.dataset.category;
        showLevelSelection();
    });
});

document.querySelectorAll('.level-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        selectedLevel = e.target.dataset.level;
        startQuiz();
    });
});

document.getElementById('back-to-category').addEventListener('click', () => {
    showScreen('start');
});

document.getElementById('level-to-top').addEventListener('click', () => {
    resetQuiz();
});

document.getElementById('quiz-to-top').addEventListener('click', () => {
    resetQuiz();
});

document.getElementById('restart-btn').addEventListener('click', () => {
    startQuiz();
});

document.getElementById('level-up-btn').addEventListener('click', () => {
    const nextLevel = parseInt(selectedLevel) + 1;
    if (nextLevel <= 5) {
        selectedLevel = nextLevel.toString();
        startQuiz();
    }
});

document.getElementById('back-to-top-btn').addEventListener('click', () => {
    resetQuiz();
});

nextBtn.addEventListener('click', () => {
    currentQuestionIndex++;
    if (currentQuestionIndex < currentQuiz.length) {
        showQuestion();
    } else {
        showResults();
    }
});

function showLevelSelection() {
    const categoryNames = {
        'grammar': '文法',
        'vocabulary': '単語',
        'numbers': '数字'
    };
    document.getElementById('level-title').textContent = `${categoryNames[selectedCategory]} - レベルを選んでください`;
    showScreen('level');
}

async function startQuiz() {
    try {
        const response = await fetch(`/api/quiz/${selectedCategory}/${selectedLevel}`);
        currentQuiz = await response.json();
        
        if (currentQuiz.length === 0) {
            alert('クイズデータの読み込みに失敗しました。');
            return;
        }
        
        currentQuestionIndex = 0;
        score = 0;
        scoreEl.textContent = '0';
        totalQuestionsEl.textContent = currentQuiz.length;
        showScreen('quiz');
        showQuestion();
    } catch (error) {
        alert('エラーが発生しました。もう一度お試しください。');
        console.error(error);
    }
}

function showQuestion() {
    const question = currentQuiz[currentQuestionIndex];
    questionEl.textContent = question.question;
    optionsEl.innerHTML = '';
    feedbackEl.style.display = 'none';
    feedbackEl.className = 'feedback';
    nextBtn.style.display = 'none';
    
    currentQuestionEl.textContent = currentQuestionIndex + 1;
    
    question.options.forEach((option, index) => {
        const button = document.createElement('button');
        button.className = 'option-btn';
        button.textContent = option;
        button.addEventListener('click', () => selectAnswer(index));
        optionsEl.appendChild(button);
    });
}

function selectAnswer(selectedIndex) {
    const question = currentQuiz[currentQuestionIndex];
    const optionBtns = document.querySelectorAll('.option-btn');
    
    optionBtns.forEach((btn, index) => {
        btn.classList.add('disabled');
        btn.disabled = true;
        
        if (index === question.answer) {
            btn.classList.add('correct');
        } else if (index === selectedIndex && selectedIndex !== question.answer) {
            btn.classList.add('incorrect');
        }
    });
    
    if (selectedIndex === question.answer) {
        score++;
        scoreEl.textContent = score;
        feedbackEl.textContent = '正解！ ' + question.explanation;
        feedbackEl.className = 'feedback correct';
    } else {
        feedbackEl.textContent = '不正解... ' + question.explanation;
        feedbackEl.className = 'feedback incorrect';
    }
    
    feedbackEl.style.display = 'block';
    nextBtn.style.display = 'block';
}

function showResults() {
    finalScoreEl.textContent = score;
    finalTotalEl.textContent = currentQuiz.length;
    
    const percentage = (score / currentQuiz.length) * 100;
    const levelUpBtn = document.getElementById('level-up-btn');
    
    if (percentage === 100) {
        resultMessageEl.textContent = '完璧です！素晴らしい！';
        if (parseInt(selectedLevel) < 5) {
            levelUpBtn.style.display = 'inline-block';
        } else {
            levelUpBtn.style.display = 'none';
        }
    } else if (percentage >= 80) {
        resultMessageEl.textContent = 'とても良くできました！';
        levelUpBtn.style.display = 'none';
    } else if (percentage >= 60) {
        resultMessageEl.textContent = 'よくできました！もう少し頑張りましょう！';
        levelUpBtn.style.display = 'none';
    } else {
        resultMessageEl.textContent = 'もう一度挑戦してみましょう！';
        levelUpBtn.style.display = 'none';
    }
    
    showScreen('result');
}

function resetQuiz() {
    currentQuiz = [];
    currentQuestionIndex = 0;
    score = 0;
    scoreEl.textContent = '0';
    showScreen('start');
}

function showScreen(screenName) {
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.remove('active');
    });
    
    switch(screenName) {
        case 'start':
            startScreen.classList.add('active');
            break;
        case 'level':
            levelScreen.classList.add('active');
            break;
        case 'quiz':
            quizScreen.classList.add('active');
            break;
        case 'result':
            resultScreen.classList.add('active');
            break;
    }
}