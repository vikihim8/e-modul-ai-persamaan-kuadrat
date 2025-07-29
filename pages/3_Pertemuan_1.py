import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

# --- Setup Spreadsheet ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
json_creds = st.secrets["gcp_service_account"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(json_creds, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("18g9_lCQQDjyU85TJpBUZRzJIrFmrVPeCnjNg4DqrPx8").sheet1

def simpan_ke_sheet(nama, kelas, pertemuan, skor, jawaban, refleksi):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([nama, kelas, pertemuan, skor, jawaban, refleksi, waktu])


# --- Judul Halaman ---
st.title("📘 Pertemuan 1: Menemukan Bentuk Umum dan Grafik Fungsi Kuadrat")

# --- Stimulus dan Identifikasi Masalah ---
st.header("1. Stimulus")
st.write("Bayangkan kamu sedang menonton lintasan bola dilempar ke udara. Bentuknya seperti parabola. Mari kita pelajari grafik fungsi kuadrat dari fenomena tersebut.")
stimulus = st.text_area("📝 Apa yang kamu pikirkan tentang bentuk lintasan parabola ini?", key="stimulus")



st.header("2. Identifikasi Masalah")
masalah = st.text_area("❓ Pertanyaan apa yang muncul di benakmu terkait grafik lintasan itu?", key="masalah")




st.title("3. Pengumpulan Data")
st.write(
    "Bentuk umum dari suatu persamaan kuadrat yaitu $$y = ax^2 + bx + c = 0$$ "
    "dengan $$a$$ adalah koefisien variabel $$x^2$$, $$b$$ adalah koefisien variabel $$x$$, "
    "dan $$c$$ adalah konstanta. Mari kita lakukan eksplorasi berikut."
)

# Eksplorasi 1
with st.expander("💡Eksplorasi 1: Bagaimana pengaruh nilai a terhadap bentuk grafik? Apa yang terjadi jika a = 0?"):
    a1 = st.number_input("Masukkan nilai $a$ (koefisien $x^2$):", value=0, step=1, key="a1")
    b1 = st.number_input("Masukkan nilai $b$ (koefisien $x$):", value=0, step=1, key="b1")
    c1 = st.number_input("Masukkan nilai $c$ (konstanta):", value=0, step=1, key="c1")


    if "grafik1_ditampilkan" not in st.session_state:
        st.session_state.grafik1_ditampilkan = False

    if st.button("Tampilkan Grafik Eksplorasi 1"):
        st.session_state.grafik1_ditampilkan = True

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

        analisis1 = st.text_area(
            "Tuliskan analisismu berdasarkan grafik di atas.",
            placeholder="Misalnya: grafik membuka ke atas saat a positif.",
            key="analisis1"
        )

        if analisis1.strip():
            with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi 1"):
                st.info("""
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**  
Jelaskan secara rinci apa yang terjadi pada grafik fungsi kuadrat jika a = 0 dalam persamaan y = ax² + bx + c. Jelaskan perubahan bentuk grafik, apakah masih berupa parabola atau tidak, dan berikan perbandingan visual antara grafik saat a = 0 dan a ≠ 0.


✅ Setelah memahami penjelasan dari AI, buka [Desmos Graphing Calculator](https://www.desmos.com/calculator) dan coba masukkan:

2x² + 3x + 1  
0x² + 3x + 1

📊 Bandingkan hasil grafiknya. Apakah bentuknya tetap parabola jika $$a = 0$$?

📝 **Refleksi:** Apa perbedaan utama yang kamu temukan antara grafik fungsi kuadrat saat $$a ≠ 0$$ dan saat $$a = 0$$?
"""
                )
                st.text_area("Tulis jawaban refleksi Eksplorasi 1 di sini...", key="refleksi_eksplorasi1", height=80)



# Eksplorasi 2 (Hanya dibuka jika eksplorasi 1 sudah selesai)
if "analisis1" in st.session_state and st.session_state.analisis1.strip() != "":
    with st.expander("💡Eksplorasi 2: Bagaimana pengaruh nilai b terhadap posisi grafik? Apakah sumbu simetri dan titik puncak berubah ketika nilai b diubah? Cobalah masukkan berbagai nilai b dan amati pergeseran grafik"):
        
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

            analisis2 = st.text_area(
                "Tuliskan analisismu berdasarkan grafik di atas.",
                placeholder="Misalnya: nilai b menggeser grafik ke kiri atau kanan.",
                key="analisis2"
            )

            if analisis2.strip() != "":
                with st.expander("🔍 Cek Hasil Verifikasi AI Eksplorasi 2"):
                    st.info(
                        """
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**  
Jelaskan bagaimana perubahan nilai b memengaruhi posisi grafik fungsi kuadrat y = ax² + bx + c, khususnya terhadap sumbu simetri dan titik puncak. Berikan ilustrasi atau contoh grafik untuk beberapa nilai b yang berbeda, serta bandingkan pergeseran posisi grafiknya.

✅ Setelah memahami penjelasan dari AI, buka [Desmos Graphing Calculator](https://www.desmos.com/calculator) dan coba masukkan:

x² + 4x + 1  
x² + 7x + 1  
x² + 0x + 1

📊 Amati bagaimana sumbu simetri dan titik puncak grafik berubah saat nilai $$b$$ berbeda.

📝 **Refleksi:** Apa yang terjadi pada posisi grafik (sumbu simetri dan titik puncak) ketika nilai $$b$$ berubah?
"""
                    )
                    st.text_area("Tulis jawabanmu di sini...", key="refleksi_eksplorasi2", height=80)




# Eksplorasi 3: Nilai b negatif
if st.session_state.get("analisis2"):
    with st.expander("💡Eksplorasi 3: Apa pengaruh nilai b negatif terhadap arah dan letak grafik fungsi kuadrat?"):
        import matplotlib.pyplot as plt

        b_negatif = st.number_input("Masukkan nilai $b$ (negatif):", value=-1, step=1, key="b3")
        a3 = st.number_input("Masukkan nilai a:", key="a3", value=0)
        c3 = st.number_input("Masukkan nilai c:", key="c3", value=0)

        # Buat grafik fungsi kuadrat
        x_vals3 = [x for x in range(-10, 11)]
        y_vals3 = [a3 * x**2 + b_negatif * x + c3 for x in x_vals3]

        fig3, ax3 = plt.subplots()
        ax3.plot(x_vals3, y_vals3, marker='o', linestyle='-', color='blue', label=f'y = {a3}x² + ({b_negatif})x + {c3}')
        ax3.axhline(0, color='gray', linewidth=1)
        ax3.axvline(0, color='gray', linewidth=1)
        ax3.set_title("Grafik Fungsi Kuadrat dengan Nilai b Negatif")
        ax3.set_xlabel("x")
        ax3.set_ylabel("y")
        ax3.grid(True)
        ax3.legend()
        st.pyplot(fig3)

        analisis3 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas.", key="analisis3")

        if analisis3.strip() != "":
            with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi 3"):
                st.info("""
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**  
Jelaskan bagaimana pengaruh nilai b yang negatif terhadap letak sumbu simetri dan posisi grafik fungsi kuadrat y = ax² + bx + c. Sertakan penjelasan visual jika memungkinkan. Apa yang terjadi saat b bernilai negatif dibandingkan b positif?

✅ Setelah memahami penjelasan dari AI, buka [Desmos Graphing Calculator](https://www.desmos.com/calculator) dan coba masukkan beberapa fungsi berikut:
x² + 4x + 1  
x² - 4x + 1  
x² - 2x + 1

📊 Amati pergeseran grafiknya. Fokus pada letak titik puncak (vertex) dan arah grafik. Bagaimana peran nilai b dalam hal ini?
""")
                st.write("📝 **Refleksi:** Setelah percobaan dan verifikasi AI, apa kesimpulanmu tentang pengaruh nilai b yang negatif terhadap grafik fungsi kuadrat?")
                st.text_area("Tulis jawabanmu di sini...", key="refleksi_eksplorasi3", height=80)




# Eksplorasi 4: Nilai b positif
if st.session_state.get("analisis3"):
    with st.expander("💡Eksplorasi 4: Apa pengaruh nilai b positif terhadap arah dan letak grafik fungsi kuadrat?"):
        st.markdown("Mari kita amati bagaimana grafik berubah ketika nilai b bernilai **positif**.")

        b_positif = st.number_input("Masukkan nilai $b$ (positif):", value=1, step=1, key="b4")

        if b_positif != 0:
        a4 = st.number_input("Masukkan nilai a:", key="a4", value=0)
        c4 = st.number_input("Masukkan nilai c:", key="c4", value=0)
            x_vals4 = sp.Symbol('x')
            y_vals4 = a4 * x_vals4**2 + b_positif * x_vals4 + c4
            y_graph4 = [float(y_vals4.subs(x_vals4, i)) for i in x_graph3]

            st.line_chart({"x": x_graph3, "y": y_graph4})

        analisis4 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas", key="analisis4")

        if analisis4:
            with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi 4"):
                st.info("""
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**  
Jelaskan bagaimana pengaruh nilai b yang positif terhadap letak sumbu simetri dan posisi grafik fungsi kuadrat y = ax² + bx + c. Sertakan penjelasan visual jika memungkinkan. Apa yang terjadi saat b bernilai positif dibandingkan b negatif?

---

✅ Setelah memahami penjelasan dari AI, buka [Desmos Graphing Calculator](https://www.desmos.com/calculator) dan coba masukkan beberapa fungsi berikut:
x² - 4x + 1  
x² + 4x + 1

📊 Amati pergeseran grafiknya. Fokus pada letak titik puncak (vertex) dan arah grafik. Bagaimana peran nilai b dalam hal ini?
""")

        st.write("📝 **Refleksi:** Setelah percobaan dan verifikasi AI, apa kesimpulanmu tentang pengaruh nilai b yang positif terhadap grafik fungsi kuadrat?")
        refleksi = st.text_area("Tulis jawabanmu di sini...", key="refleksi_eksplorasi4", height=80)


            

# Eksplorasi 5: Nilai c negatif
if st.session_state.get("analisis4"):
    with st.expander("💡Eksplorasi 5: Apa pengaruh nilai c negatif terhadap grafik fungsi kuadrat?"):
        st.markdown("Mari kita amati bagaimana grafik berubah ketika nilai c bernilai **negatif**")

        c5 = st.number_input("Masukkan nilai $$c$$ (negatif):", value=-1, step=1, key="c5")
        a5 = st.session_state.get("a4", 1)
        b5 = st.session_state.get("b_positif", 1)

        # Gunakan x_vals3 dan x_graph3 jika sudah didefinisikan sebelumnya
        y_vals5 = a5 * x_vals3**2 + b5 * x_vals3 + c5
        y_graph5 = [float(y_vals5.subs(x_vals3, i)) for i in x_graph3]
        st.line_chart({"x": x_graph3, "y": y_graph5})
        
        analisis5 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas", key="analisis5")

        if analisis5:
            with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi 5"):
                st.info("""
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**
Jelaskan apa pengaruh nilai c negatif terhadap grafik fungsi kuadrat y = ax^2 + bx + c, terutama terhadap posisi titik potong grafik terhadap sumbu y. Sertakan juga contoh nilai a dan b yang positif serta nilai c negatif.

✅ Setelah memahami penjelasan dari AI, buka [Desmos Graphing Calculator](https://www.desmos.com/calculator) dan coba masukkan beberapa fungsi berikut:
x² + 4x + 3  
x² + 4x - 3  

📊 Amati pergeseran grafiknya. Fokus pada **pergeseran vertikal** dan **letak titik potong terhadap sumbu y** dan bentuk grafik. Bagaimana peran nilai **c** dalam hal ini?
""")

        st.write("📝 **Refleksi:** Setelah percobaan dan verifikasi AI, apa kesimpulanmu tentang pengaruh nilai **c yang negatif** terhadap grafik fungsi kuadrat?")
        refleksi = st.text_area("Tulis jawabanmu di sini...", key="refleksi_eksplorasi5", height=80)




# Eksplorasi 6: Nilai c positif
if st.session_state.get("analisis5"):
    with st.expander("💡Eksplorasi 6: Apa pengaruh nilai c positif terhadap grafik fungsi kuadrat?"):
        st.markdown("Mari kita amati bagaimana grafik berubah ketika nilai c bernilai **positif**")

        a6 = st.number_input("Masukkan nilai a:", key="a6", value=1)
        b6 = st.number_input("Masukkan nilai b:", key="b6", value=0)
        c6 = st.number_input("Masukkan nilai $$c$$ (positif):", key="c6", value=1, step=1)

        import numpy as np
        import pandas as pd

        x_vals6 = np.linspace(-10, 10, 200)
        y_vals6 = a6 * x_vals6**2 + b6 * x_vals6 + c6
        chart_data6 = pd.DataFrame({"x": x_vals6, "y": y_vals6})
        st.line_chart(chart_data6, x="x", y="y", height=300)

        analisis6 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas", key="analisis6")

        if analisis6:
            with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi 6"):
                st.info("""
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**
Jelaskan apa pengaruh nilai c positif terhadap grafik fungsi kuadrat y = ax^2 + bx + c, terutama terhadap posisi titik potong grafik terhadap sumbu y. Sertakan juga contoh nilai a dan b yang positif serta nilai c positif.

✅ Setelah memahami penjelasan dari AI, buka [Desmos Graphing Calculator](https://www.desmos.com/calculator) dan coba masukkan beberapa fungsi berikut:
x² + 4x - 1  
x² + 4x + 1  

📊 Amati pergeseran grafiknya. Fokus pada **pergeseran vertikal** dan **letak titik potong terhadap sumbu y** dan bentuk grafik. Bagaimana peran nilai **c** dalam hal ini?
""")

        st.write("📝 **Refleksi:** Setelah percobaan dan verifikasi AI, apa kesimpulanmu tentang pengaruh nilai **c yang positif** terhadap grafik fungsi kuadrat?")
        refleksi6 = st.text_area("Tulis jawabanmu di sini...", key="refleksi_eksplorasi6", height=80)

        


# Eksplorasi 7: Semua koefisien negatif
if st.session_state.get("analisis6"):
    with st.expander("💡Eksplorasi 7: Apa pengaruh nilai semua koefisien negatif terhadap grafik fungsi kuadrat?"):
        st.markdown("Mari kita amati bagaimana grafik berubah ketika nilai semua koefisien **negatif**")

        a7 = st.number_input("Masukkan nilai $$a$$ (harus negatif):", value=-1, step=1, key="a7")
        b7 = st.number_input("Masukkan nilai $$b$$ (harus negatif):", value=-1, step=1, key="b7")
        c7 = st.number_input("Masukkan nilai $$c$$ (harus negatif):", value=-1, step=1, key="c7")

        error_eksplorasi7 = False
        if a7 >= 0 or b7 >= 0 or c7 >= 0:
            st.warning("Semua nilai a, b, dan c harus negatif.")
            error_eksplorasi7 = True

        if not error_eksplorasi7:
            y_vals7 = a7 * x_vals3**2 + b7 * x_vals3 + c7
            y_graph7 = [float(y_vals7.subs(x_vals3, i)) for i in x_graph3]
            st.line_chart({"x": x_graph3, "y": y_graph7})

            analisis7 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas", key="analisis7")
            if analisis7:
                with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi 7"):
                    st.info("""
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**
Apa yang terjadi pada grafik fungsi kuadrat y = ax² + bx + c jika semua koefisien (a, b, dan c) bernilai negatif? Jelaskan bentuk grafiknya, arah bukaannya, dan posisi relatif terhadap sumbu x dan sumbu y. Sertakan contoh fungsi dan gambarnya.

✅ Setelah membaca penjelasan dari AI, buka [Desmos Graphing Calculator](https://www.desmos.com/calculator) dan masukkan fungsi-fungsi berikut:
-x² - 2x - 3  
-2x² - 4x - 1  

📊 Perhatikan arah bukaannya (menghadap ke bawah), bentuk grafiknya (melebar atau menyempit), dan posisi titik potong terhadap sumbu y. Apa pola yang kamu temukan jika semua koefisien negatif?
""")

        st.write("📝 **Refleksi:** Setelah percobaan dan verifikasi AI, apa kesimpulanmu tentang grafik fungsi kuadrat dengan semua koefisien negatif?")
        refleksi7 = st.text_area("Tulis jawabanmu di sini...", key="refleksi_eksplorasi7", height=80)




# Eksplorasi 8: Semua koefisien positif
if st.session_state.get("analisis7"):
    with st.expander("💡Eksplorasi 8: Apa pengaruh nilai semua koefisien positif terhadap grafik fungsi kuadrat?"):
        st.markdown("Mari kita amati bagaimana grafik berubah ketika nilai semua koefisien **positif**")

        a8 = st.number_input("Masukkan nilai $$a$$ (harus positif):", value=1, step=1, key="a8")
        b8 = st.number_input("Masukkan nilai $$b$$ (harus positif):", value=1, step=1, key="b8")
        c8 = st.number_input("Masukkan nilai $$c$$ (harus positif):", value=1, step=1, key="c8")

        error_eksplorasi8 = False
        if a8 <= 0 or b8 <= 0 or c8 <= 0:
            st.warning("Semua nilai a, b, dan c harus positif.")
            error_eksplorasi8 = True

        if not error_eksplorasi8:
            y_vals8 = a8 * x_vals3**2 + b8 * x_vals3 + c8
            y_graph8 = [float(y_vals8.subs(x_vals3, i)) for i in x_graph3]
            st.line_chart({"x": x_graph3, "y": y_graph8})

            analisis8 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas", key="analisis8")
            if analisis8:
                with st.expander("🔍Cek Hasil Verifikasi AI Eksplorasi 8"):
                    st.info("""
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**
Jelaskan bagaimana grafik fungsi kuadrat y = ax² + bx + c berubah jika semua koefisien a, b, dan c bernilai positif. Jelaskan arah bukaannya, bentuk parabola, letak titik potong terhadap sumbu y, dan apakah grafik memotong sumbu x. Sertakan contoh fungsi dan gambar grafik jika memungkinkan.

✅ Setelah membaca penjelasan dari AI, buka [Desmos Graphing Calculator](https://www.desmos.com/calculator) dan masukkan fungsi-fungsi berikut:
x² + 2x + 3  
x² + 4x + 5  

📊 Perhatikan arah bukaannya (menghadap ke atas), posisi minimum (titik puncak), dan apakah grafik menyentuh atau tidak menyentuh sumbu x. Apa pola yang bisa kamu simpulkan?
""")

        st.write("📝 **Refleksi:** Setelah percobaan dan verifikasi AI, apa kesimpulanmu tentang grafik fungsi kuadrat jika semua koefisien positif?")
        refleksi8 = st.text_area("Tulis jawabanmu di sini...", key="refleksi_eksplorasi8", height=80)





# --- Pengolahan Data (Soal Latihan) ---
st.title("4. Pengolahan Data")
st.write("""
Sebuah bola dilemparkan dan lintasannya membentuk fungsi kuadrat:
$$h(t) = -5t^2 + 20t + 1$$
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
st.title("5. Verifikasi")
st.info("Cek kembali jawabanmu dengan bantuan AI dan grafik dari Desmos.")
    
st.markdown("**✅ Jawaban AI untuk soal ini:**")
with st.expander("📘 Tampilkan Jawaban dari AI"):
    st.write("""
    Fungsi kuadratnya: h(t) = -5t² + 20t + 1  
    Titik puncaknya: t = -b/2a = -20/(2×-5) = 2 detik  
    Tinggi maksimum: h(2) = -5(2)² + 20(2) + 1 = -20 + 40 + 1 = 21 meter
    """)

st.markdown("**🔎 Cek ulang keakuratan dengan AI eksternal:**")
st.markdown("""
> 📋 *Salin dan tempelkan prompt ini ke Perplexity atau AI lainnya:*  
```
Diketahui fungsi kuadrat h(t) = -5t² + 20t + 1. Tentukan titik puncaknya dan tinggi maksimumnya.
    ```
[🔗 Klik ke Perplexity](https://www.perplexity.ai)
    """)

st.markdown("**📈 Verifikasi bentuk grafik fungsi dengan Desmos:**")
st.markdown("""
- [🌐 Buka Desmos Graphing Calculator](https://www.desmos.com/calculator)
- Masukkan fungsi: `h(t) = -5t^2 + 20t + 1`
- Perhatikan:  
    • Apakah grafik berbentuk parabola terbuka ke bawah?  
    • Apakah titik puncaknya sesuai?  
    • Apakah titik potong sumbu Y = 1?

Cek semua ini untuk memverifikasi pemahamanmu.
""")

verifikasi = st.radio("Apakah jawabanmu sesuai dengan hasil AI dan grafik Desmos?", ["Ya", "Tidak", "Sebagian"])
if verifikasi:
    st.session_state.verifikasi_done = True




# --- 7. Kesimpulan ---
st.title("6. Penarikan Kesimpulan")
kesimpulan = st.text_area("Apa kesimpulanmu tentang bentuk umum persamaan kuadrat dan karakteristik grafik berdasarkan masing-masing nilai koefisiennya?")
if kesimpulan.strip() != "":
    st.success("Kesimpulan kamu telah dicatat. Selesai.")

with st.expander("📖 Bandingkan dengan Kesimpulan Versi AI"):
    st.markdown("""
    🔗 [Klik untuk melihat jawaban versi AI di Perplexity](https://www.perplexity.ai/search/kesimpulan-bentuk-umum-fung-3bCVmPvZTa2mjJdTMEPPrg)

    💡 *Kamu juga bisa menyalin prompt ini ke AI:*
    ```
    Apa kesimpulan tentang bentuk umum persamaan kuadrat dan karakteristik grafik berdasarkan masing-masing nilai koefisiennya?
    ```
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

