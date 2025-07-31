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
st.header("🔍 Eksplorasi: Menemukan Metode Penyelesaian Persamaan Kuadrat")

# ------------------------- Eksplorasi 1 --------------------------
st.subheader("✍️ Eksplorasi 1: Menyelesaikan dengan Pemfaktoran")
st.latex(r"x^2 - 5x + 6 = 0")

st.markdown("**Langkah 1:** Temukan dua bilangan yang hasil kali = 6 dan jumlah = -5.")

bil1 = st.text_input("Masukkan bilangan pertama:", key="eks1_bil1")
bil2 = st.text_input("Masukkan bilangan kedua:", key="eks1_bil2")

valid_faktor = False
if bil1 and bil2:
    try:
        b1 = int(bil1)
        b2 = int(bil2)
        if b1 * b2 == 6 and b1 + b2 == -5:
            st.success("✅ Tepat! Pasangan bilangan kamu sesuai.")
            valid_faktor = True
        else:
            st.warning("⚠️ Coba periksa lagi. Hasil kali harus 6 dan jumlah -5.")
    except ValueError:
        st.error("❌ Masukkan bilangan bulat.")

if valid_faktor:
    bentuk_faktor = st.text_input("Tulis bentuk faktornya:", key="eks1_faktor")
    if bentuk_faktor:
        akar1 = st.text_input("Akar pertama dari bentuk faktornya:", key="eks1_akar1")
        akar2 = st.text_input("Akar kedua dari bentuk faktornya:", key="eks1_akar2")

        if akar1 and akar2:
            analisis1 = st.text_area("🔍 Apa yang kamu pelajari dari metode faktorisasi ini?", key="analisis1")

            if analisis1:
                with st.expander("🤖 Cek AI untuk eksplorasi ini"):
                    st.markdown("#### Prompt untuk AI (salin dan tempel di Perplexity):")
                    st.code(
                        "Bagaimana cara menyelesaikan persamaan kuadrat x² - 5x + 6 = 0 menggunakan metode faktorisasi? Jelaskan langkah-langkahnya.",
                        language="markdown"
                    )
                    st.markdown("[🔗 Buka Perplexity AI](https://www.perplexity.ai/)")

# ------------------------- Eksplorasi 2 --------------------------
if analisis1:
    st.subheader("✍️ Eksplorasi 2: Menemukan Metode Umum dari Bentuk Akar")

    st.markdown(
        """
        Sekarang kamu sudah menemukan akar-akar dari faktorisasi.

        Pernahkah kamu bertanya:
        > "Bagaimana caranya jika bentuk kuadratnya **tidak bisa difaktorkan** dengan mudah?"

        Mari kita coba kembangkan cara **menggeneralisasi** langkahmu tadi.
        """
    )

    st.markdown("Tulis ekspresi kuadrat dalam bentuk: $(x - p)(x - q)$ dan kembangkan bentuknya.")
    ekspansi = st.text_input("Hasil ekspansi dari (x - p)(x - q):", key="eks2_expand")

    if ekspansi:
        st.markdown("Bandingkan hasil ekspansimu dengan bentuk umum kuadrat: $ax^2 + bx + c$")
        hubungan = st.text_area("Apa hubungan antara $p + q$, $p \\times q$, dan koefisien $b$, $c$?", key="eks2_hubungan")

        if hubungan:
            with st.expander("🤖 Cek AI untuk eksplorasi ini"):
                st.markdown("#### Prompt untuk AI (salin dan tempel):")
                st.code(
                    "Apa hubungan antara akar-akar p dan q dengan koefisien b dan c pada persamaan kuadrat ax^2 + bx + c?",
                    language="markdown"
                )
                st.markdown("[🔗 Buka Perplexity AI](https://www.perplexity.ai/)")

# ------------------------- Eksplorasi 3 --------------------------
if hubungan:
    st.subheader("✍️ Eksplorasi 3: Menemukan Rumus Umum dari Akar")

    st.markdown(
        """
        Sekarang kita ingin menyusun **rumus umum** dari akar-akar tersebut.

        Misalkan persamaan kuadratnya:
        $$ax^2 + bx + c = 0$$

        Coba kamu rumuskan:  
        > Jika tidak bisa difaktorkan, bagaimana kamu bisa menyelesaikan persamaan itu?

        Gunakan ide dari menyelesaikan bentuk kuadrat sederhana.
        """
    )

    langkah_rumus = st.text_area("Coba uraikan idemu untuk membuat rumus mencari akar:", key="eks3_ide")

    if langkah_rumus:
        with st.expander("🤖 Cek AI untuk eksplorasi ini"):
            st.markdown("#### Prompt untuk AI:")
            st.code(
                "Bagaimana cara menyusun rumus ABC untuk menyelesaikan ax^2 + bx + c = 0? Jelaskan langkah-langkah pembentukannya.",
                language="markdown"
            )
            st.markdown("[🔗 Buka Perplexity AI](https://www.perplexity.ai/)")

# ------------------------- Eksplorasi 4 --------------------------
if langkah_rumus:
    st.subheader("✍️ Eksplorasi 4: Menyelidiki Peran Diskriminan")

    st.markdown(
        """
        Setelah kamu menyusun rumus ABC untuk menyelesaikan $ax^2 + bx + c = 0$, coba amati lebih dalam bentuk rumusnya:

        $$
        x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}
        $$

        Lihat bagian di dalam akar (radikal), yaitu:  
        $$
        D = b^2 - 4ac
        $$

        Bagian ini disebut **diskriminan**.  
        Coba kamu selidiki:

        > Apa pengaruh nilai diskriminan terhadap banyaknya akar real dari suatu persamaan kuadrat?

        Isilah berdasarkan contoh-contoh nilai $a$, $b$, dan $c$ yang kamu pilih sendiri.
        """
    )

    disk_check = st.text_area("Apa dugaanmu tentang pengaruh nilai diskriminan (D)?", key="eks4_dugaan")

    if disk_check:
        with st.expander("🤖 Cek AI untuk eksplorasi ini"):
            st.markdown("#### Prompt untuk AI:")
            st.code(
                "Jelaskan bagaimana diskriminan (D = b^2 - 4ac) menentukan banyaknya akar real dalam persamaan kuadrat ax^2 + bx + c = 0.",
                language="markdown"
            )
            st.markdown("[🔗 Buka Perplexity AI dengan Prompt Ini](https://www.perplexity.ai/search?q=Jelaskan+bagaimana+diskriminan+(D+%3D+b%5E2+-+4ac)+menentukan+banyaknya+akar+real+dalam+persamaan+kuadrat+ax%5E2+%2B+bx+%2B+c+%3D+0.)")



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
