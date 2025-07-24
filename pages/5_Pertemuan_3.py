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

# LANGKAH 1: STIMULUS
st.header("1. Stimulus")
st.image("pages/lintasan_bola.png", caption="Lintasan Gerak Parabola", use_column_width=True)
st.write("Perhatikan gambar di atas! Bagaimana hubungan antara lintasan bola dengan bentuk persamaan kuadrat?")
stimulus_jawaban = st.text_area("Tuliskan analisismu berdasarkan stimulus tersebut di sini:")
st.markdown("---")

# LANGKAH 2: IDENTIFIKASI MASALAH
st.header("2. Identifikasi Masalah")
st.write("Diberikan permasalahan berikut:")
st.markdown("""
> Sebuah bola dilempar ke atas membentuk lintasan parabola. Persamaan lintasan tersebut dinyatakan dalam bentuk umum persamaan kuadrat. Tentukan akar-akar dari persamaan tersebut menggunakan rumus ABC!
""")
identifikasi_jawaban = st.text_area("Tuliskan identifikasi masalah yang kamu temukan:")
if identifikasi_jawaban:
    st.success("Masalah telah diidentifikasi. Kamu bisa eksplorasi lebih lanjut dengan bantuan AI.")
    st.markdown("[Cek penjelasan AI di Preplexity](https://www.perplexity.ai)")

st.markdown("---")

# LANGKAH 3: PENGUMPULAN & PENGOLAHAN DATA
st.header("3. Pengumpulan dan Pengolahan Data")
st.write("Masukkan nilai koefisien berikut dari persamaan kuadrat:")
col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input("Masukkan nilai a", step=1.0)
with col2:
    b = st.number_input("Masukkan nilai b", step=1.0)
with col3:
    c = st.number_input("Masukkan nilai c", step=1.0)

if a != 0:
    x = sp.Symbol('x')
    diskriminan = b**2 - 4*a*c
    akar1 = (-b + sp.sqrt(diskriminan)) / (2*a)
    akar2 = (-b - sp.sqrt(diskriminan)) / (2*a)
    
    st.subheader("🔹 Bentuk Persamaan Kuadrat")
    st.latex(f"{a}x^2 + {b}x + {c} = 0")

    st.subheader("🔹 Solusi dengan Rumus ABC")
    st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
    st.latex(rf"x = \frac{{-{b} \pm \sqrt{{{b}^2 - 4({a})({c})}}}}{{2({a})}}")
    st.latex(rf"x_1 = {sp.simplify(akar1)}, \quad x_2 = {sp.simplify(akar2)}")

    st.subheader("🔹 Faktorisasi Persamaan")
    bentuk_faktorisasi = a * (x - akar1) * (x - akar2)
    st.latex(f"{sp.expand(bentuk_faktorisasi)} = 0")

    analisis_pengolahan = st.text_area("Apa yang kamu simpulkan dari hasil perhitungan di atas?")
    if analisis_pengolahan:
        st.success("Kamu telah menyelesaikan analisis pengolahan data.")
        st.markdown("[Cek validasi penjelasan di Preplexity](https://www.perplexity.ai)")

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
