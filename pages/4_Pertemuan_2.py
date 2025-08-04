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

# Eksplorasi 1
st.subheader("🔬 Eksplorasi 1: Menentukan **Akar-akar dari Grafik**")
st.write("Grafik fungsi kuadrat memotong sumbu $$x$$ ,  di $$x = 2$$ dan $$x = 3$$.  Itu artinya nilai $$x$$ yang membuat $$y = 0$$ adalah akar-akar dari fungsi kuadrat tersebut")

akar1 = st.number_input("Masukkan akar pertama:", key="akar1_input", step=1)
akar2 = st.number_input("Masukkan akar kedua:", key="akar2_input", step=1)

# Simpan ke session state
st.session_state.akar1 = akar1
st.session_state.akar2 = akar2

# Tampilkan bentuk faktornya langsung
if akar1 != 0 or akar2 != 0:  # atau bisa pakai kondisi yang lebih ketat
    st.latex(f"f(x) = a(x - {akar1})(x - {akar2})")
    st.write("Bentuk ini disebut *bentuk faktor* dari fungsi kuadrat.")

# Analisis konsep
analisis1 = st.text_area(
    "Apa hubungan antara titik potong grafik dan akar-akar fungsi kuadrat?", 
    key="analisis1_input"
)
st.session_state.analisis1 = analisis1

# Jika sudah menuliskan analisis awal, baru tampilkan bagian AI
if analisis1.strip() != "":
    st.markdown("---")
    st.markdown("#### 🔎 Cek Jawabanmu dengan AI (Perplexity)")
    st.info("""💬 Bandingkan hasil jawabanmu dengan AI. Apakah serupa? Apa bedanya?
            
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**
Apa hubungan antara akar-akar fungsi kuadrat dan titik potong grafik terhadap sumbu x?

✍️ Setelah membandingkan, tuliskan kembali kesimpulanmu tentang hubungan tersebut:
""")

    # Tambahkan kotak refleksi setelah membandingkan
    st.text_area("Tulis jawaban refleksi Eksplorasi 1 di sini...", key="refleksi_eksplorasi1p2", height=80)



# Eksplorasi 2 (muncul jika analisis1 sudah diisi)
if st.session_state.get("analisis1"):
    st.subheader("🔬 Eksplorasi 2: Membangun Fungsi Kuadrat dari Akar-akar")
    st.write("Jika kamu tahu akar-akarnya, kamu bisa menyusun bentuk faktornya yaitu:")
    
    akar1 = st.number_input("Masukkan akar pertama (p):", step=1, key="akar(1)_input")
    akar2 = st.number_input("Masukkan akar kedua (q):", step=1, key="akar(2)_input")

    if akar1 and akar2:
        # Menampilkan hasil bentuk fungsi kuadrat
        st.markdown("### ✍️ Bentuk Umum Fungsi Kuadrat")
        st.latex(rf"f(x) = (x - {akar1})(x - {akar2})")

        # Hitung koefisien
        a = 1
        b = -(akar1 + akar2)
        c = akar1 * akar2
        st.latex(rf"f(x) = x^2 + ({b})x + ({c})")
    
        # Input analisis eksplorasi
        analisis2 = st.text_area("🔎 Tuliskan penjelasanmu: bagaimana kamu menyusun fungsi kuadrat tersebut?", key="analisis2_input")
        st.session_state.analisis2 = analisis2
        
        if analisis2:
            st.markdown("#### 🔎 Cek Jawabanmu dengan AI (Perplexity)")
            st.info("""💬 Bandingkan hasil jawabanmu dengan AI. Apakah serupa? Apa bedanya?
            
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**
Bagaimana cara menyusun fungsi kuadrat jika diketahui dua akarnya?

✍️ Setelah membandingkan, tuliskan kembali kesimpulanmu tentang hubungan tersebut:
""")

    # Tambahkan kotak refleksi setelah membandingkan
            st.text_area("Tulis jawaban refleksi Eksplorasi 2 di sini...", key="refleksi_eksplorasi2p2", height=80)



# Eksplorasi 3: Mengalikan bentuk faktor menjadi bentuk umum
if (
    st.session_state.get("analisis2") and
    st.session_state.get("akar1") is not None and
    st.session_state.get("akar2") is not None
):
    st.subheader("🔬 Eksplorasi 3: Pengaruh Nilai a terhadap Bentuk Umum Fungsi Kuadrat")
    from sympy import symbols, expand
    
    st.markdown("Sekarang kita akan mencoba mengubah-ubah nilai $$a$$ dan melihat bagaimana bentuk fungsi kuadrat berubah.")
    
    a_eksplorasi = st.number_input("🔢 Coba masukkan nilai a yang berbeda", value=1, key="a_eksplorasi3")
    akar1 = st.number_input("🧮 Masukkan akar pertama", value=0, step=1, key="akar1_eksplorasi3")
    akar2 = st.number_input("🧮 Masukkan akar kedua", value=0, step=1, key="akar2_eksplorasi3")

    x = symbols('x')
    f_eksplorasi = a_eksplorasi * (x - akar1) * (x - akar2)
    f_eksplorasi_expand = expand(f_eksplorasi)

    # Tampilkan dalam bentuk fungsi kuadrat yang diperluas
    st.latex(f"f(x) = {sp.latex(f_eksplorasi_expand)}")
    
    st.write("Apakah bentuk umum fungsi kuadrat berubah saat kamu mengubah nilai a? Coba ganti nilai a beberapa kali.")

    analisis3 = st.text_area("Apa yang kamu perhatikan dari hasil perkalian ini?", key="analisis3")
    
    if analisis3:
        st.markdown("#### 🔎 Cek Jawabanmu dengan AI (Perplexity)")
        st.info("""💬 Bandingkan hasil jawabanmu dengan AI. Apakah serupa? Apa bedanya?
            
📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**
Bagaimana cara mengubah bentuk faktor fungsi kuadrat menjadi bentuk umum?

✍️ Setelah membandingkan, tuliskan kembali kesimpulanmu tentang hubungan tersebut:
""")

    # Tambahkan kotak refleksi setelah membandingkan
        st.text_area("Tulis jawaban refleksi Eksplorasi 3 di sini...", key="refleksi_eksplorasi3p2", height=80)




# ------------------------- Eksplorasi 4: Menyelidiki Pola dari Bentuk Umum --------------------------
import streamlit as st
from sympy import symbols, expand, latex

if st.session_state.get("analisis3"):
    st.header("✍️ Eksplorasi 4: Menyelidiki Pola dari Bentuk Umum")

    x = symbols('x')

    st.write("""
    Misalkan kita punya fungsi kuadrat dalam bentuk faktor:
    
    **$$f(x) = a(x - p)(x - q)$$**
    
    Ayo ubah bentuk ini menjadi bentuk umum (standar):  
    **$$f(x) = ax² + bx + c$$**
    """)

    nilai_a = st.number_input("Masukkan nilai a", value=1, key="nilai_a_input")
    nilai_p = st.number_input("Masukkan nilai p", value=1, key="nilai_p_input")
    nilai_q = st.number_input("Masukkan nilai q", value=2, key="nilai_q_input")

    # Simpan ke session
    st.session_state.a = nilai_a
    st.session_state.p = nilai_p
    st.session_state.q = nilai_q

    # Expand bentuk faktornya
    bentuk_umum = expand(nilai_a * (x - nilai_p)*(x - nilai_q))
    st.latex("f(x) = " + latex(bentuk_umum))

    # Pertanyaan reflektif
    analisis4_1 = st.text_area("Apa yang kamu perhatikan dari hasil bentuk umum tersebut?", key="analisis4_1")

    # Lanjut jika siswa menulis analisis

        st.markdown("---")
        st.write("Sekarang coba ubah nilai $$p$$ dan $$q$$ beberapa kali.")
        st.write("Amati perubahan pada koefisien $$**b**$$ dan $$**c**$$ dari bentuk umum tersebut.")
        st.text_area("Apa pola hubungan antara $$p$$, $$q$$ dengan koefisien $$b$$ dan $$c$$ yang kamu temukan?", key="analisis4_2")

    if analisis4_1:
        st.markdown("---")
        st.markdown("#### 🔎 Cek Jawabanmu dengan AI (Perplexity)")
        st.info("""💬 Bandingkan hasil temuanmu dengan AI. Apakah serupa? Apa perbedaannya?

📌 **Salin dan tempel prompt ini ke [Perplexity AI](https://www.perplexity.ai) untuk mendapatkan penjelasan lengkap:**

**Prompt:**
Bagaimana hubungan antara akar-akar (p dan q) dengan koefisien b dan c dalam fungsi kuadrat f(x) = a(x - p)(x - q)?

✍️ Setelah membandingkan, tuliskan kesimpulanmu di bawah ini:
""")

        st.text_area("Tulis jawaban refleksi Eksplorasi 4 di sini...", key="refleksi_eksplorasi4", height=80)




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



# 4. Pengolahan Data
st.header("📝 Pengolahan Data")
st.write("Faktorkan bentuk berikut:")

st.latex(r"f(x) = x^2 - 7x + 10")

analisisdata = st.text_input("Tulis bentuk faktornya:")

if analisisdata.strip():
    st.success("✅ Jawaban disimpan.")

    

# --- 5. Pembuktian (Verifikasi) ---
st.header("Verifikasi")
with st.expander("🔍 Cek AI setelah menjawab"):
    st.markdown("#### 🔗 Periksa pemahamanmu dengan AI")

    # Prompt AI
    st.markdown("##### 🔎 Cek AI")
    st.code("Sebuah fungsi kuadrat diberikan dalam bentuk umum f(x) = x² - 7x + 10. "
            "Faktorkan fungsi tersebut menjadi bentuk (x - p)(x - q). "
            "Tunjukkan proses langkah demi langkah bagaimana kamu menemukan nilai p dan q, "
            "beserta alasan matematisnya.")
    
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














