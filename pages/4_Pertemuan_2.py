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

st.set_page_config(page_title="Pertemuan 2", layout="centered")

st.title("🧮 Pertemuan 2: Bentuk Umum, Faktor, dan Akar Persamaan Kuadrat")
st.markdown("**Capaian:** Siswa dapat menyatakan bentuk umum fungsi kuadrat dalam bentuk faktor dan menentukan akarnya.")

# Identitas
st.subheader("👤 Identitas")
nama = st.text_input("Nama Siswa:")
kelas = st.text_input("Kelas:")

# Langkah 1: Stimulus
st.subheader("🔹 Langkah 1: Stimulus (Self-construction)")
st.markdown("""
Salin prompt berikut ke Gemini AI dan pelajari jawabannya.  
Tuliskan pemahamanmu berdasarkan jawaban Gemini.  
""")
st.code("Apa yang dimaksud dengan bentuk faktor dari fungsi kuadrat dan bagaimana hubungannya dengan akar persamaan kuadrat?")
st.markdown("[🔎 Cek AI di Gemini](https://gemini.google.com/app)")
jawaban1 = st.text_area("📥 Ringkasan pemahamanmu dari hasil Gemini AI:")

if jawaban1.strip():
    st.success("✅ Jawaban diterima. Sekarang kamu dapat melanjutkan ke langkah berikutnya.")

# Langkah 2: Identifikasi Masalah
st.subheader("🔹 Langkah 2: Identifikasi Masalah")
jawaban2 = st.text_area("📥 Menurutmu, mengapa penting mengetahui bentuk faktor dari persamaan kuadrat?")
if jawaban2.strip():
    st.success("✅ Bagus. Ayo lanjut ke langkah berikutnya.")

# Langkah 3: Pengumpulan Data dan Materi
st.subheader("🔹 Langkah 3: Pengumpulan Data dan Materi (Self-contained)")
st.markdown(r"""
**Materi: Faktor dan Akar Persamaan Kuadrat**

Jika suatu fungsi kuadrat berbentuk f(x) = ax² + bx + c dan dapat difaktorkan menjadi 
f(x) = (x - p)(x - q)

maka akar-akar persamaannya adalah:
x1 = p  dan  x2 = q

#### Contoh:
x² - 5x + 6 = 0
 
Faktorkan:  
(x - 2)(x - 3) = 0

Jadi, akar-akarnya adalah:  
x1 = 2   dan    x2 = 3
""")

contoh = st.text_input("✍️ Masukkan persamaan kuadratmu (contoh: x² - 5x + 6):")
analisis = st.text_area("📥 Tuliskan faktorisasi dan akarnya berdasarkan persamaanmu:")

if analisis.strip():
    with st.expander("🤖 Cek AI untuk Faktorisasi"):
        st.markdown("Salin prompt ini ke Gemini AI:")
        st.code(f"Faktorkan persamaan kuadrat {contoh} dan tentukan akar-akarnya.")
        st.markdown("[🔎 Cek AI di Gemini](https://gemini.google.com/app)")
        st.markdown("Bandingkan hasil dari AI dengan jawabanmu di atas.")


# Langkah 4: Pengolahan Data
st.subheader("🔹 Langkah 4: Pengolahan Data (Interactive)")
st.markdown(r"""
Misalnya kamu diberikan persamaan:  
x² - 4x - 5 = 0

Cobalah faktorkan dan tentukan akarnya.
""")

analisis_l4 = st.text_area("📥 Tuliskan faktorisasi dan akar dari soal tersebut:")
if analisis_l4:
    st.session_state.analisis_l4 = analisis_l4

# Langkah 5: Verifikasi
st.subheader("🔹 Langkah 5: Verifikasi")
st.markdown("❗ *Jawab dulu pertanyaan di Langkah 4 agar dapat melakukan verifikasi.*")

# Cek apakah siswa sudah menjawab Langkah 4
if "analisis_l4" in st.session_state and st.session_state.analisis_l4.strip() != "":
    with st.expander("🤖 Cek AI untuk Verifikasi Jawaban"):
        st.markdown("Salin dan tempelkan prompt berikut ke Gemini AI:")
        st.code("Jelaskan cara menyelesaikan persamaan kuadrat dengan metode pemfaktoran. Bandingkan hasilnya dengan jawaban saya sebelumnya.")
        st.markdown("[🔎 Cek AI di Gemini](https://gemini.google.com/app)")
        
        st.markdown("🟩 Setelah membaca hasil Gemini AI, isilah bagian berikut:")

        kesesuaian = st.selectbox(
            "Apakah jawabanmu sesuai dengan hasil Gemini?",
            ["Semua sama", "Sebagian sama", "Tidak sama sekali"]
        )

        refleksi = st.text_area("📥 Tulis refleksi atau perenunganmu setelah membandingkan:")

        st.session_state.verifikasi_kesesuaian = kesesuaian
        st.session_state.verifikasi_refleksi = refleksi
else:
    st.info("⛔ Silakan lengkapi jawaban di Langkah 4 terlebih dahulu agar dapat membuka verifikasi.")


# Langkah 6: Kesimpulan
st.subheader("🔹 Langkah 6: Kesimpulan (Reflective & Self-regulated)")
kesimpulan = st.text_area("📝 Tulis kesimpulanmu dari pembelajaran hari ini:")

if kesimpulan.strip():
    with st.expander("🤖 Cek AI untuk Simpulan"):
        st.markdown("Salin prompt ini ke Gemini AI:")
        st.code("Buatkan simpulan tentang cara memfaktorkan fungsi kuadrat dan menentukan akarnya.")
        st.markdown("[🔎 Cek AI di Gemini](https://gemini.google.com/app)")
        st.markdown("Bandingkan dengan simpulan yang kamu tulis.")

# Refleksi akhir
st.subheader("🔹 Refleksi")
refleksi = st.text_area("💬 Apa yang kamu pelajari secara umum dari pertemuan ini? (Refleksi Akhir)")

# Kirim
if st.button("📤 Kirim Jawaban ke Spreadsheet"):
    if nama and kelas:
        semua_jawaban = f"Stimulus: {jawaban1} | Identifikasi: {jawaban2} | Analisis: {analisis} | Analisis Soal: {analisis_l4} | Verifikasi: {st.session_state.get('verifikasi_kesesuaian', '')} | Kesimpulan: {kesimpulan}"
        refleksi_akhir = refleksi or st.session_state.get("verifikasi_refleksi", "")

        # Simpan ke spreadsheet
        simpan_ke_sheet(nama, kelas, "Pertemuan 2", "-", semua_jawaban, refleksi_akhir)

        st.success("✅ Jawaban berhasil dikirim ke spreadsheet!")
    else:
        st.warning("❗ Harap lengkapi nama dan kelas sebelum mengirim.")


# Navigasi
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("⬅️ Pertemuan 1"):
        st.switch_page("pages/3_Pertemuan_1.py")
with col2:
    if st.button("🏠 Daftar Isi"):
        st.switch_page("pages/0_Daftar_Isi.py")
with col3:
    if st.button("➡️ Pertemuan 3"):
        st.switch_page("pages/5_Pertemuan_3.py")
