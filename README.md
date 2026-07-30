# USS TAKAMATSU YouTube List

UNITED SS TAKAMATSU（ユナイテッドSS高松）の試合動画・Team Cam・おすすめ再生リスト・エンタメ動画を快適に閲覧できるPWA対応Webアプリケーションです。

---

## 📌 概要

**USS TAKAMATSU YouTube List** は、UNITED SS TAKAMATSUのYouTube再生リストを年度別・学年別・イベント別に分類し、直感的な横スクロールカードUIおよびグリッドUIで提供します。スマートフォン、タブレット、PCのすべてのデバイスで最適に表示されるレスポンシブデザインと、PWA（Progressive Web App）対応によるアプリ同等の快適な操作性を実現しています。

---

## 🚀 主な機能・特徴

- **カテゴリ・年度別再生リスト一覧 (`index.html`)**
  - **⭐ おすすめ再生リスト**: Team Camや注目の主要大会動画をピックアップ表示
  - **📅 学年・年度別アーカイブ**: 2026年度（U-12）、2025年度（U-11）、2024年度（U-10）、2023年度（U-9）など各世代の大会・遠征動画
  - **▶️ エンタメ動画**: 実況動画、ゴール集、テレビ放送、徹底解説シリーズなど
- **2026 U-12 特集ページ (`2026u12.html`)**
  - 動的な写真スライドショー表示機能
  - グリッドレイアウトによる大会再生リストカード表示
- **📱 モバイル最適化 & PWA対応**
  - タッチ操作しやすいレスポンシブ・横スクロールUI
  - Web App Manifest (`manifest.json`) および Service Worker (`sw.js`) 搭載
  - スマホのホーム画面に追加して独立アプリのように起動可能
- **🐍 サムネイル自動取得スクリプト (`download_thumbnail.py`)**
  - YouTube Data API v3 を活用し、再生リスト内最新動画のサムネイル画像を自動取得・保存

---

## 📂 プロジェクト構成

```
uss-takamatsu/
├── index.html              # メインWebページ（カテゴリ別再生リスト一覧・PWA対応）
├── 2026u12.html            # 2026 U-12 特集ページ（スライドショー＆グリッド表示）
├── download_thumbnail.py   # YouTube Data APIを利用したサムネイル自動取得スクリプト
├── manifest.json           # PWAマニフェスト設定ファイル
├── sw.js                   # サービスワーカー（キャッシュ制御・PWA対応）
├── usslogo.png             # チームロゴ画像
├── ussicon.png             # アプリアイコン画像
├── favicon-*.png           # 各種サイズファビコン
├── thumbnail/              # サムネイル画像格納フォルダ
└── AGENTS.md               # エージェント運用ルール設定
```

---

## 🛠 使い方・開発方法

### 1. Webページの閲覧
ローカル環境で `index.html` または `2026u12.html` をブラウザで開くか、Webサーバー（GitHub Pages等）にデプロイしてアクセスします。

### 2. サムネイルの自動更新
`download_thumbnail.py` を実行して、対象再生リストのサムネイル画像を最新に更新できます。

```bash
# 依存ライブラリのインストール
pip install requests

# サムネイル取得スクリプトの実行
python download_thumbnail.py
```

---

## 📄 ライセンス・権利表記

© UNITED SS TAKAMATSU
