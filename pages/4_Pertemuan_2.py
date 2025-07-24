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

# --- 1. STIMULUS ---
st.header("1. Stimulus")
st.write("""
Perhatikan bentuk umum fungsi kuadrat berikut:  
$$f(x) = x^2 - 5x + 6$$  
Coba ingat kembali bagaimana bentuk ini bisa diubah menjadi bentuk faktor.
""")

# --- 2. IDENTIFIKASI MASALAH ---
st.header("2. Identifikasi Masalah")
masalah = st.text_area("❓ Apa yang menjadi pertanyaan atau masalah yang muncul dari stimulus di atas?")

if masalah.strip():
    st.success("✅ Masalah telah dicatat.")
else:
    st.warning("Silakan tulis masalah yang kamu temukan dari stimulus.")

# --- 3. PENGUMPULAN DATA ---
st.header("3. Pengumpulan Data")
st.write("""
Mari kita ingat rumus faktorisasi bentuk kuadrat:  
Jika $f(x) = ax^2 + bx + c$, maka kita cari dua bilangan yang hasil kalinya $a×c$ dan jumlahnya $b$.
""")

# --- 4. PENGOLAHAN DATA ---
st.header("4. Pengolahan Data")
st.write("Silakan faktorkan fungsi berikut secara manual:")
soal_pengolahan = st.text_input("📝 Faktorkan:  \n$$f(x) = x^2 - 7x + 10$$")

if soal_pengolahan.strip():
    st.success("✅ Jawaban kamu disimpan.")
else:
    st.warning("Silakan faktorkan fungsi terlebih dahulu.")

# --- 5. PEMBUKTIAN ---
st.header("5. Pembuktian")
st.write("Coba kerjakan soal berikut dan simak hasil dari AI setelah kamu menjawab:")
st.write("**Soal:** Faktorkan bentuk:  \n$$f(x) = x^2 - 3x - 10$$")

jawaban = st.text_input("🧠 Jawabanmu (dalam bentuk faktor):")

if jawaban.strip():
    st.success("✅ Jawaban kamu telah dicatat.")
    if st.button("Buka Perplexity untuk klarifikasi", key="buka_ai_faktorisasi"):
        st.markdown("[Klik untuk Buka Perplexity](https://www.perplexity.ai/search/faktorkan-x-kuadrat-minus-3x-minus-10-vV0n2C6WTLmaV6Sg_y-qGA)")
else:
    st.warning("Silakan isi jawaban terlebih dahulu sebelum membuka referensi AI.")

# --- 6. PENARIKAN KESIMPULAN ---
st.header("6. Penarikan Kesimpulan")
kesimpulan = st.text_area("📚 Apa kesimpulan yang kamu dapatkan dari aktivitas ini?")

if kesimpulan.strip():
    st.success("✅ Kesimpulan kamu tercatat.")
    if st.button("Lihat rangkuman AI", key="buka_ai_kesimpulan_2"):
        st.markdown("[Klik untuk Buka Perplexity](https://www.perplexity.ai/search/kesimpulan-materi-faktorisasi-fungsi-kuadrat-r1Az5zNSfTicI7hAo9FqBg)")
else:
    st.warning("Silakan isi kesimpulan terlebih dahulu sebelum membuka rangkuman AI.")
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
