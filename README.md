cat << 'EOF' > ~/ros2_ws/src/sicaklik_izleyici_py/README.md
# Sıcaklık İzleyici ROS 2 Projesi (`sicaklik_izleyici_py`)

Bu proje, ROS 2 Humble ortamında Python (`rclpy`) kullanılarak geliştirilmiş bir sıcaklık izleme ve uyarı sistemidir. Proje geliştirme ve ortam kurulumu sürecinde **Gemini (Yapay Zeka)** desteğinden faydalanılmıştır.

---

##  Projede Ne Yaptım? (Açıklama & Mantık)

Projenin temel amacı, iki farklı ROS 2 düğümünün (node) bir konu (topic) üzerinden birbiriyle haberleşmesini sağlamaktır.

1. **Sanal Makine ve ROS 2 Kurulumu:** 
   Ubuntu sanal makinesi üzerinde gerekli disk genişletmelerini yapıp ROS 2 Humble ortamını ve bağımlılıklarını kurdum.
2. **Yayıncı Düğüm (`sensor.py`):** 
   `/sicaklik` konusu (topic) üzerinden her 1 saniyede bir `Float32` formatında 20.0 ile 40.0 °C arasında rastgele sıcaklık verisi üreten ve yayınlayan sensör düğümünü yazdım.
3. **Dinleyici / İzleyici Düğüm (`izleyici.py`):** 
   `/sicaklik` konusunu dinleyen bir subscriber düğümü oluşturdum. `declare_parameter` kullanarak dinamik bir eşik değeri (`esik_degeri = 30.0`) belirledim. Okunan sıcaklık 30 °C üzerine çıktığında terminalde `get_logger().warn()` ile sarı renkli uyarı logu bastırdım; 30 °C altında ise normal log olarak gösterdim.
4. **Derleme ve Görselleştirme:** 
   `setup.py` dosyasına `console_scripts` tanımlamalarını ekleyip `colcon build` ile paketi hatasız derledim. İki düğümün haberleştiğini kanıtlamak için `rqt_graph` üzerinden düğüm ağının ekran görüntüsünü alıp (`rqt_graph.png`) depoya ekledim.

---

## 🛠️ Nasıl Çalıştırılır?

1. **Çalışma alanını derleyin ve ortamı yükleyin:**
   ```bash
   cd ~/ros2_ws
   colcon build
   source install/setup.bash
