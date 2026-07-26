class Floppy:
    def __init__(self, scramble = []):
        # Van por la forma de escribir (de izquierda a derecha, y de arriba a abajo) si miras esa cara de frente
        self.U = [0]*16 # White
        self.D = [1]*16 # Yellow
        # Van de izquierda a derecha si miras esa cara de frente
        self.F = [2]*4 # Green
        self.B = [3]*4 # Blue
        self.R = [4]*4 # Red
        self.L = [5]*4 # Orange

        self.scramble = []
        for i in scramble:
            self.move(i)

    def __eq__(self, other):
        # Solo mirando U, F, R, B y L se puede saber si el cubo esta igual o no
        if self.U == other.U and self.F == other.F and self.B == other.B and self.R == other.R and self.L == other.L:
            return True
                        
        # Esto es para mirar si es la misma mezcla pero con una rotación y2 (Ejemplo, caso resuelto)
        elif self.U == other.U[::-1] and self.F == other.B and self.B == other.F and self.R == other.L and self.L == other.R:
            return True

        # Esto es para mirar si es la misma mezcla pero con una rotación x2 (Ejemplo, Fw)
        elif self.U == other.D and self.F == other.B[::-1] and self.B == other.F[::-1] and self.R == other.R[::-1] and self.L == other.L[::-1]:
            return True

        # Esto es para mirar si es la misma mezcla pero con una rotación z2 (Ejemplo, Rw)
        elif self.U == other.D[::-1] and self.F == other.F[::-1] and self.B == other.B[::-1] and self.R == other.L[::-1] and self.L == other.R[::-1]:
            return True

        return False

    def move(self, move):
        self.scramble.append(move)
        
        if move == "F" or move == "Fw":
            self.F = self.F[::-1]
            self.R[0], self.L[3] = self.L[3], self.R[0]
            self.U[12:16], self.D[0:4] = self.D[0:4][::-1], self.U[12:16][::-1]
        elif move == "B":
            self.B = self.B[::-1]
            self.R[3], self.L[0] = self.L[0], self.R[3]
            self.U[0:4], self.D[12:16] = self.D[12:16][::-1], self.U[0:4][::-1]
        elif move == "R" or move == "Rw":
            self.R = self.R[::-1]
            self.F[3], self.B[0] = self.B[0], self.F[3]
            for i in (3, 7, 11, 15):
                self.U[i], self.D[i] = self.D[i], self.U[i]
        elif move == "L":
            self.L = self.L[::-1]
            self.F[0], self.B[3] = self.B[3], self.F[0]
            for i in (0, 4, 8, 12):
                self.U[i], self.D[i] = self.D[i], self.U[i]
        if move == "Fw":
            self.R[1], self.L[2] = self.L[2], self.R[1]
            self.U[8:12], self.D[4:8] = self.D[4:8][::-1], self.U[8:12][::-1]
        elif move == "Rw":
            self.F[2], self.B[1] = self.B[1], self.F[2]
            for i in (2, 6, 10, 14):
                self.U[i], self.D[i] = self.D[i], self.U[i]

    def __str__(self):
        return str(self.U) + str(self.F) + str(self.R)

    def __len__(self):
        return len(self.scramble)

    def __hash__(self):
        # Se coje el minimo para no contar rotaciones
        return hash(min(tuple(self.U + self.F + self.B + self.R + self.L), # Normal
                        tuple(self.U[::-1] + self.B + self.F + self.L + self.R), # Rotación y2
                        tuple(self.D + self.B[::-1] + self.F[::-1] + self.R[::-1] + self.L[::-1]), # Rotación x2
                        tuple(self.D[::-1] + self.F[::-1] + self.B[::-1] + self.L[::-1] + self.R[::-1]))) # Rotación z2

# Codigo para generar todos los floppys
moves = ["F", "B", "R", "L", "Fw", "Rw"]
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
            print(" ".join(floppy.scramble[::-1]))

def show(scramble):
    scramble = scramble.split()
    objetivo = Floppy(scramble)
    for floppy in tabla:
        if floppy == objetivo:
            print(floppy)

solve("Fw F Rw L B F Rw R Fw F")
show("Fw F Rw L B F Rw R Fw F")
