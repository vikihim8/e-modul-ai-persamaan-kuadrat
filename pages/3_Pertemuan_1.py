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

# --- Sidebar untuk Nama dan Kelas ---
st.sidebar.header("Identitas")
nama = st.sidebar.text_input("Nama")
kelas = st.sidebar.text_input("Kelas")

# --- Judul Halaman ---
st.title("📘 Pertemuan 1: Menemukan Konsep Umum dan Grafik Fungsi Kuadrat")

# --- Stimulus dan Identifikasi Masalah ---
st.header("1. Stimulus")
st.write("Bayangkan kamu sedang menonton lintasan bola dilempar ke udara. Bentuknya seperti parabola. Mari kita pelajari grafik fungsi kuadrat dari fenomena tersebut.")
stimulus = st.text_area("📝 Apa yang kamu pikirkan tentang bentuk lintasan parabola ini?", key="stimulus")

st.header("2. Identifikasi Masalah")
masalah = st.text_area("❓ Pertanyaan apa yang muncul di benakmu terkait grafik lintasan itu?", key="masalah")

st.title("3. Pengumpulan Data")
st.write("Bentuk umum dari suatu persamaan kuadrat yaitu $$y = ax^2 + bx + c = 0$$ dengan $$a$$ adalah koefien variabel $$x^2$$, b adalah koefisien variabel $$x$$ dan c adalah konstanta dari persamaan kuadrat. Mari kita lakukan eksplorasi berikut")

# Eksplorasi 1
with st.expander("Eksplorasi 1: Bagaimana pengaruh nilai a terhadap bentuk grafik? Bagaimana jika a = 0? Apa yang akan terjadi? Masukan nilai a = 0 untuk mengetahui jawabannya"):
    a1 = st.number_input("Masukkan nilai $a$ (koefisien x²):", value=1.0, step=0.1, key="a1")
    b1 = st.number_input("Masukkan nilai $b$ (koefisien x):", value=0.0, step=0.1, key="b1")
    c1 = st.number_input("Masukkan nilai $c$ (konstanta):", value=0.0, step=0.1, key="c1")
    
    if "grafik1_ditampilkan" not in st.session_state:
        st.session_state.grafik1_ditampilkan = False

    if st.button("Tampilkan Grafik Eksplorasi 1"):
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

        st.session_state.grafik1_ditampilkan = True

    if st.session_state.grafik1_ditampilkan:
        analisis1 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas.", 
                                 placeholder="Misalnya: grafik membuka ke atas saat a positif.", key="analisis1")
        if analisis1.strip() != "":
            with st.expander("Cek Hasil Verifikasi AI Eksplorasi 1"):
                st.success("📋 Untuk penjelasan lebih lanjut, salin dan tempel prompt berikut ke Perplexity AI:\n\n**Jelaskan apa yang terjadi pada grafik fungsi kuadrat jika a = 0**")


# Eksplorasi 2 (Hanya dibuka jika eksplorasi 1 sudah selesai)
if "analisis1" in st.session_state and st.session_state.analisis1.strip() != "":
    with st.expander("Eksplorasi 2: Pengaruh nilai b terhadap posisi grafik"):
        b2 = st.number_input("Masukkan nilai b (misal: 2 atau -3):", key="b2")
        
        if "grafik2_ditampilkan" not in st.session_state:
            st.session_state.grafik2_ditampilkan = False

        if st.button("Tampilkan Grafik Eksplorasi 2"):
            x = np.linspace(-10, 10, 400)
            y = x**2 + b2 * x
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)
            ax.set_title(f"Grafik y = x² + {b2}x")
            st.pyplot(fig)
            st.session_state.grafik2_ditampilkan = True

        if st.session_state.grafik2_ditampilkan:
            analisis2 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas.", 
                                     placeholder="Misalnya: nilai b menggeser grafik ke kiri atau kanan.", key="analisis2")
            if analisis2.strip() != "":
                with st.expander("Cek Hasil Verifikasi AI Eksplorasi 2"):
                    st.success("Untuk penjelasan lengkap, kamu dapat membuka: [Perplexity AI](https://www.perplexity.ai/search/materi-grafik-nilai-b)")

# Eksplorasi 3: Nilai b negatif
if eksplorasi_2_terjawab:
    st.markdown("### Eksplorasi 3: Nilai b negatif")
    b_negatif = st.number_input("Masukkan nilai b (negatif):", key="b3")
    a3 = st.session_state.get("a1", 1)
    c3 = st.session_state.get("c1", 1)
    x_vals3 = sp.Symbol('x')
    y_vals3 = a3 * x_vals3**2 + b_negatif * x_vals3 + c3
    x_graph3 = [i for i in range(-10, 11)]
    y_graph3 = [float(y_vals3.subs(x_vals3, i)) for i in x_graph3]
    st.line_chart({"x": x_graph3, "y": y_graph3})

    analisis_3 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas.", key="analisis3")
    if analisis_3:
        st.success("Untuk materi lengkap, kamu dapat membuka: [Perplexity AI - Eksplorasi 3](https://www.perplexity.ai/search/materi-eksplorasi-3)")

        eksplorasi_3_terjawab = True

# Eksplorasi 4: Nilai b positif
if 'eksplorasi_3_terjawab' in locals() and eksplorasi_3_terjawab:
    st.markdown("### Eksplorasi 4: Nilai b positif")
    b_positif = st.number_input("Masukkan nilai b (positif):", key="b4")
    a4 = a3
    c4 = c3
    y_vals4 = a4 * x_vals3**2 + b_positif * x_vals3 + c4
    y_graph4 = [float(y_vals4.subs(x_vals3, i)) for i in x_graph3]
    st.line_chart({"x": x_graph3, "y": y_graph4})

    analisis_4 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas.", key="analisis4")
    if analisis_4:
        st.success("Untuk materi lengkap, kamu dapat membuka: [Perplexity AI - Eksplorasi 4](https://www.perplexity.ai/search/materi-eksplorasi-4)")

        eksplorasi_4_terjawab = True

# Eksplorasi 5: Nilai c negatif
if 'eksplorasi_4_terjawab' in locals() and eksplorasi_4_terjawab:
    st.markdown("### Eksplorasi 5: Nilai c negatif")
    c_negatif = st.number_input("Masukkan nilai c (negatif):", key="c5")
    b5 = b_positif
    y_vals5 = a4 * x_vals3**2 + b5 * x_vals3 + c_negatif
    y_graph5 = [float(y_vals5.subs(x_vals3, i)) for i in x_graph3]
    st.line_chart({"x": x_graph3, "y": y_graph5})

    analisis_5 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas.", key="analisis5")
    if analisis_5:
        st.success("Untuk materi lengkap, kamu dapat membuka: [Perplexity AI - Eksplorasi 5](https://www.perplexity.ai/search/materi-eksplorasi-5)")

        eksplorasi_5_terjawab = True

# Eksplorasi 6: Nilai c positif
if 'eksplorasi_5_terjawab' in locals() and eksplorasi_5_terjawab:
    st.markdown("### Eksplorasi 6: Nilai c positif")
    c_positif = st.number_input("Masukkan nilai c (positif):", key="c6")
    y_vals6 = a4 * x_vals3**2 + b5 * x_vals3 + c_positif
    y_graph6 = [float(y_vals6.subs(x_vals3, i)) for i in x_graph3]
    st.line_chart({"x": x_graph3, "y": y_graph6})

    analisis_6 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas.", key="analisis6")
    if analisis_6:
        st.success("Untuk materi lengkap, kamu dapat membuka: [Perplexity AI - Eksplorasi 6](https://www.perplexity.ai/search/materi-eksplorasi-6)")

        eksplorasi_6_terjawab = True

# Eksplorasi 7: Semua koefisien negatif
if 'eksplorasi_6_terjawab' in locals() and eksplorasi_6_terjawab:
    st.markdown("### Eksplorasi 7: Semua koefisien negatif")
    a7 = st.number_input("Masukkan nilai a (negatif):", key="a7")
    b7 = st.number_input("Masukkan nilai b (negatif):", key="b7")
    c7 = st.number_input("Masukkan nilai c (negatif):", key="c7")
    y_vals7 = a7 * x_vals3**2 + b7 * x_vals3 + c7
    y_graph7 = [float(y_vals7.subs(x_vals3, i)) for i in x_graph3]
    st.line_chart({"x": x_graph3, "y": y_graph7})

    analisis_7 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas.", key="analisis7")
    if analisis_7:
        st.success("Untuk materi lengkap, kamu dapat membuka: [Perplexity AI - Eksplorasi 7](https://www.perplexity.ai/search/materi-eksplorasi-7)")

        eksplorasi_7_terjawab = True

# Eksplorasi 8: Semua koefisien positif
if 'eksplorasi_7_terjawab' in locals() and eksplorasi_7_terjawab:
    st.markdown("### Eksplorasi 8: Semua koefisien positif")
    a8 = st.number_input("Masukkan nilai a (positif):", key="a8")
    b8 = st.number_input("Masukkan nilai b (positif):", key="b8")
    c8 = st.number_input("Masukkan nilai c (positif):", key="c8")
    y_vals8 = a8 * x_vals3**2 + b8 * x_vals3 + c8
    y_graph8 = [float(y_vals8.subs(x_vals3, i)) for i in x_graph3]
    st.line_chart({"x": x_graph3, "y": y_graph8})

    analisis_8 = st.text_area("Tuliskan analisismu berdasarkan grafik di atas.", key="analisis8")
    if analisis_8:
        st.success("Untuk materi lengkap, kamu dapat membuka: [Perplexity AI - Eksplorasi 8](https://www.perplexity.ai/search/materi-eksplorasi-8)")

        eksplorasi_8_terjawab = True


for i in range(1, 10):
    if f'eksplorasi_{i}_selesai' not in st.session_state:
        st.session_state[f'eksplorasi_{i}_selesai'] = False

def plot_graph(a, b, c):
    x_vals = np.linspace(-10, 10, 400)
    y_vals = a * x_vals**2 + b * x_vals + c
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f'{a}x² + {b}x + {c}')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title("Grafik Fungsi Kuadrat")
    ax.legend()
    st.pyplot(fig)

def eksplorasi_form(id, title):
    st.subheader(title)
    a = st.number_input(f"Masukkan nilai a (eksplorasi {id})", key=f'a_{id}')
    b = st.number_input(f"Masukkan nilai b (eksplorasi {id})", key=f'b_{id}')
    c = st.number_input(f"Masukkan nilai c (eksplorasi {id})", key=f'c_{id}')
    
    if st.button(f"Plot grafik eksplorasi {id}"):
        st.session_state[f'eksplorasi_{id}_plotted'] = True
        st.session_state[f'eksplorasi_{id}_abc'] = (a, b, c)

    if st.session_state.get(f'eksplorasi_{id}_plotted'):
        a, b, c = st.session_state[f'eksplorasi_{id}_abc']
        plot_graph(a, b, c)
        analisis = st.text_area("Tuliskan analisismu berdasarkan grafik di atas.", key=f'analisis_{id}', placeholder="Misalnya: grafik terbuka ke atas, titik puncak ada di sekitar x = -1, dst.")
        
        if analisis:
            st.success(f"Untuk materi lengkap, kamu dapat membuka: [Perplexity AI](https://www.perplexity.ai/search/materi-analisis-grafik-berdasa-lpxD.jhxQJSogx7G7Gjdgw)")
            st.session_state[f'eksplorasi_{id}_selesai'] = True

st.title("Eksplorasi Fungsi Kuadrat")

eksplorasi_titles = {
    1: "Eksplorasi 1: Variasi nilai a (b=0, c=0)",
    2: "Eksplorasi 2: Variasi nilai b (a=1, c=0)",
    3: "Eksplorasi 3: Variasi nilai c (a=1, b=0)",
    4: "Eksplorasi 4: Variasi a dan b, tetap c",
    5: "Eksplorasi 5: Variasi a dan c, tetap b",
    6: "Eksplorasi 6: Variasi b dan c, tetap a",
    7: "Eksplorasi 7: Semua variabel negatif",
    8: "Eksplorasi 8: Semua variabel positif",
    9: "Final: Bentuk Umum dan Karakteristik Grafik"
}

for i in range(1, 10):
    if i == 1 or st.session_state.get(f'eksplorasi_{i-1}_selesai'):
        eksplorasi_form(i, eksplorasi_titles[i])


# Pengolahan Data (Soal Latihan) ---
if st.session_state.explore_2_done:
    st.subheader("📊 Pengolahan Data")
    soal = """
    Sebuah bola dilemparkan dan lintasannya membentuk fungsi kuadrat: 
    $$h(t) = -5t^2 + 20t + 1$$
    Tentukan:
    1. Waktu ketika bola mencapai tinggi maksimum
    2. Tinggi maksimum bola
    """
    st.latex(soal)
    jawaban_olah = st.text_area("Tuliskan langkah dan jawabanmu di sini:", key="olah_data")
    if st.button("Kirim Pengolahan Data"):
        if jawaban_olah.strip() != "":
            st.session_state.olah_data_done = True
            st.success("Jawaban pengolahan data disimpan.")
        else:
            st.warning("Isi dulu jawaban kamu.")

# --- 6. Verifikasi ke AI ---
if st.session_state.olah_data_done:
    st.subheader("🤖 Verifikasi dengan AI")
    st.info("Berikut adalah jawaban versi AI setelah kamu menjawab sendiri.")
    st.markdown("**Jawaban AI:**")
    with st.expander("Lihat Jawaban dari AI"):
        st.write("""
        Fungsi kuadratnya: h(t) = -5t² + 20t + 1
        Titik puncaknya: t = -b/2a = -20/(2×-5) = 2 detik
        Tinggi maksimum: h(2) = -5(2)² + 20(2) + 1 = -20 + 40 + 1 = 21 meter
        """)

    verifikasi = st.radio("Apakah jawabanmu sesuai dengan AI?", ["Ya", "Tidak", "Sebagian"])
    if verifikasi:
        st.session_state.verifikasi_done = True

# --- 7. Kesimpulan ---
if st.session_state.verifikasi_done:
    st.subheader("🧠 Kesimpulan")
    kesimpulan = st.text_area("Apa kesimpulanmu tentang bentuk umum fungsi kuadrat dan sifat titik puncaknya?")
    if kesimpulan.strip() != "":
        st.success("Kesimpulan kamu telah dicatat. Selesai.")

with st.expander("📖 Bandingkan dengan AI", expanded=False):
        st.markdown("[Klik untuk lihat versi AI](https://www.perplexity.ai/search/kesimpulan-bentuk-umum-fung-3bCVmPvZTa2mjJdTMEPPrg)")

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

