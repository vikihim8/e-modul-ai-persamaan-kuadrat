import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import sympy as sp



# --- Judul Halaman ---
st.title("📘 Pertemuan 1: Menemukan Bentuk Umum dan Grafik Fungsi Kuadrat")
st.markdown("**Capaian:** Siswa dapat mengidentifikasi bentuk umum persamaan kuadrat dan menganalisis pengaruh koefisien terhadap bentuk grafik.")

# Setup Spreadsheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
json_creds = st.secrets["gcp_service_account"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(json_creds, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("18g9_lCQQDjyU85TJpBUZRzJIrFmrVPeCnjNg4DqrPx8").sheet1

def simpan_ke_sheet(nama, kelas, pertemuan, skor, jawaban, refleksi):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([nama, kelas, pertemuan, skor, jawaban, refleksi, waktu])

# Identitas
st.header("👤 Identitas")
nama = st.text_input("Nama Siswa:")
kelas = st.text_input("Kelas:")


# --- Stimulus dan Identifikasi Masalah ---
st.header("📌 Stimulus")
st.write("Bayangkan kamu sedang menonton lintasan bola dilempar ke udara. Bentuknya seperti parabola. Mari kita pelajari grafik fungsi kuadrat dari fenomena tersebut.")
stimulus = st.text_input("📝 Apa yang kamu pikirkan tentang bentuk lintasan parabola ini?", placeholder="Tulis jawabanmu di sini...", key="stimulus")
if stimulus:
    st.success("✅ Jawabanmu telah dicatat")


st.header("🔍 Identifikasi Masalah")
masalah = st.text_input("❓ Pertanyaan apa yang muncul di benakmu terkait grafik lintasan itu?", placeholder="Tulis jawabanmu di sini...", key="masalah")
if masalah:
    st.success("✅ Jawabanmu telah dicatat, Mari lanjutkan ke tahap eksplorasi")


st.header("🔍 Pengumpulan Data")
st.write(
    "Bentuk umum dari suatu persamaan kuadrat yaitu $$y = ax^2 + bx + c$$, dengan $$a$$ adalah koefisien variabel $$x^2$$, $$b$$ adalah koefisien variabel $$x$$, dan $$c$$ adalah konstanta. Mari kita lakukan eksplorasi berikut:"
)

# --- Eksplorasi 1: Pengaruh Nilai a terhadap Bentuk Grafik ---
with st.expander("💡 Eksplorasi 1: Bagaimana pengaruh nilai a terhadap bentuk grafik? Apa yang terjadi jika **$$a = 0$$**? Apa yang terjadi jika **$$a ≠ 0$$**?"):

    # Input nilai a, b, c
    a1 = st.number_input("Masukkan nilai $a = 0$ dan $a ≠ 0$ (koefisien $x^2$):", value=0, step=1, key="a1")
    b1 = st.number_input("Masukkan nilai $b$ (koefisien $x$):", value=0, step=1, key="b1")
    c1 = st.number_input("Masukkan nilai $c$ (konstanta):", value=0, step=1, key="c1")

    # Status tombol untuk menampilkan grafik
    if "grafik1_ditampilkan" not in st.session_state:
        st.session_state.grafik1_ditampilkan = False

    if st.button("Tampilkan Grafik Eksplorasi 1"):
        st.session_state.grafik1_ditampilkan = True

    # Tampilkan grafik jika tombol sudah ditekan
    if st.session_state.grafik1_ditampilkan:
        x = np.linspace(-10, 10, 400)
        y = a1 * x**2 + b1 * x + c1
        fig, ax = plt.subplots()
        ax.plot(x, y, label=f"$y = {a1}x^2 + {b1}x + {c1}$")
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(True)
        ax.legend()
        ax.set_title("Grafik Fungsi Kuadrat")
        st.pyplot(fig)

    # --- Analisis ---
    analisis1 = st.text_area(
        """
**💡 Instruksi Analisis:**

1. Masukkan nilai $a = 0$ dan atur nilai $b$ & $c$ sesuai kemauanmu.  
   ➡️ Amati bentuk grafiknya.

2. Masukkan nilai $a ≠ 0$ dan atur nilai $b$ & $c$ sesuai kemauanmu.  
   ➡️ Amati bentuk grafiknya.

3. Bandingkan kedua grafik tersebut dan tuliskan hasil pengamatanmu.
        """,
        key="analisis1",
        height=100
    )

    # --- Cek AI ---
    if analisis1.strip():
        with st.expander("🔍 Cek Hasil Verifikasi AI Eksplorasi 1"):
            st.info("""
📌 **Instruksi Cek AI:**  
Salin prompt berikut ke **3 AI berbeda** ([Perplexity AI](https://www.perplexity.ai), [Gemini AI](https://gemini.google.com/app), [ChatGPT](https://chatgpt.com/)) untuk membandingkan hasil.

**Prompt:**  
> Jelaskan secara rinci apa yang terjadi pada grafik fungsi kuadrat jika a = 0 dan jika a ≠ 0 dalam persamaan y = ax² + bx + c.  
> Jelaskan perubahan bentuk grafik, apakah masih berupa parabola atau tidak, dan sertakan perbandingan visual.

✅ Setelah itu, verifikasi dengan [Desmos Graphing Calculator](https://www.desmos.com/calculator) menggunakan dua contoh:
- `y = 2x² + 3x + 1`
- `y = 0x² + 3x + 1`

Lalu bandingkan bentuk grafiknya.
            """)

        # --- Refleksi ---
        refleksi_eksplorasi1 = st.text_area(
            "📝 Refleksi: Apa perbedaan utama antara grafik fungsi kuadrat saat $a ≠ 0$ dan saat $a = 0$?",
            key="refleksi_eksplorasi1",
            height=80
        )

        # --- Verifikasi ---
        if refleksi_eksplorasi1.strip():
            st.success("✅ Refleksi sudah diisi. Berikut materi verifikasinya 👇")
            with st.expander("📖 Verifikasi Jawaban"):
                st.markdown("""
                **📚 Materi Verifikasi:**

                - **Jika $a ≠ 0$**  
                  Fungsi berbentuk kuadrat (**grafiknya parabola**).  
                  - $a > 0$ → parabola membuka ke atas.  
                  - $a < 0$ → parabola membuka ke bawah.  
                  - Memiliki titik puncak & sumbu simetri.

                - **Jika $a = 0$**  
                  Fungsi berubah menjadi persamaan linear $$y = bx + c$$ (**grafiknya garis lurus**).  
                  - Kemiringan garis ditentukan oleh nilai $$b$$.  
                  - Tidak memiliki titik puncak atau sumbu simetri.
                """)



# Eksplorasi 2 (Hanya dibuka jika eksplorasi 1 sudah selesai)
if st.session_state.get("analisis1"):
    with st.expander("💡 Eksplorasi 2: Pengaruh Nilai $b$ terhadap Posisi Grafik"):
        
        b2 = st.number_input("Masukkan nilai $b$:", value=0, step=1, key="b2")

        if "grafik2_ditampilkan" not in st.session_state:
            st.session_state.grafik2_ditampilkan = False

        if st.button("Tampilkan Grafik Eksplorasi 2"):
            st.session_state.grafik2_ditampilkan = True

        # Gambar grafik jika tombol pernah ditekan
        if st.session_state.grafik2_ditampilkan:
            x = np.linspace(-10, 10, 400)
            y = x**2 + b2 * x
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)
            ax.set_title(f"Grafik y = x² + {b2}x")
            st.pyplot(fig)

            # --- Analisis ---
            analisis2 = st.text_area(
                """
**💡 Instruksi Analisis:**

1. Ubah nilai $b$ menjadi beberapa angka berbeda (positif, negatif, dan nol).
2. Amati bagaimana **sumbu simetri** dan **titik puncak** berpindah.
3. Bandingkan pergeseran grafik untuk setiap perubahan nilai $b$.
                """,
                key="analisis2",
                height=100
            )

            # --- Cek AI muncul hanya jika analisis diisi ---
            if analisis2.strip():
                with st.expander("🔍 Cek Hasil Verifikasi AI Eksplorasi 2"):
                    st.info("""
📌 **Instruksi Cek AI:**  
Salin prompt berikut ke **3 AI berbeda** ([Perplexity AI](https://www.perplexity.ai), [Gemini AI](https://gemini.google.com/app), [ChatGPT](https://chatgpt.com/)) untuk membandingkan hasil.

**Prompt:**  
> Jelaskan bagaimana perubahan nilai b memengaruhi posisi grafik fungsi kuadrat y = ax² + bx + c, khususnya terhadap sumbu simetri dan titik puncak.  
> Sertakan ilustrasi atau contoh grafik untuk beberapa nilai b yang berbeda.

✅ Setelah itu, verifikasi dengan [Desmos Graphing Calculator](https://www.desmos.com/calculator) menggunakan contoh:
- `y = x² + 4x + 1`
- `y = x² - 7x + 1`
- `y = x² + 0x + 1`

Amati bagaimana sumbu simetri & titik puncak berubah saat nilai $b$ berbeda.
                    """)

                # --- Refleksi muncul setelah cek AI ---
                refleksi_eksplorasi2 = st.text_area(
                    "📝 Refleksi: Apa yang terjadi pada sumbu simetri dan titik puncak ketika nilai $b$ berubah?",
                    key="refleksi_eksplorasi2",
                    height=80
                )

                # --- Verifikasi hanya muncul jika refleksi diisi ---
                if refleksi_eksplorasi2.strip():
                    st.success("✅ Refleksi sudah diisi. Berikut materi verifikasinya 👇")

                    with st.expander("📖 Verifikasi Jawaban"):
                        st.markdown("""
                        **📚 Materi Verifikasi:**
                        
                        - Perubahan nilai $b$ **tidak mengubah bentuk parabola**, tetapi **menggeser posisi puncak parabola secara horizontal**.
                        - **Sumbu simetri** dapat ditentukan dari rumus $x_{\\text{puncak}} = \\frac{-b}{2a}$.  
                          Semakin besar nilai $|b|$, semakin jauh pergeserannya dari sumbu $y$.
                        - **Titik puncak** ikut berpindah sesuai perubahan $b$, baik ke kiri maupun ke kanan.
                        """)




# --- Eksplorasi 3: Pengaruh Nilai b Negatif ---
if st.session_state.get("analisis2"):
    with st.expander("💡 Eksplorasi 3: Apa pengaruh nilai $b$ negatif terhadap arah dan letak grafik fungsi kuadrat?"):

        a3 = st.number_input("Masukkan nilai $a$:", value=1, step=1, key="a3")
        b3 = st.number_input("Masukkan nilai $b$ (negatif):", value=-1, step=1, key="b3")
        c3 = st.number_input("Masukkan nilai $c$:", value=0, step=1, key="c3")

        if "grafik3_ditampilkan" not in st.session_state:
            st.session_state.grafik3_ditampilkan = False

        if st.button("Tampilkan Grafik Eksplorasi 3"):
            st.session_state.grafik3_ditampilkan = True

        if st.session_state.grafik3_ditampilkan:
            x = np.linspace(-10, 10, 400)
            y = a3 * x**2 + b3 * x + c3
            fig, ax = plt.subplots()
            ax.plot(x, y, label=f"$y = {a3}x^2 + ({b3})x + {c3}$")
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)
            ax.grid(True)
            ax.legend()
            ax.set_title("Grafik Fungsi Kuadrat dengan Nilai b Negatif")
            st.pyplot(fig)

            analisis3 = st.text_area(
                """
**💡 Instruksi Analisis:**

1. Masukkan nilai $b$ negatif dengan $a$ dan $c$ tetap.  
   ➡️ Amati posisi titik puncak dan arah grafiknya.

2. Bandingkan dengan grafik ketika $b$ bernilai positif.  
   ➡️ Catat perbedaan letak sumbu simetri dan titik puncak.

3. Tuliskan hasil pengamatanmu.
                """,
                key="analisis3",
                height=100
            )

            if analisis3.strip():
                with st.expander("🔍 Cek Hasil Verifikasi AI Eksplorasi 3"):
                    st.info("""
📌 **Instruksi Cek AI:**  
Salin prompt berikut ke **3 AI berbeda** ([Perplexity AI](https://www.perplexity.ai), [Gemini AI](https://gemini.google.com/app), [ChatGPT](https://chatgpt.com)) untuk membandingkan hasil.

**Prompt:**  
> Jelaskan pengaruh nilai $b$ negatif terhadap letak sumbu simetri dan posisi grafik fungsi kuadrat y = ax² + bx + c.  
> Bandingkan dengan saat $b$ positif dan sertakan visualisasi perbedaan grafiknya.

✅ Uji di [Desmos Graphing Calculator](https://www.desmos.com/calculator) dengan:
- `y = x² + 4x + 1`
- `y = x² - 4x + 1`

Amati perubahan posisi titik puncak dan sumbu simetri.
                    """)

                refleksi_eksplorasi3 = st.text_area(
                    "📝 Refleksi: Apa pengaruh nilai $b$ negatif terhadap letak grafik fungsi kuadrat dibandingkan $b$ positif?",
                    key="refleksi_eksplorasi3",
                    height=80
                )

                if refleksi_eksplorasi3.strip():
                    st.success("✅ Refleksi sudah diisi. Berikut materi verifikasinya 👇")

                    with st.expander("📖 Verifikasi Jawaban"):
                        st.markdown("""
                        **📚 Materi Verifikasi:**

                        - Nilai $b$ negatif **menggeser titik puncak parabola ke arah kanan** dibandingkan jika $b$ positif (dengan $a$ tetap).
                        - **Sumbu simetri** ditentukan dari rumus $x_{\\text{puncak}} = \\frac{-b}{2a}$.  
                          Jika $b < 0$, nilai $x_{\\text{puncak}}$ menjadi positif → puncak bergeser ke kanan.
                        - **Arah parabola** tetap ditentukan oleh tanda $a$, bukan $b$.
                        """)




# --- Eksplorasi 4: Pengaruh Nilai b Positif ---
if st.session_state.get("analisis3"):
    with st.expander("💡 Eksplorasi 4: Apa pengaruh nilai $b$ positif terhadap arah dan letak grafik fungsi kuadrat?"):

        a4 = st.number_input("Masukkan nilai $a$:", value=1, step=1, key="a4")
        b4 = st.number_input("Masukkan nilai $b$ (positif):", value=1, step=1, key="b4")
        c4 = st.number_input("Masukkan nilai $c$:", value=0, step=1, key="c4")

        if "grafik4_ditampilkan" not in st.session_state:
            st.session_state.grafik4_ditampilkan = False

        if st.button("Tampilkan Grafik Eksplorasi 4"):
            st.session_state.grafik4_ditampilkan = True

        if st.session_state.grafik4_ditampilkan:
            x = np.linspace(-10, 10, 400)
            y = a4 * x**2 + b4 * x + c4
            fig, ax = plt.subplots()
            ax.plot(x, y, label=f"$y = {a4}x^2 + ({b4})x + {c4}$")
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)
            ax.grid(True)
            ax.legend()
            ax.set_title("Grafik Fungsi Kuadrat dengan Nilai b Positif")
            st.pyplot(fig)

            analisis4 = st.text_area(
                """
**💡 Instruksi Analisis:**

1. Masukkan nilai $b$ positif dengan $a$ dan $c$ tetap.  
   ➡️ Amati posisi titik puncak dan arah grafiknya.

2. Bandingkan dengan grafik ketika $b$ bernilai negatif.  
   ➡️ Catat perbedaan letak sumbu simetri dan titik puncak.

3. Tuliskan hasil pengamatanmu.
                """,
                key="analisis4",
                height=100
            )

            if analisis4.strip():
                with st.expander("🔍 Cek Hasil Verifikasi AI Eksplorasi 4"):
                    st.info("""
📌 **Instruksi Cek AI:**  
Salin prompt berikut ke **3 AI berbeda** ([Perplexity AI](https://www.perplexity.ai), [Gemini AI](https://gemini.google.com/app), [ChatGPT](https://chatgpt.com)) untuk membandingkan hasil.

**Prompt:**  
> Jelaskan pengaruh nilai $b$ positif terhadap letak sumbu simetri dan posisi grafik fungsi kuadrat y = ax² + bx + c.  
> Bandingkan dengan saat $b$ negatif dan sertakan visualisasi perbedaan grafiknya.

✅ Uji di [Desmos Graphing Calculator](https://www.desmos.com/calculator) dengan:
- `y = x² - 5x + 1`
- `y = x² + 5x + 1`

Amati perubahan posisi titik puncak dan sumbu simetri.
                    """)

                refleksi_eksplorasi4 = st.text_area(
                    "📝 Refleksi: Apa pengaruh nilai $b$ positif terhadap letak grafik fungsi kuadrat dibandingkan $b$ negatif?",
                    key="refleksi_eksplorasi4",
                    height=80
                )

                if refleksi_eksplorasi4.strip():
                    st.success("✅ Refleksi sudah diisi. Berikut materi verifikasinya 👇")

                    with st.expander("📖 Verifikasi Jawaban"):
                        st.markdown("""
                        **📚 Materi Verifikasi:**

                        - Nilai $b$ positif **menggeser titik puncak parabola ke arah kiri** dibandingkan jika $b$ negatif (dengan $a$ tetap).
                        - **Sumbu simetri**: $x_{\\text{puncak}} = \\frac{-b}{2a}$.  
                          Jika $b > 0$, nilai $x_{\\text{puncak}}$ menjadi negatif → puncak bergeser ke kiri.
                        - **Arah parabola** tetap ditentukan oleh tanda $a$, bukan $b$.
                        """)



            

# --- Eksplorasi 5: Pengaruh Nilai c Negatif ---
if st.session_state.get("analisis4"):
    with st.expander("💡 Eksplorasi 5: Apa pengaruh nilai $c$ negatif terhadap grafik fungsi kuadrat?"):

        a5 = st.number_input("Masukkan nilai $a$:", value=1, step=1, key="a5")
        b5 = st.number_input("Masukkan nilai $b$:", value=0, step=1, key="b5")
        c5 = st.number_input("Masukkan nilai $c$ (negatif):", value=-1, step=1, key="c5")

        if "grafik5_ditampilkan" not in st.session_state:
            st.session_state.grafik5_ditampilkan = False

        if st.button("Tampilkan Grafik Eksplorasi 5"):
            st.session_state.grafik5_ditampilkan = True

        if st.session_state.grafik5_ditampilkan:
            x = np.linspace(-10, 10, 400)
            y = a5 * x**2 + b5 * x + c5
            fig, ax = plt.subplots()
            ax.plot(x, y, label=f"$y = {a5}x^2 + ({b5})x + ({c5})$")
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)
            ax.grid(True)
            ax.legend()
            ax.set_title("Grafik Fungsi Kuadrat dengan Nilai c Negatif")
            st.pyplot(fig)

            analisis5 = st.text_area(
                """
**💡 Instruksi Analisis:**
1. Masukkan nilai $c$ negatif dengan $a$ dan $b$ tetap.
2. Amati pergeseran grafik secara vertikal.
3. Catat perbedaan titik potong terhadap sumbu $y$ dibanding $c$ positif.
                """,
                key="analisis5",
                height=100
            )

            if analisis5.strip():
                with st.expander("🔍 Cek Hasil Verifikasi AI Eksplorasi 5"):
                    st.info("""
📌 **Instruksi Cek AI:**
Salin prompt berikut ke **3 AI berbeda** ([Perplexity AI](https://www.perplexity.ai), [Gemini AI](https://gemini.google.com/app), [ChatGPT](https://chatgpt.com/)) untuk membandingkan hasil.

**Prompt:**  
> Jelaskan pengaruh nilai $c$ negatif terhadap grafik fungsi kuadrat $y = ax^2 + bx + c$,  
> khususnya pada posisi titik potong terhadap sumbu $y$.  
> Sertakan contoh visualisasi.

✅ Uji di [Desmos](https://www.desmos.com/calculator):
- `y = x² + 4x + 3`
- `y = x² + 4x - 3`
                    """)

                refleksi5 = st.text_area(
                    "📝 Refleksi: Apa kesimpulanmu tentang pengaruh nilai $c$ negatif terhadap grafik?",
                    key="refleksi_eksplorasi5",
                    height=80
                )

                if refleksi5.strip():
                    st.success("✅ Refleksi sudah diisi. Berikut materi verifikasinya 👇")
                    with st.expander("📖 Verifikasi Jawaban"):
                        st.markdown("""
                        **📚 Materi Verifikasi:**
                        - Nilai $c$ mengatur **titik potong grafik dengan sumbu $y$**.
                        - Jika $c$ negatif, grafik bergeser ke bawah sehingga titik potong berada di bawah sumbu $x$.
                        - Pergeseran ini **tidak mengubah bentuk** atau lebar parabola, hanya posisinya secara vertikal.
                        """)


# --- Eksplorasi 6: Pengaruh Nilai c Positif ---
if st.session_state.get("analisis5"):
    with st.expander("💡 Eksplorasi 6: Apa pengaruh nilai $c$ positif terhadap grafik fungsi kuadrat?"):

        a6 = st.number_input("Masukkan nilai $a$:", value=1, step=1, key="a6")
        b6 = st.number_input("Masukkan nilai $b$:", value=0, step=1, key="b6")
        c6 = st.number_input("Masukkan nilai $c$ (positif):", value=1, step=1, key="c6")

        if "grafik6_ditampilkan" not in st.session_state:
            st.session_state.grafik6_ditampilkan = False

        if st.button("Tampilkan Grafik Eksplorasi 6"):
            st.session_state.grafik6_ditampilkan = True

        if st.session_state.grafik6_ditampilkan:
            x = np.linspace(-10, 10, 400)
            y = a6 * x**2 + b6 * x + c6
            fig, ax = plt.subplots()
            ax.plot(x, y, label=f"$y = {a6}x^2 + ({b6})x + ({c6})$")
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)
            ax.grid(True)
            ax.legend()
            ax.set_title("Grafik Fungsi Kuadrat dengan Nilai c Positif")
            st.pyplot(fig)

            analisis6 = st.text_area(
                """
**💡 Instruksi Analisis:**
1. Masukkan nilai $c$ positif dengan $a$ dan $b$ tetap.
2. Amati pergeseran grafik secara vertikal.
3. Catat perbedaan titik potong terhadap sumbu $y$ dibanding $c$ negatif.
                """,
                key="analisis6",
                height=100
            )

            if analisis6.strip():
                with st.expander("🔍 Cek Hasil Verifikasi AI Eksplorasi 6"):
                    st.info("""
📌 **Instruksi Cek AI:**
Salin prompt berikut ke **3 AI berbeda** ([Perplexity AI](https://www.perplexity.ai), [Gemini AI](https://gemini.google.com/app), [ChatGPT](https://chatgpt.com/)) untuk membandingkan hasil.

**Prompt:**  
> Jelaskan pengaruh nilai $c$ positif terhadap grafik fungsi kuadrat $y = ax^2 + bx + c$,  
> khususnya pada posisi titik potong terhadap sumbu $y$.  
> Sertakan contoh visualisasi.

✅ Uji di [Desmos](https://www.desmos.com/calculator):
- `y = x² + 4x - 1`
- `y = x² + 4x + 1`
                    """)

                refleksi6 = st.text_area(
                    "📝 Refleksi: Apa kesimpulanmu tentang pengaruh nilai $c$ positif terhadap grafik?",
                    key="refleksi_eksplorasi6",
                    height=80
                )

                if refleksi6.strip():
                    st.success("✅ Refleksi sudah diisi. Berikut materi verifikasinya 👇")
                    with st.expander("📖 Verifikasi Jawaban"):
                        st.markdown("""
                        **📚 Materi Verifikasi:**
                        - Nilai $c$ positif membuat titik potong sumbu $y$ berada di atas sumbu $x$.
                        - Pergeseran ini **hanya vertikal** dan tidak memengaruhi bentuk parabola.
                        - Semakin besar $c$, semakin tinggi letak seluruh grafik parabola.
                        """)


        


# Eksplorasi 7: Semua koefisien negatif
if st.session_state.get("analisis6"):
    with st.expander("💡Eksplorasi 7: Apa pengaruh nilai **semua koefisien negatif** terhadap grafik fungsi kuadrat?"):
        st.markdown("Masukkan nilai a, b, dan c yang semuanya negatif, lalu klik tombol untuk melihat grafik.")

        a7 = st.number_input("Masukkan nilai $$a$$ (negatif):", value=-1, step=1, key="a7")
        b7 = st.number_input("Masukkan nilai $$b$$ (negatif):", value=-1, step=1, key="b7")
        c7 = st.number_input("Masukkan nilai $$c$$ (negatif):", value=-1, step=1, key="c7")

        if a7 >= 0 or b7 >= 0 or c7 >= 0:
            st.warning("Semua nilai a, b, dan c harus negatif.")
        else:
            if st.button("Tampilkan Grafik Eksplorasi 7", key="btn7"):
                x_vals7 = sp.Symbol('x')
                x_graph7 = list(range(-10, 11))
                y_vals7 = a7 * x_vals7**2 + b7 * x_vals7 + c7
                y_graph7 = [float(y_vals7.subs(x_vals7, i)) for i in x_graph7]
                st.line_chart({"x": x_graph7, "y": y_graph7})

        analisis7 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas", key="analisis7")

        if analisis7.strip() != "":
            with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi 7"):
                st.info("""
📌Salin prompt berikut ke **3 AI berbeda** ([Perplexity AI](https://www.perplexity.ai), [Gemini AI](https://gemini.google.com/app), [ChatGPT](https://chatgpt.com/)) untuk membandingkan hasil.

**Prompt:**
Apa yang terjadi pada grafik fungsi kuadrat y = ax² + bx + c jika semua koefisien (a, b, dan c) bernilai negatif? Jelaskan bentuk grafiknya, arah bukaannya, dan posisi relatif terhadap sumbu x dan y. Sertakan contoh fungsi dan gambarnya.

✅ Coba di [Desmos](https://www.desmos.com/calculator) dengan:
- -x² - 2x - 3
- -2x² - 4x - 1

📊 Amati arah bukaannya, bentuk grafiknya, dan letak titik potong terhadap sumbu $$y$$.

📝 **Refleksi:** Apa kesimpulanmu?
""")

                refleksi7 = st.text_area("Tulis jawaban refleksi Eksplorasi 7 di sini...", key="refleksi_eksplorasi7", height=80)
            
                if refleksi7.strip():
                    st.success("✅ Refleksi sudah diisi. Berikut materi verifikasinya 👇")
                    with st.expander("📚 Materi Verifikasi"):
                        st.markdown("""
        - Nilai $$a < 0$$ (negatif) → parabola membuka ke bawah.
        - Nilai $$b < 0$$ (negatif) → sumbu simetri bergeser ke kanan.
        - Nilai $$c < 0$$ (negatif) → titik potong sumbu $$y$$ berada di bawah titik asal.
        - Semua koefisien negatif membuat grafik berada di kuadran bawah dengan puncak di atas titik potong sumbu $$y$$.
        """)


# Eksplorasi 8: Semua koefisien positif
if st.session_state.get("analisis7"):
    with st.expander("💡Eksplorasi 8: Apa pengaruh nilai **semua koefisien positif** terhadap grafik fungsi kuadrat?"):
        st.markdown("Masukkan nilai a, b, dan c yang semuanya positif, lalu klik tombol untuk melihat grafik.")

        a8 = st.number_input("Masukkan nilai $$a$$ (positif):", value=1, step=1, key="a8")
        b8 = st.number_input("Masukkan nilai $$b$$ (positif):", value=1, step=1, key="b8")
        c8 = st.number_input("Masukkan nilai $$c$$ (positif):", value=1, step=1, key="c8")

        if a8 <= 0 or b8 <= 0 or c8 <= 0:
            st.warning("Semua nilai a, b, dan c harus positif.")
        else:
            if st.button("Tampilkan Grafik Eksplorasi 8", key="btn8"):
                x_vals8 = sp.Symbol('x')
                x_graph8 = list(range(-10, 11))
                y_vals8 = a8 * x_vals8**2 + b8 * x_vals8 + c8
                y_graph8 = [float(y_vals8.subs(x_vals8, i)) for i in x_graph8]
                st.line_chart({"x": x_graph8, "y": y_graph8})

        analisis8 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas", key="analisis8")

        if analisis8.strip() != "":
            with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi 8"):
                st.info("""
📌Salin prompt berikut ke **3 AI berbeda** ([Perplexity AI](https://www.perplexity.ai), [Gemini AI](https://gemini.google.com/app), [ChatGPT](https://chatgpt.com/)) untuk membandingkan hasil.


**Prompt:**
Jelaskan bagaimana grafik fungsi kuadrat y = ax² + bx + c berubah jika semua koefisien a, b, dan c bernilai positif. Jelaskan arah bukaannya, bentuk parabola, letak titik potong terhadap sumbu y, dan apakah grafik memotong sumbu x. Sertakan contoh fungsi.

✅ Coba di [Desmos](https://www.desmos.com/calculator) dengan:
- x² + 2x + 3
- x² + 4x + 5

📊 Amati arah bukaannya, posisi minimum, dan letak titik potong.

📝 **Refleksi:** Apa kesimpulanmu?
""")

                refleksi8 = st.text_area("Tulis jawaban refleksi Eksplorasi 8 di sini...", key="refleksi_eksplorasi8", height=80)
                
                if refleksi8.strip():
                    st.success("✅ Refleksi sudah diisi. Berikut materi verifikasinya 👇")
                    with st.expander("📚 Materi Verifikasi"):
                        st.markdown("""
        - Nilai $$a > 0$$ → parabola membuka ke atas.
        - Nilai $$b > 0$$ → sumbu simetri bergeser ke kiri.
        - Nilai $$c > 0$$ → titik potong sumbu $$y$$ berada di atas titik asal.
        - Semua koefisien positif membuat grafik berada di kuadran atas dengan titik puncak di bawah titik potong sumbu $$y$$.
        """)



if st.session_state.get("analisis8"):
    with st.expander("📝 Kesimpulan Eksplorasi"):
        st.markdown("""
✅ **Petunjuk:**
Silakan cek kembali hasil analisismu dan jawaban dari AI yang telah kamu pelajari dari 8 eksplorasi sebelumnya.

Tuliskan **kesimpulan eksplorasi** ke dalam kotak di bawah ini. Pastikan kesimpulanmu mencakup:

- Bentuk umum persamaan kuadrat beserta syaratnya.
- Karakteristik grafik fungsi kuadrat berdasarkan nilai masing-masing koefisien ($$a$$, $$b$$, dan $$c$$).
""")

        kesimpulan = st.text_area("✍️ Masukkan kesimpulan eksplorasimu di sini:", key="kesimpulan_eksplorasi", height=100)

        if kesimpulan.strip() != "":
            with st.expander("📚 Verifikasi Materi Kesimpulan Eksplorasi"):
                st.markdown("""
**Materi Verifikasi:**
- **Bentuk umum persamaan kuadrat:** $$y = ax^2 + bx + c$$ dengan $$a ≠ 0$$.
- **Pengaruh koefisien a:**
    - $$a > 0$$ → parabola membuka ke atas.
    - $$a < 0$$ → parabola membuka ke bawah.
    - Semakin besar nilai |a| → parabola semakin sempit, semakin kecil → parabola melebar.
- **Pengaruh koefisien b:**
    - Menggeser sumbu simetri parabola secara horizontal.
    - Titik puncak bergeser ke kiri/kanan mengikuti perubahan b.
- **Pengaruh koefisien c:**
    - Menentukan titik potong parabola dengan sumbu $$y$$ di titik (0, c).
- Kombinasi tanda dari a, b, dan c memengaruhi posisi keseluruhan grafik pada bidang koordinat.
""")

        



# --- Pengolahan Data (Soal Latihan) ---
st.header("📊 Pengolahan Data")
st.write("""
Sebuah bola dilemparkan dan lintasannya membentuk fungsi kuadrat:
$$h(x) = -5x^2 + 20x + 1$$
Tentukan:
1. Waktu ketika bola mencapai tinggi maksimum
2. Tinggi maksimum bola
""")

jawaban_olah = st.text_area("Tuliskan langkah dan jawabanmu di sini:", key="olah_data")
if st.button("Kirim Pengolahan Data"):
    if jawaban_olah.strip() != "":
        st.session_state.olah_data_done = True
        st.success("Jawaban pengolahan data disimpan.")
    else:
        st.warning("Isi dulu jawaban kamu.")


# --- 6. Verifikasi ke AI dan Desmos ---
st.header("🔍 Verifikasi Hasil Pengolahan Data")
st.info("Cek kembali jawabanmu dengan bantuan AI dan grafik dari Desmos.")

# Expander: petunjuk prompt dan link ke beberapa AI eksternal
with st.expander("📘 Cek jawaban dengan AI untuk soal ini"):
    st.markdown(
        """
**Prompt yang digunakan untuk semua AI:**  
> Diketahui fungsi kuadrat $h(x) = -5x^2 + 20x + 1$. Tentukan titik puncaknya dan tinggi maksimumnya.

**🔗 Cek di AI berikut:**  
- [Perplexity AI](https://www.perplexity.ai) — tempel prompt di kolom pencarian.  
- [Gemini (Google)](https://gemini.google.com) — tempel prompt dan bandingkan hasilnya.  
- [ChatGPT (OpenAI)](https://chat.openai.com) — tempel prompt dan lihat penjelasan langkah demi langkah.
"""
    )
    
# Verifikasi Desmos
with st.expander("**📈 Verifikasi bentuk grafik fungsi dengan Desmos:**")
st.markdown("""
🌐 Buka [Desmos Graphing Calculator](https://www.desmos.com/calculator)  
Masukkan fungsi: `-5x² + 20x + 1`

Perhatikan:
- Apakah grafik berbentuk parabola terbuka ke bawah?
- Apakah titik puncaknya di (2, 21)?
- Apakah titik potong sumbu $$y = 1$$?
""")

# Konfirmasi siswa
verifikasi = st.radio(
    "Apakah jawabanmu sesuai dengan hasil AI dan grafik Desmos?",
    ["Ya", "Tidak", "Sebagian"],
    key="verifikasi_pengolahan"
)

if verifikasi:
    st.session_state["verifikasi_done"] = True

    # Materi verifikasi
with st.expander("📚 Materi Verifikasi Pengolahan Data"):
    st.markdown("""
    **Materi yang benar sesuai soal:**
    - **Bentuk umum:** $$y = ax^2 + bx + c$$ dengan $$a < 0$$ → parabola terbuka ke bawah.
    
    **Fungsi kuadratnya:**  
    $$h(x) = -5x^2 + 20x + 1$$  

    **Titik puncak:**  dihitung dengan $$x = -\\frac{b}{2a}$$
    
    $$x = \\frac{-b}{2a} = \\frac{-20}{2(-5)} = \\frac{-20}{-10} = 2$$ detik  

    **Tinggi maksimum:**  lalu substitusi ke fungsi untuk mendapatkan tinggi maksimum
    
    $$h(2) = -5(2)^2 + 20(2) + 1 = -20 + 40 + 1 = 21$$  meter

    - Grafiknya simetris terhadap garis $$x = 2$$.
    """)


# --- 7. Kesimpulan ---
st.header("🎯 Penarikan Kesimpulan")

# Input kesimpulan dari pengguna
kesimpulan = st.text_area(
    "Apa kesimpulanmu tentang bentuk umum persamaan kuadrat dan karakteristik grafik berdasarkan masing-masing nilai koefisiennya?",
    key="kesimpulan_siswa",
    height=120
)

# Tampilkan notifikasi jika kesimpulan sudah diisi
if kesimpulan.strip() != "":
    st.success("✅ Kesimpulan kamu telah dicatat. Selesai.")

    # Bandingkan dengan AI eksternal
    with st.expander("🤖 Bandingkan Kesimpulanmu dengan AI Eksternal"):
        st.markdown("""
        **Prompt yang digunakan untuk semua AI:**
        > Apa kesimpulan tentang bentuk umum persamaan kuadrat dan karakteristik grafik berdasarkan masing-masing nilai koefisiennya?

        **🔗 Cek di AI berikut:**
        - [Perplexity AI](https://www.perplexity.ai)  
        - [Gemini](https://gemini.google.com)  
        - [ChatGPT](https://chat.openai.com)  
        """)

    # Materi verifikasi kesimpulan
    with st.expander("📚 Materi Verifikasi Kesimpulan"):
        st.markdown("""
        **Bentuk Umum Persamaan Kuadrat:**
        - Ditulis sebagai: $$y = ax^2 + bx + c$$ dengan $$a ≠ 0$$

        **Pengaruh masing-masing koefisien:**
        1. **Koefisien a**  
           - Menentukan arah buka parabola:  
             - $$a > 0$$ → terbuka ke atas  
             - $$a < 0$$ → terbuka ke bawah  
           - Nilai |a| besar → parabola lebih sempit, |a| kecil → parabola lebih lebar  
        
        2. **Koefisien b**  
           - Mempengaruhi posisi sumbu simetri: $$x = -\\frac{b}{2a}$$  
           - Menggeser puncak parabola ke kiri/kanan  

        3. **Koefisien c**  
           - Menentukan titik potong dengan sumbu y pada titik (0, c)

        **Ringkasan:**
        - Grafik parabola simetris terhadap garis $$x = -\\frac{b}{2a}$$
        - Titik puncak dapat dihitung dengan:  
          $$x_{puncak} = -\\frac{b}{2a}, \quad y_{puncak} = f(x_{puncak})$$
        - Bentuk parabola (lebar/sempit) dan arah buka tergantung nilai a
        """)




# --- Refleksi Akhir ---
st.subheader("🪞 Refleksi Belajar")
refleksi = st.radio("Seberapa yakin kamu memahami materi?", 
                    ["Tidak yakin", "Kurang yakin", "Cukup yakin", "Yakin", "Sangat yakin"])
kuis = st.radio("Jika a > 0, grafik akan terbuka ke arah:", 
                ["Garis lurus", "Melingkar", "Parabola terbuka ke bawah", "Parabola terbuka ke atas"])

cek_kuis = ""
if kuis:
    if kuis == "Parabola terbuka ke atas":
        st.success("✅ Jawaban benar!")
        cek_kuis = "Benar"
    else:
        st.error("❌ Jawaban kurang tepat.")
        cek_kuis = "Salah"

# Pastikan semua variabel memiliki nilai default jika belum terisi
jawaban1 = jawaban1 if 'jawaban1' in locals() else ""
jawaban2 = jawaban2 if 'jawaban2' in locals() else ""
analisis1 = analisis1 if 'analisis1' in locals() else ""
analisis2 = analisis2 if 'analisis2' in locals() else ""
jawaban_siswa = jawaban_siswa if 'jawaban_siswa' in locals() else ""
verifikasi = verifikasi if 'verifikasi' in locals() else ""
kesimpulan = kesimpulan if 'kesimpulan' in locals() else ""
cek_kuis = cek_kuis if 'cek_kuis' in locals() else ""
refleksi = refleksi if 'refleksi' in locals() else ""

# --- Kirim Semua Data ke Spreadsheet ---
if st.button("📤 Kirim Semua Jawaban"):
    if nama and kelas:
        semua_jawaban = f"Stimulus: {jawaban1} | Masalah: {jawaban2} | Eksplorasi1: {analisis1} | Eksplorasi2: {analisis2} | Latihan: {jawaban_siswa} | Verifikasi: {verifikasi} | Kesimpulan: {kesimpulan} | Kuis: {cek_kuis}"
        simpan_ke_sheet(nama, kelas, "Pertemuan 1", "-", semua_jawaban, refleksi)
        st.success("✅ Semua jawaban berhasil dikirim.")
    else:
        st.warning("❗ Nama dan Kelas wajib diisi di sidebar.")


# --- Navigasi Halaman ---
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ Capaian Pembelajaran"):
        st.switch_page("pages/2_Capaian_Pembelajaran.py")
with col2:
    if st.button("🏠 Daftar Isi"):
        st.switch_page("pages/0_Daftar_Isi.py")
with col3:
    if st.button("➡️ Pertemuan 2"):
        st.switch_page("pages/4_Pertemuan_2.py")



