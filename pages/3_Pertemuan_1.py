import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from PIL import Image

# --- Setup Spreadsheet ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
json_creds = st.secrets["gcp_service_account"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(json_creds, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("18g9_lCQQDjyU85TJpBUZRzJIrFmrVPeCnjNg4DqrPx8").sheet1

def simpan_ke_sheet(nama, kelas, pertemuan, skor, jawaban, refleksi):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([nama, kelas, pertemuan, skor, jawaban, refleksi, waktu])

# --- Input Identitas ---
st.sidebar.header("🧑 Identitas Siswa")
nama = st.sidebar.text_input("Nama Lengkap")
kelas = st.sidebar.text_input("Kelas")

# --- Judul ---
st.title("📘 Pertemuan 1: Menemukan Konsep Fungsi Kuadrat dari Lintasan Bola")

# --- 1. Pemberian Rangsangan ---
st.header("1. Stimulus")
st.write("""
Bayangkan kamu sedang bermain basket. Kamu melempar bola ke arah ring. Bola akan membentuk lintasan yang melengkung.
Bagaimana kamu bisa mengetahui tinggi maksimum bola?
""")

jawaban1 = st.text_area("📝 Apa yang menarik dan membingungkan dari cerita di atas?")

# --- 2. Identifikasi Masalah ---
st.header("2. Identifikasi Masalah")
jawaban2 = st.text_area("❓ Apa masalah atau pertanyaan yang ingin kamu selesaikan?")

if jawaban2.strip():
    st.success("Kamu dapat mengeksplorasi masalah ini menggunakan Perplexity.")
    st.markdown("[Klik untuk Buka Perplexity](https://www.perplexity.ai/search/bayangkan-kamu-sedang-bermain-ZtKUkcimR8eBfPTulaVLhQ)")

# --- 3. Pengumpulan Data ---
st.header("3. Pengumpulan Data")
st.markdown("## Masukkan nilai untuk persamaan kuadrat")
a = st.number_input("Masukkan nilai a", value=1.0)
b = st.number_input("Masukkan nilai b", value=0.0)
c = st.number_input("Masukkan nilai c", value=0.0)

if a != 0:
    # ---------- Bagian Grafik ----------
    st.markdown("## Grafik Fungsi Kuadrat")
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"y = {a}x² + {b}x + {c}")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

analisis_siswa = st.text_area("Tuliskan analisismu berdasarkan grafik di atas.", placeholder="Misalnya: grafik terbuka ke atas, titik puncak ada di sekitar x = -1, dst.")
if analisis_siswa.strip() != "":
    with st.expander("👉 Klik untuk cek AI (materi otomatis)", expanded=False):
        st.info(
            f"""
            Berdasarkan grafik fungsi kuadrat $$y = {a}x^2 + {b}x + {c}$$, berikut kesimpulan:

            - Grafik terbuka ke **{'atas' if a > 0 else 'bawah'}** karena nilai $$a = {a}$$
            - Titik puncak grafik: $$x = -\\frac{{b}}{{2a}} = {-b/(2*a):.2f}$$
            - Sumbu simetri: $$x = {-b/(2*a):.2f}$$
            - Nilai {'minimum' if a > 0 else 'maksimum'} fungsi: 
              $$y = {a*(-b/(2*a))**2 + b*(-b/(2*a)) + c:.2f}$$
            """
        )
        st.success("Untuk materi lengkap, kamu dapat membuka: [Perplexity AI](https://www.perplexity.ai/search/materi-analisis-grafik-berdasa-lpxD.jhxQJSogx7G7Gjdgw)")

# ---------- Latihan Soal ----------
st.markdown("## 4. Pengolahan Data")
soal = "Berapakah nilai koordinat titik puncak dari fungsi kuadrat ini?"
st.write(soal)
jawaban_siswa = st.text_input("Masukkan jawabanmu (format: x,y)")

if jawaban_siswa:
    x_puncak = -b / (2 * a)
    y_puncak = a * x_puncak**2 + b * x_puncak + c
    jawaban_benar = f"{x_puncak:.2f},{y_puncak:.2f}"

    st.markdown("## Cek Jawaban")
    if jawaban_siswa.replace(" ", "") == jawaban_benar:
        st.success("Jawaban kamu benar! 🎉")
    else:
        st.warning(f"Jawaban belum tepat. Jawaban AI: **{jawaban_benar}**")
else:
    if a == 0:
        st.error("Nilai a tidak boleh 0. Fungsi kuadrat tidak valid jika a = 0.")

# --- 5. Pembuktian ---
st.header("5. Verifikasi")
st.write("Kerjakan soal ini: Grafik fungsi kuadrat memiliki titik puncak (2, 4) dan melalui titik (0, 0). Tentukan persamaan fungsinya.")

verifikasi = st.text_input("🧠 Tulis jawabanmu di sini")

if verifikasi.strip():
    st.success("✅ Jawaban kamu telah disimpan.")
    
    # Tampilkan tombol hanya setelah ada jawaban
    if st.button("🔎 Buka Perplexity untuk klarifikasi/refleksi", key="buka_ai_pembuktian"):
        st.markdown("[Klik untuk Buka Perplexity](https://www.perplexity.ai/search/selesaikan-grafik-fungsi-kuadr-c5uvbD.7SDqcc9vDc_yV0Q)")
else:
    st.warning("Silakan isi jawaban terlebih dahulu untuk membuka bantuan AI.")


# --- 6. Penarikan Kesimpulan ---
st.header("6. Penarikan Kesimpulan")
kesimpulan = st.text_area("📚 Apa kesimpulan yang kamu dapatkan dari aktivitas ini?")

if kesimpulan.strip():
    st.success("✅ Kesimpulan kamu tercatat.")
    
    # Tampilkan tombol hanya setelah ada kesimpulan
    if st.button("🧠 Lihat rangkuman AI", key="buka_ai_kesimpulan"):
        st.markdown("[Klik untuk Buka Perplexity](https://www.perplexity.ai/search/kesimpulan-materi-bentuk-umum-wngG3ZztQfSJDu1vq._F_g)")
else:
    st.warning("Silakan isi kesimpulan terlebih dahulu sebelum membuka rangkuman AI.")

# --- Refleksi Akhir ---
st.subheader("🪞 Refleksi Belajar")
refleksi = st.radio("Seberapa yakin kamu memahami materi fungsi kuadrat?", 
                    ["Tidak yakin", "Kurang yakin", "Cukup yakin", "Yakin", "Sangat yakin"])

kuis = st.radio("Jika a > 0, grafik fungsi kuadrat akan terbuka ke arah mana?", 
                ["Melingkar", "Parabola terbuka ke atas", "Parabola terbuka ke bawah", "Garis lurus"])

cek = ""
if kuis:
    if kuis == "Parabola terbuka ke atas":
        st.success("✅ Jawaban benar!")
        cek = "Benar"
    else:
        st.error("❌ Jawaban kurang tepat.")
        cek = "Salah"

# --- Simpan ke Spreadsheet ---
if st.button("📤 Kirim Jawaban"):
    if nama and kelas:
        semua_jawaban = f"Stimulus: {jawaban1} | Identifikasi: {jawaban2} | Analisis: {analisis_siswa} | Verifikasi: {verifikasi} | Kuis: {cek} | Kesimpulan: {kesimpulan}"
        simpan_ke_sheet(nama, kelas, "Pertemuan 1", "-", semua_jawaban, refleksi)
        st.success("✅ Jawaban berhasil dikirim ke spreadsheet!")
    else:
        st.warning("❗ Nama dan Kelas wajib diisi terlebih dahulu di sidebar.")

# --- Navigasi ---
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
