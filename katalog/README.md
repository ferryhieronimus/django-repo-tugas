# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

[Lihat website di sini](https://tugaspbpferry.herokuapp.com/katalog)


## Model View Template (MVT)

![diagram1](/images/diagram1.png)

Pertama-tama, user ingin mengunjungi suatu website melalui browser (website yang menggunakan Django). Dalam kasus ini, user meminta request ke website. Django menerima request tersebut. URL yang diterima oleh Django akan dicek dan akan memanggil view yang sesuai dengan url. Setelah mendapat view yang sesuai, views.py akan mengecek model yang sesuai dari models.py Setelah mengimport model yang sesuai, view akan memanggil template yang sesuai dari folder templates. User akan menerima respons berupa HTML dari template yang diteruskan ke browser dan akan ditampilkan ke pengguna.

[Referensi 1](https://prasetyadi.name/2021/pengantar-framework-django/), [Referensi 2](https://www.w3schools.com/django/django_intro.php)

## Kenapa menggunakan virtual environment?

Virtual Environment adalah _environment_ (lingkungan) Python sedemikan rupa sehingga _interpreter_, _libraries_, dan _scripts_ yang di-_install_ di lingkungan tersebut terisolasi dari Virtual Environment lain dan _libraries_ lain yang di-_install_ di sistem Python, misalnya di dalam sistem operasi.

Satu hal yang perlu diingat adalah bahwa jika kita tidak menyatakan secara eksplisit, `pip` akan menempatkan _package_ eksternal di direktori _site-packages_ Python. Hal ini dapat menyebabkan permasalahan. Misalkan ada dua proyek, A dan B, dan keduanya memiliki _dependecy_ pada _library_ yang sama, C. Jika pada suatu saat proyek B membutuhkan versi _library_ yang lebih baru dari proyek A, maka Python tidak bisa membedakan proyek mana yang membutuhkan versi _library_ yang mana karena semua _package_ eksternal berada di _site-packages_ Python. Bisa saja _library_ yang lebih baru tersebut tidak _backward compatible_ dengan versi sebelumnya.

Seperti yang sudah dijelaskan, Virtual Environment digunakan untuk menghindari _system pollution_ dan _sidestep dependency conflicts_. Kita tetap apat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, bisa saja muncul masalah seperti di atas jika kita sedang men-_develop_ beberapa aplikasi web berbasis Django sekaligus.

[Referensi 1](https://web.archive.org/web/20210616110104/https://realpython.com/web/20210616110104/https://realpython.com/python-virtual-environments-a-primer/#why-the-need-for-virtual-environments), [Referensi 2](https://realpython.com/python-virtual-environments-a-primer/#why-do-you-need-virtual-environments)

## Pengimplementasian Tugas 2


1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML
   ```shell
    def show_catalog(request):
        data_barang_katalog = CatalogItem.objects.all()
        context = {
            'name': 'Ferry',
            'student_id': '2106701936',
            'list_katalog': data_barang_katalog
        }
        return render(request, "katalog.html", context)
   ```
   Fungsi ini mengambil semua data pada model `CatalogItem` dengan menggunakan method `objects.All()` dan menyimpannya ke `data_barang_katalog`. Fungsi mengembalikan data tersebut beserta context ke dalam sebuah HTML.
2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py

   ```shell
   app_name = "katalog"

   urlpatterns = [
       path("", show_catalog, name="show_catalog"),
   ]       
   ```
   Pada `katalog/urls.py` kita tambahkan path pada `urlpatterns`. Selain itu, pada `project_django/urls.py` juga ditambahkan kode berikut pada `urlpatterns`.
   ```shell
   path("katalog", include("katalog.urls"))
   ```
3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template
   
   Untuk menampilkan data yang telah ikut di-render pada fungsi views dan memunculkannya pada halaman HTML, kita gunakan sintkas template seperti ini:
   ```shell
   {{data}}
   ```
   Untuk memasukkan data yang didapat dari show_catalog ke template, kita lakukan iterasi data.
   ```shell
    <table>
        <tr>
            <th>Item Name</th>
            <th>Item Price</th>
            <th>Item Stock</th>
            <th>Rating</th>
            <th>Description</th>
            <th>Item URL</th>
        </tr>
        {% for catalog in list_katalog %}
            <tr>
                <td>{{catalog.item_name}}</td>
                <td>{{catalog.item_price}}</td>
                <td>{{catalog.item_stock}}</td>
                <td>{{catalog.rating}}</td>
                <td>{{catalog.description}}</td>
                <td>{{catalog.item_url}}</td>
            </tr>
        {% endfor %}
    </table>
   ```
   Untuk me-load data yang terdapat di json, jangan lupa untuk melakukan migrasi.
   ```shell
   python manage.py makemigrations
   python manage.py migrate
   python manage.py loaddata initial_catalog_data.json
   ```
4. Melakukan deployment ke Heroku
   
   Untuk mendeploy aplikasi ke Heroku,
   1. Buatlah sebuah aplikasi di Heroku, kemudian _connect_ app tersebut dengan repo GitHub aplikasi 
   2. Di repo GitHub, pergi ke Settings > Secrets > Actions, kemudian tambahkan dua secrets
      * HEROKU_API_KEY dengan valuenya diisi dengan API key
      * HEROKU_APP_NAME dengan valuenya diisi dengan nama app Heroku
   3. Jalankan kembali actions yang gagal pada tab Actions