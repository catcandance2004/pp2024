from typing import List, Tuple
import numpy as np

class StudentMark:
    def __init__(self, id: int, name: str, dob: str, mark: float):
        self.id = id
        self.name= name
        self.dob = dob
        self.mark = mark