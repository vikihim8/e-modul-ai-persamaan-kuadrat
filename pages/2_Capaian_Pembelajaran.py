import streamlit as st

st.set_page_config(page_title="📘 Capaian Pembelajaran", layout="centered")

st.title("🎯 Capaian Pembelajaran")

st.markdown("""
### 🧩 Tujuan Umum
Siswa mampu menyelesaikan masalah persamaan kuadrat melalui pendekatan *discovery learning* berbantuan AI, dengan mengembangkan pemahaman konsep secara mandiri dan reflektif.

### 🎯 Tujuan Khusus
Setelah mempelajari modul ini, siswa diharapkan mampu:
1. Mengidentifikasi bentuk umum fungsi kuadrat.
2. Menganalisis pengaruh koefisien terhadap bentuk grafik.
3. Menentukan akar-akar persamaan kuadrat.
4. Menyelesaikan soal dengan metode pemfaktoran dan rumus ABC.
5. Mengaplikasikan konsep fungsi kuadrat dalam masalah kontekstual.
6. Memanfaatkan AI untuk eksplorasi dan refleksi terhadap pemecahan masalah matematika.
""")

st.markdown("""
### 📘 Prinsip E-Modul

E-modul ini dirancang dengan prinsip sebagai berikut:

- **Self-instruction**: siswa dapat belajar mandiri tanpa bergantung pada guru.  
- **Self-contained**: materi cukup lengkap tanpa harus mencari sumber lain.  
- **Stand-alone**: dapat digunakan secara mandiri tanpa bantuan buku atau media lain.  
- **Adaptive**: menyesuaikan dengan tingkat kemampuan siswa yang beragam.  
- **User Friendly**: mudah digunakan dan tampilan bersahabat.  
- **Interactive**: menyediakan aktivitas yang melibatkan siswa secara aktif.  
- **Self-construction**: siswa membangun sendiri pemahamannya melalui eksplorasi.  
- **Self-regulated learning**: siswa mengatur strategi dan waktu belajarnya sendiri.  
- **Reflective**: siswa mengevaluasi dan merefleksikan pemahaman mereka secara berkala.  
""")

st.markdown("""
### 🗂️ Daftar Pertemuan
- **Pertemuan 1:** Bentuk Umum dan Grafik  
- **Pertemuan 2:** Akar Persamaan dengan Pemfaktoran
- **Pertemuan 3:** Metode Rumus ABC  
- **Pertemuan 4:** Aplikasi Persamaan Kuadrat dalam Kehidupan Sehari-hari
""")

# Navigasi
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("⬅️ Kembali ke Beranda"):
        st.switch_page("modul_ai.py")
with col2:
    if st.button("➡️ Pertemuan 1"):
        st.switch_page("pages/3_Pertemuan_1.py")
