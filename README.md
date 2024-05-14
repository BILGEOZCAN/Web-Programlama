README.md

Görüntü İşleme ile Araç Takibi

Projenin amacı, görüntü işleme kullanarak video üzerindeki araçları takip ederek giriş-çıkış sayılarını belirlemektir. Python ve OpenCV kütüphanesi kullanılarak geliştirilmiştir.

Kullanılan Teknolojiler:
Python
OpenCV kütüphanesi

Proje Aşamaları:
Python ve gerekli kütüphanelerin kurulumu.
OpenCV kütüphanesinin araştırılması ve kullanılacak fonksiyonların belirlenmesi.
Takip edilecek araçların bulunduğu video kaynağının belirlenmesi.

Kullanılan Fonksiyonlar:
imshow("Ana Görüntü", image): Videoyu normal şekilde gösterir.
imshow("Gray Görüntü", gray): Gri tonlamalı görüntü elde eder.
imshow("fgmask", fgmask): Hareket eden cisimleri tespit eder.
imshow("Bel_Nok_Giderme", closing): Belirlenen cisimlerin içindeki noktaları giderir.
imshow("Cev_Nok_Giderme", opening): Cisimlerin çevresindeki noktaları temizler.
imshow("Nesneleri kalinlastirma", dilation): Nesneleri kalınlaştırarak yerlerini belirginleştirir.
imshow("retvalbin", retvalbin): Görüntüyü ikili forma dönüştürür.
imshow("Sonuc", image): Sonuç görüntüsünü gösterir.

Algoritma:
Video gri tonlamalı hale getirilir.
Hareket eden cisimler tespit edilir.
Cisimlerin iç ve dış noktaları temizlenir.
Nesneler kalınlaştırılır.
Nesneler ikili forma dönüştürülür.
Koordinatları belirlenen cisimlerin çizgilerden geçip geçmediği kontrol edilerek araç sayısı belirlenir.