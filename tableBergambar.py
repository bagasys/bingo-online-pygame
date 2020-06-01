from cellBergambar import CellBergambar

class TabelBergambar:
    def __init__(self):
        self.cell_surfaces = []
        self.generateCellSurfaces(5)
        self.tabel = [None] * 25
        self.angkaTerpilih = None
        self.count_isi = 0
        self.tabelCoret = [False] * 25
        self.tabelPilih = [False] * 25

    def generateCellSurfaces(self, n):
        id = 1
        for row in range(n):
            for column in range(n):
                x = 100 + 80 * column + 5 * column
                y = 100 + 80 * row + 5 * row
                newCell = CellBergambar(id, "", x, y)
                self.cell_surfaces.append(newCell)
                id += 1

    def draw(self, screen):
        idx = 0
        for cell in self.cell_surfaces:
            cell.draw(screen, self.tabel[idx], self.tabelCoret[idx], self.tabelPilih[idx])
            idx += 1

    def coretTabel(self, angka):
        idx = self.tabel.index(angka)
        self.tabelCoret[idx] = True

    def pilihKotak(self, index):
        for i in range(len(self.tabelPilih)):
            if i == index:
                self.tabelPilih[i] = True
                self.angkaTerpilih = self.tabel[i]
            else:
                self.tabelPilih[i] = False

    def pilihKotakByAngka(self, angka):
        idxBaru = self.tabel.index(angka)
        for i in range(len(self.tabelPilih)):
            if i == idxBaru:
                self.tabelPilih[i] = True
                self.angkaTerpilih = self.tabel[i]
            else:
                self.tabelPilih[i] = False

    def isiTabel(self, idx):
        if self.count_isi < 25 and self.tabel[idx] == None:
            self.count_isi += 1
            self.tabel[idx] = self.count_isi
            # print(self.tabel)

    def checkClick(self, titik_klik):
        idx = 0
        for cell in self.cell_surfaces:
            if cell.isClicked(titik_klik):
                return idx
            idx += 1
        return -1

    def reset(self):
        self.tabel = [None] * 25
        self.angkaTerpilih = None
        self.count_isi = 0
        self.tabelCoret = [False] * 25
        self.tabelPilih = [False] * 25
