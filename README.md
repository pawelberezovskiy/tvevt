Порядок настройки

1 . настройка базы

 python /manage.py  syncdb

2. Запуск приложения

 python manage.py runserver 0.0.0.0:8081

3 . Настройка nginx


 server {
        listen 80;
        server_name %server name%;

        root %project path%;

        location / {
                client_max_body_size 2048m;
                proxy_pass_header Server;
                proxy_set_header Host $http_host;
                proxy_redirect off;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Scheme $scheme;
                proxy_connect_timeout 30;
                proxy_read_timeout 30;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_pass http://127.0.0.1:8081;
                expires off;
        }

    }


4 . Проверка


a) GET /api/user 

 curl -H 'Accept: application/json; indent=4' -u pawel@berezovskiy.su:gfhjkmxtu http://127.0.0.1:8081/api/user/

b) GET PATCH /api/user

curl --request PATCH http://127.0.0.1:8081/api/user/ -u email:password  -d "age=19"

c) GET /api/users

curl -H 'Accept: application/json; indent=4' -u pawel@berezovskiy.su:gfhjkmxtu http://127.0.0.1:8081/api/users/

d) GET /api/users/{user-id}

 curl -H 'Accept: application/json; indent=4' -u pawel@berezovskiy.su:gfhjkmxtu http://127.0.0.1:8081/api/users/pawel@berezovskiy.su/



