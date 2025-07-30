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
if page == "Stimulus":
    st.subheader("📍 Stimulus")
    st.write("Diketahui grafik fungsi kuadrat memotong sumbu X di x = 2 dan x = 3")
    st.image("pages/grafik_pq.png", caption="Contoh Grafik p dan q", use_container_width=True)
    st.text_input("Apa yang bisa kamu simpulkan dari titik potong tersebut terhadap bentuk fungsi kuadrat?")

# Identifikasi Masalah
elif page == "Identifikasi Masalah":
    st.subheader("🔍 Identifikasi Masalah")
    identifikasi = st.text_area("Apa yang ingin kamu ketahui atau cari berdasarkan grafik di atas?")
    st.text_input("Tuliskan satu pertanyaan utamamu di sini:", key="pertanyaan")

# Eksplorasi 1
elif page == "Eksplorasi 1":
    st.subheader("🔬 Eksplorasi 1: Menentukan Akar-akar dari Grafik")
    st.write("Grafik fungsi kuadrat memotong sumbu $$x$$ di $$x$$ = 2 dan $$x$$ = 3. Itu artinya nilai $$x$$ yang membuat $$y = 0$$ adalah akar-akar dari fungsi kuadrat tersebut.")
    st.session_state.akar1 = st.number_input("Masukkan akar pertama:", key="akar1_input")
    st.session_state.akar2 = st.number_input("Masukkan akar kedua:", key="akar2_input")
    st.session_state.analisis1 = st.text_area("Apa hubungan antara titik potong grafik dan akar-akar fungsi kuadrat?")

    if st.session_state.analisis1:
        st.markdown("##### 🔎 Cek AI (Perplexity)")
        st.code("Apa hubungan antara akar-akar fungsi kuadrat dan titik potong grafik terhadap sumbu x?")
        st.info("💡 Salin dan tempelkan prompt di atas ke Perplexity.ai untuk membandingkan pemahamanmu.")

# Eksplorasi 2 (muncul jika analisis1 sudah diisi)
elif page == "Eksplorasi 2" and st.session_state.analisis1:
    st.subheader("🔬 Eksplorasi 2: Membangun Fungsi Kuadrat dari Akar-akar")
    st.write("Jika kamu tahu akar-akarnya, kamu bisa menyusun bentuk faktornya yaitu: $$f(x) = a(x - akar1)(x - akar2)$$")
    st.latex("f(x) = a(x - %s)(x - %s)" % (st.session_state.akar1, st.session_state.akar2))
    st.session_state.nilai_a = st.number_input("Tentukan nilai $$a$$ (gunakan $$a$$ = 1 untuk sementara):", key="nilai_a_input")
    analisis2 = st.text_area("Apa pendapatmu tentang hubungan antara akar dan bentuk faktornya?")

    if analisis2:
        st.markdown("##### 🔎 Cek AI (Perplexity)")
        st.code("Bagaimana menyusun fungsi kuadrat dari dua akar yang diketahui?")
        st.info("🧠 Salin dan tempelkan prompt tersebut ke Perplexity.ai.")

# Eksplorasi 3
elif page == "Eksplorasi 3":
    st.subheader("🔬 Eksplorasi 3: Mengalikan Bentuk Faktor menjadi Bentuk Umum")
    a = st.session_state.nilai_a
    akar1 = st.session_state.akar1
    akar2 = st.session_state.akar2
    x = symbols('x')
    f = a * (x - akar1) * (x - akar2)
    f_expand = expand(f)
    st.latex(f"f(x) = {f_expand}")
    st.write("Sekarang kamu sudah mendapatkan bentuk umum dari fungsi kuadrat.")
    analisis3 = st.text_area("Apa yang kamu perhatikan dari hasil perkalian bentuk faktor ini?")

    if analisis3:
        st.markdown("##### 🔎 Cek AI")
        st.code("Bagaimana cara mengalikan bentuk faktorisasi fungsi kuadrat menjadi bentuk umum?")
        st.info("🔍 Salin dan tempelkan ke Perplexity untuk mengecek pemahamanmu.")

# Eksplorasi 4
elif page == "Eksplorasi 4":
    st.subheader("🔬 Eksplorasi 4: Menemukan $$p$$ dan $$q dari $$a$$, $$b$$, dan $$c$$")
    st.write("Tanpa diberitahu bagaimana mencari nilai $$p$$ dan $$q$$, coba amati koefisien dari bentuk umum $$ax^2 + bx + c$$")
    f_expand = expand(st.session_state.nilai_a * (x - st.session_state.akar1)*(x - st.session_state.akar2))
    st.latex(f"f(x) = {f_expand}")
    tebakan_p = st.number_input("Tebak nilai $$p$$ (akar pertama):", key="tebakan_p")
    tebakan_q = st.number_input("Tebak nilai $$q$$ (akar kedua):", key="tebakan_q")
    analisis4 = st.text_area("Apa alasanmu memilih nilai $$p$$ dan $$q$$ tersebut?")

    if analisis4:
        if st.button("Cek Tebakan"):
            hasil_c = tebakan_p * tebakan_q
            hasil_b = -1 * (tebakan_p + tebakan_q)
            st.write(f"Hasil perkalian $$p*q$$ = {hasil_c}")
            st.write(f"Hasil penjumlahan $$(p+q)$$ = {hasil_b}")
            st.info("Bandingkan hasil ini dengan nilai $$b$$ dan $$c$$ dari bentuk umum.")
            st.markdown("##### 🔎 Cek AI")
            st.code("Bagaimana cara menemukan p dan q untuk memfaktorkan fungsi kuadrat dalam bentuk umum?")
            st.info("💬 Coba bandingkan hasil tebakanmu dengan penjelasan dari AI.")

# Eksplorasi 5
elif page == "Eksplorasi 5":
    st.subheader("🔬 Eksplorasi 5: Buat Kesimpulan Umum")
    st.write("Setelah melakukan semua eksplorasi, apa kesimpulanmu untuk menentukan bentuk umum fungsi kuadrat dari grafiknya?")
    kesimpulan = st.text_area("Tuliskan kesimpulanmu:")
    if kesimpulan:
        st.markdown("##### 🔎 Cek AI")
        st.code("Bagaimana mengubah bentuk umum fungsi kuadrat menjadi bentuk faktor dan menemukan akarnya?")
        st.info("📝 Bandingkan kesimpulanmu dengan versi AI.")


st.header("4. Pengolahan Data")
st.write("Faktorkan bentuk berikut:")
st.latex(r"f(x) = x^2 - 7x + 10")
analisis = st.text_input("📝 Tulis bentuk faktornya:")

if analisis.strip():
    st.success("✅ Jawaban disimpan.")
    with st.expander("🔍 Cek AI setelah menjawab"):
        st.markdown("[Buka Perplexity](https://www.perplexity.ai/search/faktorkan-bentuk-berikut-f-x-x-zX63Q4XtQvmPVB..m6yvOg)")
else:
    st.warning("Silakan faktorkan dulu sebelum cek AI.")
    

# --- 5. Pembuktian (Verifikasi) ---
st.header("5. Pembuktian")
st.write("Soal: Faktorkan bentuk berikut:")
st.latex(r"f(x) = x^2 - 3x - 10")
analisis_l4 = st.text_input("🧠 Jawabanmu (dalam bentuk faktor):")

if analisis_l4.strip():
    st.success("✅ Jawaban disimpan.")
    with st.expander("🔍 Lihat pembahasan AI setelah menjawab"):
        st.markdown("[Buka Perplexity](https://www.perplexity.ai/search/soal-faktorkan-bentuk-berikut-787Tzl.dRTSZOdt4ppj4QQ)")
else:
    st.warning("Silakan isi jawaban terlebih dahulu.")

# --- 6. Penarikan Kesimpulan ---
st.header("6. Penarikan Kesimpulan")
kesimpulan = st.text_area("📚 Apa kesimpulan yang kamu dapatkan dari aktivitas ini?")
if kesimpulan.strip():
    st.success("✅ Kesimpulan kamu tercatat.")
    if st.button("Lihat rangkuman AI", key="buka_ai_kesimpulan_2"):
        st.markdown("[Buka Rangkuman AI](https://www.perplexity.ai/search/kesimpulan-materi-faktorisasi-_FgcWfjBTE6928qG9BJ9kQ)")
else:
    st.warning("Silakan isi kesimpulan sebelum cek rangkuman.")

# --- Refleksi Akhir ---
st.subheader("🪞 Refleksi Belajar")
refleksi = st.radio("Seberapa yakin kamu memahami materi faktorisasi fungsi kuadrat?", 
                    ["Tidak yakin", "Kurang yakin", "Cukup yakin", "Yakin", "Sangat yakin"])

kuis = st.radio("Jika f(x) = x² - 7x + 10, maka faktornya adalah ...", 
                ["(x-5)(x-2)", "(x+5)(x+2)", "(x-7)(x+10)", "Tidak bisa difaktorkan"])

cek = ""
if kuis:
    if kuis == "(x-5)(x-2)":
        st.success("✅ Jawaban benar!")
        cek = "Benar"
    else:
        st.error("❌ Jawaban belum tepat.")
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
