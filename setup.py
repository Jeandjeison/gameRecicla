import cx_Freeze

executables = [cx_Freeze.Executable(
    script="game.py", icon="assets/ico-reciclagem.ico")]
cx_Freeze.setup(
    name="Jogo da Reciclagem",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets","funcoes.py"]}},
    executables=executables
)
