from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="clone_push_GitHub",
    version="1.0",
    description="Descrizione dell'applicazione",
    executables=executables
)