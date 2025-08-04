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

st.set_page_config(page_title="Pertemuan 4", layout="centered")

st.title("🧮 Pertemuan 4: Aplikasi Persamaan Kuadrat dalam Kehidupan Sehari-hari")
st.markdown("**Capaian Pembelajaran:** Siswa dapat menyelesaikan masalah kontekstual yang berkaitan dengan persamaan kuadrat dalam kehidupan sehari-hari.")

# Identitas
st.subheader("👤 Identitas Siswa")
nama = st.text_input("Nama:")
kelas = st.text_input("Kelas:")

# Langkah 1: Stimulus
st.header("📌 Stimulus")
st.image("pages/lintasan_bola.png", caption="Contoh lintasan bola (fungsi kuadrat)", use_container_width=True)
st.markdown("**Perhatikan gambar lintasan bola di atas!**")
st.markdown("Bola dilempar ke atas hingga mencapai ketinggian maksimum lalu jatuh kembali ke tanah. Bentuk lintasan bola menyerupai grafik fungsi kuadrat.")
stimulus_input = st.text_input("✍️ Analisis: Apa yang bisa kamu amati dari lintasan bola tersebut?", key="stimulus")

# Langkah 2: Identifikasi Masalah
st.header("🎯 Identifikasi Masalah")
st.markdown("**Dapatkah kamu merumuskan pertanyaan atau masalah dari gambar tersebut?**")
identifikasi_input = st.text_input("✍️ Tulis pertanyaan atau masalah yang kamu identifikasi berdasarkan stimulus", key="identifikasi")


# Langkah 3: Pengumpulan Data
st.header("Pengumpulan Data")
st.markdown("📈 Eksplorasi fungsi kuadrat dalam bentuk umum: `h(t) = t² + vt + h₀`, di mana:")
st.markdown("- `t`: waktu (detik)")
st.markdown("- `v`: kecepatan awal (m/s)")
st.markdown("- `h₀`: tinggi awal (meter)")

# Input pengguna
v = st.number_input("Masukkan kecepatan awal (v) dalam m/s", value=20)
h0 = st.number_input("Masukkan tinggi awal (h₀) dalam meter", value=1)

if st.button("🔍 Hitung Tinggi Maksimum & Waktu Tempuh"):
    import sympy as sp
    t = sp.Symbol('t', real=True, positive=True)
    h = 1 * t**2 + v * t + h0

    # Hitung waktu saat tinggi maksimum (turunan = 0)
    t_max = sp.solve(h.diff(t), t)[0]
    h_max = h.subs(t, t_max)

    # Hitung kapan bola menyentuh tanah (h = 0)
    total_waktu = [sol.evalf() for sol in sp.solve(h, t) if sol.is_real and sol >= 0]

    st.success(f"⏱️ Waktu saat tinggi maksimum: {float(t_max):.2f} detik")
    st.success(f"📏 Tinggi maksimum bola: {float(h_max):.2f} meter")
    
    if total_waktu:
        st.success(f"🕒 Perkiraan bola menyentuh tanah: {float(max(total_waktu)):.2f} detik")
    else:
        st.warning("⚠️ Tidak ditemukan waktu bola menyentuh tanah secara realistis.")


st.markdown("✍️ Apa yang kamu pahami dari hasil perhitungan di atas?")
pengumpulan_input = st.text_area("Tulis pemahamanmu di sini", key="pengumpulan")
if kesimpulan_input.strip():
    with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi"):
        st.info("""
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**
Apa kesimpulan detail materi tentang penerapan fungsi kuadrat dalam kehidupan sehari-hari

📝 **Refleksi:** Setelah kegiatan pada pertemuan ini, tuliskan refleksimu di sini
""")
        st.text_area("Tulis jawaban refleksi pertemuan 4 di sini...", key="refleksi_kesimpulan", height=80)


        
# Langkah 4: Pengolahan Data (Latihan)
st.header("Pengolahan Data")
st.markdown("📝 **Latihan Soal:**\nSeseorang melempar bola dengan kecepatan awal 15 m/s dari atas tebing setinggi 5 meter. Tentukan:")
st.markdown("- Tinggi maksimum bola")
st.markdown("- Waktu untuk mencapai tanah")

pengolahan_input = st.text_area("✍️ Tulis jawabanmu di sini", key="pengolahan")


# Langkah 5: Verifikasi
st.header("Verifikasi")
if pengolahan_input.strip():
    with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi"):
            st.info("""
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapat penjelasan lengkap dan verifikasi terhadap jawabanmu:**

**Prompt:**
Seseorang melempar bola dengan kecepatan awal 15 m/s dari atas tebing setinggi 5 meter. Tentukan: Tinggi maksimum bola dan Waktu untuk mencapai tanah
    """)
        
st.markdown(" **Bandingkan jawabanmu dengan hasil yang ditampilkan AI**")
verifikasi_input = st.text_area("✍️ Apa yang perlu kamu perbaiki atau pertahankan dari jawabanmu?", key="verifikasi")

# Langkah 6: Kesimpulan
st.header("Kesimpulan")
st.markdown("📍 **Tuliskan kesimpulanmu tentang penerapan fungsi kuadrat dalam kehidupan sehari-hari!**")
kesimpulan_input = st.text_area("✍️ Tuliskan kesimpulanmu di sini...", key="kesimpulan")
if kesimpulan_input.strip():
    with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi"):
        st.info("""
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**
Apa kesimpulan detail materi tentang penerapan fungsi kuadrat dalam kehidupan sehari-hari

📝 **Refleksi:** Setelah kegiatan pada pertemuan ini, tuliskan refleksimu di sini
""")
         st.text_area("Tulis jawaban refleksi pertemuan 4 di sini...", key="refleksi_eksplorasip4", height=80)


        
# --- Refleksi Akhir ---
st.subheader("🪞 Refleksi Belajar")
refleksi = st.radio("Seberapa yakin kamu memahami pengolahan data melalui latihan soal fungsi kuadrat?", 
                    ["Tidak yakin", "Kurang yakin", "Cukup yakin", "Yakin", "Sangat yakin"])

kuis = st.radio("Jika diketahui persamaan kuadrat x² + 2x - 8 = 0, maka akar-akarnya adalah ...", 
                ["x = -4 atau x = 2", "x = 4 atau x = -2", "x = 2 atau x = 4", "x = -2 atau x = -4"])

cek = ""
if kuis:
    if kuis == "x = -4 atau x = 2":
        st.success("✅ Jawaban benar!")
        cek = "Benar"
    else:
        st.error("❌ Jawaban belum tepat.")
        cek = "Salah"

if st.button("📤 Kirim Jawaban"):
    if nama and kelas:
        simpan_ke_sheet(nama, kelas, "Pertemuan 4", "-", identifikasi, kesimpulan)
        st.success("✅ Jawaban berhasil disimpan!")
    else:
        st.warning("❗ Nama dan Kelas wajib diisi.")

# Navigasi
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ Pertemuan 3"):
        st.switch_page("pages/5_Pertemuan_3.py")
with col2:
    if st.button("🏠 Daftar Isi"):
        st.switch_page("pages/0_Daftar_Isi.py")
with col3:
    if st.button("➡️ Latihan dan Refleksi"):
        st.switch_page("pages/8_Latihan_dan_Refleksi.py")







