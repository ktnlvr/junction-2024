from dataclasses import dataclass

@dataclass
class Product:
    name: str
    decay: float

TOMATO = Product("Tomato", 0.5)
SALAD = Product("Salad")
