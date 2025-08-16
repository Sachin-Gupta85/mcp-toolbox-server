"""Unit-conversion tool (length, mass, temperature)."""
from __future__ import annotations

# conversion factors to a base unit
_LENGTH = {"m": 1.0, "km": 1000.0, "cm": 0.01, "mi": 1609.344, "ft": 0.3048, "in": 0.0254}
_MASS = {"kg": 1.0, "g": 0.001, "mg": 1e-6, "lb": 0.45359237, "oz": 0.028349523125}


def _to_celsius(v: float, unit: str) -> float:
    return {"c": v, "f": (v - 32) * 5 / 9, "k": v - 273.15}[unit]


def _from_celsius(c: float, unit: str) -> float:
    return {"c": c, "f": c * 9 / 5 + 32, "k": c + 273.15}[unit]


def convert(value: float, from_unit: str, to_unit: str) -> float:
    f, t = from_unit.lower(), to_unit.lower()
    if f in _LENGTH and t in _LENGTH:
        return value * _LENGTH[f] / _LENGTH[t]
    if f in _MASS and t in _MASS:
        return value * _MASS[f] / _MASS[t]
    if f in ("c", "f", "k") and t in ("c", "f", "k"):
        return _from_celsius(_to_celsius(value, f), t)
    raise ValueError(f"cannot convert {from_unit!r} to {to_unit!r}")
