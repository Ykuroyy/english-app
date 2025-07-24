# 英語にチャレンジ - 中学生向け英語4択クイズアプリ

中学生が気軽にスマホで英語学習できる4択クイズアプリです。

## 機能

- **文法クイズ**: 基本的な英文法問題
- **単語クイズ**: 日常的な英単語の意味や読み方
- **数字クイズ**: 英語での数字の表現

## 技術スタック

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **デプロイ**: Railway

## ローカル環境での実行

1. リポジトリをクローン
```bash
git clone <repository-url>
cd english-app
```

2. 仮想環境を作成・有効化
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 依存関係をインストール
```bash
pip install -r requirements.txt
```

4. アプリケーションを実行
```bash
python app.py
```

5. ブラウザで `http://localhost:5000` にアクセス

## デプロイ

このアプリはRailwayでのデプロイに対応しています。
GitHubリポジトリをRailwayに接続するだけで自動デプロイされます。

## アプリの使い方

1. トップページでカテゴリー（文法、単語、数字）を選択
2. 4択問題に答える
3. 解答後に正解・不正解と解説が表示される
4. 5問終了後に結果が表示される
5. 「もう一度挑戦する」で最初に戻る

## 今後の拡張予定

- 問題数の追加
- 難易度設定
- 学習履歴の保存
- タイマー機能