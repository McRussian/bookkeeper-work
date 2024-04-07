# pylint: disable=missing-module-docstring
from dataclasses import dataclass


@dataclass(slots=True)
class Budget:
    """
    Бюджет
    amount - сумма
    category - id категории расходов
    tern - срок использования
    pk - id записи в базе данных
    """
    amount: int
    category: int
    tern: str = 'month'
    pk: int = 0
