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

# 1. STIMULUS
st.header("1️. Stimulus")
st.markdown("""
Rumus ABC digunakan untuk menyelesaikan semua bentuk persamaan kuadrat, bahkan yang tidak bisa difaktorkan.

Bentuk umum persamaan kuadrat:
""")
st.latex(r"ax^2 + bx + c = 0")
st.markdown("Masukkan nilai a, b, dan c untuk melihat hasil penyelesaiannya:")

a = st.number_input("Nilai a", format="%.2f")
b = st.number_input("Nilai b", format="%.2f")
c = st.number_input("Nilai c", format="%.2f")

jawaban1, jawaban2, analisis, analisis_l4, kesesuaian, kesimpulan = "", "", "", "", "", ""

if a != 0:
    persamaan = a*x**2 + b*x + c
    D = b**2 - 4*a*c
    akar1 = (-b + sp.sqrt(D)) / (2*a)
    akar2 = (-b - sp.sqrt(D)) / (2*a)

    st.success("Persamaan Kuadrat yang Dibentuk:")
    st.latex(sp.Eq(persamaan, 0))

    st.markdown("Rumus ABC:")
    st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
    st.markdown(f"Diskriminan D = {D}")

    st.markdown("Hasil akar-akarnya:")
    st.latex(sp.Eq(x, akar1))
    st.latex(sp.Eq(x, akar2))

    # 2. IDENTIFIKASI MASALAH
    st.header("2️. Identifikasi Masalah")
    jawaban2 = st.text_area("❓ Jenis akar apa yang kamu dapatkan dari nilai D di atas?")

    # 3. PENGUMPULAN DATA
    st.header("3️. Pengumpulan Data")
    jawaban_siswa = st.text_area("✍️ Tulis langkah-langkah penyelesaian versimu:")

    # 4. PENGOLAHAN DATA
    if jawaban_siswa.strip():
        analisis = jawaban_siswa
        st.header("4️. Pengolahan Data")
        st.markdown("Bandingkan jawabanmu dengan bantuan AI berikut:")
        st.markdown("🔎 [Cek di Gemini AI](https://gemini.google.com/)")

    # 5. GENERALISASI
    st.header("5️. Generalisasi")
    st.markdown("""
    Dari kegiatan ini, kamu dapat menyimpulkan bahwa:
    - Rumus ABC selalu bisa digunakan untuk menyelesaikan persamaan kuadrat apa pun.
    - Jenis akar ditentukan oleh nilai diskriminan:
        - D > 0 → dua akar real berbeda  
        - D = 0 → satu akar real (kembar)  
        - D < 0 → dua akar kompleks (tidak real)
    """)

    # 6. PENARIKAN KESIMPULAN
    st.header("6️. Penarikan Kesimpulan")
    kesimpulan = st.text_area("🧠 Apa kelebihan dan kekurangan dari rumus ABC dibanding cara lain?")
else:
    st.warning("Nilai a tidak boleh nol. Karena bukan persamaan kuadrat.")

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
