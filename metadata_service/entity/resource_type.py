from enum import Enum, auto


class ResourceType(Enum):
    Table = auto()
    Dashboard = auto()
    User = auto()


def to_resource_type(*, label: str) -> ResourceType:
    return ResourceType[label.title()]
