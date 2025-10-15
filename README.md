# Тестирование веб-формы 

Проект автоматизации тестирования для формы [https://practice-automation.com/form-fields/](https://practice-automation.com/form-fields/) на языке программирования Python с использованием фреймворков PyTest, Selenium и подхода PageObjectModel.

## Запуск тестов
1. Клонируйте репозиторий на локальную машину с помощью команды:
```
git clone https://github.com/denkho/simsoft_test_task.git
```
2.На локальной машине перейдите в раздел с клонированным репозиторием, установите виртуальное окружение и активируйте его. 
Для Windows команды будут следующие:
```
python -m venv venv
venv\Scripts\activate
```
Для Linux:
```
python3 -m venv venv
source venv/bin/activate
```
3. Установите требуемые зависимости из файла requirements.txt командой:
```
pip install -r requirements.txt
```
4. Запустите тесты командой
```
pytest -s ./tests
```
5. Сгенерировать отчет можно командой
```
allure serve reports
```
Просмотреть скрины из отчета Allure можно в директории [/allure_report/](/allure_report/)
