from tkinter import*
from openpyxl import Workbook
from openpyxl.styles import Font,Alignment,Border,Side
from tkinter import font as tkfont

root = Tk()
root.title("Buku Tamu Perpustakaan")
root.resizable(width=False,height=False)
workbook = Workbook()
sheet = workbook.active

styling = tkfont.Font(family='Heltevica',weight='bold',size=15)
styling2 = tkfont.Font(family='Heltevica',size=9)

HEIGT = 500
WIDTH = 600
canvas = Canvas(root, height=HEIGT, width=WIDTH, bg='salmon')
canvas.pack()

frameJudul = Frame(root, bg='white')
frameJudul.place(rely=0.025,relx=0.5,relheight=0.1,relwidth=0.8,anchor='n')
judul = Label(frameJudul, bg='white', text='-- Guest Book --', font=styling)
judul.place(relheight=1,relwidth=1)

frameNama = Frame(root, bg='white')
frameNama.place(rely=0.24,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
namainfo = Label(frameNama, bg='white', text='Nama', font=styling2)
namainfo.place(relwidth=0.5,relheight=1)
namaEntry = Entry(frameNama)
namaEntry.place(relx=0.5,relheight=1,relwidth=0.5)

frameJenisKelamin = Frame(root, bg='white')
frameJenisKelamin.place(rely=0.31,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
jeniskelamininfo = Label(frameJenisKelamin, bg='white', text='Jenis Kelamin', font=styling2)
jeniskelamininfo.place(relwidth=0.5,relheight=1)
jeniskelaminEntry = Entry(frameJenisKelamin)
jeniskelaminEntry.place(relx=0.5,relheight=1,relwidth=0.5)

framePekerjaan = Frame(root, bg='white')
framePekerjaan.place(rely=0.38,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
pekerjaaninfo = Label(framePekerjaan, bg='white', text='Pekerjaan', font=styling2)
pekerjaaninfo.place(relwidth=0.5,relheight=1)
pekerjaanEntry = Entry(framePekerjaan)
pekerjaanEntry.place(relx=0.5,relheight=1,relwidth=0.5)

frameNomorPonsel = Frame(root, bg='white')
frameNomorPonsel.place(rely=0.45,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
nomorponselinfo = Label(frameNomorPonsel, bg='white', text='Nomor Ponsel', font=styling2)
nomorponselinfo.place(relwidth=0.5,relheight=1)
nomorponselEntry = Entry(frameNomorPonsel)
nomorponselEntry.place(relx=0.5,relheight=1,relwidth=0.5)

frameAlamat = Frame(root, bg='white')
frameAlamat.place(rely=0.52,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
alamatinfo = Label(frameAlamat, bg='white', text='Alamat', font=styling2)
alamatinfo.place(relwidth=0.5,relheight=1)
alamatEntry = Entry(frameAlamat)
alamatEntry.place(relx=0.5,relheight=1,relwidth=0.5)

Informasi = Label(root, bg='white')
Informasi.place(rely=0.6,relx=0.5,relheight=0.06,relwidth=0.75,anchor='n')

frameButton = Frame(root, bg='white')
frameButton.place(rely=0.76,relx=0.5,relheight=0.2,relwidth=0.2,anchor='n')
insert = Button(frameButton,text='Insert')
insert.place(rely=0,relx=0.5,relheight=0.25,relwidth=1,anchor='n')
save = Button(frameButton,text='Save')
save.place(rely=0.25,relx=0.5,relheight=0.25,relwidth=1,anchor='n')
createNewData = Button(frameButton,text='Create New')
createNewData.place(rely=0.5,relx=0.5,relheight=0.25,relwidth=1,anchor='n')
Exit = Button(frameButton,text='Exit')
Exit.place(rely=0.75,relx=0.5,relheight=0.25,relwidth=1,anchor='n')

root.mainloop()
