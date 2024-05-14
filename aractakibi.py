import cv2
import numpy as np
import vehicles
import time

# Yukarı ve aşağı yönlü sayaçlar
yukari_sayac = 0
asagi_sayac = 0

# Video yakalama
video = cv2.VideoCapture("cars.mp4")

# Video genişliği ve yüksekliği
genislik = video.get(3)
yukseklik = video.get(4)
frame_alani = yukseklik * genislik
alan_esik_degeri = frame_alani / 400

# Çizgilerin belirlenmesi
yukari_cizgi = int(2 * (yukseklik / 5))
asagi_cizgi = int(3 * (yukseklik / 5))

ust = int(1 * (yukseklik / 5))
alt = int(4 * (yukseklik / 5))

pt5 = [0, ust]
pt6 = [genislik, ust]
pts_L3 = np.array([pt5, pt6], np.int32)
pts_L3 = pts_L3.reshape((-1, 1, 2))
pt7 = [0, alt]
pt8 = [genislik, alt]
pts_L4 = np.array([pt7, pt8], np.int32)
pts_L4 = pts_L4.reshape((-1, 1, 2))

# Kernel oluşturma
kernel_op = np.ones((3, 3), np.uint8)
kernel_op2 = np.ones((5, 5), np.uint8)
kernel_cl = np.ones((11, 11), np.uint8)

# Yazı fontu
font = cv2.FONT_HERSHEY_SIMPLEX
araclar_listesi = []
pid = 1

# Arka plan çıkarıcısı oluşturma
subtractor = cv2.createBackgroundSubtractorMOG2()

ret, frame = video.read()
oran = 1.0

while(video.isOpened()):
    ret, frame = video.read()
    if not ret:
        frame = cv2.VideoCapture("cars.mp4")
        continue
    if ret:
        goruntu = cv2.resize(frame, (0, 0), None, oran, oran)
        cv2.imshow("Ana Görüntü", goruntu)
        gri = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gri Görüntü", gri)
        fg_maske = subtractor.apply(gri)
        cv2.imshow("Hareket Algılama", fg_maske)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        kapanis = cv2.morphologyEx(fg_maske, cv2.MORPH_CLOSE, kernel)
        cv2.imshow("Gürültü Kaldırma", kapanis)
        acilim = cv2.morphologyEx(kapanis, cv2.MORPH_OPEN, kernel)
        cv2.imshow("Kenar Tespiti", acilim)
        genisleme = cv2.dilate(acilim, kernel)
        cv2.imshow("Nesneleri Kalınlaştırma", genisleme)
        ret_degeri_bin, binaryler = cv2.threshold(genisleme, 220, 255, cv2.THRESH_BINARY)
        cv2.imshow("İkili", ret_degeri_bin)

        _, contours, hierarchy = cv2.findContours(binaryler, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            alan = cv2.contourArea(cnt)
            print(alan)
            if alan > alan_esik_degeri:

                m = cv2.moments(cnt)
                cx = int(m['m10'] / m['m00'])
                cy = int(m['m01'] / m['m00'])
                x, y, w, h = cv2.boundingRect(cnt)

                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                yeni = True
                if cy in range(yukari, asagi):
                    for i in araclar_listesi:
                        if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                            yeni = False
                            i.koordinat(cx, cy)

                            if i.yukari_hareket(asagi_cizgi, yukari_cizgi):
                                yukari_sayac += 1
                                print("ID:", i.getId(), time.strftime("%c"))

                            break
                    if yeni:
                        p = vehicles.Vehicle(pid, cx, cy)
                        araclar_listesi.append(p)
                        pid += 1

        # Araç sayısını yazdırma
        str_yukari = 'Araç Sayısı: ' + str(yukari_sayac)

        # Çizgileri çizme
        frame = cv2.polylines(frame, [pts_L3], False, (255, 255, 255), thickness=1)
        frame = cv2.polylines(frame, [pts_L4], False, (255, 255, 255), thickness=1)

        # Yazı rengi ve kalınlığı
        cv2.putText(frame, str_yukari, (10, 40), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, str_yukari, (10, 40), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    else:
        break

video.release()
cv2.destroyAllWindows()
