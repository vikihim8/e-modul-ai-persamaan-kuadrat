import streamlit as st
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Setup Spreadsheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
json_creds = st.secrets["gcp_service_account"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(json_creds, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("18g9_lCQQDjyU85TJpBUZRzJIrFmrVPeCnjNg4DqrPx8").sheet1

def simpan_ke_sheet(nama, kelas, pertemuan, skor, jawaban, refleksi):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([nama, kelas, pertemuan, skor, jawaban, refleksi, waktu])

# Konfigurasi halaman
st.set_page_config(page_title="Latihan dan Refleksi", layout="centered")

# Judul
st.title("📓 Latihan & Refleksi")

st.markdown("Silakan kerjakan latihan berikut dan isikan jawaban serta refleksi belajar berdasarkan pemahamanmu.")

# Identitas
st.subheader("👤 Identitas")
nama = st.text_input("Nama Siswa:")
kelas = st.text_input("Kelas:")

# Soal 1
st.subheader("📝 Latihan")
st.markdown(r"""**1.** Sebuah benda dilemparkan ke atas dan lintasannya dimodelkan oleh fungsi
$$
h(t) = -t^2 + 6t
$$
Tentukan:
""")
st.markdown("- a) Waktu ketika benda mencapai titik tertinggi")
st.markdown("- b) Ketinggian maksimum yang dicapai benda")
latihan1 = st.text_area("📥 Jawaban Soal 1:")

# Soal 2
st.markdown(r"""**2.** Tentukan akar-akar dari persamaan
$$
x^2 - 4x - 5 = 0
$$
menggunakan rumus ABC
""")
latihan2 = st.text_area("📥 Jawaban Soal 2:")

# Soal 3
st.markdown("**3.** Sebuah fungsi kuadrat memiliki akar-akar $$3$$ dan $$-2$$. Tentukan bentuk fungsi kuadrat tersebut.")
latihan3 = st.text_area("📥 Jawaban Soal 3:")

# Refleksi
st.subheader("🪞 Refleksi Belajar")
ref1 = st.text_area("1. Apa pemahaman penting yang kamu dapatkan dari pembelajaran ini?")
ref2 = st.text_area("2. Bagian mana yang paling menantang untukmu?")
ref3 = st.text_area("3. Apa yang akan kamu lakukan untuk meningkatkan pemahamanmu ke depan?")

# Kirim jawaban
if st.button("📤 Kirim Jawaban ke Google Sheets"):
    if nama and kelas:
        jawaban = f"1: {latihan1} | 2: {latihan2} | 3: {latihan3}"
        refleksi = f"Ref1: {ref1} | Ref2: {ref2} | Ref3: {ref3}"
        simpan_ke_sheet(nama, kelas, "Latihan & Refleksi", "", jawaban, refleksi)
        st.success("✅ Jawaban dan refleksi berhasil dikirim!")
    else:
        st.warning("⚠️ Mohon isi nama dan kelas terlebih dahulu.")

# Navigasi
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("⬅️ Pertemuan 4"):
        st.switch_page("pages/6_Pertemuan_4.py")
with col2:
    if st.button("🏠 Daftar Isi"):
        st.switch_page("pages/0_Daftar_Isi.py")
with col3:
    st.empty()
