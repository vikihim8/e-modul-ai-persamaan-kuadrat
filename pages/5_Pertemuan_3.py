import streamlit as st
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import sympy as sp

# Setup Spreadsheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
json_creds = st.secrets["gcp_service_account"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(json_creds, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("18g9_lCQQDjyU85TJpBUZRzJIrFmrVPeCnjNg4DqrPx8").sheet1

def simpan_ke_sheet(nama, kelas, pertemuan, skor, jawaban, refleksi):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([nama, kelas, pertemuan, skor, jawaban, refleksi, waktu])

x = sp.Symbol('x')
st.set_page_config(page_title="Pertemuan 3", layout="centered")

st.title("📘 Pertemuan 3: Menyelesaikan Persamaan Kuadrat dengan Rumus ABC")

# Identitas
st.subheader("👤 Identitas")
nama = st.text_input("Nama Siswa:")
kelas = st.text_input("Kelas:")

# Langkah 1: Stimulus
st.header("1️⃣ Stimulus")
st.write("""
Bayangkan kamu sedang bermain game mencari harta karun. Kamu menemukan sebuah peta dengan petunjuk yang ditulis dalam bentuk persamaan kuadrat. Untuk membuka peti, kamu harus menyelesaikan persamaan tersebut. Bagaimana cara kamu menyelesaikannya?
""")

# Langkah 2: Identifikasi Masalah
st.header("2️⃣ Identifikasi Masalah")
st.write("Masalah: Bagaimana cara menyelesaikan persamaan kuadrat ax² + bx + c = 0 dengan menggunakan rumus ABC?")

# Langkah 3: Pengumpulan Data
st.header("3️⃣ Pengumpulan Data")
st.write("Masukkan nilai a, b, dan c dari persamaan kuadrat yang ingin kamu selesaikan:")

a = st.number_input("Masukkan nilai a", step=1.0)
b = st.number_input("Masukkan nilai b", step=1.0)
c = st.number_input("Masukkan nilai c", step=1.0)

# Langkah 4: Pengolahan Data
st.header("4️⃣ Pengolahan Data")
if a != 0:
    st.markdown(f"Persamaan kuadrat: **{a}x² + {b}x + {c} = 0**")

    # Hitung diskriminan
    D = b**2 - 4*a*c
    st.write(f"Diskriminan (D) = {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        st.success(f"Akar-akar real dan berbeda:\nx₁ = {x1:.2f}, x₂ = {x2:.2f}")
    elif D == 0:
        x = -b / (2*a)
        st.info(f"Akar real dan sama:\nx = {x:.2f}")
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(abs(D)) / (2*a)
        st.warning(f"Akar-akar kompleks:\nx₁ = {real_part:.2f} + {imag_part:.2f}i, x₂ = {real_part:.2f} - {imag_part:.2f}i")
else:
    st.error("Nilai a tidak boleh nol (a ≠ 0) dalam persamaan kuadrat.")

# Langkah 5: Verifikasi (Analisis Siswa)
st.header("5️⃣ Verifikasi")
st.write("Tuliskan hasil analisismu berdasarkan langkah-langkah penyelesaian yang kamu lakukan.")
analisis = st.text_area("📝 Jawabanmu di sini")

# Langkah 6: Menarik Kesimpulan dan Cek AI
st.header("6️⃣ Menarik Kesimpulan")
if analisis:
    st.success("Terima kasih! Sekarang kamu bisa mengecek jawabanmu menggunakan AI.")
    st.markdown(
        '[🔍 Cek Jawabanmu di Perplexity](https://www.perplexity.ai/)'
    )
else:
    st.info("Silakan isi analisis terlebih dahulu untuk membuka link cek jawaban AI.")
# Refleksi akhir
st.subheader("🔹 Refleksi")
refleksi = st.text_area("💬 Apa yang kamu pelajari secara umum dari pertemuan ini? (Refleksi Akhir)")

# Kirim ke Spreadsheet
if st.button("📤 Kirim Jawaban"):
    if nama and kelas:
        semua_jawaban = f"Langkah 1: {jawaban1} | Langkah 2: {jawaban2} | Langkah 3: {analisis} | Langkah 4: {analisis_l4} | Verifikasi: {kesesuaian} | Kesimpulan: {kesimpulan}"
        refleksi_akhir = refleksi
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
