<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PBP README.md</title>
</head>
<body>

## Profile
***Nama:*** Daffa Aqil Mahmud<br/>
***NPM:*** 2306245056<br/>
***Kelas:*** PBP C

## Project Link
**Link:** http://daffa-aqil31-sigmart.pbp.cs.ui.ac.id

## Jawaban Pertanyaan Tugas 2
***1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!***
<ul>
    <i>Checklist 1:</i>
        <ol>
            <li>Membuat repositori github baru dengan nama sigmart.</li>
            <li>Membuat direktori lokal utama bernama sigmart.</li>
            <li>Membuat virtual environtment pada direktori utama dan mengaktifkannya.</li>
            <li>Virtual environtment digunakan untuk menginstall library-library python yang dibutuhkan seperti Django, Gunicorn, URLLib3, dan lain-lain.</li>
            <li>Memulai projek Django baru dengan menjalankan perintah "django-admin startproject sigmart ."</li>
            <li>Menambahkan host lokal dan host dari server pws ke variabel "ALLOWED_HOST" pada modul <code>settings.py</code> agar projek dapat diakses dari server lokal dan pws.</li>
            <li>Membuat projek baru pada akun pws saya dengan nama sigmart.</li>
            <li>Menghubungkan projek sigmart pada pws dengan direktori sigmart yang terdapat pada direktori lokal saya.</li>
            <li>Melakukan add-commit-push ke github dan deploy ke pws.</li>
        </ol>
    <i>Checklist 2:</i>
        <ol>
            <li>Membuat direktori main (aplikasi main) dengan menggunakan fungsi "startapp" yang ada di dalam modul <code>manage.py</code>.</li>
            <li>Menambahkan aplikasi main ke dalam variabel “INSTALLED_APPS” pada <code>settings.py</code> untuk mendaftarkan aplikasi main ke projek sigmart.</li>
            <li>Membuat direktori baru dalam direktori main beenama “templates”.</li>
            <li>Membuat file html bernama <code>main.html</code> dalam direktori template yg baru dibuat. File html ini berfungsi untuk mengatur tampilan dari aplikasi.</li>
        </ol>
    <i>Checklist 3:</i>
        <ol>
            <li>Pada direktori projek utama terdapat modul bernama <code>urls.py</code>. Pada file tersebut saya menambahkan rute URL yang mengarah ke tampilan main.</li>
        </ol>
    <i>Checklist 4:</i>
        <ol>
            <li>Membuat class bernama Product dalam <code>models.py</code> yang terdapat dalam aplikasi main.</li>
            <li>Menambahkan atribut-atribut wajib di dalam class Product yaitu name (nama produk/item), price (harga produk), dan description (deskripsi penjelasan tentang produk).</li>
            <li>Selain atribut wajib, saya juga menambahkan dua atribut lain, yaitu rating (rating dari pembeli tentang produk) dan date (tanggal).</li>
        </ol>
    <i>Checklist 5:</i>
        <ol>
            <li>Menambahkan fungsi show_main dalam modul <code>views.py</code> pada aplikasi main.</li>
            <li>Membuat variabel dictionary baru bernama context. Dictionary ini akan diisi dengan data-data yang akan ditampilkan saat aplikasi main diakses.</li>
            <li>Menambahkan data-data berupa informasi nama aplikasi, nama saya, dan kelas PBP di dalam dictionary context.</li>
            <li>Menambahkan kode dalam <code>main.html</code> yang sudah dibuat pada checklist pertama sehingga file <code>main.html</code> dapat menampilkan ucapan selamat datang dan juga menampilkan data-data yang ada dalam dictionary context.</li>
        </ol>
    <i>Checklist 6:</i>
        <ol>
            <li>Membuat modul <code>urls.py</code> dalam direktori main. Modul ini bertanggung jawab dalam mengatur rute URL yang berkaitan dengan aplikasi main. Modul <code>urls.py</code> dalam aplikasi main akan memanggil fungsi show_main yg ada pada modul view.py sebagai tampilan yang akan ditampilkan ketika URL diakses.</li>
            <li>Membuat return render yang akan me-render tampilan dari <code>main.html</code>.</li>
        </ol>
    <i>Checklist 7:</i>
        <ol>
            <li>Setelah langkah-langkah pada checklist sebelumnya dilakukan, saya melakukan add-commit-push untuk kedua kalinya untuk memperbarui halaman repositori sigmart pada github saya.</li>
            <li>Setelah push ke github, langkah terakhir adalah untuk push ke server pws (deployment) untuk memperbarui server pws sigmart.</li>
        </ol>
</ul><br>

***2. Bagan Request-Respond Django:***
![Bagan Request-Respond Django](bagan_request-respond_django.jpeg)
Request yang dikirim oleh user melalui web browser akan dikirim ke server dan diterima oleh <code>urls.py</code>. Lalu, berdasarkan URL yang diterima, <code>urls.py</code> akan mengatur/menentukan (routing) request tersebut diteruskan ke fungsi atau class mana yang berada di dalam <code>views.py</code>. <code>views.py</code> adalah modul yang mengatur jalannya logika aplikasi. Jika diperlukan, <code>views.py</code> dapat menentukan untuk mengakses <code>models.py</code> untuk dapat berinteraksi dengan database. Setelah semua request telah dijalankan, <code>views.py</code> akan me-render berkas HTML untuk ditampilkan ke user.

***3. Jelaskan fungsi git dalam pengembangan perangkat lunak!***
<ul>
    Git utamanya digunakan untuk dokumentasi source code. Git memungkinkan untuk menyimpan,  mengelola, dan berbagi source code secara efisien dan kolaboratif. Selain itu, developers juga dapat melacak perubahan kode, membuat backup, dan menyimpan versi-versi berbeda dari source code yang mereka buat. Dengan kemampuan yang ditawarkan tersebut, git sangatlah berguna dalam membantu pengembangan perangkat lunak.
</ul><br>

***4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?***
<ul>
    Menurut saya, Django digunakan untuk permulaan pembelajaran pengembangan perangkat lunak karena mudah dipelajari dan digunakan. Django juga menyediakan banyak fitur bawaan yang diperlukan untuk pengembangan aplikasi web, sehingga pemula tidak perlu repot-repot mengonfigurai banyak komponen eksternal. Selain itu, Django adalah framework yang berbasis python, dan python adalah bahasa yang paling mudah untuk dipelajari oleh pemula karena bahasanya yang simpel. Hal ini akan memudahkan pemula dalam mempelajari pengembangan perangkat lunak menggunakan Django.
</ul><br>

***5. Mengapa model pada Django disebut sebagai ORM?***
<ul>
    Model pada Django disebut ORM karena Django menerapkan ORM untuk mengelola interaksi objek dan database. ORM sendiri adalah teknik pemrograman yang menghubungkan atau memetakan objek dalam kode program ke tabel-tabel dalam database relasional, seperti PostgreSQL, MySQL, SQLite, dan lainnya. Pada Django, ORM digunakan untuk menerjemahkan operasi pada objek model python ini menjadi query SQL yang sesuai untuk mengakses, menyimpan, mengubah, atau menghapus data dalam database. Oleh karena itu, model Django disebut sebagai ORM.
</ul><br>

## Jawaban Pertanyaan Tugas 3
***1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?***
<ul>
    Data delivery adalah tulang punggung dalam pengimplementasian sebuah platform karena memungkinkan akses cepat, konsisten, dan aman terhadap data yang dibutuhkan oleh pengguna atau komponen lain dalam platform. Tanpa data delivery yang bagus, platform tidak akan dapat beroperasi secara efisien, mengurangi keandalan, skalabilitas, dan kualitas pengalaman pengguna.
</ul><br>

***2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?*** 
<ul>
    Menurut saya, JSON lebih baik daripada XML karena format penjabaran informasi pada JSON lebih mudah untuk dibaca dan dipahami (lebih *human-readable*). Hal itu juga merupakan hal yang membuat JSON lebih populer dari XML.
</ul><br>

***3. Jelaskan fungsi dari method <code>is_valid()</code> pada form Django dan mengapa kita membutuhkan method tersebut?*** 
<ul>
    Method <code>is_valid</code> pada Django memiliki peran untuk memastikan data yang diproses sudah valid (dalam format yang tepat), sehingga dapat menghindari memproses data-data yang rusak.
</ul><br>

***4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan <code>csrf_token</code> pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?***
<ul>
    <code>csrf_token</code> dalam form Django sangat penting untuk mencegah serangan Cross-Site Request Forgery (CSRF) yang bisa memanipulasi aplikasi untuk melakukan tindakan yang tidak diinginkan atas nama pengguna yang sah. Jika tidak menambahkan csrf_token, aplikasi yang dibuat menjadi rentan terhadap berbagai serangan yang bisa dieksploitasi oleh penyerang (hacker) untuk mencuri data, mengubah pengaturan akun, atau melakukan transaksi berbahaya.
</ul><br>

***5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!***
<ul>
    <i>Checklist 1:</i>
        <ol>
            <li>Membuat direktori <code>templates</code> di folder root dan membuat file <code>base.html</code> di dalamnya.</li>
            <li>Menghapus file <code>db.sqlite3</code> sebelumnya.</li>
            <li>Mengubah id yang tadinya integer menjadi UUID.</li>
            <li>Membuat file <code>forms.py</code> di direktori <code>main</code>.</li>
            <li>Menambahkan list <code>field</code> di dalam <code>forms.py</code> dengan nilai <code>["name", "description", "price"]</code>.</li>
            <li>Menambahkan fungsi <code>create_product_entry</code> pada modul <code>views.py</code>.</li>
            <li>Menambahkan pattern urls dari fungsi <code>create_product_entry</code> ke <code>urls.py</code> yang ada dalam direktori <code>main</code>.</li>
            <li>Membuat file <code>create_product_entry.html</code> untuk tampilan memasukkan product baru.</li>
            <li>Menampilkan data <code>Product</code> yang telah dimasukkan dengan mengubah isi <code>main.html</code>.</li>
        </ol>
    <i>Checklist 2:</i>
        <ol>
            <li>Menambahkan fungsi-fungsi pada modul <code>views.py</code> untuk mendapatkan informasi objek yang sudah dimasukkan ke aplikasi dalam format XML, JSON, XML by id, dan JSON by id.</li>
        </ol>
    <i>Cheklist 3:</i>
        <ol>
            <li>Menambahkan pattern urls dari fungsi-fungsi XML dan JSON yang telah ditambahkan di <code>views.py</code> ke <code>urls.py</code> yang ada dalam direktori <code>main</code>.</li>
        </ol>
</ul><br>

***6. ScreenShot JSON dan XML***
![alt text](<XML by id.png>) 
![alt text](<JSON by id.png>) 
![alt text](JSON.png) 
![alt text](XML.png)

## Jawaban Pertanyaan Tugas 4
***1. Apa perbedaan antara <code>HttpResponseRedirect()</code> dan <code>redirect()<code>*** 
<ul>
    <li>HttpResponseRedirect() hanya menerima URL string dan lebih manual dalam penggunaannya.</li>
    <li>redirect() lebih fleksibel karena mendukung lebih banyak jenis argumen dan memudahkan pengembangan.</li>
</ul><br>

***2. Jelaskan cara kerja penghubungan model <code>Product</code> dengan <code>User<code>!***
<ul>
    <li><strong>OneToMany:</strong> Menggunakan <code>ForeignKey</code> untuk menghubungkan setiap produk ke satu pemilik (User).</li>
</ul><br>

***3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.***
<ul>
    <li><strong>Authentication</strong> adalah proses verifikasi identitas pengguna. Ini mencakup memastikan bahwa pengguna adalah siapa yang mereka klaim dengan cara memeriksa kredensial mereka, seperti username dan password.</li>
        <ul>
            <li>Saat pengguna melakukan login, Django menggunakan modul <code>django.contrib.auth</code> untuk memverifikasi kredensial pengguna.</li>
            <li>Jika kredensial valid, pengguna dianggap terautentikasi dan dapat mengakses bagian tertentu dari aplikasi.</li>
        </ul>
    <li><strong>Authorization</strong> adalah proses menentukan apakah pengguna yang terautentikasi memiliki izin untuk mengakses sumber daya tertentu atau melakukan tindakan tertentu. Ini berhubungan dengan kontrol akses.</li>
        <ul>
            <li>Setelah pengguna terautentikasi, sistem dapat memeriksa apakah mereka memiliki izin untuk mengakses view atau melakukan tindakan tertentu, seperti mengedit atau menghapus data.</li>
            <li>Django menyediakan decorator seperti <code>@login_required</code> dan sistem izin untuk membantu mengelola otorisasi.</li>
        </ul>
</ul><br>

***4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?***
<ol>
    <li><strong>Cara Django Mengingat Pengguna yang Telah Login</strong></li>
    <ol>
        <li><i>Sesi:</i></li>
        <ul>
            Saat pengguna berhasil login, Django membuat sesi untuk pengguna tersebut. Sesi ini menyimpan informasi tentang pengguna, seperti ID pengguna, yang akan digunakan untuk mengidentifikasi mereka di permintaan berikutnya.
        </ul>
        <li><i>Cookies:</i></li>
        <ul>
            Django menggunakan cookies untuk menyimpan ID sesi di sisi klien. Cookie ini biasanya disebut sessionid.
            Setiap kali pengguna melakukan permintaan ke server, browser mengirimkan cookie ini bersama dengan permintaan tersebut. Django dapat menggunakan ID sesi yang terdapat dalam cookie untuk mengambil informasi sesi dari server.
        </ul>
        <li><i>Penyimpanan Sesi:</i></li>
        <ul>
            Informasi sesi dapat disimpan di berbagai backend, seperti database, cache, atau filesystem, tergantung pada pengaturan aplikasi.
        </ul>
    </ol>
    <li><strong>Kegunaan Lain dari Cookies</strong></li>
    <ol>
        <li><i>Personalisasi:</i></li>
        <ul>
            Cookies dapat digunakan untuk menyimpan preferensi pengguna, seperti tema atau bahasa yang dipilih.
        </ul>
        <li><i>Pelacakan:</i></li>
        <ul>
            Cookies sering digunakan untuk melacak perilaku pengguna di situs web, seperti halaman yang dikunjungi dan produk yang dilihat. Ini berguna untuk analisis dan pengoptimalan.
        </ul>
        <li><i>Pengiklanan:</i></li>
        <ul>
            Banyak layanan iklan menggunakan cookies untuk melacak efektivitas iklan dan menampilkan iklan yang relevan berdasarkan perilaku pengguna.
        </ul>
        <li><i>Keamanan:</i></li>
        <ul>
            Cookies dapat membantu dalam meningkatkan keamanan aplikasi, misalnya, dengan menyimpan token untuk otorisasi.
        </ul>
    </ol>
    <li><strong>Keamanan Cookies</strong></li>
    <ul>
        Tidak semua cookies aman digunakan. Meskipun cookies sangat berguna untuk mengelola sesi pengguna dan menyimpan informasi lain, ada beberapa risiko dan kondisi yang dapat membuat cookies tidak aman.
    </ul>
    <ol>
        <li><i>Risiko Keamanan Cookies</i></li>
        <ul>
            <strong>XSS (Cross-Site Scripting):</strong> Jika aplikasi web rentan terhadap serangan XSS, penyerang dapat menyisipkan skrip berbahaya ke dalam halaman yang dapat mengakses cookies pengguna. Jika cookies tidak diatur dengan flag HttpOnly, penyerang bisa mencuri informasi sensitif yang tersimpan dalam cookies.
        </ul>
        <ul>
            <strong>CSRF (Cross-Site Request Forgery):</strong> Cookies yang tidak dilindungi dapat digunakan dalam serangan CSRF, di mana penyerang memanfaatkan sesi pengguna yang sudah terautentikasi untuk melakukan tindakan tanpa sepengetahuan pengguna.
        </ul>
        <ul>
            <strong>Man-in-the-Middle Attacks:</strong> Jika cookie tidak dilindungi oleh HTTPS (dengan flag Secure), penyerang dapat menangkap cookies dalam perjalanan antara klien dan server, terutama dalam koneksi yang tidak aman.
        </ul>
        <li><i>Kebocoran Data Sensitif</i></li>
        <ul>
            <strong>Data Pribadi:</strong> Jika aplikasi menyimpan data pribadi atau informasi sensitif (seperti password, nomor kartu kredit, dll.) dalam cookies, itu bisa berisiko. Cookies bisa diakses oleh pengguna lain yang menggunakan perangkat yang sama atau melalui serangan.
        </ul>
        <li><i>Cookies Permanen vs. Cookies Sesi</i></li>
        <ul>
            <strong>Cookies Permanen:</strong> Cookies yang disimpan untuk periode yang lebih lama dapat menjadi target bagi penyerang. Jika seorang penyerang mendapatkan akses ke perangkat pengguna, mereka dapat mengakses cookies yang tersimpan dan melakukan penyalahgunaan.
        </ul>
        <ul>
            <strong>Cookies Sesi:</strong> Meskipun lebih aman karena hanya aktif selama sesi pengguna, jika tidak diatur dengan baik, mereka masih dapat berisiko jika terdapat kerentanan keamanan lainnya.
        </ul>
    </ol>
</ol><br>

***5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step***
<ul>
    <i>Checklist 1:</i>
        <ul>
            <li>Registrasi:</li>
            <ol>
                <li>Menyalakan virtual environment.</li>
                <li>Import <code>UserCreationForm</code> dan <code>messages</code> ke modul <code>views.py</code> yang ada di direktori <code>main</code>.</li>
                <li>Menambahkan fungsi register pada <code>views.py</code> untuk mengatur logic saat registrasi ingin dilakukan.</li>
                <li>Membuat file <code>register.html</code> di direktori <code>templates</code> yang ada di direktori <code>main</code>. File ini akan menampilkan laman registrasi tempat dimana registrasi dapat dilakukan.</li>
                <li>Mengimport fungsi register yang telah dibuat ke modul <code>urls.py</code> dan menambahkan routing fungsi tersebut pada list <code>urlpatterns</code>.</li>
            </ol>
            <li>Login:</li>
            <ol>
                <li>Import <code>authenticate</code>, <code>login</code>, dan <code>AuthenticationForm</code> ke <code>views.py</code>.</li>
                <li>Membuat fungsi <code>login_user</code> di dalam <code>views.py</code> untuk mengatur logic proses login.</li>
                <li>Membuat file <code>login.html</code> di direktori <code>templates</code> yang ada di direktori <code>main</code>. File ini akan menampilkan laman login tempat dimana login dapat dilakukan.</li>
                <li>Mengimport fungsi login yang telah dibuat ke modul <code>urls.py</code> dan menambahkan routing fungsi tersebut pada list <code>urlpatterns</code>.</li>
            </ol>
            <li>Logout:</li>
            <ol>
                <li>Import <code>logout</code> ke <code>views.py</code>.</li>
                <li>Membuat fungsi <code>logout_user</code> di dalam <code>views.py</code> untuk mengatur logic proses logout.</li>
                <li>Membuat file <code>logout.html</code> di direktori <code>templates</code> yang ada di direktori <code>main</code>. File ini akan menampilkan laman logout tempat dimana logout dapat dilakukan.</li>
                <li>Mengimport fungsi logout yang telah dibuat ke modul <code>urls.py</code> dan menambahkan routing fungsi tersebut pada list <code>urlpatterns</code>.</li>
            </ol>
        </ul>
    <i>Checklist 2:</i>
        <ol>
            <li>Menjalankan aplikasi sigmart secara local dengan command <code>python manage.py runserver</code></li>
            <li>Membuat 2 akun baru dengan meng-klik tombol register di login page</li>
            <li>Memasukan 3 produk (nama produk, deskripsi, dan harga) di setiap akun yang dibikin</li>
        </ol>
    <i>Checklist 3:</i>
        <ol>
            <li>Import <code>from django.contrib.auth.models import User</code> ke <code>models.py</code>.</li>
            <li>Membuat dan menginstansiasi variabel user dalam class <code>Product</code> di modul <code>models.py</code> dengan class <code>ForeignKey</code> dari class <code>User</code>.</li>
            <li>Menambahkan potongan-potongan kode untuk mengimplementasikan fungsi user di modul <code>views.py</code>.</li>
        </ol>
    <i>Checklist 4:</i>
        <ol>
            <li>Membuka modul <code>views.py</code>.</li>
            <li>Mengubah isi dari key <code>name</code> pada dictionary <code>context</code> yang berada di dalam fungsi <code>show_main</code> menjadi <code>request.user.username</code> untuk menampilkan nama dari user yang sedang login.</li>
            <li>Menambahkan fungsi cookie bernama <code>last_login</code> ke dalam potongan kode <code>if form.is_valid()</code> yang ada di dalam fungsi <code>login_user</code>.</li>
            <li>Menambahkan fungsi <code>response.delete_cookie('last_login')</code> ke dalam fungsi <code>logout_user</code>.</li>
        </ol>
</ul><br>
</body>
</html>