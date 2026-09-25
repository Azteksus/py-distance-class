class Distance:
    def __init__(self, km: int) -> None:
        self.km = km
        self.real = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "int | float") -> "Distance":
        return Distance(
            self.km + other.real
        )

    def __iadd__(self, other: "int | float") -> "Distance":
        self.km += other.real
        return self

    def __mul__(self, other: "int | float") -> "Distance":
        if isinstance(other, Distance):
            return NotImplemented
        return Distance(self.km * other.real)

    def __truediv__(self, other: "int | float") -> "Distance":
        if isinstance(other, Distance):
            return NotImplemented
        return Distance(round(self.km / other.real, 2))

    def __lt__(self, other: "Distance | int | float") -> bool:
        return self.km < other.real

    def __gt__(self, other: "Distance | int | float") -> bool:
        return self.km > other.real

    def __eq__(self, other: "Distance | int | float") -> bool:
        return self.km == other.real

    def __le__(self, other: "Distance | int | float") -> bool:
        return self.km <= other.real

    def __ge__(self, other: "Distance | int | float") -> bool:
        return self.km >= other.real
