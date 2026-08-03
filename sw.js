const CACHE_NAME = 'uss-takamatsu-v5'; // ★更新時はここを v2, v3... と書き換えます
const STATIC_ASSETS = [
  './index.html',
  './manifest.json',
  './usslogo.png',
  './favicon-192x192.png',
  './favicon-512x512.png',
];

// 1. インストール（新しいアセットの事前キャッシュと即時有効化）
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(STATIC_ASSETS))
  );
  self.skipWaiting(); // 待機せずにすぐアクティブにする
});

// 2. アクティブ化（古いキャッシュの削除とクライアントの制御権取得）
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim(); // 既存のページを即座に制御する
});

// 3. リクエスト制御（ネットワーク優先で常に最新を取得）
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // POST等の取得以外の方法や、DevTools拡張等のリクエストはスキップ
  if (event.request.method !== 'GET') return;

  // 自サイトのリソース & 外部リクエスト（YouTube等）ともに「ネットワーク優先」
  event.respondWith(
    fetch(event.request)
      .then(response => {
        // 正常なレスポンスであればキャッシュを最新版に上書き
        if (response && response.status === 200 && response.type === 'basic') {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        }
        return response;
      })
      .catch(() => {
        // オフラインなどでネットワーク取得に失敗した時だけキャッシュを返す
        return caches.match(event.request);
      })
  );
});
