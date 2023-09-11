import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("board.py", base=base)]

setup(
    name="StoryboardApp",
    version="1.0",
    description="Storyboard and Previsualization Tool",
    executables=executables,
)
