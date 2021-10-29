docker stop mysql && docker rm mysql
docker run -itd \
--name mysql \
-p 3306:3306 \
-v $PWD/src/jessie.list:/etc/apt/sources.list \
-v $PWD/data/:/home/ \
-e MYSQL_ROOT_PASSWORD=hfut \
-e LANG=c.UTF-8 \
-e TZ='Asia/Shanghai' \
mysql:5.7.17 \
--collation-server=utf8mb4_unicode_ci \
--character-set-server=utf8mb4 \
