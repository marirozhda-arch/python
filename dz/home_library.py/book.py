from dataclasses import dataclass


@dataclass(slots=True)
class Book:
    title: str
    author: str
    publication_year: int
    genre: str
    is_read: bool
    id: int | None = None