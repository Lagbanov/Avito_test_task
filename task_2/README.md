## Запуск тестов через Docker(рекомендуемый способ)
1. запустить Docker 
2. в терминале открыть текущий проект и выполнить команду `cd task_2`
3. выполнить команду `docker build -t avito-tests .`
4. после сборки образа выполнить команду `docker run -v $(pwd)/output:/avito_tests/output -it avito-tests`
5. после прогона тестов в папке output появятся скриншоты счетчика

## Запуск тестов на хосте 
1. в терминале перейти в текущий проект
2. создать виртуальное окружение `python3.10 -m venv venv` (должна быть установления версия python3.10 или выше)
3. активировать виртуальное окружение `sourse venv/bin/activate`
4. обновить `pip install --upgrade pip`
5. установить зависимости `pip install -r requirements.txt`
6. установить драйвера командой `playwright install`
7. возможно понадобится дополнительно установить зависимости `playwright install-deps`
8. отметить папку task_2 как source root (в PyCharm в ПКМ по папке task_2 -> Mark directory as -> Sources Root)
9. запустить тесты командой `pytest -s -v`
10. после прогона тестов в папке output появятся скриншоты счетчика 