import logging
import sys
from src.source import Source, FileSource, GeneratorSource, ApiSource
from src.handler import collect_all

def interactive_menu() -> list[Source]:
    """
    Интерактивное меню для настройки источников задач.
    Позволяет добавлять несколько источников и запускать обработку.
    """
    sources: list[Source] = []
    
    while True:
        print("\nНастройка источников задач")
        print("1. Добавить GeneratorSource")
        print("2. Добавить FileSource (tasks.json)")
        print("3. Добавить ApiSource")
        print(f"4. Запустить обработку (выбрано: {len(sources)})")
        print("5. Выход")
        print()
        
        choice = input("Выберите действие: ").strip()
        
        if choice == '1':
            count = input("Количество задач: ")
            if count.isdigit() and int(count) > 0:
                sources.append(GeneratorSource(count=int(count)))
                print(f"Добавлен GeneratorSource({count})\n")
            else:
                print("Ошибка: введите положительное число\n")
        elif choice == '2':
            sources.append(FileSource("tasks.json"))
            print("Добавлен FileSource\n")
        elif choice == '3':
            items = input("Введите данные (через запятую): ")
            if items.strip():
                data = [{"payload": i.strip()} for i in items.split(",") if i.strip()]
                sources.append(ApiSource(data))
                print(f"Добавлен ApiSource ({len(data)} элементов)\n")
            else:
                print("Отменено\n")
        elif choice == '4':
            if sources:
                break
            else:
                print("Добавьте хотя бы один источник\n")
        elif choice == '5':
            sys.exit(0)
            
    return sources

def main() -> None:
    """
    Запуск сборщика задач, который запрашивает и выполняет задачи
    из различных источников.
    """
    logging.basicConfig(
        filename="log.txt",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

    sources = interactive_menu()
    
    if not sources:
        print("Не выбрано ни одного источника. Завершение работы.")
        return
        
    collect_all(sources)

if __name__ == "__main__":
    main()
