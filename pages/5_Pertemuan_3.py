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

st.markdown("**Capaian:** Siswa dapat menyelesaikan soal persamaan kuadrat menggunakan rumus ABC")

# Identitas
st.header("👤 Identitas")
nama = st.text_input("Nama Siswa:")
kelas = st.text_input("Kelas:")


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
st.header("🔍 Eksplorasi: Menemukan Metode Penyelesaian Persamaan Kuadrat Rumus ABC")

# Eksplorasi 1
with st.expander("💡Eksplorasi 1: Dapatkah kamu menyelesaikan persamaan kuadrat tanpa difaktorkan?"):
    st.markdown("""
    Coba selesaikan persamaan kuadrat di bawah ini dengan cara apapun yang kamu tahu.

    ### Soal:
    $$x^2 - 5x + 6 = 0$$

    Kamu boleh menggunakan tebak-tebakan, grafik, atau strategi lainnya.
    """)

    jawaban1 = st.text_area("Tuliskan bagaimana kamu menyelesaikan persamaan di atas", key="jawaban_eksplorasi1")

    if jawaban1.strip():
        with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi 1"):
            st.info("""

**Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai):**

**Prompt:**  
Bagaimana cara menyelesaikan persamaan kuadrat x^2 - 5x + 6 = 0? Jelaskan beberapa metode termasuk faktorisasi, grafik, dan metode lainnya jika ada.

✅ Setelah membaca penjelasan AI, bandingkan dengan strategi yang kamu gunakan.

📝 **Refleksi:** Apa metode paling mudah menurutmu? Apakah metode itu bisa digunakan untuk semua bentuk persamaan kuadrat?
"""
                )
            st.text_area("Tulis jawaban refleksi Eksplorasi 1 di sini...", key="refleksi_eksplorasi1", height=80)


# Eksplorasi 2
if st.session_state.get("jawaban_eksplorasi1", "").strip():
    with st.expander("💡Eksplorasi 2: Bagaimana jika persamaan kuadrat tidak bisa difaktorkan?"):
        st.markdown("""
        Sekarang coba selesaikan persamaan kuadrat ini:
    
        ### Soal:
        $$x^2 - 4x + 2 = 0$$
    
        Apakah kamu bisa menyelesaikannya dengan metode yang sama seperti tadi?
        """)
    
        jawaban2 = st.text_area("Ceritakan bagaimana kamu mencoba menyelesaikan soal tersebut", key="jawaban_eksplorasi2")
    
        if jawaban2.strip():
            with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi 2"):
                st.info("""
**Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai):**

**Prompt:**
Bagaimana cara menyelesaikan persamaan kuadrat x^2 - 4x + 2 = 0 jika tidak bisa difaktorkan secara langsung?
    
    ✅ Setelah membaca penjelasan AI, bandingkan dengan cara kamu menyelesaikan.
    
    📝 **Refleksi:** Apa kelemahan metode faktorisasi? Kapan kita butuh cara lain selain faktorisasi?
    """
                )
                st.text_area("Tulis jawaban refleksi Eksplorasi 2 di sini...", key="refleksi_eksplorasi2", height=80)

# Eksplorasi 3
if st.session_state.get("jawaban_eksplorasi2", "").strip():
    with st.expander("💡Eksplorasi 3: Apa pola akar jika nilai $$a, b,$$ dan $$c$$ diubah?"):
        st.markdown("""
        Coba masukkan berbagai nilai $$a$$, $$b$$, dan $$c$$ lalu perhatikan bentuk akar-akarnya.
        """)
    
        a3 = st.number_input("Masukkan nilai $$a$$:", value=1, step=1, key="a3")
        b3 = st.number_input("Masukkan nilai $$b$$:", value=0, step=1, key="b3")
        c3 = st.number_input("Masukkan nilai $$c$$:", value=0, step=1, key="c3")
    
        x = sp.symbols('x')
        akar_eksplorasi = sp.solve(a3 * x**2 + b3 * x + c3, x)
        akar_str = ", ".join([sp.latex(akar) for akar in akar_eksplorasi])
    
        st.latex(f"Akar-akarnya: {akar_str}")
    
        pola = st.text_area("Apa yang kamu perhatikan dari akar-akar ini ketika nilai a, b, dan c berubah?", key="analisis_pola_abc")
    
        if pola.strip():
            with st.expander("🔍Cek Pola dengan AI"):
                st.info("""
    
    **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai):**
    
    **Prompt:**
    Apa pola akar-akar dari persamaan kuadrat jika diketahui nilai \(a\), \(b\), dan \(c\)? Apakah ada hubungan umum yang bisa ditemukan?
    
    ✅ Coba temukan bentuk umum dari solusi berdasarkan input a, b, dan c.
    
    📝 **Refleksi:** Apakah kamu melihat adanya rumus tertentu yang bisa digunakan untuk menyelesaikan semua persamaan kuadrat?
    
    """)
                st.text_area("Tulis jawaban refleksi Eksplorasi 3 di sini...", key="refleksi_eksplorasi3", height=80)

if st.session_state.get("analisis_pola_abc", "").strip():
    with st.expander("💡Eksplorasi 4: Menyusun Rumus Penyelesaian Umum"):
        st.markdown(r"""
        Kamu sudah menemukan pola hubungan antara koefisien $$a, b,$$ dan $$c$$ terhadap akar-akar persamaan kuadrat.

        Sekarang, mari kita susun **rumus penyelesaian umum** dengan menyelesaikan bentuk umum persamaan kuadrat:  
        $$
        ax^2 + bx + c = 0
        $$

        **Langkah 1:**  
        Bagi semua suku dengan $$a$$, agar koefisien $$x^2$$ menjadi 1.
        $$
        x^2 + \frac{b}{a}x + \frac{c}{a} = 0
        $$
        """)
        
        step1 = st.text_area("✅ Tulis hasil setelah dibagi semua suku dengan a:", key="eksplorasi4_step1", height=60)

        if step1.strip():
            st.markdown(r"""
            **Langkah 2:**  
            Pindahkan konstanta ke ruas kanan:
            $$
            x^2 + \frac{b}{a}x = -\frac{c}{a}
            $$

            **Langkah 3:**  
            Lengkapi kuadrat kiri agar jadi bentuk kuadrat sempurna. Tambahkan
            \(
            \left( \frac{b}{2a} \right)^2
            \)
            ke kedua ruas.
            \[
            x^2 + \frac{b}{a}x + \left( \frac{b}{2a} \right)^2 = -\frac{c}{a} + \left( \frac{b}{2a} \right)^2
            \]
            """)
            step2 = st.text_area("✅ Apa bentuk kuadrat sempurna di ruas kiri?", key="eksplorasi4_step2", height=60)

        if st.session_state.get("eksplorasi4_step2", "").strip():
            st.markdown(r"""
            **Langkah 4:**  
            Bentuk ruas kiri menjadi kuadrat sempurna, lalu akar-kan kedua ruas:
            \[
            \left( x + \frac{b}{2a} \right)^2 = \frac{b^2 - 4ac}{4a^2}
            \]
            \[
            x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}
            \]

            **Langkah 5 (Terakhir):**  
            Isolasi \( x \) untuk mendapatkan rumus umum:
            \[
            x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
            \]
            step3 = st.text_area("✅ Apa kamu sudah mendapatkan rumus yang sama?", key="eksplorasi4_step3", height=60)
            """)
            if eksplorasi4_step3:
                st.success("🎉 Kamu berhasil menyusun **rumus kuadrat**!")
    
            if eksplorasi4_step3.strip():
               with st.expander("🔍Cek Pola dengan AI"):
                    st.info("""
    **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai):**
    
    **Prompt:**
    Bagaimana rumus \(x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\) bisa ditemukan dari bentuk umum persamaan kuadrat \(ax^2 + bx + c = 0\)?
    
    ✅ Bandingkan dengan pola yang kamu temukan di eksplorasi sebelumnya.
    
    📝 **Refleksi:** Apa kelebihan menggunakan rumus ini dibandingkan metode lainnya?
    
    """
                )
                    st.text_area("Tulis jawaban refleksi Eksplorasi 4 di sini...", key="refleksi_eksplorasi4", height=80)


# Eksplorasi 5
if st.session_state.get("eksplorasi4_step3", "").strip():
    with st.expander("💡Eksplorasi 5: Apa pengaruh nilai di dalam akar? (Diskriminan)"):
        st.markdown("""
        Sekarang kita fokus pada bagian dalam tanda akar:
    
        $$\Delta = b^2 - 4ac$$
    
        Ubah-ubah nilai a, b, dan c untuk melihat efeknya pada akar.
        """)
    
        a5 = st.number_input("a:", value=1, step=1, key="a5")
        b5 = st.number_input("b:", value=0, step=1, key="b5")
        c5 = st.number_input("c:", value=0, step=1, key="c5")
    
        D = b5**2 - 4*a5*c5
    
        st.latex(f"\Delta = {D}")
    
        if D > 0:
            jenis = "D > 0 → Dua akar real berbeda"
        elif D == 0:
            jenis = "D = 0 → Satu akar real kembar"
        else:
            jenis = "D < 0 → Akar tidak real (imajiner)"
    
        st.success(jenis)
    
        analisis_d = st.text_area("Apa kesimpulanmu tentang pengaruh nilai diskriminan terhadap jenis akar?", key="analisis_d")
    
        if analisis_d.strip():
            with st.expander("🔍Cek Penjelasan AI"):
                st.info("""
    📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai):**
    
    **Prompt:**
    Apa pengaruh nilai diskriminan \(\Delta = b^2 - 4ac\) terhadap jenis akar dari persamaan kuadrat?
    
    ✅ Coba cocokkan hasil eksperimenmu dengan teori dari AI.
    
    📝 **Refleksi:** Apakah kamu dapat menebak jenis akar hanya dari nilai \(\Delta\)?
                """
                )
                st.text_area("Tulis jawaban refleksi Eksplorasi 5 di sini...", key="refleksi_eksplorasi5", height=80)



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
if hasil_abc.strip():
    with st.expander("🔍Cek Penjelasan AI"):
            st.info("""
    **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai):**
    
    **Prompt:**
    Bagaimana cara menyelesaikan persamaan kuadrat x^2 - 5x + 6 = 0 dengan dua metode: pemfaktoran dan rumus ABC?
    
    ✅ Coba cocokkan hasil eksperimenmu dengan teori dari AI.
    
    📝 **Refleksi:** Apakah kamu dapat menebak jenis akar hanya dari nilai \(\Delta\)?
    
    """)
            st.text_area("Tulis refleksimu di sini...", key="refleksi_eksplorasiakhir", height=80)


import streamlit as st

# --- 6. Penarikan Kesimpulan ---
st.header("🎯 Penarikan Kesimpulan")
kesimpulan = st.text_area(
    "Apa kesimpulanmu dari hasil eksplorasi metode rumus ABC? Manakah yang menurutmu lebih mudah atau lebih cepat?",
    key="kesimpulan_akhir"
)

if kesimpulan.strip():
    with st.expander("🔍Cek Penjelasan AI"):
            st.info("""
    **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai):**
    
    **Prompt:**
    Bandingkan dua metode penyelesaian persamaan kuadrat: metode faktorisasi dan metode rumus ABC. Berikan kelebihan dan kekurangan masing-masing serta contoh soal yang bisa diselesaikan dengan dua metode tersebut
    
    ✅ Coba cocokkan hasil eksperimenmu dengan teori dari AI.
    
    📝 **Refleksi:** Apakah kamu dapat menebak jenis akar hanya dari nilai \(\Delta\)?
    
    """)
            st.text_area("Tulis refleksi dari pertemuan 3 di sini...", key="refleksi_p3", height=80)



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





















