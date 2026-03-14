import pytest
from datetime import datetime
from src.task import Task, StatusEnum

def test_task_creation():
    t = Task(1, "payload data")
    assert t.id == "task_1"
    assert t.payload == "payload data"
    assert t.priority == "medium"
    assert t.status == StatusEnum.NOT_STARTED

def test_property_priority():
    t = Task(2, "data")
    t.priority = "high"
    assert t.priority == "high"
    with pytest.raises(ValueError):
        t.priority = "invalid"

def test_property_status():
    t = Task(3, "data")
    t.status = StatusEnum.PROCESSING
    assert t.status == StatusEnum.PROCESSING
    t.status = StatusEnum.COMPLETED
    
    with pytest.raises(ValueError):
        t.status = StatusEnum.PROCESSING

def test_time_created_readonly():
    t = Task(4, "data")
    with pytest.raises(AttributeError):
        t.time_created = "now"
