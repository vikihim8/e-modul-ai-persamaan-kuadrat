import streamlit as st

st.set_page_config(page_title="📘 E-Modul AI - Persamaan Kuadrat", layout="centered")

col1, col2 = st.columns([1, 5])

with col1:
    st.image("logo_univ.png", width=100)  # Sesuaikan ukuran

with col2:
    st.title("📘 E-Modul Matematika Berbasis AI")
    st.markdown("**Kelas X SMA | Semester 2**")


st.markdown("""
Selamat datang di e-modul pembelajaran pendekatan **Discovery Learning** berbasis *Artificial Intelligence* (AI). Modul ini dirancang untuk:
- Meningkatkan pemahaman konsep persamaan kuadrat
- Membiasakan siswa berpikir kritis dan mandiri
- Memanfaatkan AI sebagai mitra belajar

Modul ini terdiri dari beberapa pertemuan:
1. **Bentuk Umum dan Grafik**
2. **Faktor dan Akar Persamaan**
3. **Metode Pemfaktoran**
4. **Penerapan dalam Masalah Kontekstual**
""")

if st.button("📌 Lihat Capaian Pembelajaran"):
    st.switch_page("pages/2_Capaian_Pembelajaran.py")

st.markdown("---")
if st.button("🚀 Mulai Pertemuan 1"):
    st.switch_page("pages/3_Pertemuan_1.py")
