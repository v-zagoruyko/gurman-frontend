FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html 404.html styles.css robots.txt sitemap.xml favicon.ico favicon.svg apple-touch-icon.png /usr/share/nginx/html/
COPY assets /usr/share/nginx/html/assets
COPY files /usr/share/nginx/html/files
