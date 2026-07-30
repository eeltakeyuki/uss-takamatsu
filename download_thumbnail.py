import os
import requests

# ✅ ここに YouTube APIキーを入力
API_KEY = "AIzaSyCwCWKarMx06ZPBcbvN-7ay-cBNyVi1Hjw"

# ✅ 取得したい再生リストIDをリストで指定
PLAYLIST_IDS = [
    "PLx5S7JmptoKkZAiAdsgdRgbOSCn3nFM2O",
    "PLx5S7JmptoKlOomBO44dNibDWjCUCBtxu",
]

# ✅ サムネイルを保存するディレクトリ (現在のフォルダ内の "thumbnail" フォルダ)
SAVE_DIR = os.path.join(os.getcwd(), "thumbnail")

# 🎯 フォルダが存在しない場合は作成
os.makedirs(SAVE_DIR, exist_ok=True)

def get_first_video_thumbnail(playlist_id):
    """
    指定したYouTube再生リストの最初の動画のサムネイルURLを取得する。
    """
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&maxResults=1&key={API_KEY}"
    response = requests.get(url).json()

    if "items" in response and len(response["items"]) > 0:
        video_id = response["items"][0]["snippet"]["resourceId"]["videoId"]
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        return thumbnail_url
    else:
        print(f"⚠️ 再生リスト {playlist_id} から動画を取得できませんでした。")
        return None

def download_thumbnail(url, playlist_id):
    """
    サムネイル画像をダウンロードして保存する。
    """
    response = requests.get(url)

    if response.status_code == 200:
        filepath = os.path.join(SAVE_DIR, f"{playlist_id}.jpg")
        with open(filepath, "wb") as file:
            file.write(response.content)
        print(f"✅ {filepath} を保存しました。")
    else:
        print(f"⚠️ {playlist_id}.jpg のサムネイル取得に失敗しました。")

# 🎯 各再生リストの最初の動画のサムネイルを取得して保存
for playlist_id in PLAYLIST_IDS:
    thumbnail_url = get_first_video_thumbnail(playlist_id)
    if thumbnail_url:
        download_thumbnail(thumbnail_url, playlist_id)

print("🎉 全てのサムネイル画像を取得しました！")
