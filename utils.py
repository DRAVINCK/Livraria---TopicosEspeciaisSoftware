# utils.py
from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def formata_moeda(v):
    return f"R$ {v:.2f}"

def eh_par(x: int) -> bool:
    return x % 2 == 0

def eh_impar(x: int) -> bool:
    return not eh_par(x)
