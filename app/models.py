from dataclasses import dataclass


@dataclass
class Project:
    path: str
    ssh_url: str