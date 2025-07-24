import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
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

# filename: pertemuan_1_fungsi_kuadrat.py

import streamlit as st
from PIL import Image

# Judul modul
st.title("Pertemuan 1: Menemukan Konsep Fungsi Kuadrat dari Lintasan Bola")

# 1. Pemberian Rangsangan
st.header("1. Pemberian Rangsangan")
st.write("""
Bayangkan kamu sedang bermain basket. Kamu melempar bola ke arah ring. Bola akan membentuk lintasan yang melengkung.
Bagaimana kamu bisa mengetahui tinggi maksimum bola?
""")
bola_image = Image.open("images/lintasan_bola.jpg")  # Pastikan gambar ini ada di folder 'images'
st.image(bola_image, caption="Lintasan Bola dalam Permainan Basket")

st.write("Tuliskan hal-hal menarik atau membingungkan dari situasi di atas.")
stimulus_reflection = st.text_area("Apa yang menarik dan membingungkan dari gambar dan cerita di atas?")

# 2. Identifikasi Masalah
st.header("2. Identifikasi Masalah")
st.write("Tuliskan masalah atau pertanyaan yang muncul berdasarkan situasi tersebut.")
problem_statement = st.text_area("Apa masalah atau pertanyaan yang ingin kamu selesaikan?")

if problem_statement.strip() != "":
    st.success("Kamu dapat mengeksplorasi masalah ini menggunakan Perplexity.")
    st.markdown("[Klik untuk Buka Perplexity](https://www.perplexity.ai)")

# 3. Pengumpulan Data
st.header("3. Pengumpulan Data")
st.write("Jawablah pertanyaan berikut secara mandiri.")

q1 = st.text_input("Apa bentuk umum fungsi kuadrat?")
q2 = st.text_input("Apa yang dimaksud dengan sumbu simetri pada grafik fungsi kuadrat?")
q3 = st.text_input("Apa peran nilai a dalam bentuk umum fungsi kuadrat?")

if all([q1.strip(), q2.strip(), q3.strip()]):
    st.success("Jawaban terkumpul. Kamu sekarang bisa menggunakan Perplexity untuk eksplorasi lanjutan.")
    st.markdown("[Gunakan Perplexity untuk Belajar Tambahan](https://www.perplexity.ai)")

# 4. Pengolahan Data
elif tahap == "4. Pengolahan Data":
    st.subheader("🧮 Pengolahan Data")
    st.markdown("Silakan analisis informasi yang telah kamu kumpulkan sebelumnya.")
    
    st.write("1. Dari tabel nilai berikut, susun persamaan kuadratnya:")
    st.table({
        "x": [-2, -1, 0, 1, 2],
        "y": [4, 1, 0, 1, 4]
    })
    jawaban_analisis = st.text_area("Tulis bentuk persamaan kuadrat berdasarkan data di atas", key="analisis")
    
    if jawaban_analisis.strip():
        st.success("✅ Jawaban kamu telah dicatat.")
        if st.button("Lihat materi tambahan dari AI (Perplexity)"):
            st.info("🔍 Contoh penyusunan persamaan kuadrat: Gunakan bentuk umum y = ax² + bx + c. Substitusi titik-titik untuk membentuk sistem persamaan.")
    else:
        st.warning("Silakan isi jawaban terlebih dahulu sebelum melihat materi AI.")

# 5. Pembuktian
st.header("5. Pembuktian")
st.write("Kerjakan soal ini: Diketahui grafik fungsi kuadrat memiliki titik puncak (2, 4) dan melalui titik (0, 0). Tentukan persamaan fungsi kuadratnya.")

proof_jawab = st.text_input("Tulis jawabanmu di sini")

if jawaban_bukti.strip():
        st.success("✅ Jawaban kamu telah disimpan.")
        if st.button("Buka Perplexity untuk klarifikasi atau refleksi mandiri"):
            st.info("✏️ Ingat: gunakan rumus puncak = -b/2a, dan rumus diskriminan untuk menyelesaikan akar.")
    else:
        st.warning("Silakan isi jawaban terlebih dahulu sebelum membuka referensi AI.")
        
# 6. Penarikan Kesimpulan
st.header("6. Penarikan Kesimpulan")
kesimpulan = st.text_area("Apa kesimpulan yang kamu dapatkan tentang fungsi kuadrat dari aktivitas ini?")

 if kesimpulan.strip():
        st.success("✅ Kesimpulan kamu tercatat.")
        if st.button("Lihat rangkuman AI setelah menuliskan kesimpulan"):
            st.info("📘 Contoh Kesimpulan:\nFungsi kuadrat berbentuk y = ax² + bx + c membentuk grafik parabola. Titik puncak ditentukan oleh -b/2a dan arah parabola tergantung tanda koefisien a.")
    else:
        st.warning("Silakan tulis kesimpulanmu dahulu.")

# Refleksi
st.subheader("Refleksi Belajar")
refleksi = st.radio("Seberapa yakin kamu memahami materi fungsi kuadrat?", ("Tidak yakin", "Kurang yakin", "Cukup yakin", "Yakin", "Sangat yakin"))

kuis = st.radio("Fungsi kuadrat berbentuk y = ax² + bx + c. Jika a > 0, grafiknya berbentuk?", 
                ("Melingkar", "Parabola terbuka ke atas", "Parabola terbuka ke bawah", "Garis lurus"))

if kuis == "Parabola terbuka ke atas":
    st.success("Jawaban benar!")
elif kuis != "":
    st.error("Jawaban belum tepat. Coba pelajari lagi grafik fungsi kuadrat.")
 ini? (Refleksi Akhir)")

# Simpan hasil ke spreadsheet (simulasi local)
if st.button("📤 Kirim Jawaban"):
    if nama and kelas:
        # Simpan lokal (opsional, jika masih ingin simpan ke file .txt)
        with open("hasil_pertemuan_1.txt", "a", encoding="utf-8") as f:
            waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n---\nWaktu: {waktu}\nNama: {nama}\nKelas: {kelas}\nStimulus: {jawaban1}\nIdentifikasi: {jawaban2}\nAnalisis: {analisis}\nVerifikasi: {verifikasi}\nCocok AI: {cek}\nKesimpulan: {kesimpulan}\n")

        # Gabungkan semua jawaban menjadi satu string jika perlu
        semua_jawaban = f"Stimulus: {jawaban1} | Identifikasi: {jawaban2} | Analisis: {analisis} | Verifikasi: {verifikasi} | Cocok AI: {cek} | Kesimpulan: {kesimpulan}"

        # Kirim ke Google Sheet
        simpan_ke_sheet(nama, kelas, "Pertemuan 1", "-", semua_jawaban, refleksi)

        st.success("✅ Jawaban berhasil dikirim ke spreadsheet dan disimpan lokal!")
    else:
        st.warning("❗ Nama dan Kelas wajib diisi.")

# Navigasi
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ Capaian Pembelajaran"):
        st.switch_page("pages/2_Capaian_Pembelajaran.py")
with col2:
    if st.button("🏠 Daftar Isi"):
        st.switch_page("pages/0_Daftar_Isi.py")
with col3:
    if st.button("➡️ Pertemuan 2"):
        st.switch_page("pages/4_Pertemuan_2.py")
