class Floppy:
    def __init__(self, scramble = []):
        # Van por la forma de escribir (de izquierda a derecha, y de arriba a abajo) si miras esa cara de frente
        self.U = [0]*25 # White
        self.D = [1]*25 # Yellow
        # Van de izquierda a derecha si miras esa cara de frente
        self.F = [2]*5 # Green
        self.B = [3]*5 # Blue
        self.R = [4]*5 # Red
        self.L = [5]*5 # Orange

        self.scramble = bytearray()
        for i in scramble:
            self.move(i)

    def __eq__(self, other):
        # Solo mirando U, F, R, B y L se puede saber si el cubo esta igual o no
        if self.U != other.U:
            return False
        elif self.F != other.F:
            return False
        elif self.B != other.B:
            return False
        elif self.R != other.R:
            return False
        elif self.L != other.L:
            return False
        return True

    def move(self, move):
        self.scramble.append(move)
        
        if move == 0 or move == 4: # 0 = F; 4 = Fw
            self.F = self.F[::-1]
            self.R[0], self.L[4] = self.L[4], self.R[0]
            self.U[20:25], self.D[0:5] = self.D[0:5][::-1], self.U[20:25][::-1]
        elif move == 1 or move == 5: # 1 = B; 5 = Bw
            self.B = self.B[::-1]
            self.R[4], self.L[0] = self.L[0], self.R[4]
            self.U[0:5], self.D[20:25] = self.D[20:25][::-1], self.U[0:5][::-1]
        elif move == 2 or move == 6: # 2 = R; 6 = Rw
            self.R = self.R[::-1]
            self.F[4], self.B[0] = self.B[0], self.F[4]
            for i in (4, 9, 14, 19, 24):
                self.U[i], self.D[i] = self.D[i], self.U[i]
        elif move == 3 or move == 7: # 3 = L; 7 = Lw
            self.L = self.L[::-1]
            self.F[0], self.B[4] = self.B[4], self.F[0]
            for i in (0, 5, 10, 15, 20):
                self.U[i], self.D[i] = self.D[i], self.U[i]
        if move == 4: # 4 = Fw
            self.R[1], self.L[3] = self.L[3], self.R[1]
            self.U[15:20], self.D[5:10] = self.D[5:10][::-1], self.U[15:20][::-1]
        elif move == 5: # 5 = Bw
            self.R[3], self.L[1] = self.L[1], self.R[3]
            self.U[5:10], self.D[15:20] = self.D[15:20][::-1], self.U[5:10][::-1]
        elif move == 6: # 6 = Rw
            self.F[3], self.B[1] = self.B[1], self.F[3]
            for i in (3, 8, 13, 18, 23):
                self.U[i], self.D[i] = self.D[i], self.U[i]
        elif move == 7: # 7 = Lw
            self.F[1], self.B[3] = self.B[3], self.F[1]
            for i in (1, 6, 11, 16, 21):
                self.U[i], self.D[i] = self.D[i], self.U[i]

    def __str__(self):
        return str(self.U) + str(self.F) + str(self.R)

    def __len__(self):
        return len(self.scramble)

    def __hash__(self):
        return hash(tuple(self.U + self.F + self.R + self.L + self.B))

def num_let(scramble):
    trans = {0:"F", 1:"B", 2:"R", 3:"L", 4:"Fw", 5:"Bw", 6:"Rw", 7:"Lw"}
    ans = []
    for i in scramble:
        ans.append(trans[i])
    return ans

def let_num(scramble):
    trans = {"F":0, "B":1, "R":2, "L":3, "Fw":4, "Bw":5, "Rw":6, "Lw":7}
    ans = []
    for i in scramble:
        ans.append(trans[i])
    return ans

# Codigo para generar todos los floppys
tabla = {Floppy()}
frontera = [Floppy()]
depth = 0

while frontera:
    nuevos = []

    for floppy in frontera:
        for m in range(8): # moves = (0, 1, 2, 3, 4, 5, 6, 7)
            nuevo = Floppy(floppy.scramble)
            nuevo.move(m)

            if nuevo not in tabla:
                tabla.add(nuevo)
                nuevos.append(nuevo)
                # Imprimir el porcentaje que lleva
                if len(tabla)%265_420 == 0:
                    print(f"Computed {int(100*len(tabla)/2_654_208)+1}%")

    if not nuevos:
        print(f"Max scramble length: {depth}")
        print(f"Number of scrambles: {len(tabla)}")
        break 

    frontera = nuevos
    depth += 1

# Sacar la solución más corta
def solve(scramble):
    scramble = let_num(scramble.split())
    objetivo = Floppy(scramble)
    for floppy in tabla:
        if floppy == objetivo:
            print(" ".join(num_let(floppy.scramble[::-1])))

def show(scramble):
    scramble = let_num(scramble.split())
    objetivo = Floppy(scramble)
    for floppy in tabla:
        if floppy == objetivo:
            print(floppy)

solve("Rw Bw F R L")
show("Rw Bw F R L")
