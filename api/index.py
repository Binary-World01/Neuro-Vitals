import sys
import os
from pathlib import Path

# Add repo root to path so 'app' module can be found
sys.path.append(str(Path(__file__).parent.parent))

from app.main import app
