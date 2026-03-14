# Лабораторная работа №2
# Модель задачи: дескрипторы и @property

Автор: Бычков Евгений, М8О-104БВ-25

## Цель работы
Освоить управление доступом к атрибутам доменной модели и защиту инвариантов объекта Task.


### 1. Атрибуты задачи
Task содержит:
- идентификатор (формат task_N);
- payload (описание/данные задачи);
- priority (low, medium, high, critical);
- status (Not started, Processing, Completed, Cancelled);
- time_created (время создания).

### 2. Валидация и защита инвариантов
- Приоритет валидируется в setter свойства priority.
- Статус валидируется в setter свойства status.
- Запрещен некорректный переход обратно в Not started.
- Запрещено менять статус уже завершенной или отмененной задачи.

### 3. Использование дескрипторов
В работе используется встроенный дескрипторный механизм Python через @property:
- data-descriptor: priority, status (есть чтение и запись);
- non-data/read-only подход: id, time_created (только чтение через property).


## Архитектура проекта
```text
property/
├── src/
│   ├── main.py        # точка входа
│   ├── source.py      # протокол Source, источники, collect_all, process_task
│   └── task.py        # модель Task, статусы, валидация свойств
├── tests/
│   ├── test_main.py
│   ├── test_source.py
│   └── test_task.py
├── tasks.json         # входные payload для FileSource
├── log.txt            # журнал выполнения
└── README.md
```

## Источники задач
- FileSource: читает payload из JSON-файла.
- GeneratorSource: генерирует тестовые payload.
- ApiSource: имитация API-источника.

Все источники реализуют протокол Source с методом get_tasks().

## Запуск
```bash
python -m src.main
```

## Запуск тестов
```bash
python -m pytest .\tests\ -v
```