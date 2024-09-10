## Project Link
Link: http://daffa-aqil31-sigmart.pbp.cs.ui.ac.id

## Jawaban Pertanyaan
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

# Checklist 1: 
    1. Membuat repositori github baru dengan nama sigmart.
    2. Membuat direktori lokal utama bernama sigmart.
    3. Membuat virtual environtment pada direktori utama dan mengaktifkannya.
    4. Virtual environtment digunakan untuk menginstall library-library python yang dibutuhkan seperti Django, Gunicorn, URLLib3, dan lain-lain.
    5. Memulai projek django baru dengan menjalankan perintah "django-admin startproject sigmart ."
    6. Menambahkan host lokal dan host dari server pws ke variabel "ALLOWED_HOST" pada settings.py agar projek dapat diakses dari server lokal dan pws.
    7. Membuat projek baru pada akun pws saya dengan nama sigmart.
    8. Menghubungkan projek sigmart pada pws dengan direktori sigmart yang terdapat pada direktori lokal saya.
    9. Melakukan add-commit-push ke github dan deploy ke pws.

# Checklist 2:
    2. Menambahkan aplikasi main ke dalam variabel “INSTALLED_APPS” pada settings.py untuk mendaftarkan aplikasi main ke projek sigmart.
    3. Membuat direktori baru dalam direktori main beenama “templates”.
    4. Membuat file html bernama main.html dalam direktori template yg baru dibuat. File html ini berfungsi untuk mengatur tampilan dari aplikasi.

# Checklist 3:
    1. Pada direktori projek utama terdapat file bernama urls.py. Pada file tersebut saya menambahkan rute URL yang mengarah ke tampilan main.

# Checklist 4:
    1. Membuat class bernama Product dalam models.py yang terdapat dalam aplikasi main.
    2. Menambahkan atribut-atribut wajib di dalam class Product yaitu name (nama produk/item), price (harga produk), dan description (deskripsi penjelasan tentang produk).
    3. Selain atribut wajib, saya juga menambahkan dua atribut lain, yaitu rating (rating dari pembeli tentang produk) dan date (tanggal).

# Checklist 5:
    1. Menambahkan fungsi show_main dalam file views.py pada aplikasi main.
    2. Membuat variabel dictionary baru bernama context. Dictionary ini akan diisi dengan data-data yang akan ditampilkan saat aplikasi main diakses.
    3. Menambahkan data-data berupa informasi nama aplikasi, nama saya, dan kelas PBP di dalam dictionary context.
    4. Menambahkan kode dalam main.html yang sudah dibuat pada checklist pertama sehingga file main.html dapat menampilkan ucapan selamat datang dan juga menampilkan data-data yang ada dalam dictionary context.

# Checklist 6:
    1. Membuat file urls.py dalam direktori main. File ini bertanggung jawab dalam mengatur rute URL yang berkaitan dengan aplikasi main. File urls.py dalam aplikasi main akan memanggil fungsi show_main yg ada pada file view.py sebagai tampilan yang akan ditampilkan ketika URL diakses.
    2. Membuat return render yang akan me-render tampilan dari main.html.

# Checklist 7:
    1. Setelah langkah-langkah pada checklist sebelumnya dilakukan, saya melakukan add-commit-push untuk kedua kalinya untuk memperbarui halaman repositori sigmart pada github saya.
    2. Setelah push ke github, langkah terakhir adalah untuk push ke server pws (deployment) untuk memperbarui server pws sigmart.

2. 

3. Git utamanya digunakan untuk dokumentasi source code. Git memungkinkan untuk menyimpan,  mengelola, dan berbagi source code secara efisien dan kolaboratif. Selain itu, developers juga dapat melacak perubahan kode, membuat backup, dan menyimpan versi-versi berbeda dari source code yang mereka buat. Dengan kemampuan yang ditawarkan tersebut, git sangatlah berguna dalam membantu pengembangan perangkat lunak.

4. Menurut saya, Django digunakan untuk permulaan pembelajaran pengembangan perangkat lunak karena mudah dipelajari dan digunakan. Django juga menyediakan banyak fitur bawaan yang diperlukan untuk pengembangan aplikasi web, sehingga pemula tidak perlu repot-repot mengonfigurai banyak komponen eksternal. Selain itu, Django adalah framework yang berbasis python, dan python adalah bahasa yang paling mudah untuk dipelajari oleh pemula karena bahasanya yang simpel. Hal ini akan memudahkan pemula dalam mempelajari pengembangan perangkat lunak menggunakan Django.

 5. Model pada Django disebut ORM karena Django menerapkan ORM untuk mengelola interaksi objek dan database. ORM sendiri adalah teknik pemrograman yang menghubungkan atau memetakan objek dalam kode program ke tabel-tabel dalam database relasional, seperti PostgreSQL, MySQL, SQLite, dan lainnya. Pada Django, ORM digunakan untuk menerjemahkan operasi pada objek model python ini menjadi query SQL yang sesuai untuk mengakses, menyimpan, mengubah, atau menghapus data dalam database. Oleh karena itu, model Django disebut sebagai ORM.