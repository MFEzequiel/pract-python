# *-- UTF--8 --*
import os

def open_program(program):
    try:
        os.system(program)
    except Exception as e:
        print(f"No se encontroel {e} prorama")
        
prog = input()
open_program(f"start {prog}")