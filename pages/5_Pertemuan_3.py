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
st.image("pages/lintasan_bola.png", caption="Lintasan Gerak Parabola", use_container_width=True)
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
    st.markdown("[Cek penjelasan AI di Preplexity](https://www.perplexity.ai/search/bagaimana-hubungan-antara-lint-jmJR_1UoSDSd12oB6nv_8A)")

st.markdown("---")

# LANGKAH 3: PENGUMPULAN & PENGOLAHAN DATA
st.header("3. Pengumpulan Data")
st.write("Masukkan nilai koefisien a, b, dan c dari bentuk persamaan kuadrat:")

col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input("a", format="%.2f")
with col2:
    b = st.number_input("b", format="%.2f")
with col3:
    c = st.number_input("c", format="%.2f")

if a != 0:
    diskriminan = b**2 - 4*a*c
    akar1 = (-b + sp.sqrt(diskriminan)) / (2*a)
    akar2 = (-b - sp.sqrt(diskriminan)) / (2*a)

    st.subheader("🔹 Persamaan Kuadrat")
    st.latex(f"{a}x^2 + {b}x + {c} = 0")

    st.subheader("🔹 Solusi dengan Rumus ABC")
    st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
    st.latex(rf"x_1 = {sp.simplify(akar1)}, \quad x_2 = {sp.simplify(akar2)}")

    if diskriminan >= 0:
        st.subheader("🔹 Faktorisasi Persamaan")
        bentuk_faktorisasi = a * (x - akar1) * (x - akar2)
        st.latex(f"{sp.expand(bentuk_faktorisasi)} = 0")
    else:
        st.info("Diskriminan < 0 → tidak bisa difaktorkan dalam bilangan real.")

    # Interpretasi D dan arah grafik
    st.markdown("### 📊 Eksplorasi Grafik Berdasarkan Nilai D dan a")
    if diskriminan > 0:
        keterangan = "Akar real dan berbeda"
    elif diskriminan == 0:
        keterangan = "Akar real dan kembar"
    else:
        keterangan = "Akar imajiner (tidak memotong sumbu-x)"

    arah_parabola = "terbuka ke atas (a > 0)" if a > 0 else "terbuka ke bawah (a < 0)"
    st.success(f"- Diskriminan = {diskriminan} → {keterangan}\n- Grafik {arah_parabola}")

    analisis_pengolahan = st.text_area("📌 Analisismu berdasarkan hasil di atas:")

    if analisis_pengolahan:
        st.success("Kamu telah menyelesaikan analisis pengolahan data.")
        st.markdown("[Cek validasi penjelasan di Perplexity](https://www.perplexity.ai/search/materi-fungsi-kuadrat-dengan-m-rnq03xB5QseNmAcFeMQ.Uw)")
else:
    st.warning("Nilai a tidak boleh 0")

st.header("4. Pengolahan Data")
st.write("""
Latihan Soal:
Selesaikan persamaan berikut dengan rumus ABC:

> 2x² - 4x - 6 = 0
""")
jawaban_pengolahan = st.text_area("Tulis jawabanmu di sini:")
if jawaban_pengolahan:
    st.markdown("[Cek jawabanmu di Perplexity AI](https://www.perplexity.ai/search/selesaikan-persamaan-berikut-d-nuMuhEe5T3m4nC7wuHTecw/)", unsafe_allow_html=True)

# LANGKAH 5: VERIFIKASI
st.header("5. Verifikasi")
st.write("""
Bandingkan jawabanmu dengan jawaban dari teman atau AI.
Apakah terdapat perbedaan?
""")
verifikasi_input = st.text_area("Tuliskan hasil verifikasimu di sini:")
if verifikasi_input:
    st.markdown("[Diskusikan dengan AI di Perplexity](https://www.perplexity.ai/search/berikan-verifikasi-dan-diskusi-DdCrBk.uTkCU0QXm_WMTIg/)", unsafe_allow_html=True)

# LANGKAH 6: KESIMPULAN
st.header("6. Kesimpulan")
st.write("""
Buatlah kesimpulan dari pembelajaran hari ini, khususnya tentang cara penyelesaian persamaan kuadrat menggunakan rumus ABC.
""")
kesimpulan_input = st.text_area("Tuliskan kesimpulanmu:")
if kesimpulan_input:
    st.markdown("[Cek kesimpulan dengan Perplexity AI](https://www.perplexity.ai/search/kesimpulan-materi-persamaan-ku-RdlMiqRjQq6VedhRfHeqCw/)", unsafe_allow_html=True)

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
