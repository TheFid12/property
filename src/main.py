from loguru import logger
from src.source import (
    FileTaskSource,
    GeneratorTaskSource,
    APITaskSource,
    collect_all,
)

logger.remove()
logger.add(
    "log.txt",
    format="{time:HH:mm:ss} - {level} - {message}",
    level="INFO",
    mode="a",
    encoding="utf-8",
)


def main() -> None:
    """
    Точка входа в модуль.
    В sources указываются источники задач.
    """
    logger.info("Начало получения задач из источников.")
    sources = [
        FileTaskSource("tasks.json"),
        GeneratorTaskSource(count=3, prefix="task"),
        APITaskSource([{"id": "api_task_1", "payload": "from api"}])
    ]
    tasks = collect_all(sources)
    logger.info(f"Сбор задач завершен. Всего: {len(tasks)}")
    for task in tasks:
        print(f"[{task.id}] {task.payload}")


if __name__ == "__main__":
    main()
