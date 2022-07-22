# Slash commands
* `\c` - показывает в какой бд мы находимся и через какого юзера
* `\c name_of _bd` - переключаемся к этой бд 
* `\l` - показывает все бд
* `\dt` - показывает все таблицы в бд, к которой мы подключились
* `\du` - показывает всех юзеров
* `\q` - выход


# Создание бд и таблиц
```sql
CREATE DATABASE name_of_db;
-- создает базу данных
```
```sql
CREATE TABLE name_of_table (
    name_of_column1 data_type constraint,
    name_of_column2 data_type constraint,
    ...
);
-- создает таблицу с полями
```

# Заполнение таблиц
```sql 
INSERT INTO name_of_table (name_of_column1,
name_of_column2)
VALUES (val1, val2);
-- добавляет запись в таблицу
```

# Вывод данных из таблицы
```sql 
SELECT * FROM name_of_table;
-- достает все поля и все записи из таблицы
```

```sql
SELECT name_of_column1, name_of_column2 FROM name_of_table;
-- достает только указанные столбцы из таблицы(все записи)
```
```sql
SELECT * FROM name_of_table WHERE name_of_column2= 'hello';
-- достает все записи из таблицы, у которых name_of_columnn2 со значением 'hello'
```

# Связи 
## pk fk
> Primary Key (pk) - первичный ключ
>  это ограничение, которое мы указываем на те поля, которые должны быть уникальными для того, чтобы потом их использовать в связах(создает btree)

> Foreign Key (fk) - внешний ключ 
>  это ограничение, которое мы указываем на те поля, которые будут ссылаться на поле с pk в другой таблице, для создания связи


```sql
CREATE TABLE author (
    id serial primary key,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE book (
    id SERIAL,
    title VARCHAR(100),
    published year,
    author_id INT,
    CONSTRAINT fk_author_book
    FOREIGN KEY (author_id)
    REFERENCES author(id)
);
```

## Виды связей (теория)
> one to one 
Например:

* Один флаг - одна страна
* Один человек - одно сердце
* Один автор - одна автобиография
* Один человек - один ИНН


> one to many
Например:

* Один Оомат - много поздравлений
* Одна страна - много городов
* Один пост - много комментов
* Одна скамья - много людей
* Один диктатор - много рабов


> many to many
Например:

* много менторов - много студентов
* много пользователей - много соц сетей
* много докторов - много пациентов


## Виды связей (практика)
### one to one
```sql
CREATE TABLE flag (
    id SERIAL PRIMARY KEY,
    photo TEXT
);

CREATE TABLE country (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    flag_id INT UNIQUE,
    CONSTRAINT fk_country_flag
    FOREIGN KEY (flag_id)
    REFERENCES flag(id)
);
```

### one to many
```sql
CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    body TEXT
);

CREATE TABLE comment (
    id SERIAL PRIMARY KEY,
    body TEXT,
    created_at DATETIME,
    post_id INT,
    CONSTRAINT fk_post_comment
    FOREIGN KEY (post_id)
    REFERENCES post(id)
);
```

### many to many
```sql
CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    age INT
);

CREATE TABLE mentor (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    age INT
);

CREATE TABLE student_mentor(
    student_id INT,
    mentor_id INT,

    CONSTRAINT fk_student
    FOREIGN KEY (student_id)
    REFERENCES student(id),

    CONSTRAINT fk_mentor
    FOREIGN KEY (mentor_id)
    REFERENCES mentor(id),
);
```

## Join (теория)
> JOIN - инструкция, которая позволяет в запросах Select выбрать данные из нескольких связанных таблиц

> INNER JOIN (JOIN) -  когда достаются только те записи, у которых есть полная связь

> FULL JOIN - когда достаются абсолютно все записи, со всех таблиц (неважно есть ли связь у записей)

> LEFT JOIN - когда достаются все записи с левой таблицы от слова LEFT JOIN и также записи с полной связью

> RIGHT JOIN - когда достаются все записи с правой таблицы от слова RIGHT JOIN и также записи с полной связью


## JOIN (практика)
### one to one 
```sql
SELECT country.title, flag.photo
FROM country
JOIN flag 
ON country.flag_id = flag.id;
```

### one to many
```sql
SELECT post.title, comment.body, comment.created_at
FROM post
JOIN comment
ON post.id = comment.post_id;
```

### many to many
```sql
SELECT mentor.first_name as mentor_name, student.first_name as student_name
FROM mentor 
JOIN student_mentor
ON mentor.id = student_mentor.mentor_id

JOIN student
ON student.id = student_mentor.student_id;
```

# импорт/экспорт данных
write from file to db
```bash
psql db_name < file.sql
```

write from db to file
```bash
pg_dump db_name > file.sql 
```
