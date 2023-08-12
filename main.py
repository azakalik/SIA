from Exercises.ej1 import ex1, graph_ex1a, graph_ex1b
from Exercises.ej2b import ex2, graph_ex2b
from Exercises.ej2a import ex2a, graph_ex2a
from Exercises.ej2d import ex2d
import sys
import os


folder_path = "./Results/"

# Check if the folder exists
fp1 = folder_path + "Ex1"
if not os.path.exists(fp1):
    os.makedirs(fp1)
fp2 = folder_path + "Ex2a"
if not os.path.exists(fp2):
    os.makedirs(fp2)
fp3 = folder_path + "Ex2b"
if not os.path.exists(fp3):
    os.makedirs(fp3)
fp4 = folder_path + "Ex2d"
if not os.path.exists(fp4):
    os.makedirs(fp4)




functions = { "1a" : graph_ex1a , "1b": graph_ex1b, "2a" : graph_ex2a, "2b" : graph_ex2b }
exerciseFunction = sys.argv[1] if len(sys.argv) > 1 else None 
if __name__ != "__main__":
    quit()

if exerciseFunction != None and exerciseFunction not in functions:
    sys.stderr.write("Invalid parameter\n")
    quit()


if exerciseFunction == None:
    print("generating data...")
    ex1("./src/configs/item1.json")
    ex2("./src/configs/item2b.json")
    ex2a("./src/configs/item2a.json")
    ex2d("./src/configs/item2d.json")
    print("Data generated successfully!")
else:
    functions[exerciseFunction]()






# Corre el Ejercicio 1
# Exporta resultados a Results/Ex1
#ex1("./src/configs/item1.json")
#graph_ex1()
#graph_ex1b()
# Corre el Ejercicio 2
# Exporta resultados a Results/Ex2
# ex2("./src/configs/item2b.json")
# graph_ex2b()