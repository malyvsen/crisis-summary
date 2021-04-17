from dataclasses import dataclass
from datetime import datetime


@dataclass
class Tweet:
    text: str
    user: str
    time: datetime
