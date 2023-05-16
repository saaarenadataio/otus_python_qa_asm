Cкрипт анализа .log файла
Формат записи в файле лога:
%h %t "%r" %>s %b "%{Referer}i" "%{User-Agent}i" %D
%h - имя удаленного хоста
%t - время получения запроса
%r - тип запроса, его содержимое и версия
%s - код состояния HTTP
%b - количество отданных сервером байт
%{Referer} - URL-источник запроса
%{User-Agent} - HTTP-заголовок, содержащий информацию о запросе
%D - длительность запроса в миллисекундах


Expected usage: log_parser.py parameter
    parameter - single log file or directory (all including 1st level files will be processed)

For each processed file returned filename.json:
    общее количество выполненных запросов
    количество запросов по HTTP-методам: GET - 20, POST - 10 и т.п. (список необходимых методов: GET, POST, PUT, HEAD, OPTIONS, DELETE)
    топ 3 IP адресов, с которых были сделаны запросы
    топ 3 самых долгих запросов, должно быть видно метод, url, ip, длительность, дату и время запроса