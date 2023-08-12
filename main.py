from Exercises.ej1 import ex1, graph_ex1, graph_ex1b
from Exercises.ej2b import ex2, graph_ex2b
from Exercises.ej2a import ex2a, graph_ex2a
import sys


functions = { "1a" : graph_ex1 , "1b": graph_ex1b, "2a" : graph_ex2a, "2b" : graph_ex2b }


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