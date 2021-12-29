from tkinter import*
from openpyxl import Workbook
from openpyxl.styles import Font,Alignment,Border,Side, alignment
from tkinter import font as tkfont

root = Tk()
root.title("Buku Tamu Perpustakaan")
root.resizable(width=False,height=False)
workbook = Workbook()
sheet = workbook.active

styling = tkfont.Font(family='Heltevica',weight='bold',size=15)
styling2 = tkfont.Font(family='Heltevica',size=9)

font = Font(bold=True)
border = Border(left=Side(border_style='thin', color='000000'),
                right=Side(border_style='thin', color='000000'),
                top=Side(border_style='thin', color='000000'),
                bottom=Side(border_style='thin', color='000000'))

alignment = Alignment(horizontal='center',vertical='center')                



HEIGT = 500
WIDTH = 600
canvas = Canvas(root, height=HEIGT, width=WIDTH, bg='salmon')
canvas.pack()

sheet['A1'] = "Acara"
A1 = sheet['A1']
A1.font = font
sheet['A2'] = "Tanggal"
A2 = sheet['A2']
A2.font = font

sheet['A3'] = "No"
A3 = sheet['A3']
A3.font = font
A3.border = border
A3.alignment = alignment

sheet['B3'] = "Nama"
B3 = sheet['B3']
B3.font = font
B3.border = border
B3.alignment = alignment

sheet['C3'] = "Jenis Kelamin"
C3 = sheet['C3']
C3.font = font
C3.border = border
C3.alignment = alignment

sheet['D3'] = "Pekerjaan"
D3 = sheet['D3']
D3.font = font
D3.border = border
D3.alignment = alignment

sheet['E3'] = "Alamat"
E3 = sheet['E3']
E3.font = font
E3.border = border
E3.alignment = alignment


num = 0

def InsertData():
    global num
    num = num + 1
    sheetnum = num + 3

    sheet['A'+str(sheetnum)] = num
    DataNo = sheet['A'+str(sheetnum)]
    DataNo.border = border
    DataNo.alignment = alignment

    sheet['B'+str(sheetnum)] = namaEntry.get()
    DataNama = sheet['B'+str(sheetnum)]
    DataNama.border = border
    DataNama.alignment = alignment

    sheet['C'+str(sheetnum)] = jeniskelaminEntry.get()
    DataJenisKelamin = sheet['C'+str(sheetnum)]
    DataJenisKelamin.border = border
    DataJenisKelamin.alignment = alignment

    sheet['D'+str(sheetnum)] = pekerjaanEntry.get()
    DataPekerjaan = sheet['D'+str(sheetnum)]
    DataPekerjaan.border = border
    DataPekerjaan.alignment = alignment

    sheet['E'+str(sheetnum)] = alamatEntry.get()
    DataAlamat= sheet['E'+str(sheetnum)]
    DataAlamat.border = border
    DataAlamat.alignment = alignment

    sheet['B1'] = acaraEntry.get()
    sheet['B2'] = tanggalEntry.get()

    namaEntry.delete(0, END)
    jeniskelaminEntry.delete(0, END)
    pekerjaanEntry.delete(0, END)
    alamatEntry.delete(0, END)


def SaveData():
    global Informasi
    workbook.save(filename=str(acaraEntry.get())+".xlsx")
    Informasi['text'] = "Data telah di save\nNama file : "+str(acaraEntry.get())+".xlsx"


def CreateNewData():
    global Informasi, num
    Informasi['text'] = 'Klik insert untuk semua tamu, klik save jika semua tamu telah hadir.'
    namaEntry.delete(0, END)
    jeniskelaminEntry.delete(0, END)
    pekerjaanEntry.delete(0, END)
    alamatEntry.delete(0, END)
    acaraEntry.delete(0, END)
    tanggalEntry.delete(0, END)
    num = 0


frameJudul = Frame(root, bg='white')
frameJudul.place(rely=0.025,relx=0.5,relheight=0.1,relwidth=0.8,anchor='n')
judul = Label(frameJudul, bg='white', text='-- Guest Book --', font=styling)
judul.place(relheight=1,relwidth=1)

frameAcara = Frame(root, bg='white')
frameAcara.place(rely=0.22,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
acarainfo = Label(frameAcara, bg='white', text='Acara', font=styling2)
acarainfo.place(relwidth=0.5,relheight=1)
acaraEntry = Entry(frameAcara)
acaraEntry.place(relx=0.5,relheight=1,relwidth=0.5)
acaraEntry.get()

frameTanggal = Frame(root, bg='white')
frameTanggal.place(rely=0.29,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
tanggalinfo = Label(frameTanggal, bg='white', text='Tanggal', font=styling2)
tanggalinfo.place(relwidth=0.5,relheight=1)
tanggalEntry = Entry(frameTanggal)
tanggalEntry.place(relx=0.5,relheight=1,relwidth=0.5)
tanggalEntry.get()

frameNama  = Frame(root, bg='white')
frameNama .place(rely=0.36,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
namainfo = Label(frameNama, bg='white', text='Nama', font=styling2)
namainfo.place(relwidth=0.5,relheight=1)
namaEntry = Entry(frameNama)
namaEntry.place(relx=0.5,relheight=1,relwidth=0.5)
namaEntry.get()

frameJenisKelamin = Frame(root, bg='white')
frameJenisKelamin.place(rely=0.43,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
jeniskelamininfo = Label(frameJenisKelamin, bg='white', text='Jenis Kelamin', font=styling2)
jeniskelamininfo.place(relwidth=0.5,relheight=1)
jeniskelaminEntry = Entry(frameJenisKelamin)
jeniskelaminEntry.place(relx=0.5,relheight=1,relwidth=0.5)
jeniskelaminEntry.get()

framePekerjaan = Frame(root, bg='white')
framePekerjaan.place(rely=0.50,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
pekerjaaninfo = Label(framePekerjaan, bg='white', text='Pekerjaan', font=styling2)
pekerjaaninfo.place(relwidth=0.5,relheight=1)
pekerjaanEntry = Entry(framePekerjaan)
pekerjaanEntry.place(relx=0.5,relheight=1,relwidth=0.5)
pekerjaanEntry.get()

frameAlamat = Frame(root, bg='white')
frameAlamat.place(rely=0.57,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
alamatinfo = Label(frameAlamat, bg='white', text='Alamat', font=styling2)
alamatinfo.place(relwidth=0.5,relheight=1)
alamatEntry = Entry(frameAlamat)
alamatEntry.place(relx=0.5,relheight=1,relwidth=0.5)
alamatEntry.get()

Informasi = Label(root, bg='white', font=styling2, text='Klik insert untuk semua tamu, klik save jika semua tamu telah hadir.')
Informasi.place(rely=0.65,relx=0.5,relheight=0.06,relwidth=0.75,anchor='n')

frameButton = Frame(root, bg='white')
frameButton.place(rely=0.78,relx=0.5,relheight=0.2,relwidth=0.2,anchor='n')
insert = Button(frameButton, text='Insert', command=InsertData)
insert.place(rely=0,relx=0.5,relheight=0.25,relwidth=1,anchor='n')
save = Button(frameButton, text='Save', command=SaveData)
save.place(rely=0.25,relx=0.5,relheight=0.25,relwidth=1,anchor='n')
createNewData = Button(frameButton, text='Create New',  command=CreateNewData)
createNewData.place(rely=0.5,relx=0.5,relheight=0.25,relwidth=1,anchor='n')
editData = Button(frameButton, text='Edit Data',  command=[])
editData.place(rely=0.75,relx=0.5,relheight=0.25,relwidth=1,anchor='n')



root.mainloop()
