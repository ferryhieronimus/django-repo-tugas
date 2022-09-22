# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

[Lihat website di sini](https://tugaspbpferry.herokuapp.com/mywatchlist)


## Perbedaan JSON, XML, dan HTML

JSON (JavaScript Object Notation) adalah sebuah format data yang digunakan untuk pertukaran dan penyimpanan data.
Data JSON ditulis secara pasangan key/value dengan key ditulis dalam double quotes, diikuti dengan colon, lalu oleh value.
JSON biasa digunakan ketika data dikirim dari server untuk ditampilkan pada web page.

```shell
    ...
    {
      "model": "mywatchlist.mywatchlist",
      "pk": 4,
      "fields": {
        "watched": true,
        "title": "Primer",
        "rating": 3,
        "release_date": "2004-10-08",
        "review": "Nonton kedua kalinya jadi lumayan seru"
      }
    }
    ...
```

XML (eXtensible Markup Language) juga adalah sebuah format data yang digunakan untuk pertukaran dan penyimpanan data. XML didesain agar self-descriptive, karena bentuk sintaksnya yang mirip dengan HTML. Namun, XML tidak memiliki predefined tags, programmer harus mendefinisikan tagsnya sendiri.

```shell
<object model="mywatchlist.mywatchlist" pk="4">
    <field name="watched" type="BooleanField">True</field>
    <field name="title" type="CharField">Primer</field>
    <field name="rating" type="FloatField">3.0</field>
    <field name="release_date" type="DateField">2004-10-08</field>
    <field name="review" type="TextField">Nonton kedua kalinya jadi lumayan seru</field>
</object>
```
HTML (HyperText Markup Language) adalah bahasa markup standar yang digunakan untuk membuat halaman web. HTML digunakan sebagai struktur dari halaman web. 
```shell
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <p>Some Text</p>
    </body>
</html>
```
Seperti yang bisa kita lihat, HTML merupakan bahasa untuk membangun halaman web, sedangkan JSON dan XML digunakan untuk pertukaran dan penyimpanan data dari server ke client. JSON umumnya lebih populer daripada XML karena JSON lebih singkat sehingga lebih mudah untuk dibaca dan ditulis.

[Referensi 1](https://www.w3schools.com/whatis/whatis_json.asp), [Referensi 2](https://www.w3schools.com/django/django_intro.php), [Referensi 3](https://www.w3schools.com/html/html_intro.asp), [Referensi 4](https://www.w3schools.com/js/js_json_xml.asp)

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform

Sebuah data biasanya disimpan di server. Untuk mengirimkan data ke client, harus ada data delivery yang dikirim dari server ke client. Selain itu, terkadang data tersebut bisa saja berubah-ubah sepanjang jalan. Dengan menyimpan data di dalam sebuah server, data tersebut bisa diubah dengan mudah, kemudian data tersebut bisa di-deliver ke client.


## Pengimplementasian Tugas 3

1. Jalankan program berikut untuk membuat sebuah django-app bernama mywatchlist
   ```shell
    python manage.py startapp mywatchlist
   ```
2. Untuk menambahkan path mywatchlist sehingga app dapat diakses pada localhost, tambahkan path di urls.py di project_django
   ```shell
    urlpatterns = [
        ...
        path("mywatchlist/", include("mywatchlist.urls"))
        ...
    ]
   ```
3. Buatlah sebuah model MyWatchList pada models.py dengan artibutnya sebagai berikut
   
   ```shell
    class MyWatchList(models.Model):
        watched = models.BooleanField()
        title = models.CharField(max_length=255)
        rating = models.FloatField()
        release_date = models.DateField()
        review = models.TextField()
   ```
4. Tambahkan initial_mywatchlist_data.json pada folder fixtures, lalu tambahkan data-datanya
   
   ```shell
    ...
    {
      "model": "mywatchlist.mywatchlist",
      "pk": 4,
      "fields": {
        "watched": true,
        "title": "Primer",
        "rating": 3,
        "release_date": "2004-10-08",
        "review": "Nonton kedua kalinya jadi lumayan seru"
      }
    }
    ...
   ```
5. Untuk menyajikan data yang telah dibuat sebelumnya dalam format HTML, JSON, dan XML:
    - Untuk HTML, tambahkan potongan berikut pada views.py
    ```shell
    context = {
        'list_film': MyWatchList.objects.all(),
        'name': 'Ferry',
        'student_id': '2106701936'
    }

    def show_mywatchlist(request):
        return render(request, "mywatchlist.html", context)
    ```

    -Untuk XML, tambahkan function berikut pada views.py
    ```shell
    def show_xml(request):
        data = MyWatchList.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```

    -Untuk JSON, tambahkan function berikut pada views.py
    ```shell
    def show_json(request):
        data = MyWatchList.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
6. Untuk membuat routing sehingga data di atas dapat diakses melalui URL, tambahkan berikut pada urls.py di folder mywatchlist
    ```shell
    urlpatterns = [
        path("", show_mywatchlist, name=""),
        path("html/", show_mywatchlist, name="show_mywatchlist"),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
    ]
    ```
7. Untuk men-deploy app ke Heroku, lakukan langkah berikut.
    1. Buatlah sebuah aplikasi di Heroku, kemudian _connect_ app tersebut dengan repo GitHub aplikasi 
    2. Di repo GitHub, pergi ke Settings > Secrets > Actions, kemudian tambahkan dua secrets
      * HEROKU_API_KEY dengan valuenya diisi dengan API key
      * HEROKU_APP_NAME dengan valuenya diisi dengan nama app Heroku
    3. Jalankan kembali actions yang gagal pada tab Actions
    

    Jangan lupa untuk mem-push program Anda terlebih ke GitHub. Perhatikan jika Anda menggunakan repo yang sama untuk tugas 2, (dengan asumsi Anda berhasil men-deploy tugas 2) app Anda seharusnya sudah ter-deploy.
8. Tambahkan potongan kode berikut pada tests.py untuk menguji URL
    ```shell
    class Test(TestCase):
        def test_html(self):
            response = self.client.get('/mywatchlist/html/')
            self.assertEqual(response.status_code, 200)
        def test_xml(self):
            response = self.client.get('/mywatchlist/xml/')
            self.assertEqual(response.status_code, 200)
        def test_json(self):
            response = self.client.get('/mywatchlist/json/')
            self.assertEqual(response.status_code, 200)
    ```

# Postman

## Postman HTML
![diagram1](/images/Postman1.png)
## Postman JSON
![diagram2](/images/Postman2.png)
## Postman XML
![diagram3](/images/Postman3.png)