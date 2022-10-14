FROM nginx:1.23.1-alpine

COPY ./docker/nginx/nginx.conf /nginx.conf.template

CMD ["/bin/sh" , "-c" , "envsubst '${CLIENT_HOST} ${SERVER_HOST}' < /nginx.conf.template > /etc/nginx/nginx.conf && exec nginx -g 'daemon off;'"]
