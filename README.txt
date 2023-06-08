данное приложение создано в процессе изучения
- Flask
- HTML/CSS 
- Botstrap 4
- docker
Это приложение Информационный Каталог. Создано для удоства хранения информация по связанной с сетью и информационными системами. 
Для запуска приложения необходимо:

1)docker-compose -f docker-compose.yml build 
2)docker-compose -f docker-compose.yml up -d
3)docker exec ktl_db_1 sh -c "pg_restore -U postgres -d ktl_db /var/lib/postgresql/backup/ktl2.sql"  ### восстановление кастомного дампа БД
4) используйте ip-адрес машины на которой запущен контейнер.
логин: admin пароль: admin

good luck:)
