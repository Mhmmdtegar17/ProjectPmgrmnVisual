import tkinter as tk

def createName():
    nama = inputNama.get()
    jeniskelamin = inputJenisKelamin.get()
    pekerjaan = inputPekerjaan.get()
    nomortelepon = inputNomorTelepon.get()
    alamat = inputAlamat.get()
    tk.Label(master, text = "Nama       : " + nama).grid(row=6, column=1, sticky=tk.W)
    tk.Label(master, text = "Jenis Kelamin       : " + jeniskelamin).grid(row=7, column=1, sticky=tk.W)
    tk.Label(master, text = "Pekerjaan       : " + pekerjaan).grid(row=8, column=1, sticky=tk.W)
    tk.Label(master, text = "Nomor Telepon      : " + nomortelepon).grid(row=9, column=1, sticky=tk.W)
    tk.Label(master, text = "Alamat      : " + alamat).grid(row=10, column=1, sticky=tk.W)


master = tk.Tk()
master.title("Buku Tamu Perpustakaan")
master.geometry("500x500")

inputNama = tk.Entry(master)
inputJenisKelamin = tk.Entry(master)
inputPekerjaan = tk.Entry(master)
inputNomorTelepon = tk.Entry(master)
inputAlamat = tk.Entry(master)

tk.Label(master, text = "Nama                        : ").grid(row=0, column=0)
inputNama.grid(row=0, column=1)
tk.Label(master, text = "Jenis Kelamin           : ").grid(row=1, column=0)
inputJenisKelamin.grid(row=1, column=1)
tk.Label(master, text = "Pekerjaan                 : ").grid(row=2, column=0)
inputPekerjaan.grid(row=2, column=1)
tk.Label(master, text = "Nomor Telepon      : ").grid(row=3, column=0)
inputNomorTelepon.grid(row=3, column=1)
tk.Label(master, text = "Alamat                     : ").grid(row=4, column=0)
inputAlamat.grid(row=4, column=1)

tk.Button(master, text = "Input").grid(row=4, column=3)

tk.mainloop()
