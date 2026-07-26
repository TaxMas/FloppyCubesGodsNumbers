class Floppy:
    def __init__(self, scramble = []):
        # Van por la forma de escribir (de izquierda a derecha, y de arriba a abajo) si miras esa cara de frente
        self.U = [0]*9 # White
        self.D = [1]*9 # Yellow
        # Van de izquierda a derecha si miras esa cara de frente
        self.F = [2]*3 # Green
        self.B = [3]*3 # Blue
        self.R = [4]*3 # Red
        self.L = [5]*3 # Orange

        self.scramble = []
        for i in scramble:
            self.move(i)  

    def __eq__(self, other):
        # Solo mirando U, F y R se puede saber si el cubo esta igual o no
        if self.U != other.U:
            return False
        elif self.F != other.F:
            return False
        elif self.R != other.R:
            return False
        return True

    def move(self, move):
        self.scramble.append(move)
        
        if move == "F":
            self.F = self.F[::-1]
            self.R[0], self.L[2] = self.L[2], self.R[0]
            self.U[6:9], self.D[0:3] = self.D[0:3][::-1], self.U[6:9][::-1]
        elif move == "B":
            self.B = self.B[::-1]
            self.R[2], self.L[0] = self.L[0], self.R[2]
            buffer = self.U[0:3]
            self.U[0:3], self.D[6:9] = self.D[6:9][::-1], self.U[0:3][::-1]
        elif move == "R":
            self.R = self.R[::-1]
            self.F[2], self.B[0] = self.B[0], self.F[2]
            for i in (2, 5, 8):
                self.U[i], self.D[i] = self.D[i], self.U[i]
        elif move == "L":
            self.L = self.L[::-1]
            self.F[0], self.B[2] = self.B[2], self.F[0]
            for i in (0, 3, 6):
                self.U[i], self.D[i] = self.D[i], self.U[i]

    def __str__(self):
        return str(self.U) + str(self.F) + str(self.R)

    def __len__(self):
        return len(self.scramble)

    def __hash__(self):
        return hash(tuple(self.U + self.F + self.R))

# Codigo para generar todos los floppys
moves = ["F", "B", "R", "L"]
tabla = {Floppy()}
frontera = [Floppy()]
depth = 0

while frontera:
    nuevos = []

    for floppy in frontera:
        for m in moves:
            nuevo = Floppy(floppy.scramble)
            nuevo.move(m)

            if nuevo not in tabla:
                tabla.add(nuevo)
                nuevos.append(nuevo)

    if not nuevos:
        print(f"Max scramble length: {depth}")
        print(f"Number of scrambles: {len(tabla)}")
        break

    frontera = nuevos
    depth += 1

# Sacar la solución más corta
def solve(scramble):
    scramble = scramble.split()
    objetivo = Floppy(scramble)
    for floppy in tabla:
        if floppy == objetivo:
            print(" ".join(floppy.scramble[::-1])) # Le damos la vuelta para conseguir la solución

def show(scramble):
    scramble = scramble.split()
    objetivo = Floppy(scramble)
    for floppy in tabla:
        if floppy == objetivo:
            print(floppy)

solve("R B R L")
show("R B R L")
