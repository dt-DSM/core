from pathlib import Path
from driftech_lib import jsonIO

DIR = Path(__file__).resolve().parent
data = jsonIO.load(DIR / "config.json")