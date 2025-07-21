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
st.subheader("🔹 Langkah 1: Stimulus (Self-construction)")
st.markdown("Salin prompt di bawah ini ke Gemini AI dan **pelajari jawabannya**.")
st.code("Jelaskan bagaimana persamaan kuadrat dapat digunakan untuk memodelkan gerak benda dalam kehidupan sehari-hari.")
st.markdown("[🔎 Cek AI di Gemini](https://gemini.google.com/app)")
stimulus_ai = st.text_area("📥 Tuliskan ringkasan pemahamanmu dari jawaban Gemini AI:")
if stimulus_ai.strip():
    st.success("✅ Jawaban diterima. Sekarang kamu dapat melanjutkan ke langkah berikutnya.")

# Langkah 2: Identifikasi Masalah
st.subheader("🔹 Langkah 2: Identifikasi Masalah")
st.markdown("Contoh: Sebuah bola dilempar ke atas, dan ketinggiannya terhadap waktu dinyatakan oleh: $$h(t) = -5t^2 + 20t$$. Apa saja informasi yang bisa diperoleh?")
identifikasi = st.text_area("📥 Tuliskan masalah yang dapat dipecahkan dari situasi tersebut:")
if identifikasi.strip():
    st.success("✅ Bagus. Ayo lanjut ke langkah berikutnya.")

# Langkah 3: Pengumpulan Data
st.subheader("🔹 Langkah 3: Pengumpulan Data")
st.markdown("Dari soal yang kamu baca di Langkah 2, jawablah pertanyaan berikut:")

data1 = st.text_input("1️⃣ Apa nilai $$a, b,$$ dan $$c$$ dari persamaan kuadrat dalam soal?", key="data1_l3")
data2 = st.text_input("2️⃣ Tentukan jenis akar-akarnya (real dan berbeda, real dan kembar, atau imajiner)?", key="data2_l3")
data3 = st.text_input("3️⃣ Berapa nilai diskriminannya ($$D= b²-4ac$$)?", key="data3_l3")

# Simpan jawaban
if data1 and data2 and data3:
    st.session_state["isidata_l3"] = True

# Tampilkan Cek AI jika semua jawaban diisi
if st.session_state.get("isidata_l3", False):
    with st.expander("🤖 Cek AI untuk Konfirmasi Jawabanmu"):
        st.markdown("""
Salin dan tempelkan prompt berikut ke Gemini AI atau AI lain:
Saya ingin memeriksa jawaban saya:
a. Nilai a, b, dan c dari x² - 4x - 5 = 0
b. Jenis akarnya
c. Nilai diskriminannya
Beritahu apakah sudah benar, dan jelaskan alasannya.
""")
        st.markdown("[🔎 Cek AI di Gemini](https://gemini.google.com/app)")
        st.markdown("""
Setelah membaca jawaban AI, tulislah:
        """)

        refleksi_l3 = st.text_area("📥 Apa yang kamu pelajari dari penjelasan AI di Langkah 3?")
        st.session_state["refleksi_l3"] = refleksi_l3
else:
    st.info("⛔ Silakan isi semua pertanyaan di atas terlebih dahulu.")

# Langkah 4: Pengolahan Data (Grafik)
st.subheader("🔹 Langkah 4: Representasi Grafis")

st.markdown("Masukkan nilai-nilai berikut untuk menggambar grafik parabola:")

a_val = st.number_input("Nilai a", step=1, format="%d", key="a_l4")
b_val = st.number_input("Nilai b", step=1, format="%d", key="b_l4")
c_val = st.number_input("Nilai c", step=1, format="%d", key="c_l4")

if a_val != 0 or b_val != 0 or c_val != 0:
    st.session_state["analisis_l4"] = f"a={a_val}, b={b_val}, c={c_val}"

    x_vals = np.linspace(-10, 10, 400)
    y_vals = a_val * x_vals**2 + b_val * x_vals + c_val

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f"{a_val}x² + {b_val}x + {c_val}")
    ax.axhline(0, color='gray', lw=1)
    if a_val != 0:
        ax.axvline(-b_val / (2 * a_val), color='red', linestyle='--', label='Sumbu Simetri')
    ax.legend()
    st.pyplot(fig)

    st.session_state["grafik_sudah_dibuat"] = True
else:
    st.info("❗Masukkan nilai a, b, dan c untuk melihat grafik.")

# Langkah 5: Verifikasi
st.subheader("🔹 Langkah 5: Verifikasi")
st.markdown("❗ *Selesaikan Langkah 4 terlebih dahulu sebelum melakukan verifikasi.*")

if st.session_state.get("analisis_l4", "").strip() != "":
    with st.expander("🤖 Cek AI untuk Verifikasi Jawaban"):
        st.markdown(r"""
Salin dan tempelkan prompt berikut ke Gemini AI (atau AI lainnya):
Jelaskan cara menyelesaikan persamaan kuadrat berikut dengan metode rumus ABC:
x^2 - 4x - 5 = 0
Bandingkan hasilnya dengan jawaban saya.
""")
        st.markdown("[🔎 Cek AI di Gemini](https://gemini.google.com/app)")
        kesesuaian = st.selectbox("Bagaimana tingkat kesesuaian jawabanmu dengan penjelasan AI?", ["Semua sama", "Sebagian sama", "Tidak sama sekali"], key="kesesuaian_l5")
        refleksi = st.text_area("📥 Apa yang kamu pelajari dari perbandingan tersebut?", key="refleksi_l5")

        st.session_state["verifikasi_kesesuaian"] = kesesuaian
        st.session_state["verifikasi_refleksi"] = refleksi
else:
    st.info("⛔ Silakan isi Langkah 4 terlebih dahulu.")

# Langkah 6: Kesimpulan
st.subheader("🔹 Langkah 6: Kesimpulan")
kesimpulan = st.text_area("📝 Tuliskan simpulanmu mengenai penggunaan persamaan kuadrat dalam kehidupan nyata:")

if kesimpulan:
    with st.expander("🤖 Cek AI untuk Validasi Kesimpulan"):
        st.markdown("Salin prompt ini ke Gemini AI:")
        st.code("Jelaskan simpulan tentang enggunaan persamaan kuadrat dalam kehidupan nyata")
        st.markdown("[🔎 Cek AI di Gemini](https://gemini.google.com/app)")

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
        st.switch_page("8_Latihan_dan_Refleksi")



