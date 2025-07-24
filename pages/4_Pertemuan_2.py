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

st.set_page_config(page_title="Pertemuan 2", layout="centered")

st.title("🧮 Pertemuan 2: Bentuk Umum, Faktor, dan Akar Persamaan Kuadrat")
st.markdown("**Capaian:** Siswa dapat menyatakan bentuk umum fungsi kuadrat dalam bentuk faktor dan menentukan akarnya.")

# Identitas
st.subheader("👤 Identitas")
nama = st.text_input("Nama Siswa:")
kelas = st.text_input("Kelas:")

# --- 1. Stimulus ---
st.header("1. Stimulus)")
st.write("Perhatikan bentuk fungsi kuadrat berikut:")
st.latex(r"f(x) = x^2 - 5x + 6")
st.write("Bentuk tersebut adalah bentuk umum fungsi kuadrat. Apakah kamu bisa mengubahnya menjadi bentuk faktor?")
jawaban1 = st.text_area("📝 Tuliskan hal yang menarik atau membingungkan dari bentuk kuadrat di atas:")

# --- 2. Identifikasi Masalah ---
st.header("2. Identifikasi Masalah")
jawaban2 = st.text_area("❓ Apa pertanyaan atau masalah yang muncul dari stimulus di atas?")

if jawaban2.strip():
    st.success("✅ Jawaban dicatat.")
    with st.expander("👉 Lihat referensi AI (setelah mengisi jawaban)"):
        st.markdown("[Buka Perplexity](https://www.perplexity.ai/search/perhatikan-bentuk-fungsi-kuadr-6B4Ys2oFSY2k7brcauEtHA)")
else:
    st.warning("Silakan isi jawaban terlebih dahulu.")

# --- 3. Pengumpulan Data ---
st.header("3. Pengumpulan Data")
st.markdown("💡 Masukkan nilai *a*, *b*, dan *c* untuk melihat bentuk persamaan kuadrat dan faktornya.")

# 1. Input a, b, c
a = st.number_input("Masukkan nilai a", value=1)
b = st.number_input("Masukkan nilai b", value=5)
c = st.number_input("Masukkan nilai c", value=6)

x = sp.Symbol('x')
persamaan = a * x**2 + b * x + c

# 2. Tampilkan persamaan kuadrat
st.latex(sp.latex(persamaan) + " = 0")

# 3. Coba faktorkan
faktorisasi = sp.factor(persamaan)

if faktorisasi == persamaan:
    st.warning("❌ Tidak bisa difaktorkan dengan bilangan rasional.")
else:
    st.success("✅ Bentuk faktorisasi:")
    st.latex(sp.latex(faktorisasi) + " = 0")

# 4. Input analisis dari siswa
analisis = st.text_area("📝 Tulis analisismu terhadap hasil faktorisasi di atas:")

# 5. Cek AI muncul setelah siswa isi analisis
if analisis.strip() != "":
    st.markdown("🔍 [Klik di sini untuk melihat penjelasan dari AI](https://www.perplexity.ai/search/materi-faktorisasi-dari-fungsi-9xV92TI5QQOZA0wFxQFUfg)")


st.header("4. Pengolahan Data")
st.write("Faktorkan bentuk berikut:")
st.latex(r"f(x) = x^2 - 7x + 10")
analisis = st.text_input("📝 Tulis bentuk faktornya:")

if analisis.strip():
    st.success("✅ Jawaban disimpan.")
    with st.expander("🔍 Cek AI setelah menjawab"):
        st.markdown("[Buka Perplexity](https://www.perplexity.ai/search/faktorkan-bentuk-berikut-f-x-x-zX63Q4XtQvmPVB..m6yvOg)")
else:
    st.warning("Silakan faktorkan dulu sebelum cek AI.")
    

# --- 5. Pembuktian (Verifikasi) ---
st.header("5. Pembuktian")
st.write("Soal: Faktorkan bentuk berikut:")
st.latex(r"f(x) = x^2 - 3x - 10")
analisis_l4 = st.text_input("🧠 Jawabanmu (dalam bentuk faktor):")

if analisis_l4.strip():
    st.success("✅ Jawaban disimpan.")
    with st.expander("🔍 Lihat pembahasan AI setelah menjawab"):
        st.markdown("[Buka Perplexity](https://www.perplexity.ai/search/soal-faktorkan-bentuk-berikut-787Tzl.dRTSZOdt4ppj4QQ)")
else:
    st.warning("Silakan isi jawaban terlebih dahulu.")

# --- 6. Penarikan Kesimpulan ---
st.header("6. Penarikan Kesimpulan")
kesimpulan = st.text_area("📚 Apa kesimpulan yang kamu dapatkan dari aktivitas ini?")
if kesimpulan.strip():
    st.success("✅ Kesimpulan kamu tercatat.")
    if st.button("Lihat rangkuman AI", key="buka_ai_kesimpulan_2"):
        st.markdown("[Buka Rangkuman AI](https://www.perplexity.ai/search/kesimpulan-materi-faktorisasi-_FgcWfjBTE6928qG9BJ9kQ)")
else:
    st.warning("Silakan isi kesimpulan sebelum cek rangkuman.")

# --- Refleksi Akhir ---
st.subheader("🪞 Refleksi Belajar")
refleksi = st.radio("Seberapa yakin kamu memahami materi faktorisasi fungsi kuadrat?", 
                    ["Tidak yakin", "Kurang yakin", "Cukup yakin", "Yakin", "Sangat yakin"])

kuis = st.radio("Jika f(x) = x² - 7x + 10, maka faktornya adalah ...", 
                ["(x-5)(x-2)", "(x+5)(x+2)", "(x-7)(x+10)", "Tidak bisa difaktorkan"])

cek = ""
if kuis:
    if kuis == "(x-5)(x-2)":
        st.success("✅ Jawaban benar!")
        cek = "Benar"
    else:
        st.error("❌ Jawaban belum tepat.")
        cek = "Salah"

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
