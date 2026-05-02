import streamlit as st

# --- KONFIGURASI ---
st.set_page_config(page_title="MHAR - Journals", layout="wide")

# --- HIDE DEFAULT UI ---
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- LOAD CSS ---
try:
    with open("styles_1/style_1.css", encoding="utf-8") as f:
        css = f.read()
except:
    css = ""

# --- STRUKTUR HALAMAN JURNAL ---
st.markdown(f"""
<style>
{css}

/* Penyesuaian khusus halaman jurnal agar rapi */
.jurnal-container {{
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 100%;
    max-width: 1155px;
    margin-top: 1px;
}}

.jurnal-box {{
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    padding: 30px;
    display: flex;
    justify-content: space-between;
    align-items: center; /* KUNCI: Menjaga tombol tetap di tengah secara vertikal */
    gap: 30px; /* Memberi jarak aman antara teks dan tombol */
    transition: 0.3s;
}}

.jurnal-box:hover {{
    border-color: rgba(124, 58, 237, 0.5);
    background: rgba(255, 255, 255, 0.08);
}}

/* TAMBAHKAN INI: Memastikan teks judul mengalah pada tombol */
.jurnal-info {{
    flex: 1; /* Mengambil ruang tersisa */
    min-width: 0; /* Mencegah overflow pada judul yang sangat panjang */
}}

/* TAMBAHKAN INI: Mengunci ukuran tombol agar tidak berubah */
.jurnal-box .cta {{
    flex-shrink: 0; /* KUNCI: Melarang tombol mengecil atau gepeng */
    white-space: nowrap; /* KUNCI: Melarang teks tombol turun ke bawah */
    width: 160px; /* Opsional: Mengunci lebar tombol agar semua tombol sama persis */
    text-align: center;
}}

</style>

<div class="main-wrapper">
    <!-- NAVBAR (Sekarang menggunakan class murni dari style.css) -->
    <div class="navbar-sensor"></div>
    <div class="navbar">
        <div class="nav-left">
            <div class="logo-text">❤️‍🩹MHAR</div>
        </div>
        <div class="nav-right">
            <a href="/" target="_self" class="cta" style="font-size: 13px; padding: 8px 18px;">Back to Home</a>
        </div>
    </div>
    <!-- CONTENT -->
    <div class="hero" style="justify-content: flex-start; padding-top: 17px; text-align: left; align-items: flex-start; padding-left: 60px;">
        <div class="hero-content" style="text-align: left; width: 100%; align-items: flex-start;">
            <div class="about-title" style="margin-bottom: 10px;">Research Journals</div>
            <p style="color: #94a3b8; margin-bottom: 40px;">Referensi jurnal medis pendukung pengembangan sistem.</p>
            <div class="jurnal-container">
                <!-- JURNAL 1 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Caregiver Burden in Different Stages of Alzheimer’s Disease</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Elif KOCA, Özlem TAŞKAPILIOĞLU, Mustafa BAKAR (2016)</p>
                    </div>
                    <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5439478/pdf/npa-54-1-82.pdf" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 2 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Treatment of anxiety disorders</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Dirk Wedekind, MD, PhD (2018)</p>
                    </div>
                    <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5573566/pdf/DialoguesClinNeurosci-19-93.pdf" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 3 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Diagnosa Penyakit Hepatitis dengan Menggunakan Metode Teorema Bayes dan Certainty Factor.</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Muhammad Zulham (2023)</p>
                    </div>
                    <a href="https://jurnal.ilmubersama.com/index.php/blendsains/article/view/241" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 4 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Case Study of Life Journey of Schizophrenic Survivor</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Sirril Wafa (2015)</p>
                    </div>
                    <a href="https://pdfs.semanticscholar.org/9782/aad98c2f8199b4d0c43f04067c8dd78d9563.pdf" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 5 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">The Global Burden of Noncommunicable Diseases and Resilience of Health Systems</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Saman Nazarian (2020)</p>
                    </div>
                    <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7370844/pdf/nihms-1573139.pdf" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 6 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Patologi Penyakit Tidak Menular</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Dr. dr. Rizki Muhammad Ihsan, M.Kes. (2022)</p>
                    </div>
                    <a href="https://media.neliti.com/media/publications/618018-patologi-penyakit-tidak-menular-3b7f9648.pdf" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 7 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Prevalensi Penyakit Kulit Infeksi dan Non-infeksi di Poliklinik Kulit dan Kelamin RSUD Jagakarsa</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Kevin J. K. J. (2024)</p>
                    </div>
                    <a href="https://ejournal.ukrida.ac.id/index.php/Meditek/article/download/3254/2707/15517" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 8 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Sistem Indera pada Manusia: Ketertarikan Antara Gangguan pada Sistem Indera dan Kesehatan Manusia</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Eka Nursolekah (2024)</p>
                    </div>
                    <a href="https://www.researchgate.net/publication/392352865_Sistem_Indera_pada_Manusia_Ketertarikan_Antara_Gangguan_pada_Sistem_Indera_dan_Kesehatan_Manusia/fulltext/683eb6dbc33afe388ac9cc55/Sistem-Indera-pada-Manusia-Ketertarikan-Antara-Gangguan-pada-Sistem-Indera-dan-Kesehatan-Manusia.pdf" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 9 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Diagnostik dan Tatalaksana Asma Berdasarkan GINA 2023</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Faisal Yunus (2023)</p>
                    </div>
                    <a href="https://jurnalrespirologi.org/index.php/jri/article/download/851/706/4959" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 10 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Mental Health Status and Literacy of Adolescent in Rural Area of Mojokerto, East Java, Indonesia</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Ardana. A. A (2025)</p>
                    </div>
                    <a href="https://e-journal.unair.ac.id/JPS/article/download/64237/33600/426847" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 11 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Sleeping Patterns, Personality Insights, and Emotional Savvy: A Study of Medical Students at Hang Tuah University in Surabaya</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Ramadhina. N. S. A. S (2025)</p>
                    </div>
                    <a href="https://e-journal.unair.ac.id/JPS/article/download/68541/33419/420788" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 12 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Karakteristik Kelainan Refraksi pada Pasien di RSUP Dr. M. Djamil Padang Tahun 2019-2020</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Diva Salsabila (2022)</p>
                    </div>
                    <a href="https://jikesi.fk.unand.ac.id/index.php/jikesi/article/download/1207/257/4191" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 13 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Diagnosis dan Tatalaksana Psoriasis Vulgaris</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Suindrayati (2023)</p>
                    </div>
                    <a href="https://www.journalofmedula.com/index.php/medula/article/download/656/485/3423" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 14 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Implementasi Sistem Pakar Untuk Mendiagnosa Penyakit Faringitis Menggunakan Metode Dempster Shafer</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Meylia Dwi Lestari Harianja (2024)</p>
                    </div>
                    <a href="https://ojs.trigunadharma.ac.id/index.php/jsi/article/view/8399" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 15 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Analisis Spasial Pemetaan Prioritas Penanganan Pneumonia pada Balita di Provinsi Jawa Timur</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Rani Delfiyanti (2024)</p>
                    </div>
                    <a href="https://www.jurnal.unismuhpalu.ac.id/index.php/MPPKI/article/view/5026" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 16 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Aplikasi Diagnosa Penyakit Hepatitis dengan Menggunakan Metode Teorema Bayes dan Certainty Factor</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Muhammad Zulham (2023)</p>
                    </div>
                    <a href="https://jurnal.ilmubersama.com/index.php/blendsains/article/view/241" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 17 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Analisis tindakan Warga Desa Payaman dalam mencegah penyakit DBD</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Didi Intan Pratiwi (2017)</p>
                    </div>
                    <a href="https://e-journal.unair.ac.id/PROMKES/article/download/7738/4583" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 18 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Pengetahuan tentang cacingan dan upaya pencegahan kecacingan</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Ganda Sigalingging (2019)</p>
                    </div>
                    <a href="http://jurnal.universitasdarmaagung.ac.id/darmaagunghusada/article/view/309" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 19 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Buku Ajar Bakteriologi (Carrier Penyakit Typus)</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Awaluddin Susanto (2020)</p>
                    </div>
                    <a href="https://www.ejournal.stikesmajapahit.ac.id/index.php/EBook/article/view/663" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 20 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Perilaku Pencegahan Penularan Tuberkulosis: Tinjauan Aspek Individu</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Rusdin Wally (2026)</p>
                    </div>
                    <a href="https://ensiklopediaku.org" target="_blank" class="cta">View Journal</a>
                </div>
                <div class="jurnal-container">
                <!-- JURNAL 21 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Implementasi Sistem Pakar Untuk Mendiagnosa Penyakit Faringitis Menggunakan Metode Dempster Shafer</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Meylia Dwi Lestari Harianja (2024)</p>
                    </div>
                    <a href="https://ojs.trigunadharma.ac.id/index.php/jsi/article/view/8399" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 22 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Analisis Spasial Pemetaan Prioritas Penanganan Pneumonia pada Balita di Provinsi Jawa Timur</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Rani Delfiyanti (2024)</p>
                    </div>
                    <a href="https://www.jurnal.unismuhpalu.ac.id/index.php/MPPKI/article/view/5026" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 23 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Aplikasi Diagnosa Penyakit Hepatitis dengan Menggunakan Metode Teorema Bayes dan Certainty Factor</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Muhammad Zulham (2023)</p>
                    </div>
                    <a href="https://jurnal.ilmubersama.com/index.php/blendsains/article/view/241" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 24 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Analisis Tindakan Warga Desa Payaman dalam Mencegah Penyakit DBD</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Didi Intan Pratiwi (2017)</p>
                    </div>
                    <a href="https://e-journal.unair.ac.id/PROMKES/article/download/7738/4583" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 25 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Pengetahuan tentang Cacingan dan Upaya Pencegahan Kecacingan</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Ganda Sigalingging (2019)</p>
                    </div>
                    <a href="http://jurnal.universitasdarmaagung.ac.id/darmaagunghusada/article/view/309" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 26 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Buku Ajar Bakteriologi (Carrier Penyakit Typus)</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Awaluddin Susanto (2020)</p>
                    </div>
                    <a href="https://www.ejournal.stikesmajapahit.ac.id/index.php/EBook/article/view/663" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 7 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Perilaku Pencegahan Penularan Tuberkulosis: Tinjauan Aspek Individu</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Rusdin Wally (2026)</p>
                    </div>
                    <a href="https://jurnal.ensiklopediaku.org/ojs-2.4.8-3/index.php/erw/article/view/3774" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 28 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Hubungan Pengetahuan dengan Pencegahan Penyakit Malaria</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Siti Rahmawati (2018)</p>
                    </div>
                    <a href="https://ejournal.poltekkes-smg.ac.id/ojs/index.php/jkm/article/view/3741" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 29 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Faktor Risiko Kejadian Diabetes Mellitus Tipe 2</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Rina Agustina (2019)</p>
                    </div>
                    <a href="https://ejournal2.litbang.kemkes.go.id/index.php/jek/article/view/1781" target="_blank" class="cta">View Journal</a>
                </div>
                <!-- JURNAL 30 -->
                <div class="jurnal-box">
                    <div class="jurnal-info">
                        <h4 style="margin-bottom: 5px;">Hubungan Pola Hidup dengan Kejadian Hipertensi</h4>
                        <p style="font-size: 13px; color: #94a3b8;">Andi Nur (2020)</p>
                    </div>
                    <a href="https://jurnal.poltekkes-kemenkes.ac.id/index.php/jhp/article/view/210" target="_blank" class="cta">View Journal</a>
                </div>
            </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
