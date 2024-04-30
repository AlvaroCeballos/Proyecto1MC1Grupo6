
from cx_Freeze import setup, Executable

setup(
    name = "NombreDelPrograma",
    version = "0.1",
    description = "Descripción del programa",
    executables = [Executable("proyectoprubea.py", base="Win32GUI")]
)