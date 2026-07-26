class Floppy:
    def __init__(self, scramble = []):
        # Van por la forma de escribir (de izquierda a derecha, y de aarriba a abajo) si miras esa cara de frente
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
        if self.U == other.U and self.F == other.F and self.B == other.B and self.R == other.R and self.L == other.L:
            return True
                        
        # Esto es para mirar si es la misma mezcla pero con una rotación y2
        elif self.U == other.U[::-1] and self.F == other.B and self.B == other.F and self.R == other.L and self.L == other.R:
            return True

        # Esto es para mirar si es la misma mezcla pero con una rotación x2
        elif self.U == other.D and self.F == other.B[::-1] and self.B == other.F[::-1] and self.R == other.R[::-1] and self.L == other.L[::-1]:
            return True

        # Esto es para mirar si es la misma mezcla pero con una rotación z2
        elif self.U == other.D[::-1] and self.F == other.F[::-1] and self.B == other.B[::-1] and self.R == other.L[::-1] and self.L == other.R[::-1]:
            return True

        return False

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
        if move == 4 or move == 8 or move == 12 or move == 19: # 4 = Fw; 8 = f; 12 = fs; 19 = S
            self.R[1], self.L[3] = self.L[3], self.R[1]
            self.U[15:20], self.D[5:10] = self.D[5:10][::-1], self.U[15:20][::-1]
        if move == 5 or move == 9 or move == 13 or move == 19: # 5 = Bw; 9 = b; 13 = bs; 19 = S
            self.R[3], self.L[1] = self.L[1], self.R[3]
            self.U[5:10], self.D[15:20] = self.D[15:20][::-1], self.U[5:10][::-1]
        if move == 6 or move == 10 or move == 14 or move == 17: # 6 = Rw; 10 = r; 14 = rm; 17 = M
            self.F[3], self.B[1] = self.B[1], self.F[3]
            for i in (3, 8, 13, 18, 23):
                self.U[i], self.D[i] = self.D[i], self.U[i]
        if move == 7 or move == 11 or move == 15 or move == 17: # 7 = Lw; 11 = l; 15 = lm; 17 = M
            self.F[1], self.B[3] = self.B[3], self.F[1]
            for i in (1, 6, 11, 16, 21):
                self.U[i], self.D[i] = self.D[i], self.U[i]
        if move == 14 or move == 15 or move == 16 or move == 17: # 14 = rm; 15 = lm; 16 = m; 17 = M
            self.F[2], self.B[2] = self.B[2], self.F[2]
            for i in (2, 7, 12, 17, 22):
                self.U[i], self.D[i] = self.D[i], self.U[i]
        elif move == 12 or move == 13 or move == 18 or move == 19: # 12 = fs; 13 = bs; 18 = s; 19 = S
            self.R[2], self.L[2] = self.L[2], self.R[2]
            self.U[10:15], self.D[10:15] = self.D[10:15][::-1], self.U[10:15][::-1]
        

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

def num_let(scramble):
    trans = {0:"F", 1:"B", 2:"R", 3:"L", 4:"Fw", 5:"Bw", 6:"Rw", 7:"Lw", 8:"f", 9:"b", 10:"r", 11:"l", 12:"fs", 13:"bs", 14:"rm", 15:"lm", 16:"m", 17:"M", 18:"s", 19:"S"}
    ans = []
    for i in scramble:
        ans.append(trans[i])
    return ans

def let_num(scramble):
    trans = {"F":0, "B":1, "R":2, "L":3, "Fw":4, "Bw":5, "Rw":6, "Lw":7, "f":8, "b":9, "r":10, "l":11, "fs":12, "bs":13, "rm":14, "lm":15, "m":16, "M":17, "s":18, "S":19}
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
        for m in range(20):
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
