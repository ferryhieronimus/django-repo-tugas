# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

[Lihat website di sini](https://tugaspbpferry.herokuapp.com/todolist)

##  Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?

CSRF adalah Cross Site Request Forgeries. CSRF adalah serangan terhadap potensi keamanan dari sebuah website yakni ketika terdapat suatu website yang memuat link, tombol, ataupun sesuatu yang bisa mengeksekusi JavaScript yang melakukan suatu hal yang tidak diinginkan user atau memiliki intensi yang lain, misalnya mengganti email atau password. `{% csrf_token %}` digunakan untuk melindungi (proteksi) website yang dibuat Django terhadap potensi serangan CSRF.

Jika suatu form POST tidak memiliki token ini, maka akan muncul error:
```shell
Forbidden (403)
CSRF verification failed. Request aborted.
...
Reason given for failure:

    CSRF token missing.
```

[Referensi 1](https://docs.djangoproject.com/en/4.1/ref/csrf/), [Referensi 2](https://portswigger.net/web-security/csrf)

## Apakah kita dapat membuat elemen ```<form>``` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

Bisa. Caranya adalah dengan menggunakan tag form `<form>...</form> ` HTML, menambahkan `{% csrf_token %}` jika method yang digunakan adalah POST, mengisi form dengan elemen `<input>` yang menspesifikasikan URL ke mana input akan direturn dan metode HTTP yang digunakan, serta elemen `<input>` atau `<button>` yang digunakan untuk mensubmit form tersebut. Contoh form yang dibuat secara manual ada pada login.html.


## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Ketika user mensubmit form, maka user akan mengirimkan request ke server tergantung method apa yang digunakan. Request tersebut akan dihandle oleh view yang bersesuaian. Untuk menyimpan data ke database, pertama kita ambil dulu datanya yang user request (misal `request.POST.get("something")`). Kemudian, untuk menyimpannya ke database, buat objectnya. Misal untuk object kali ini
```shell
ToDoList.objects.create(
            user=request.user,
            title=title,
            description=description,
            date=datetime.datetime.today(),
        )
``` 
Untuk mengambil objectnya,
```shell
todolist_objects = ToDoList.objects.filter(user=request.user)
```
bisa juga menggunakan all() atau yang lainnya.

## Pengimplementasian Tugas 4

1. Jalankan program berikut untuk membuat sebuah django-app bernama todolist
   ```shell
    python manage.py startapp todolist
   ```
2. Untuk menambahkan path mywatchlist sehingga app dapat diakses pada localhost, tambahkan path di urls.py di project_django
   ```shell
    urlpatterns = [
        ...
        path("mywatchlist/", include("mywatchlist.urls"))
        ...
    ]
   ```
   Tambahkan app pada INSTALLED_APPS di settings.py
   ```shell
   INSTALLED_APPS = [
    ...
    'todolist',
   ] 
   ```
3. Buatlah sebuah model ToDoList pada models.py dengan artibutnya sebagai berikut
   
   ```shell
    class ToDoList(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.DateTimeField()
        title = models.CharField(max_length=255)
        description = models.TextField()
        is_finished = models.BooleanField(default=False)
   ```
4. Tambahkan potongan ke berikut ke templates/register.html
   
   ```shell
    {% extends 'base.html' %}

    {% block meta %}
    <title>Registrasi Akun</title>
    {% endblock meta %}

    {% block content %}  

    <div class = "login">
        
        <h1>Formulir Registrasi</h1>  

            <form method="POST" >  
                {% csrf_token %}  
                <table>  
                    {{ form.as_table }}  
                    <tr>  
                        <td><input type="submit" name="submit" value="Daftar"/></td>  
                    </tr>
                    <tr>
                        <td>
                            <button>
                                <a href="{% url 'todolist:login' %}">Batal</a>
                            </button>
                        </td>
                    </tr>  
                </table>  
            </form>

        {% if messages %}  
            <ul>   
                {% for message in messages %}  
                    <li>{{ message }}</li>  
                    {% endfor %}  
            </ul>   
        {% endif %}

    </div>  

    {% endblock content %}
   ```
   Tambahkan potongan ke berikut ke templates/login.html
   
   ```shell
    {% extends 'base.html' %}
    {% load static %}

    {% block meta %}
    <title>Login</title>
    <link rel="stylesheet" href="{% static 'css/styles_login.css' %}">
    {% endblock meta %}

    {% block content %}

    <div class = "login" id="boxlogin">

        <h1>Welcome!</h1>
        <form method="POST" action="">
            {% csrf_token %}
            <table>
                <tr>
                    <td>
                        <input type="text" name="username" placeholder="Username" class="form-control">
                    </td>
                </tr>
                <tr>
                    <td>
                        <input type="password" name="password" placeholder="Password" class="form-control">
                    </td>
                </tr>

                <tr>
                    <td>
                        <input class="btn login_btn" type="submit" value="Login">
                    </td>
                </tr>
            </table>
        </form>

        {% if messages %}
                {% for message in messages %}
                    <p id="eror">{{ message }}</p>
                {% endfor %}
        {% endif %}     
            
        <p>Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a></p> 

    </div>

    {% endblock content %}
   ```

   Tambahkan potongan kode berikut pada views.py. Jangan lupa untuk meng-import package yang dibutuhkan
   ```shell
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Akun telah berhasil dibuat!')
                return redirect('todolist:login')
        
        context = {'form':form}
        return render(request, 'register.html', context)

    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
                response.set_cookie(
                    'last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.info(request, 'Username atau Password salah!')
        context = {}
        return render(request, 'login.html', context)

    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('todolist:login'))
        response.delete_cookie('last_login')
        return response
   ```

   Tambahkan potongan kode berikut pada todolist/urls.py
   ```shell
    urlpatterns = [
        path("", show_todolist, name="show_todolist"),
        path("login/", login_user, name="login"),
        path("register/", register, name="register"),
        path("logout/", logout_user, name="logout"),    
    ]
   ```
5. Tambahkan potongan kode berikut pada templates/todolist.html
    ```shell
    {% extends 'base.html' %}

    {% block meta %}
    <title>Todolist {{ username }}</title>
    {% endblock meta %}

    {% block content %}
    <h1>Welcome back, {{ username }}!</h1>

    <table>
    <tr>
        <th>Task</th>
        <th>Description</th>
        <th>Created At</th>
    </tr>
    {% for todo in todolist %}
        <tr>
        <td>{{todo.title}}</td>
        <td>{{todo.description}}</td>
        <td>{{todo.date|date:'Y-m-d H:i:s'}}</td>
        </tr>
    {% endfor %}  
    </table>

    <button>
    <a href="{% url 'todolist:logout' %}">Logout</a>
    </button>

    <button>
    <a href="{% url 'todolist:create_todo' %}">Tambah Task Baru</a>
    </button>
    {% endblock content %}
    ```
6. Tambahkan potongan kode berikut pada templates/create_todo.html
    ```shell
    {% extends "base.html" %}

    {% block meta %}
    <title>Create Todo</title>
    {% endblock meta %}

    {% block content %}

    <h3>{{ title }}</h3>
    <form method="post">
        {% csrf_token %}

        <label for="title">Title</label>
        <input type="text" name="title" placeholder="Judul task">

        <label for="description">Description</label>
        <input type="text" name="description" placeholder="Deskripsi task">

        <button type="submit">Create Task</button>
    </form>

    {% endblock %}
    ```
7. Tambahkan potongan kode berikut pada todolist/urls.py
   ```shell
    urlpatterns = [
        path("", show_todolist, name="show_todolist"),
        path("login/", login_user, name="login"),
        path("register/", register, name="register"),
        path("logout/", logout_user, name="logout"), 
        path("create-task/", create_todo, name="create_todo"),
    ]
   ```
8. Untuk men-deploy app ke Heroku, lakukan langkah berikut.
    1. Buatlah sebuah aplikasi di Heroku, kemudian _connect_ app tersebut dengan repo GitHub aplikasi 
    2. Di repo GitHub, pergi ke Settings > Secrets > Actions, kemudian tambahkan dua secrets
      * HEROKU_API_KEY dengan valuenya diisi dengan API key
      * HEROKU_APP_NAME dengan valuenya diisi dengan nama app Heroku
    3. Jalankan kembali actions yang gagal pada tab Actions
    

    Jangan lupa untuk mem-push program Anda terlebih ke GitHub. Perhatikan jika Anda menggunakan repo yang sama untuk tugas 2, (dengan asumsi Anda berhasil men-deploy tugas 2) app Anda seharusnya sudah ter-deploy.