import streamlit as st
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

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

st.title("📘 Pertemuan 3: Menyelesaikan Persamaan Kuadrat")

st.markdown("**Capaian:** Siswa dapat menyelesaikan soal persamaan kuadrat menggunakan metode pemfaktoran dan rumus ABC.")

# --- 1. Stimulus ---
st.header("Stimulus")
st.markdown("Seorang siswa ingin menyelesaikan persamaan kuadrat \( x^2 - 5x + 6 = 0 \). Ia mencoba menggunakan dua cara berbeda: pemfaktoran dan rumus ABC. Yuk, pelajari bagaimana prosesnya dan bandingkan kedua metode ini.")

# --- 2. Identifikasi Masalah ---
st.header("Identifikasi Masalah")
st.markdown("Apa yang perlu dilakukan untuk menyelesaikan persamaan kuadrat \( x^2 - 5x + 6 = 0 \)? Metode apa saja yang dapat digunakan? Apakah keduanya menghasilkan solusi yang sama?")

# --- 3. Eksplorasi ---
st.header("Eksplorasi")
st.markdown("#### ✍️ Eksplorasi 1: Selesaikan dengan Pemfaktoran")
st.latex("x^2 - 5x + 6 = 0")
st.markdown("**Langkah:** Temukan dua bilangan yang hasil kalinya 6 (konstanta \( c \)) dan jumlahnya -5 (koefisien \( b \)).")
st.text_input("Tulis pasangan bilangan yang mungkin:", key="faktor")
st.text_input("Tuliskan bentuk faktornya:", placeholder="Contoh: (x - 2)(x - 3)", key="faktorisasi")

st.markdown("#### ✍️ Eksplorasi 2: Gunakan Rumus ABC")
st.latex("x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
st.markdown("Diketahui \( a = 1, b = -5, c = 6 \)")
st.text_input("Tentukan nilai diskriminan (\( b^2 - 4ac \)):", key="diskriminan")
st.text_input("Hitung akarnya menggunakan rumus ABC:", key="rumus_abc")

# --- 4. Pengolahan Data ---
st.header("Pengolahan Data")
st.markdown("Bandingkan hasil dari kedua metode. Apakah akarnya sama? Tuliskan hasil akarnya di bawah ini.")
st.text_area("📝 Akar dari metode faktorisasi:", key="hasil_faktorisasi")
st.text_area("📝 Akar dari metode rumus ABC:", key="hasil_abc")

# --- 5. Verifikasi ---
st.header("Verifikasi")
st.markdown("#### 🔎 Cek AI")
st.code("Bagaimana cara menyelesaikan persamaan kuadrat x^2 - 5x + 6 = 0 dengan dua metode: pemfaktoran dan rumus ABC?")
st.info("Gunakan jawaban AI sebagai referensi. Bandingkan dengan jawabanmu dan perhatikan perbedaan langkah atau hasil yang ditemukan.")
st.markdown("[🔗 Lihat jawaban AI di Perplexity](https://www.perplexity.ai/search/persamaan-kuadrat-dengan-pemfaktoran-dan-abc-H6DRKHO2RYKW6hZgAVk6eQ)")

# --- 6. Penarikan Kesimpulan ---
st.header("Penarikan Kesimpulan")
st.text_area("🎯 Apa kesimpulanmu dari hasil eksplorasi dua metode tersebut? Manakah yang menurutmu lebih mudah atau lebih cepat?")

# --- Refleksi & Kuis ---
st.subheader("🪞 Refleksi Belajar")
refleksi = st.radio("Seberapa yakin kamu memahami materi penyelesaian persamaan kuadrat dengan rumus abc?", 
                    ["Tidak yakin", "Kurang yakin", "Cukup yakin", "Yakin", "Sangat yakin"])

kuis = st.radio("Jika f(x) = x² - 4x - 5, maka akar-akar dari persamaan tersebut adalah ...", 
                ["x = -5 atau x = 1", "x = 5 atau x = -1", "x = -4 atau x = 5", "x = 4 atau x = 5"])

cek = ""
if kuis:
    if kuis == "x = 5 atau x = -1":
        st.success("✅ Jawaban benar!")
        cek = "Benar"
    else:
        st.error("❌ Jawaban belum tepat.")
        cek = "Salah"

# Kirim ke Spreadsheet
if st.button("📤 Kirim Jawaban"):
    if nama and kelas:
        semua_jawaban = f"Langkah 1: {jawaban1} | Langkah 2: {jawaban2} | Langkah 3: {analisis} | Langkah 4: {analisis_l4} | Verifikasi: {kesesuaian} | Kesimpulan: {kesimpulan}"
        simpan_ke_sheet(nama, kelas, "Pertemuan 3", cek, semua_jawaban, refleksi)
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
