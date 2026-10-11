const CACHE_NAME = "spam-detector-shell-v2";
const APP_SHELL = [
    "/static/detector/style.css",
    "/static/detector/script.js",
    "/static/detector/icon.svg",
    "/static/detector/icon-192.png",
    "/static/detector/icon-512.png",
    "/static/detector/offline.html",
    "/static/detector/manifest.webmanifest"
];

self.addEventListener("install", (event) => {
    event.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(APP_SHELL)));
    self.skipWaiting();
});

self.addEventListener("activate", (event) => {
    event.waitUntil(
        caches.keys().then((keys) => Promise.all(
            keys.filter((key) => key.startsWith("spam-detector-") && key !== CACHE_NAME)
                .map((key) => caches.delete(key))
        )).then(() => self.clients.claim())
    );
});

self.addEventListener("fetch", (event) => {
    const request = event.request;
    const url = new URL(request.url);

    if (request.method !== "GET" || url.origin !== self.location.origin) return;

    if (url.pathname.startsWith("/static/detector/")) {
        event.respondWith(
            caches.match(request).then((cached) => cached || fetch(request).then((response) => {
                if (response.ok) {
                    const copy = response.clone();
                    caches.open(CACHE_NAME).then((cache) => cache.put(request, copy));
                }
                return response;
            }))
        );
        return;
    }

    if (request.mode === "navigate") {
        event.respondWith(fetch(request).catch(() => caches.match("/static/detector/offline.html")));
    }
});