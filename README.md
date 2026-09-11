# Sprint_6 — UI-автотесты «Яндекс Самокат»

Проект покрывает обязательные сценарии финального задания шестого спринта:

- восемь вопросов раздела «Вопросы о важном»;
- два позитивных сценария заказа с разными данными и точками входа;
- переход по логотипу Самоката;
- переход по логотипу Яндекса в новую вкладку: на Дзен для старого редиректа
  или на актуальную главную Яндекса;
- формирование результатов Allure.

## Стек

- Python 3.10+
- pytest
- Selenium WebDriver
- Mozilla Firefox
- Allure Pytest
- Page Object Model

## Подготовка в VS Code

1. Открой папку `Sprint_6` в VS Code.
2. Создай и активируй виртуальное окружение:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   В Windows PowerShell команда активации:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Установи зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Убедись, что Mozilla Firefox установлен. Selenium Manager автоматически
   подберёт совместимый `geckodriver` при первом запуске.

## Запуск тестов

```bash
pytest
```

По умолчанию Firefox запускается с интерфейсом. Для фонового запуска:

```bash
HEADLESS=1 pytest
```

В Windows PowerShell:

```powershell
$env:HEADLESS="1"; pytest
```

Результаты Allure автоматически сохраняются в `allure_results`.

## Просмотр и генерация Allure-отчёта

Для локального просмотра:

```bash
allure serve allure_results
```

Для генерации статического отчёта:

```bash
allure generate allure_results -o allure_report --clean
```

В репозиторий нужно добавить исходный код и папку `allure_results`. Папка
`allure_report` исключена из Git через `.gitignore`, потому что её всегда можно
пересобрать из результатов.

## Структура проекта

```text
Sprint_6/
├── pages/
│   ├── base_page.py
│   ├── main_page.py
│   └── order_page.py
├── test/
│   ├── test_faq.py
│   ├── test_navigation.py
│   └── test_order.py
├── conftest.py
├── faq_data.py
├── order_data.py
├── pytest.ini
├── requirements.txt
├── texts.py
└── urls.py
```
# Sprint_6
# Sprint_6
