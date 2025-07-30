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
st.text_input("Apa yang bisa kamu simpulkan dari titik potong tersebut terhadap bentuk fungsi kuadrat?")

# Identifikasi Masalah
st.subheader("🔍 Identifikasi Masalah")
identifikasi = st.text_area("Apa yang ingin kamu ketahui atau cari berdasarkan grafik di atas?")
st.text_input("Tuliskan satu pertanyaan utamamu di sini:", key="pertanyaan")

# Eksplorasi 1
st.subheader("🔬 Eksplorasi 1: Menentukan Akar-akar dari Grafik")
st.write("Grafik fungsi kuadrat memotong sumbu $$x$$ di $$x$$ = 2 dan $$x$$ = 3. Itu artinya nilai $$x$$ yang membuat $$y = 0$$ adalah akar-akar dari fungsi kuadrat tersebut.")
akar1 = st.number_input("Masukkan akar pertama:", key="akar1_input")
akar2 = st.number_input("Masukkan akar kedua:", key="akar2_input")
st.session_state.akar1 = akar1
st.session_state.akar2 = akar2

analisis1 = st.text_area("Apa hubungan antara titik potong grafik dan akar-akar fungsi kuadrat?", key="analisis1_input")
st.session_state.analisis1 = analisis1

if analisis1:
    st.markdown("##### 🔎 Cek AI (Perplexity)")
    st.code("Apa hubungan antara akar-akar fungsi kuadrat dan titik potong grafik terhadap sumbu x?")
    st.info("💡 Salin dan tempelkan prompt di atas ke Perplexity.ai untuk membandingkan pemahamanmu.")


# Eksplorasi 2 (muncul jika analisis1 sudah diisi)
if st.session_state.get("analisis1"):
    st.subheader("🔬 Eksplorasi 2: Membangun Fungsi Kuadrat dari Akar-akar")
    st.write("Jika kamu tahu akar-akarnya, kamu bisa menyusun bentuk faktornya yaitu:")
    
    # Pastikan akar1 dan akar2 sudah ada
    akar1 = st.session_state.get("akar1", "akar1")
    akar2 = st.session_state.get("akar2", "akar2")
    st.latex(r"f(x) = a(x - \text{akar1})(x - \text{akar2})")

    st.latex(f"f(x) = a(x - {akar1})(x - {akar2})")
    st.session_state.nilai_a = st.number_input(
        "Tentukan nilai $$a$$ (gunakan $$a$$ = 1 untuk sementara):", 
        key="nilai_a_input"
        value=1.0
    )

    
    analisis2 = st.text_area("Apa pendapatmu tentang hubungan antara akar dan bentuk faktornya?")
    
    if analisis2:
        st.markdown("##### 🔎 Cek AI (Perplexity)")
        st.code("Bagaimana menyusun fungsi kuadrat dari dua akar yang diketahui?")
        st.info("🧠 Salin dan tempelkan prompt tersebut ke Perplexity.ai.")


# Eksplorasi 3 (muncul jika nilai a dan akar sudah tersedia)
if st.session_state.get("analisis2"):
   st.session_state.get("nilai_a") is not None and \
   st.session_state.get("akar1") is not None and \
   st.session_state.get("akar2") is not None:

    st.subheader("🔬 Eksplorasi 3: Mengalikan Bentuk Faktor menjadi Bentuk Umum")

    a = st.session_state.nilai_a
    akar1 = st.session_state.akar1
    akar2 = st.session_state.akar2

    x = symbols('x')
    f = a * (x - akar1) * (x - akar2)
    f_expand = expand(f)

    st.latex(f"f(x) = {f_expand}")
    st.write("Sekarang kamu sudah mendapatkan bentuk umum dari fungsi kuadrat.")

    analisis3 = st.text_area("Apa yang kamu perhatikan dari hasil perkalian bentuk faktor ini?", key="analisis3")

    if analisis3:
        st.markdown("##### 🔎 Cek AI")
        st.code("Bagaimana cara mengalikan bentuk faktorisasi fungsi kuadrat menjadi bentuk umum?")
        st.info("🔍 Salin dan tempelkan ke Perplexity untuk mengecek pemahamanmu.")

# Eksplorasi 4
if st.session_state.get("analisis3"):
    st.subheader("🔬 Eksplorasi 4: Menemukan $$p$$ dan $$q$$ dari $$a$$, $$b$$, dan $$c$$")
    st.write("Tanpa diberitahu bagaimana mencari nilai $$p$$ dan $$q$$, coba amati koefisien dari bentuk umum $$ax^2 + bx + c$$")
    f_expand = expand(st.session_state.nilai_a * (x - st.session_state.akar1)*(x - st.session_state.akar2))
    st.latex(f"f(x) = {f_expand}")
    tebakan_p = st.number_input("Tebak nilai $$p$$ (akar pertama):", key="tebakan_p")
    tebakan_q = st.number_input("Tebak nilai $$q$$ (akar kedua):", key="tebakan_q")
   
    analisis4 = st.text_area("Apa alasanmu memilih nilai $$p$$ dan $$q$$ tersebut?", key="analisis4")

    if analisis4:
        if st.button("Cek Tebakan"):
            hasil_c = tebakan_p * tebakan_q
            hasil_b = -1 * (tebakan_p + tebakan_q)
            st.write(f"Hasil perkalian $$p \\times q$$ = {hasil_c}")
            st.write(f"Hasil penjumlahan $$(p + q)$$ = {hasil_b}")
            st.info("Bandingkan hasil ini dengan nilai $$b$$ dan $$c$$ dari bentuk umum.")
            st.markdown("##### 🔎 Cek AI")
            st.code("Bagaimana cara menemukan p dan q untuk memfaktorkan fungsi kuadrat dalam bentuk umum?")
            st.info("💬 Coba bandingkan hasil tebakanmu dengan penjelasan dari AI.")


# Eksplorasi 5
if st.session_state.get("analisis4"):  # Pastikan Eksplorasi 4 sudah dijawab
    st.subheader("🔬 Eksplorasi 5: Buat Kesimpulan Umum")
    st.write("Setelah melakukan semua eksplorasi, apa kesimpulanmu untuk menentukan bentuk umum fungsi kuadrat dari grafiknya?")

    kesimpulan = st.text_area("✍️ Tuliskan kesimpulanmu di sini:", key="kesimpulan")

    if kesimpulan.strip():
        if st.button("💡 Bandingkan dengan AI"):
            st.markdown("##### 🔎 Cek AI")
            st.code("Bagaimana mengubah bentuk umum fungsi kuadrat menjadi bentuk faktor dan menemukan akarnya?")
            st.info("📝 Bandingkan kesimpulanmu dengan versi AI.")
else:
    st.warning("Silakan selesaikan Eksplorasi 4 terlebih dahulu sebelum lanjut ke Eksplorasi 5.")



# 4. Pengolahan Data
st.header("📝 Pengolahan Data")
st.write("Faktorkan bentuk berikut:")

st.latex(r"f(x) = x^2 - 7x + 10")

analisisdata = st.text_input("Tulis bentuk faktornya:")

if analisisdata.strip():
    st.success("✅ Jawaban disimpan.")
    with st.expander("🔍 Cek AI setelah menjawab"):
        st.markdown("#### 🔗 Periksa pemahamanmu dengan AI")
        st.code("Faktorkan bentuk f(x) = x^2 - 7x + 10")
        st.markdown("[Buka Perplexity](https://www.perplexity.ai/search/faktorkan-bentuk-berikut-f-x-x-zX63Q4XtQvmPVB..m6yvOg)")
else:
    st.info("✍️ Silakan faktorkan terlebih dahulu sebelum mengecek ke AI.")

    

# --- 5. Pembuktian (Verifikasi) ---
st.header("Verifikasi")
with st.expander("🔍 Lihat pembahasan AI setelah menjawab"):
    prompt = (
        "Sebuah fungsi kuadrat diberikan dalam bentuk umum f(x) = x² - 7x + 10. "
        "Faktorkan fungsi tersebut menjadi bentuk (x - p)(x - q). "
        "Tunjukkan proses langkah demi langkah bagaimana kamu menemukan nilai p dan q, "
        "beserta alasan matematisnya."
    )
    st.code(prompt, language="markdown")
    st.markdown("[🔗 Buka Perplexity untuk melihat jawaban AI](https://www.perplexity.ai/search/faktorkan-bentuk-berikut-f-x-x-zX63Q4XtQvmPVB..m6yvOg)")



# --- 6. Penarikan Kesimpulan ---
st.header("✍️Penarikan Kesimpulan")
st.write("Tuliskan kesimpulanmu terlebih dahulu berdasarkan proses eksplorasi, pengolahan dan pembuktian sebelumnya.")
kesimpulan = st.text_area("📚 Apa kesimpulan yang kamu dapatkan dari aktivitas ini?")

if kesimpulan.strip():
    st.success("✅ Kesimpulan kamu tercatat.")
    
    with st.expander("🔍 Cek Kesimpulan AI setelah kamu menjawab"):
        st.write("📌 *Salin dan tempel prompt ini di Perplexity.ai untuk membandingkan kesimpulanmu dengan AI:*")
        st.code("Buatkan kesimpulan singkat dan jelas tentang bagaimana cara memfaktorkan bentuk kuadrat f(x) = x^2 - 7x + 10 dan apa yang bisa dipelajari dari proses tersebut.")
        st.markdown("[Klik untuk membuka Perplexity](https://www.perplexity.ai)")
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
