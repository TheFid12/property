from datetime import datetime
from enum import Enum
from typing import Any

class StatusEnum(Enum):
    NOT_STARTED = "Not started"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

PRIORITIES = ("low", "medium", "high", "critical")

class Task:
    """
    Класс задачи
    """
    def __init__(self, id: int, payload: Any, priority: str = "medium") -> None:
        self._id = id
        self.payload = payload
        self.priority = priority 
        self._status = StatusEnum.NOT_STARTED
        self._time_created = datetime.now()

    def __str__(self):
        return f"Task(id='{self.id}', payload={repr(self.payload)}, priority='{self.priority}', status='{self.status.value}', time_created='{str(self.time_created)}')"                                                       

    @staticmethod
    def format_id(task_id: int) -> str:
        return f"task_{task_id}"

    @property
    def id(self) -> str:
        return self.format_id(self._id)
    
    @property
    def time_created(self) -> datetime:
        return self._time_created

    @property
    def priority(self) -> str:
        return self._priority
    
    @priority.setter
    def priority(self, value: str) -> None:
        val = str(value).lower()
        if val not in PRIORITIES:
            raise ValueError(f"Недопустимый приоритет. Доступные: {PRIORITIES}")
        self._priority = val

    @property
    def status(self) -> StatusEnum:
        return self._status
    
    @status.setter
    def status(self, value: StatusEnum) -> None:
        if self._status != StatusEnum.NOT_STARTED and value == StatusEnum.NOT_STARTED:
            raise ValueError(f"Нельзя поменять статус {self._status} на {StatusEnum.NOT_STARTED}")
        if self._status in [StatusEnum.CANCELLED, StatusEnum.COMPLETED]:
            raise ValueError(f"Нельзя менять статус {self._status}")
        self._status = value
