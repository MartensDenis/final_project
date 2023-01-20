Введение
------------

тестирование сайта Ростелеком.     
Включает в себя:     
1). [тестовую документацию: чек-листы, тест-кейсы, диаграммы состояний и переходов в соответствии с пользовательскими сценариями](https://docs.google.com/spreadsheets/d/1ozhYKREWZtFxSL6fGxtmr54SYOnzvWw7kLGjS6JgYv8/edit?usp=sharing)  
2). 36 автотестов


Автотесты
-----
1). Автотесты написаны на языке python, использованы библиотеки Pytest, Selenium, beautifulsoup4 и 2captcha-python и др.           
2). При проектировании автотестов использован паттерн PageObject, за основу взята библиотека Smart Page Object.                    
3). Использован Webdriver Manager for Python, тесты стабильно работают для driver.Chrome(), Firefox не видит некоторые используемые локаторы             
4). Автотесты перехватывают почту и смс для прохождения аутентификаций. Для получения смс телефона использовано дополнительное програмное обеспечение на андройд         
5). Для автоматического прохождения каптчи использован автосервис rucaptcha.com и её библиотеки               
6). Автотесты подменяют текст в браузере страницы для визуального понимания того что происходит на этапах тестирования                
7). Общее время прохождения тестов 10 минут               

Примечания
----------------
Все необходимые библиотеки отражены в requirements.txt                    
Все тесты запускаются из командной строки командой pytest             
При падении некоторых тестов необходимо запустить их повторно pytest --last-failed     



