import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2].as_posix()
sys.path.insert(0, ROOT)