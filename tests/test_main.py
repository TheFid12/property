import pytest

from src.source import (
    GeneratorSource,
    ApiSource,
    collect_all,
)
from src.main import main


class BrokenSource:
    def get_items(self):
        return []


def test_collect_all_multiple_sources():
    gen = GeneratorSource(count=2, prefix="t")
    api = ApiSource(tasks=[{"payload": "data"}])

    result = collect_all([gen, api])

    assert len(result) == 3


def test_collect_all_empty():
    assert collect_all([]) == []


def test_collect_all_rejects_invalid():
    broken = BrokenSource()

    with pytest.raises(TypeError, match="не соответствует протоколу"):
        collect_all([broken])


def test_main_output(capsys):
    main()
    output = capsys.readouterr().out

    assert "task_" in output
    assert "api data" in output
