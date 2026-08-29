from pathlib import Path
from driftech_lib import jsonIO
from types import ModuleType

DIR = Path(__file__).resolve().parent
data = jsonIO.load(DIR / "config.json")
managers: dict[str, ModuleType] = {}

# TEMP
from managers import minecraft
managers["minecraft"] = minecraft