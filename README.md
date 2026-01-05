# Задание 3: Автотесты для UI Stellar Burgers

## Что проверяем
- Переход по клику на «Конструктор»
- Переход по клику на «Лента заказов»
- Клик по ингредиенту открывает модальное окно с деталями
- Модальное окно закрывается по крестику
- При добавлении ингредиента в заказ счётчик ингредиента растёт
- Лента заказов:
  - счётчик «Выполнено за всё время» увеличивается при новом заказе
  - счётчик «Выполнено за сегодня» увеличивается при новом заказе
  - номер нового заказа появляется в разделе «В работе»

## Стек
- Page Object для описания элементов и действий
- `pytest` + `selenium`
- `allure-pytest` для отчетов

## Установка зависимостей
```powershell
pip install -r requirements.txt
```

## Запуск UI-тестов
### Windows CMD
```cmd
set BROWSER=chrome
python -m pytest --alluredir=allure_results
```

### Windows PowerShell
```powershell
$env:BROWSER="chrome"
python -m pytest --alluredir=allure_results
```

### Доступные браузеры
- `chrome` (по умолчанию)
- `firefox`

## Просмотр Allure-отчета
```powershell
allure serve allure_results
```
