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

st.title("📘 Pertemuan 3: Menyelesaikan Persamaan Kuadrat")

st.markdown("**Capaian:** Siswa dapat menyelesaikan soal persamaan kuadrat menggunakan metode pemfaktoran dan rumus ABC.")

# --- 1. Stimulus ---
st.header("📌 Stimulus")

st.markdown(
    r"""
    Seorang siswa mencoba menyelesaikan persamaan kuadrat berikut:

    $$
    2x^2 - 4x - 6 = 0
    $$

    Ia merasa kesulitan karena bentuknya tidak bisa langsung difaktorkan dengan mudah.

    🔎 **Menurutmu, strategi apa yang bisa digunakan siswa tersebut untuk menyelesaikan persamaan kuadrat ini?**
    (Petunjuk: apakah kamu ingat dengan sebuah rumus yang melibatkan diskriminan?)

    Silakan tuliskan pendapatmu di bawah ini:
    """
)

# Kotak masukan interaktif
jawaban_stimulus = st.text_input("💬 Pendapatmu:", placeholder="Tulis jawabanmu di sini...")

# Menyimpan atau menampilkan hasil input pengguna (jika ingin digunakan lebih lanjut)
if jawaban_stimulus:
    st.success("✅ Jawabanmu telah dicatat")



# --- 2. Identifikasi Masalah ---
st.header("🔍 Identifikasi Masalah")

st.markdown(
    r"""
    Kita ingin menyelesaikan persamaan kuadrat:

    $$
    x^2 - 5x + 6 = 0
    $$

    Untuk itu, coba identifikasi hal-hal berikut:

    - Apa tujuan dari menyelesaikan persamaan kuadrat ini?
    - Metode apa saja yang bisa digunakan untuk menyelesaikannya?
    - Apakah kedua metode tersebut (pemfaktoran dan rumus ABC) akan menghasilkan solusi yang sama?

    ✏️ Tuliskan hasil identifikasimu di bawah ini:
    """
)

# Kotak masukan jawaban dari siswa
jawaban_identifikasi = st.text_input("💬 Jawabanmu:", placeholder="Tuliskan jawabanmu di sini...")

# Menampilkan feedback sederhana
if jawaban_identifikasi:
    st.success("✅ Jawabanmu telah dicatat")
    

# --- 3. Eksplorasi ---
st.header("🔬 Eksplorasi")

st.markdown("#### ✍️ Eksplorasi 1: Menyelesaikan dengan Pemfaktoran")
st.latex(r"x^2 - 5x + 6 = 0")

st.markdown(
    """
    Untuk menyelesaikan persamaan kuadrat tersebut dengan pemfaktoran, ikuti langkah-langkah eksploratif berikut:
    
    **Langkah 1:**  
    Temukan dua bilangan yang jika dikalikan hasilnya **6** dan jika dijumlahkan hasilnya **-5**.
    """
)

bilangan1 = st.text_input("Masukkan bilangan pertama:", key="bil1")
bilangan2 = st.text_input("Masukkan bilangan kedua:", key="bil2")

if bilangan1 and bilangan2:
    try:
        b1 = int(bilangan1)
        b2 = int(bilangan2)
        hasil_kali = b1 * b2
        hasil_jumlah = b1 + b2

        if hasil_kali == 6 and hasil_jumlah == -5:
            st.success("✅ Tepat! Pasangan bilangan kamu sesuai.")
        else:
            st.warning(f"⚠️ Periksa kembali. {b1} × {b2} = {hasil_kali}, {b1} + {b2} = {hasil_jumlah}. Seharusnya hasil kali 6 dan jumlah -5.")
    except ValueError:
        st.error("❌ Harap masukkan bilangan bulat.")

st.markdown(
    """
    **Langkah 2:**  
    Gunakan pasangan bilangan tersebut untuk menuliskan bentuk faktornya.
    
    _(Misal: jika pasangannya 2 dan 3, maka bentuknya: (x - 2)(x - 3))_
    """
)

faktorisasi = st.text_input("Tulis bentuk faktornya:", placeholder="Contoh: (x - 2)(x - 3)", key="faktorisasi")

if faktorisasi:
    st.success("✅ Bentuk faktormu telah dicatat. Lanjutkan ke langkah berikutnya.")

st.markdown(
    """
    **Langkah 3:**  
    Dari bentuk faktornya, tentukan akar-akarnya!
    """
)

akar1 = st.text_input("Akar pertama:", key="akar1")
akar2 = st.text_input("Akar kedua:", key="akar2")

if akar1 and akar2:
    st.success(f"✅ Akar-akar yang kamu masukkan: {akar1} dan {akar2}")

# --- Input Langkah Faktorisasi (jika dibutuhkan) ---
langkah_faktorisasi = st.text_area("🧮 Tuliskan langkah-langkah faktorisasi yang kamu lakukan:", key="faktorisasi")


# --- Eksplorasi 2: Gunakan Rumus ABC ---
st.markdown("#### ✍️ Eksplorasi 2: Gunakan Rumus ABC untuk Menyelesaikan Persamaan Kuadrat")
st.latex(r"x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
st.markdown("Persamaan yang akan diselesaikan: $$x^2 - 5x + 6 = 0$$")

# Step 1: Identifikasi nilai a, b, dan c
st.markdown("**Langkah 1: Tentukan nilai koefisien**")
a_input = st.text_input("Masukkan nilai $$a$$:", value="1", key="a_input")
b_input = st.text_input("Masukkan nilai $$b$$:", value="-5", key="b_input")
c_input = st.text_input("Masukkan nilai $$c$$:", value="6", key="c_input")

# Step 2: Hitung diskriminan
st.markdown("**Langkah 2: Hitung nilai diskriminan $$D = b^2 - 4ac$$**")
st.text_input("Tulis hasil perhitungan diskriminan:", key="diskriminan_input")

# Step 3: Akar-akar kuadrat
st.markdown("**Langkah 3: Hitung akar-akar menggunakan rumus ABC**")
st.markdown("Gunakan nilai $$a$$, $$b$$, dan diskriminan yang sudah kamu temukan.")
st.text_input("Tulis akar pertama (x₁):", key="akar1")
st.text_input("Tulis akar kedua (x₂):", key="akar2")

# Opsional: Umpan balik reflektif
st.markdown("**🧠 Refleksi:**")
st.text_area("Apa kelebihan menggunakan rumus ABC dibanding pemfaktoran?", key="refleksi_abc")



# --- Eksplorasi 3: Hubungan Faktorisasi dan Rumus ABC ---
st.markdown("#### ✍️ Eksplorasi 3: Hubungan antara Faktorisasi dan Rumus ABC")

st.markdown(
    """
    Setelah kamu menyelesaikan persamaan kuadrat $$x^2 - 5x + 6 = 0$$ dengan **pemfaktoran** dan **rumus ABC**, mari kita cermati lebih dalam:
    
    - Hasil dari faktorisasi: akar-akar apa yang kamu temukan?
    - Hasil dari rumus ABC: apakah akarnya sama?
    """
)

akar_faktorisasi = st.text_input("Tulis kembali akar-akar dari hasil faktorisasi:", key="akar_faktorisasi")
akar_abc = st.text_input("Tulis kembali akar-akar dari hasil rumus ABC:", key="akar_abc")

st.markdown("---")

st.markdown(
    """
    Sekarang, perhatikan kembali bentuk faktornya. Misalnya, jika hasil faktorisasi adalah:
    
    $$(x - p)(x - q) = 0$$
    
    maka akarnya adalah $$x = p$$ dan $$x = q$$
    
    Bandingkan dengan hasil dari rumus ABC:
    """
)

st.text_input("Apakah nilai $$p$$ dan $$q$$ bisa kamu dapatkan dari rumus ABC?", key="hubungan_pq")
st.text_area("Tuliskan kesimpulanmu tentang hubungan antara metode pemfaktoran dan rumus ABC", key="kesimpulan_hubungan")


# --- 3. Soal Persamaan Kuadrat ---
st.header("🧮 Soal Persamaan Kuadrat")
st.markdown(
    """
    Diberikan persamaan kuadrat berikut:

    $$x^2 - 5x + 6 = 0$$

    Selesaikan persamaan ini menggunakan:
    
    1. Metode Faktorisasi
    2. Metode Rumus ABC (Rumus Kuadrat)

    Setelah itu, bandingkan hasil yang kamu peroleh dari kedua metode.
    """
)
# --- 4. Pengolahan Data ---
st.header("📊 Pengolahan Data")
st.markdown(
    """
    Bandingkan hasil dari kedua metode penyelesaian persamaan kuadrat berikut:
    
    - Apakah akarnya sama?
    - Apa kelebihan atau kekurangan dari masing-masing metode menurutmu?
    
    Tuliskan hasil akarnya dan pendapatmu di bawah ini.
    """
)

hasil_faktorisasi = st.text_area("📝 Akar dari metode faktorisasi:", key="hasil_faktorisasi")
hasil_abc = st.text_area("📝 Akar dari metode rumus ABC:", key="hasil_abc")



# --- 5. Verifikasi ---
st.header("Verifikasi")
st.markdown("#### 🔎 Cek AI")
st.code("Bagaimana cara menyelesaikan persamaan kuadrat x^2 - 5x + 6 = 0 dengan dua metode: pemfaktoran dan rumus ABC?")
st.info("Gunakan jawaban AI sebagai referensi. Bandingkan dengan jawabanmu dan perhatikan perbedaan langkah atau hasil yang ditemukan.")
st.markdown("[🔗 Lihat jawaban AI di Perplexity](https://www.perplexity.ai)")

import streamlit as st

# --- 6. Penarikan Kesimpulan ---
st.header("🎯 Penarikan Kesimpulan")
kesimpulan = st.text_area(
    "Apa kesimpulanmu dari hasil eksplorasi dua metode tersebut? Manakah yang menurutmu lebih mudah atau lebih cepat?",
    key="kesimpulan_akhir"
)

# Prompt untuk Perplexity
prompt = f"""Bandingkan dua metode penyelesaian persamaan kuadrat: metode faktorisasi dan metode rumus ABC.
Berikan kelebihan dan kekurangan masing-masing serta contoh soal yang bisa diselesaikan dengan dua metode tersebut."""

# Tampilkan tombol untuk menyalin prompt dan mengakses Perplexity
if kesimpulan.strip() != "":
    st.markdown("### 🔍 Coba Bandingkan Jawabanmu dengan AI!")
    st.code(prompt, language="markdown")

    st.markdown(
        f"""
        <a href="https://www.perplexity.ai" target="_blank">
            <button style='padding:10px 20px;font-size:16px;border:none;border-radius:8px;background-color:#4CAF50;color:white;cursor:pointer;'>
                Buka Perplexity AI untuk Cek Jawaban
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.info("📋 Salin prompt di atas, lalu tempel di Perplexity AI untuk membandingkan jawabanmu.")
else:
    st.warning("❗Isi dulu kesimpulanmu sebelum lanjut ke AI ya!")



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
