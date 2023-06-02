import tkinter as tk
from tkinter import messagebox

class TiketPesawat(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Pemesanan Tiket Pesawat")
        self.geometry("400x300")
        self.configure(bg="#212121")  # Warna latar belakang tema dark

        self.pages = {
            "page1": self.create_page1,
            "page2": self.create_page2,
            "page3": self.create_page3,
            "page4": self.create_page4
        }
        self.current_page = None

        self.name = tk.StringVar()
        self.age = tk.StringVar()
        self.destination = tk.StringVar()
        self.selected_seats = []

        self.widget()

    def widget(self):
        label = tk.Label(self, text="Selamat Datang", font=("Helvetica", 16), fg="white", bg="#212121")
        label.pack(pady=20)

        self.show_page("page1")

    def show_page(self, page):  # biar bisa next and back
        if self.current_page:
            self.current_page.destroy()

        self.current_page = self.pages[page]()
        self.current_page.pack()

    def create_page1(self):
        page1 = tk.Frame(self, bg="#212121")

        label_name = tk.Label(page1, text="Nama:", font=("Helvetica", 12), fg="white", bg="#212121")
        label_name.pack(pady=10)

        entry_name = tk.Entry(page1, textvariable=self.name, font=("Helvetica", 12))
        entry_name.pack()

        label_age = tk.Label(page1, text="Umur:", font=("Helvetica", 12), fg="white", bg="#212121")
        label_age.pack(pady=10)

        entry_age = tk.Entry(page1, textvariable=self.age, font=("Helvetica", 12))
        entry_age.pack()

        label_dest = tk.Label(page1, text="Tujuan:", font=("Helvetica", 12), fg="white", bg="#212121")
        label_dest.pack(pady=10)

        entry_dest = tk.Entry(page1, textvariable=self.destination, font=("Helvetica", 12))
        entry_dest.pack()

        next_button = tk.Button(page1, text="Selanjutnya", font=("Helvetica", 12), command=self.validasi)
        next_button.pack(pady=20)

        return page1

    def validasi(self):
        name = self.name.get()
        age = self.age.get()
        destination = self.destination.get()

        if name.strip() == "":
            messagebox.showerror("Kesalahan", "Nama harus diisi.")
        elif age.strip() == "":
            messagebox.showerror("Kesalahan", "Umur harus diisi.")
        elif not age.isdigit():
            messagebox.showerror("Kesalahan", "Umur harus berupa angka.")
        elif destination.strip() == "":
            messagebox.showerror("Kesalahan", "Tujuan harus diisi.")
        else:
            self.show_page("page2")

    def create_page2(self):
        page2 = tk.Frame(self, bg="#212121")

        label_seat = tk.Label(page2, text="Pilih Kursi (Maksimal 2):", font=("Helvetica", 12), fg="white", bg="#212121")
        label_seat.pack(pady=10)

        seat_frame = tk.Frame(page2, bg="#212121")
        seat_frame.pack()

        # Daftar kursi yang tersedia
        seats = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

        def select_seat(seat):
            if seat in self.selected_seats:
                self.selected_seats.remove(seat)
            else:
                if len(self.selected_seats) < 2:
                    self.selected_seats.append(seat)
                else:
                    messagebox.showerror("Kesalahan", "Anda hanya dapat memesan maksimal 2 kursi.")

        for seat in seats:
            seat_button = tk.Button(seat_frame, text=seat, font=("Helvetica", 10), width=5, pady=5,
                                    command=lambda s=seat: select_seat(s), bg='black', fg='white')
            seat_button.grid(row=int(seats.index(seat) / 3), column=int(seats.index(seat) % 3), padx=5, pady=5)

        back_button = tk.Button(page2, text="Kembali", font=("Helvetica", 12), command=lambda: self.show_page("page1"))
        back_button.pack(pady=20)

        next_button = tk.Button(page2, text="Selanjutnya", font=("Helvetica", 12), command=lambda: self.show_page("page3"))
        next_button.pack()

        return page2

    def create_page3(self):
        page3 = tk.Frame(self, bg="#212121")

        summary_label = tk.Label(page3, text="Rangkuman Pembelian", font=("Helvetica", 16), fg="white", bg="#212121")
        summary_label.pack(pady=10)

        name_label = tk.Label(page3, text="Nama: " + self.name.get(), font=("Helvetica", 12), fg="white", bg="#212121")
        name_label.pack()

        age_label = tk.Label(page3, text="Umur: " + self.age.get(), font=("Helvetica", 12), fg="white", bg="#212121")
        age_label.pack()

        dest_label = tk.Label(page3, text="Tujuan: " + self.destination.get(), font=("Helvetica", 12), fg="white",
                            bg="#212121")
        dest_label.pack()

        seat_label = tk.Label(page3, text="Kursi: " + ", ".join(self.selected_seats), font=("Helvetica", 12),
                            fg="white", bg="#212121")
        seat_label.pack()

        back_button = tk.Button(page3, text="Kembali", font=("Helvetica", 12), command=lambda: self.show_page("page2"))
        back_button.pack(pady=20)

        order_again_button = tk.Button(page3, text="Pesan Kembali", font=("Helvetica", 12),
                                    command=lambda: self.show_page("page1"))
        order_again_button.pack(pady=10)

        finish_button = tk.Button(page3, text="Selesai", font=("Helvetica", 12), command=lambda: self.show_page("page4"))
        finish_button.pack()

        return page3

    def create_page4(self):
        page4 = tk.Frame(self, bg="#212121")

        summary_label = tk.Label(page4, text="Rangkuman Pembelian", font=("Helvetica", 16), fg="white", bg="#212121")
        summary_label.pack(pady=10)

        name_label = tk.Label(page4, text="Nama: " + self.name.get(), font=("Helvetica", 12), fg="white", bg="#212121")
        name_label.pack()

        age_label = tk.Label(page4, text="Umur: " + self.age.get(), font=("Helvetica", 12), fg="white", bg="#212121")
        age_label.pack()

        dest_label = tk.Label(page4, text="Tujuan: " + self.destination.get(), font=("Helvetica", 12), fg="white",
                            bg="#212121")
        dest_label.pack()

        seat_label = tk.Label(page4, text="Kursi: " + ", ".join(self.selected_seats), font=("Helvetica", 12),
                            fg="white", bg="#212121")
        seat_label.pack()

        finish_label = tk.Label(page4, text="Pemesanan berhasil!", font=("Helvetica", 16), fg="white", bg="#212121")
        finish_label.pack(pady=10)

        exit_button = tk.Button(page4, text="Selesai", font=("Helvetica", 12), command=self.keluar)
        exit_button.pack(pady=10)

        return page4

    def keluar(self):
        messagebox.showinfo("Terima Kasih", "Terima kasih telah menggunakan aplikasi pemesanan tiket pesawat.")
        self.destroy()

if __name__ == "__main__":
    app = TiketPesawat()
    app.mainloop()
