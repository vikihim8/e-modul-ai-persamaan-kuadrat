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

import streamlit as st
from sympy import symbols, expand

# Stimulus
st.subheader("📍 Stimulus")
st.write("Diketahui grafik fungsi kuadrat memotong sumbu X di x = 2 dan x = 3")
st.image("pages/grafik_pq.png", caption="Contoh Grafik p dan q", use_container_width=True)
stimulusp2 = st.text_input("Apa yang bisa kamu simpulkan dari titik potong tersebut terhadap bentuk fungsi kuadrat?", placeholder="Tulis jawabanmu di sini...", key ="stimulusp2")
if stimulusp2:
    st.success("✅ Jawabanmu telah dicatat")

# Identifikasi Masalah
st.subheader("🔍 Identifikasi Masalah")
identifikasi = st.text_area("Apa yang ingin kamu ketahui atau cari berdasarkan grafik di atas?")
pertanyaan = st.text_input("Tuliskan satu pertanyaan utamamu di sini:", placeholder="Tulis jawabanmu di sini...", key="pertanyaan")
if pertanyaan:
    st.success("✅ Jawabanmu telah dicatat, Mari lanjutkan ke tahap eksplorasi")

# --- Eksplorasi 1: Menentukan Akar-akar dari Grafik ---
with st.expander("💡 Eksplorasi 1: Menentukan **Akar-akar dari Grafik**"):
    st.markdown("""
    Grafik fungsi kuadrat memotong sumbu $$x$$ di $$x = 2$$ dan $$x = 3$$.  
    Itu artinya nilai $$x$$ yang membuat $$y = 0$$ adalah akar-akar dari fungsi kuadrat tersebut.
    """)

    # Input akar-akar
    akar1 = st.number_input("Masukkan akar pertama:", key="akar1_input", step=1)
    akar2 = st.number_input("Masukkan akar kedua:", key="akar2_input", step=1)

    # Simpan ke session state
    st.session_state.akar1 = akar1
    st.session_state.akar2 = akar2

    # Tampilkan bentuk faktornya langsung jika sudah diisi
    if akar1 != 0 or akar2 != 0:
        st.latex(f"f(x) = a(x - {akar1})(x - {akar2})")
        st.write("Bentuk ini disebut *bentuk faktor* dari fungsi kuadrat.")

    # --- Analisis ---
    analisis1p2 = st.text_area(
        """
**💡 Instruksi Analisis:**

1. Amati grafik fungsi kuadrat yang memotong sumbu $$x$$ di dua titik berbeda.  
2. Tentukan koordinat titik potong tersebut.  
3. Hubungkan titik potong itu dengan akar-akar fungsi kuadrat.  
4. Tuliskan kesimpulan hubungan antara titik potong grafik dengan akar-akar fungsi kuadrat.
        """,
        key="analisis1p2",
        height=100
    )

    # --- Cek AI ---
    if analisis1p2.strip():
        with st.expander("🔍 Cek Hasil Verifikasi AI Eksplorasi 1"):
            st.info("""
📌 **Instruksi Cek AI:**  
Salin prompt berikut ke **3 AI berbeda** ([Perplexity AI](https://www.perplexity.ai), [Gemini AI](https://gemini.google.com/app), [ChatGPT](https://chatgpt.com/)) untuk membandingkan hasil.

**Prompt:**  
> Apa hubungan antara akar-akar fungsi kuadrat dan titik potong grafik terhadap sumbu x?  
> Jelaskan secara rinci, sertakan contoh, dan hubungan bentuk faktor dengan posisi akar di grafik.

✅ Setelah itu, verifikasi dengan [Desmos Graphing Calculator](https://www.desmos.com/calculator) menggunakan contoh:
- `y = (x - 2)(x - 3)`

Lalu perhatikan apakah titik potongnya sesuai dengan akar-akarnya.
            """)

        # --- Refleksi ---
        refleksi1p2 = st.text_area(
            "📝 Refleksi: Apa hubungan pasti antara akar-akar fungsi kuadrat dengan titik potong sumbu x pada grafiknya?",
            key="refleksi_eksplorasi1p2",
            height=80
        )

        # --- Verifikasi ---
        if refleksi1p2.strip():
            st.success("✅ Refleksi sudah diisi. Berikut materi verifikasinya 👇")
            with st.expander("📖 Verifikasi Jawaban"):
                st.markdown("""
                **📚 Materi Verifikasi:**
                
                - **Akar-akar fungsi kuadrat** adalah nilai $$x$$ yang membuat $$y = 0$$.  
                - Pada grafik, akar-akar ini adalah **titik potong grafik dengan sumbu x**.  
                - Jika persamaan dalam bentuk faktor: $$y = a(x - r_1)(x - r_2)$$  
                  maka:
                  - $$r_1$$ = titik potong pertama
                  - $$r_2$$ = titik potong kedua  
                - Jika hanya ada satu akar (diskriminan = 0), grafik menyentuh sumbu x di satu titik.
                """)

# ------------------------- Eksplorasi 2 -------------------------
if st.session_state.get("analisis1p2"):
    st.subheader("🔬 Eksplorasi 2: Membangun Fungsi Kuadrat dari Akar-akar")

    akar1 = st.number_input("Masukkan akar pertama (p):", step=1, key="akar1p2_input")
    akar2 = st.number_input("Masukkan akar kedua (q):", step=1, key="akar2p2_input")

    if akar1 and akar2:
        # Bentuk faktornya
        st.markdown("### ✍️ Bentuk Umum Fungsi Kuadrat")
        st.latex(rf"f(x) = (x - {akar1})(x - {akar2})")

        # Hitung koefisien
        a = 1
        b = -(akar1 + akar2)
        c = akar1 * akar2
        st.latex(rf"f(x) = x^2 + ({b})x + ({c})")

        # Analisis
        analisis2 = st.text_area("🔎 Tuliskan penjelasanmu: bagaimana kamu menyusun fungsi kuadrat tersebut?", key="analisis2_input")

        if analisis2:
            with st.expander("📘 Cek jawaban dengan AI"):
                st.markdown("""
                **Prompt yang digunakan untuk semua AI:**
                > Bagaimana cara menyusun fungsi kuadrat jika diketahui dua akarnya?

                **🔗 Cek di AI berikut:**
                - [Perplexity AI](https://www.perplexity.ai)  
                - [Gemini](https://gemini.google.com)  
                - [ChatGPT](https://chat.openai.com)  
                """)

            refleksi2 = st.text_area("✍️ Tulis refleksi Eksplorasi 2 setelah membandingkan dengan AI:", key="refleksi_eksplorasi2")
            if refleksi2:
                with st.expander("📚 Verifikasi Materi Eksplorasi 2"):
                    st.markdown("""
                    - Jika diketahui akar-akar $p$ dan $q$, bentuk faktornya adalah:  
                      $$f(x) = a(x - p)(x - q)$$
                    - Untuk $a = 1$, bentuk umumnya menjadi:  
                      $$f(x) = x^2 - (p+q)x + pq$$
                    - Nilai $b = -(p+q)$ dan $c = pq$.
                    """)


# ------------------------- Eksplorasi 3 -------------------------
if st.session_state.get("analisis2_input"):
    st.subheader("🔬 Eksplorasi 3: Pengaruh Nilai a terhadap Bentuk Umum Fungsi Kuadrat")
    from sympy import symbols, expand
    import sympy as sp

    a_eksplorasi = st.number_input("🔢 Masukkan nilai a", value=1, key="a_eksplorasi3")
    akar1 = st.number_input("🧮 Akar pertama", value=0, step=1, key="akar1_eksplorasi3")
    akar2 = st.number_input("🧮 Akar kedua", value=0, step=1, key="akar2_eksplorasi3")

    x = symbols('x')
    f_eksplorasi = a_eksplorasi * (x - akar1) * (x - akar2)
    st.latex(f"f(x) = {sp.latex(expand(f_eksplorasi))}")

    analisis3 = st.text_area("Apa yang kamu perhatikan dari perubahan nilai a?", key="analisis3_input")
    if analisis3:
        with st.expander("📘 Cek jawaban dengan AI"):
            st.markdown("""
            **Prompt yang digunakan untuk semua AI:**
            > Bagaimana pengaruh nilai a terhadap bentuk grafik fungsi kuadrat dalam bentuk umum?

            **🔗 Cek di AI berikut:**
            - [Perplexity AI](https://www.perplexity.ai)  
            - [Gemini](https://gemini.google.com)  
            - [ChatGPT](https://chat.openai.com)  
            """)
        refleksi3 = st.text_area("✍️ Tulis refleksi Eksplorasi 3 setelah membandingkan dengan AI:", key="refleksi_eksplorasi3")
        if refleksi3:
            with st.expander("📚 Verifikasi Materi Eksplorasi 3"):
                st.markdown("""
                - Nilai $a$ menentukan lebar dan arah buka parabola:
                  - $a > 0$: parabola terbuka ke atas  
                  - $a < 0$: parabola terbuka ke bawah  
                - Semakin besar $|a|$, parabola semakin sempit.
                """)


# ------------------------- Eksplorasi 4 -------------------------
if st.session_state.get("analisis3_input"):
    st.header("✍️ Eksplorasi 4: Hubungan Akar-akar dengan Koefisien b dan c")
    x = symbols('x')

    nilai_a = st.number_input("Masukkan nilai a", value=1, key="nilai_a_input4")
    nilai_p = st.number_input("Masukkan nilai p", value=1, key="nilai_p_input4")
    nilai_q = st.number_input("Masukkan nilai q", value=2, key="nilai_q_input4")

    bentuk_umum = expand(nilai_a * (x - nilai_p) * (x - nilai_q))
    st.latex("f(x) = " + sp.latex(bentuk_umum))

    analisis4 = st.text_area("Apa pola hubungan antara p, q dengan b dan c?", key="analisis4_input")
    if analisis4:
        with st.expander("📘 Cek jawaban dengan AI"):
            st.markdown("""
            **Prompt yang digunakan untuk semua AI:**
            > Bagaimana hubungan antara akar-akar p dan q dengan koefisien b dan c pada fungsi kuadrat?

            **🔗 Cek di AI berikut:**
            - [Perplexity AI](https://www.perplexity.ai)  
            - [Gemini](https://gemini.google.com)  
            - [ChatGPT](https://chat.openai.com)  
            """)
        refleksi4 = st.text_area("✍️ Tulis refleksi Eksplorasi 4 setelah membandingkan dengan AI:", key="refleksi_eksplorasi4")
        if refleksi4:
            with st.expander("📚 Verifikasi Materi Eksplorasi 4"):
                st.markdown("""
                - Untuk $f(x) = a(x - p)(x - q)$ berlaku:
                  - $b = -a(p + q)$
                  - $c = apq$
                - Hubungan ini berlaku untuk semua nilai $a$, $p$, dan $q$.
                """)


# ------------------------- Eksplorasi 5 -------------------------
if st.session_state.get("analisis4_input"):
    st.subheader("🔬 Eksplorasi 5: Kesimpulan Umum Bentuk Faktor dan Bentuk Umum")
    kesimpulan5 = st.text_area("✍️ Tuliskan kesimpulanmu di sini:", key="kesimpulan5_input")

    if kesimpulan5:
        with st.expander("📘 Cek jawaban dengan AI"):
            st.markdown("""
            **Prompt yang digunakan untuk semua AI:**
            > Bagaimana mengubah bentuk umum fungsi kuadrat menjadi bentuk faktor dan menemukan akarnya?

            **🔗 Cek di AI berikut:**
            - [Perplexity AI](https://www.perplexity.ai)  
            - [Gemini](https://gemini.google.com)  
            - [ChatGPT](https://chat.openai.com)  
            """)
        refleksi5 = st.text_area("✍️ Tulis refleksi Eksplorasi 5 setelah membandingkan dengan AI:", key="refleksi_eksplorasi5")
        if refleksi5:
            with st.expander("📚 Verifikasi Materi Eksplorasi 5"):
                st.markdown(r"""
                - Bentuk umum: $f(x) = ax^2 + bx + c$  
                - Bentuk faktor: $f(x) = a(x - p)(x - q)$ dengan $p$ dan $q$ adalah akar-akar persamaan kuadrat.  
                - Untuk mengubah bentuk umum ke bentuk faktor, gunakan rumus akar-akar:
                  $$p, q_{\text{akar}} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
                """)



# 4. Pengolahan Data
st.header("📝 Pengolahan Data")
st.write("Faktorkan bentuk berikut:")

st.latex(r"f(x) = x^2 - 7x + 10")

analisisdata = st.text_input("Tulis bentuk faktornya:")

if analisisdata.strip():
    st.success("✅ Jawaban disimpan.")

    

# --- 5. Pembuktian (Verifikasi) ---
st.header("🔍 Verifikasi Pembuktian")
st.info("Cek kembali jawaban pembuktianmu dengan bantuan AI dan grafik dari Desmos (jika relevan).")

# Expander: petunjuk prompt dan link ke beberapa AI eksternal
with st.expander("📘 Cek jawaban dengan AI untuk soal ini"):
    st.markdown(
        """
**Prompt yang digunakan untuk semua AI:**  
> Sebuah fungsi kuadrat diberikan dalam bentuk umum $f(x) = x^2 - 7x + 10$.  
> Faktorkan fungsi tersebut menjadi bentuk $(x - p)(x - q)$.  
> Tunjukkan proses langkah demi langkah bagaimana menemukan nilai $p$ dan $q$, beserta alasan matematisnya.

**🔗 Cek di AI berikut:**  
- [Perplexity AI](https://www.perplexity.ai) — tempel prompt di kolom pencarian.  
- [Gemini (Google)](https://gemini.google.com) — tempel prompt dan bandingkan hasilnya.  
- [ChatGPT (OpenAI)](https://chat.openai.com) — tempel prompt dan lihat penjelasan langkah demi langkah.
"""
    )

# (Opsional) Verifikasi Desmos jika ingin visualisasi grafiknya
with st.expander("📈 Verifikasi bentuk grafik fungsi dengan Desmos:"):
    st.markdown("""
    🌐 Buka [Desmos Graphing Calculator](https://www.desmos.com/calculator)  
    Masukkan fungsi: `x^2 - 7x + 10`
    
    Perhatikan:
    - Apakah grafik memotong sumbu-x di $x = 2$ dan $x = 5$?  
    - Apakah grafik terbuka ke atas?  
    - Apakah titik potong sumbu-y di $y = 10$?
    """)

# Konfirmasi siswa
verifikasi = st.radio(
    "Apakah jawabanmu sesuai dengan hasil AI dan grafik Desmos?",
    ["Ya", "Tidak", "Sebagian"],
    key="verifikasi_pembuktian"
)

if verifikasi:
    st.session_state["verifikasi_pembuktian_done"] = True

# Materi verifikasi
with st.expander("📚 Materi Verifikasi Pembuktian"):
    st.markdown("""
    **Materi yang benar sesuai soal:**
    - **Bentuk umum:** $f(x) = x^2 - 7x + 10$  
    - Cari $p$ dan $q$ dengan mencari dua bilangan yang hasilnya $10$ (c) dan jumlahnya $-7$ (b).  
      → $p = 2$, $q = 5$  

    **Bentuk faktor:**  
    $$f(x) = (x - 2)(x - 5)$$  

    - Grafiknya parabola terbuka ke atas karena $a = 1 > 0$.  
    - Titik potong sumbu-x: $(2,0)$ dan $(5,0)$  
    - Titik potong sumbu-y: $(0,10)$
    """)



# --- 6. Penarikan Kesimpulan ---
st.header("🎯 Penarikan Kesimpulan")

# Input kesimpulan dari pengguna
kesimpulan = st.text_area(
    "📚 Apa kesimpulan yang kamu dapatkan dari aktivitas ini?",
    key="kesimpulan_faktorisasi",
    height=120
)

# Tampilkan notifikasi jika kesimpulan sudah diisi
if kesimpulan.strip() != "":
    st.success("✅ Kesimpulan kamu telah dicatat. Selesai.")

    # Bandingkan dengan AI eksternal
    with st.expander("🤖 Bandingkan Kesimpulanmu dengan AI Eksternal"):
        st.markdown("""
        **Prompt yang digunakan untuk semua AI:**
        > Buatkan kesimpulan singkat dan jelas tentang bagaimana cara memfaktorkan bentuk kuadrat $f(x) = x^2 - 7x + 10$ dan apa yang bisa dipelajari dari proses tersebut.

        **🔗 Cek di AI berikut:**
        - [Perplexity AI](https://www.perplexity.ai)  
        - [Gemini](https://gemini.google.com)  
        - [ChatGPT](https://chat.openai.com)  
        """)

    # Materi verifikasi kesimpulan
    with st.expander("📚 Materi Verifikasi Kesimpulan"):
        st.markdown("""
        **Cara Memfaktorkan Bentuk Kuadrat:**
        1. Bentuk umum: $$f(x) = ax^2 + bx + c$$  
        2. Cari dua bilangan yang:
           - Hasil kalinya = $$a*c$$
           - Jumlahnya = $$b$$
        3. Pecah suku tengah menggunakan dua bilangan tersebut.
        4. Kelompokkan dan faktorkan per kelompok.
        5. Gabungkan faktor yang sama untuk mendapatkan bentuk akhir.

        **Contoh Soal:**  
        $$f(x) = x^2 - 7x + 10$$  
        - Hasil kali: $$1*10 = 10$$  
        - Jumlah: $$-7$$  
        → Bilangan: $$-5$$ dan $$-2$$  

        **Pecah suku tengah:**  
        $$x^2 - 5x - 2x + 10$$  

        **Kelompokkan:**  
        $$(x^2 - 5x) - (2x - 10)$$  

        **Faktorkan:**  
        $$x(x - 5) - 2(x - 5)$$  

        **Hasil akhir:**  
        $$f(x) = (x - 2)(x - 5)$$  

        **Ringkasan:**
        - Faktorisasi membantu menemukan akar persamaan kuadrat dengan cepat.
        - Akar dari contoh di atas: $$x = 2$$ dan $$x = 5$$
        - Grafiknya parabola terbuka ke atas, memotong sumbu-x di dua titik tersebut.
        """)
else:
    st.warning("✍️ Silakan isi kesimpulan terlebih dahulu sebelum melihat versi AI.")



# --- Refleksi Akhir ---
st.subheader("🪞 Refleksi Belajar")
refleksi = st.radio("Seberapa yakin kamu memahami materi faktorisasi fungsi kuadrat?", 
                    ["Tidak yakin", "Kurang yakin", "Cukup yakin", "Yakin", "Sangat yakin"])

kuis = st.radio("Jika f(x) = x² - 6x + 8, maka faktornya adalah ...", 
                ["(x - 2)(x - 4)", "(x + 2)(x + 4)", "(x - 6)(x + 8)", "Tidak bisa difaktorkan"])

cek = ""
if kuis:
    if kuis == "(x - 2)(x - 4)":
        st.success("✅ Jawaban benar! Karena -2 dan -4 jika dijumlahkan hasilnya -6, dan jika dikalikan hasilnya 8.")
        cek = "Benar"
    else:
        st.error("❌ Jawaban belum tepat. Perhatikan kembali hubungan antara koefisien dan konstanta.")
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


























