# AZK-TS система информационной поддержки (autotests)
проект предназначен для тестирование веб-приложение UI, API. Основные библиотеки для тестирования "Selenium" и "Requests"
## Установка 
1) Склонируйте репозиторий на локальное устройство с github 
2) Создайте виртуальное окружение 
3) Установите необходимые зависимости `pip intsall -r requirements.txt`
## Использование
1) запустить тесты с созданием папки для отчётов `pytest -v .\tests\ --alluredir reports_after_run_tests`
2) Открыть алюр для отображение отчёта `allure serve reports_after_run_tests`
### Разные способы для запуска отдельных папок с тестами и отдельными методами
```commandline
 запуск папки pytest -v .\test\
 запуска фалйа pytest -v .\tests\gui_tests\test_app.py
 запуск только одного метода  pytest -v .\tests\gui_tests\test_app.py::TestApppage::test_create_applicationVT
```