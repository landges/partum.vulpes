FROM nginx:1.23-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY /etc/ssl/partumvulpes.crt /etc/ssl
COPY /etc/ssl/partumvulpes.key /etc/ssl