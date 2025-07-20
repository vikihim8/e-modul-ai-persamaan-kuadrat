import streamlit as st
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup spreadsheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("18g9_lCQQDjyU85TJpBUZRzJIrFmrVPeCnjNg4DqrPx8").sheet1

def simpan_ke_sheet(nama, kelas, pertemuan, skor, jawaban, refleksi):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([nama, kelas, pertemuan, skor, jawaban, refleksi, waktu])

st.set_page_config(page_title="Pertemuan 2", layout="centered")

st.title("📘 Pertemuan 3: Menyelesaikan Persamaan Kuadrat dengan Rumus ABC")

# Identitas
st.subheader("👤 Identitas")
nama = st.text_input("Nama Siswa:")
kelas = st.text_input("Kelas:")


# Langkah 1: Stimulus (Self-construction)
st.subheader("🔹 Langkah 1: Stimulus (Self-construction)")
st.markdown("Salin prompt di bawah ini ke Gemini AI dan **pelajari jawabannya**.")
st.code("Jelaskan bagaimana rumus ABC dapat digunakan untuk menyelesaikan persamaan kuadrat.")
st.markdown("[🔎 Cek AI di Gemini](https://gemini.google.com/app)")
jawaban1 = st.text_area("📥 Tuliskan ringkasan pemahamanmu dari jawaban Gemini AI:")
if jawaban1.strip():
    st.success("✅ Jawaban diterima. Sekarang kamu dapat melanjutkan ke langkah berikutnya.")

# Langkah 2: Identifikasi Masalah (Self-instruction)
st.subheader("🔹 Langkah 2: Identifikasi Masalah")
st.markdown("Apa yang terjadi jika sebuah persamaan kuadrat tidak dapat difaktorkan? Bagaimana kamu dapat menemukan akarnya?")
jawaban2 = st.text_area("📥 Tuliskan identifikasimu:")
if jawaban2.strip():
    st.success("✅ Bagus. Ayo lanjut ke langkah berikutnya.")

# Langkah 3: Pengumpulan Data (Modeling)
st.subheader("🔹 Langkah 3: Pengumpulan Data")
st.markdown(r"""
### 📘 Materi: Rumus ABC

Persamaan kuadrat memiliki bentuk umum:
ax² + bx + c = 0

Untuk menyelesaikannya, kita gunakan **rumus ABC**:
$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

Keterangan:
- a, b, c adalah koefisien dari persamaan kuadrat
- D = b² - 4ac   disebut **diskriminan**, menentukan jumlah dan jenis akar
""")

contoh = st.text_input("Masukkan persamaan kuadratmu (contoh: x² - 5x + 6):")
analisis = st.text_area("📥 Tuliskan cara menyelesaikannya dengan rumus ABC, termasuk nilai diskriminan dan akarnya:")

if analisis.strip():
    with st.expander("🤖 Cek AI untuk Rumus ABC"):
        st.markdown("Salin prompt ini ke Gemini AI:")
        st.code(f"Selesaikan persamaan kuadrat {contoh} menggunakan rumus ABC. Jelaskan langkah-langkahnya.")
        st.markdown("[🔎 Cek AI di Gemini](https://gemini.google.com/app)")
        st.markdown("Bandingkan hasilnya dengan analisismu.")

st.subheader("🔹 Langkah 4: Pengolahan Data (Interactive)")
st.markdown(r"""
Misalnya kamu diberikan persamaan kuadrat berikut:  
x² - 4x - 5 = 0

Lakukan analisis terhadap soal tersebut:  
- Apa bentuk umum dari persamaan kuadrat tersebut?  
- Apakah kamu bisa mencari akar-akar dari persamaan itu?  
- Tentukan akar-akarnya berdasarkan rumus ABC.

Tuliskan hasil analisismu di bawah ini:
""")

analisis_l4 = st.text_area("📥 Tuliskan hasil penyelesaian akar-akar dari soal tersebut:")
if analisis_l4:
    st.session_state.analisis_l4 = analisis_l4

# Visualisasi Grafik
import matplotlib.pyplot as plt
import numpy as np

# Definisikan fungsi kuadrat
def f(x):
    return x**2 - 4*x - 5

x_vals = np.linspace(-5, 9, 400)
y_vals = f(x_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label=r"$y = x^2 - 4x - 5$")
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_title("Grafik Persamaan Kuadrat")
ax.legend()
st.pyplot(fig)


st.subheader("🔹 Langkah 5: Verifikasi")
st.markdown("❗ *Selesaikan Langkah 4 terlebih dahulu sebelum melakukan verifikasi.*")

# Cek apakah siswa sudah menjawab Langkah 4
if "analisis_l4" in st.session_state and st.session_state.analisis_l4.strip() != "":
    with st.expander("🤖 Cek AI untuk Verifikasi Jawaban"):
        st.markdown("""
Salin dan tempelkan prompt berikut ke Gemini AI (atau AI lainnya):  
""")
        st.code("""
Jelaskan cara menyelesaikan persamaan kuadrat berikut dengan metode rumus ABC:
x^2 - 4x - 5 = 0
Bandingkan hasilnya dengan jawaban saya.
""")
        st.markdown("[🔎 Cek AI di Gemini](https://gemini.google.com/app)")
        st.markdown("🟩 Setelah membaca hasil dari Gemini AI, isilah bagian berikut:")

        kesesuaian = st.selectbox("Bagaimana tingkat kesesuaian jawabanmu dengan penjelasan AI?", ["Semua sama", "Sebagian sama", "Tidak sama sekali"])

        refleksi = st.text_area("📥 Apa yang kamu pelajari dari perbandingan tersebut?")

        st.session_state.verifikasi_kesesuaian = kesesuaian
        st.session_state.verifikasi_refleksi = refleksi
else:
    st.info("⛔ Silakan isi jawaban di Langkah 4 terlebih dahulu.")


# Langkah 6: Kesimpulan
st.subheader("🔹 Langkah 6: Kesimpulan")
kesimpulan = st.text_area("📝 Tuliskan simpulanmu tentang bagaimana rumus ABC digunakan untuk menyelesaikan persamaan kuadrat:")

if kesimpulan:
    with st.expander("🤖 Cek AI untuk Validasi Kesimpulan"):
        st.markdown("Salin prompt ini ke Gemini AI:")
        st.code("Jelaskan simpulan tentang bagaimana rumus ABC digunakan untuk menyelesaikan persamaan kuadrat.")
        st.markdown("[🔎 Cek AI di Gemini](https://gemini.google.com/app)")

# Refleksi akhir
st.subheader("🔹 Refleksi")
refleksi = st.text_area("💬 Apa yang kamu pelajari secara umum dari pertemuan ini? (Refleksi Akhir)")

# Kirim ke Spreadsheet
if st.button("📤 Kirim Jawaban"):
    if nama and kelas:
        semua_jawaban = f"Langkah 1: {jawaban1} | Langkah 2: {jawaban2} | Langkah 3: {analisis} | Langkah 4: {analisis_l4} | Verifikasi: {kesesuaian}{refleksi} | Kesimpulan: {kesimpulan}"
        refleksi_akhir = refleksi or st.session_state.get("verifikasi_refleksi", "")
        simpan_ke_sheet(nama, kelas, "Pertemuan 3", "-", semua_jawaban, refleksi_akhir)
        st.success("✅ Jawaban berhasil dikirim ke spreadsheet!")
    else:
        st.warning("❗ Nama dan Kelas wajib diisi.")

# Navigasi
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ Pertemuan 2"):
        st.switch_page("pages/4_Pertemuan_2.py")
with col2:
    if st.button("🏠 Daftar Isi"):
        st.switch_page("pages/0_Daftar_Isi.py")
with col3:
    if st.button("➡️ Pertemuan 4"):
        st.switch_page("pages/6_Pertemuan_4.py")

