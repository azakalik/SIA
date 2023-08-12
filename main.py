from Exercises.ej1 import ex1, graph_ex1a, graph_ex1b
from Exercises.ej2b import ex2b, graph_ex2b
from Exercises.ej2a import ex2a, graph_ex2a
from Exercises.ej2c import ex2c, graph_ex2c
from Exercises.ej2d import ex2d
import sys

functions = {"1a": graph_ex1a, "1b": graph_ex1b, "2a": graph_ex2a, "2b": graph_ex2b, "2c": graph_ex2c()}

exerciseFunction = sys.argv[1] if len(sys.argv) > 1 else None
if __name__ != "__main__":
    quit()

if exerciseFunction != None and exerciseFunction not in functions:
    sys.stderr.write("Invalid parameter\n")
    quit()

if exerciseFunction == None:
    print("generating data...")
    ex1("./src/configs/item1.json")
    ex2a("./src/configs/item2a.json")
    ex2b("./src/configs/item2b.json")
    ex2c("./src/configs/item2c.json")
    ex2d("./src/configs/item2d.json")
    print("Data generated successfully!")
else:
    functions[exerciseFunction]()
