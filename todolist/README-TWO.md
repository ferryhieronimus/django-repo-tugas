# Tugas 6: Javascript dan AJAX

[Lihat website di sini](https://tugaspbpferry.herokuapp.com/todolist)

##  Jelaskan perbedaan antara asynchronous programming dengan synchronous programming

Pada synchronous programming, sebuah instruksi akan di-hold terlebih dahulu sebelum task sebelumnya telah selesai, sedangkan pada asynchronous programming, sebuah instruksi dapat berjalan bersamaan dengan task sebelumnya. Asynchronous programming dapat menyelesaikan dan berjalan dari satu tugas ke tugas lainnya dan memberi tahu sistem ketika masing-masing selesai. Synchronous programming, di sisi lain, memeriksa satu tugas pada satu waktu. Asynchronous programming memungkinkan lebih banyak hal untuk dilakukan pada saat yang sama dan biasanya digunakan untuk meningkatkan pengalaman pengguna dengan menyediakan waktu reload yang lebih cepat.

##  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-Driven Programming merupakan paradigma pemrograman di mana alur dari suatu program ditentukan oleh "event" yang sedang terjadi. Event tersebut bisa berupa gerakan pada mouse, input dari keyboard, dan sebagainya. Setelah muncul event tersebut, biasanya akan ada suatu program yang tereksekusi, tergantung dari jenis event dan event handler yang digunakan. Pada tugas ini, misalnya jika ingin mensubmit form dari modal, kita akan menekan tombol "submit". Setelah tombol tersebut ditekan, maka todolist akan ditampilkan.

## Jelaskan penerapan asynchronous programming pada AJAX.

AJAX memungkinkan halaman website untuk diupdate secara asinkronus dengan cara menukar informasi ke server yang terjadi di proses background. Dengan demikian, sebuah website mampu mengupdate tampilannya tanpa perlu me-reload keseluruhan page. 

Biasanya, Javascript yang menerima data atau "event" yang terjadi, kemudian mengirimkannya ke database, dan menerima response tersebut (Biasanya JSON). Javascript juga mampu untuk mengubah tampilan website dengan memanipulasi DOM.

## Pengimplementasian Tugas 6

1.  Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.
   ```shell
    def show_json(request):
        data = ToDoList.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```
2. Buatlah path /todolist/json yang mengarah ke view yang baru dibuat dengan cara menambahkan `path('json/', show_json, name='show_json'),` pada urls.py

3. Lakukan pengambilan task menggunakan AJAX GET dengan cara menambahkan kode berikut pada todolist.html
   
   ```shell
    $(document).ready(function () {
        $.get("{% url 'todolist:show_json' %}", function (data) {
            console.log(data)
            $.each(data, function(index, value) {
            let status = value.fields.is_finished ? `<a class="btn btn-success" href="/todolist/update/${value.pk}">
                            Selesai
                            </a>`: `<a class="btn btn-warning" href="/todolist/update/${value.pk}">
                            Belum selesai
                            </a>`
            $(".card-container").append (
                `
                <div class="col" >
                <div class="card h-100 hoverable" id="card" style="min-width: 200px">
                    <div class="card-body d-flex justify-content-between flex-column">
                    <div class="main-item">
                        <h4 class="card-title">${value.fields.title}</h4>
                        <p class="card-subtitle mb-2 text-muted">${value.fields.description}</p>
                    </div>
                    <div class="row row-cols-1 row-cols-md-1 g-1">
    
                        <div class="col">
                        ${status}
                        </div>
    
                        <div class="col">
    
                        <a class="btn btn-danger" href="/todolist/delete/${value.pk}">Hapus Task</a>
                        </div>
                        
                    </div>
                
    
                    </div>
                    <div class="card-footer">
                    <small class="text-muted">created at: ${value.fields.date}</small>
                    </div>
                </div>
                </div>
                `
            );
            });
        });
   ```
4. Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task dengan cara menambahkan potongan kode untuk modal berikut ke todolist.html
   
   ```shell
    <div class="modal fade" id="modal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Tambah Task</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <form method="POST" onsubmit="return false">
            {% csrf_token %}
            <div class="mb-3">
                <label for="recipient-name" class="col-form-label">Judul Task</label>
                <input type="text" class="form-control" id="judul">
            </div>
            <div class="mb-3">
                <label for="message-text" class="col-form-label">Deskripsi Task</label>
                <textarea class="form-control" id="deskripsi"></textarea>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="submit" class="btn btn-primary" data-bs-dismiss="modal" id="tambahTask">Tambah</button>
            </div>
            </form>
        </div>
        </div>
    </div>
    </div>
   ```
   Dan sebuah button untuk membuka modal tersebut
   
   ```shell
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modal" data-bs-whatever="@mdo">Tambah task baru</button>
   ```
5. Buatlah view baru untuk menambahkan task baru ke dalam database dengan cara menambah view baru bernama add yang mereturn JsonResponse
    ```shell
    @login_required(login_url='/todolist/login/')
    def add(request):
        if request.method == "POST":
            title = request.POST.get("judul")
            description = request.POST.get("deskripsi")
            task = ToDoList.objects.create(
                user=request.user,
                title=title,
                description=description,
                date=datetime.datetime.today(),
            )
        return JsonResponse(
            {
                    "pk": task.id,
                    "fields": {
                        "title": task.title,
                        "description": task.description,
                        "is_finished": task.is_finished,
                        "date": task.date,
                    },
                }
        )
    ```
6. Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat dengan cara menambahkan `path('add/', add, name='add'),` ke urls.py

7. Tambahkan potongan kode berikut pada todolist.html
   ```shell
    $("#tambahTask").click(function(){
            const judul = $("#judul").val();
            const deskripsi = $("#deskripsi").val();
            const data = {judul: judul, deskripsi: deskripsi, csrfmiddlewaretoken: '{{ csrf_token }}'};
            $.ajax({url: "/todolist/add/", data: data, method: "POST"}).done(function (resp) {
            $(".card-container").append (
                `
                <div class="col" >
                <div class="card h-100 hoverable" id="card" style="min-width: 200px">
                    <div class="card-body d-flex justify-content-between flex-column">
                    <div class="main-item">
                        <h4 class="card-t itle">${judul}</h4>
                        <p class="card-subtitle mb-2 text-muted">${deskripsi}</p>
                    </div>
                    <div class="row row-cols-1 row-cols-md-1 g-1">
    
                        <div class="col">
                            <a class="btn btn-warning" href="/todolist/update/${resp.pk}">
                            Belum selesai
                            </a>
                        </div>
    
                        <div class="col">
    
                        <a class="btn btn-danger" href="/todolist/delete/${resp.pk}">Hapus Task</a>
                        </div>
                        
                    </div>
                
    
                    </div>
                    <div class="card-footer">
                    <small class="text-muted">created at: ${resp.fields.date}</small>
                    </div>
                </div>
                </div>
                `
            );
            })
        });
        });
   ```