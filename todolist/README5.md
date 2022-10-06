# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

[Lihat website di sini](https://tugaspbpferry.herokuapp.com/todolist)

##  Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

<b>Inline CSS</b> adalah styling CSS yang digunakan di dalam tags HTML langsung. Setiap elemen pada HTML memiliki attribute style, misalnya `<div style="">`

Kelebihan Inline CSS :
- Tidak perlu membuat file CSS terpisah
- Cepat jika ingin mengubah satu elemen

Kekurangan Inline CSS :
- Tidak efisien untuk mengubah banyak elemen atau untuk styling satu halaman
- Proses debugging akan sangat susah karena harus mencari styling internal

<b>Internal CSS</b>  adalah styling CSS yang digunakan di dalam tags `<style>` yang ada di bagian `<head>` HTML. Di dalam tags tersebut, kita bisa memasukkan syling kita, misalnya

```shell
<style>
div {
    margin: 0 auto;
}
<style>
```

Kelebihan Internal CSS :
- Tidak perlu membuat file CSS terpisah
- Bisa menggunakan class dan ID
- Cepat jika ingin mengubah satu halaman

Kekurangan Internal CSS :
- File HTML akan jadi banyak line
- Styling tidak bisa digunakan pada page lain (melanggar DRY)

<b>External CSS</b>  adalah styling CSS yang dituliskan pada file yang terpisah pada file .css. File tersebut ditambahkan ke page HTML dengan memasukkan `<link rel="stylesheet" href="namafile.css">` yang ada di bagian `<head>` HTML.

Kelebihan External CSS :
- Mengganti tampilan cepat sekali, hanya perlu mengubah hrefnya saja
- Kode HTML lebih sedikit line dan lebih rapih

Kekurangan External CSS :
- Lambat jika ingin mengubah satu atau beberapa elemen
- File css bisa saja gagal diload jika internet lambat, menyebabkan cssnya tidak digunakan

## Jelaskan tag HTML5 yang kamu ketahui.

Banyak sekali tags HTML5 yang ada. Hampir mustahil untuk menghafal semua sekaligus. Berikut tags HTML yang paling sering saya gunakan:

- `<p>` tags untuk paragrah (text)
- `<div>` tags untuk container
- `<pre>` tags untuk menampilkan text preformatted
- `<a>` tags untuk link
- `<h1>` tags untuk heading 1

Tags HTML ada yang block-level ada yang inline-level. Block level akan menyebabkan tags lain berada dibawahnya, sedangkan inline-level akan menyebabkan tags lain berada disampingnya.

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

CSS selector digunakan untuk menselect bagian HTML yang ingin ditarget. Secara basic, CSS selector ada yang universal, type, class, id, attribute. CSS selector juga bisa lebih advance lagi, misalnya menggunakan descendant combinator, child combinator, dan sibling combinator. Selain itu, terdapat juga pseudo selector, yaitu pseudo-classes dan pseudo-element.

## Pengimplementasian Tugas 5

Saya menggunakan Bootstrap dan juga vanilla css dalam menstyling website ini. Untuk dapat menggunakan Bootstrap, tambahkan kode berikut pada head di base.html
```shell
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
```
kemudian tambahkan kode berikut di body di base.html
```shell
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
```
Untuk menggunakan Bootstrap, refer ke documentation Bootstrap. Umumnya, kita menambahkan class pada tags di HTML. Responsiveness website menggunakan Bootstrap dan juga flexbox dan grid.

Untuk menambahkan animasi hover pada card, tambahkan kode berikut:
```shell
<style>
  #card:hover{
    transform: scale(1.03);
    transition-timing-function: ease;
    transition: 0.2s;
  }
</style>
```