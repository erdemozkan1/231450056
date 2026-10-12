Markdown
# Homework 3: Mini Security Event API

Bu proje, Python'ın yerleşik kütüphaneleri (`http.server`, `urllib`, `json`, `csv`) kullanılarak geliştirilmiş, HTTP protokolü, REST API mimarisi, JSON veri formatı, durum kodları (status codes), hata yönetimi ve veri filtreleme konularını kapsayan bir istemci-sunucu (client-server) uygulamasıdır.

## 1. Klasör Yapısı

Proje deposu içerisinde `homework3` klasörünün yapısı şu şekildedir:

```text
yazilim-laboratuvari/
│
├── homework1/
├── homework2/
└── homework3/
    ├── server.py
    ├── client.py
    ├── high_events.csv
    └── README.md
```
## 2. Server Uygulaması (server.py)  
Sunucu tarafı, harici bir çatı (Flask vb.) kullanılmadan tamamen Python'ın yerleşik http.server modülüyle geliştirilmiştir. Hafızasında farklı önem seviyelerine (low, medium, high) sahip en az 8 adet güvenlik olayı barındırır.   
Desteklenen Endpoint'ler:   
GET /api/events: Tüm güvenlik olaylarını JSON formatında döndürür.   
GET /api/events/high: Yalnızca severity değeri high olan olayları filtreleyerek döndürür.  
GET /api/summary: Toplam olay sayısını ve önem seviyelerine göre dağılım özetini döndürür.  
Tanımsız Endpoint'ler: Geçersiz bir adres çağrıldığında 404 durum kodu ve JSON formatında hata mesajı döner ({"error": "Endpoint not found"}).   
## 3. Client Uygulaması (client.py)
İstemci uygulaması, sunucu üzerindeki /api/events endpointine bir HTTP GET isteği gönderir. Gelen JSON verisini işleyerek aşağıdaki işlemleri gerçekleştirir:   
Toplam olay sayısını hesaplar.  
low, medium ve high önem seviyelerinin dağılımını ekrana yazdırır.   
Yalnızca high seviyesindeki olayları filtreler ve ekranda listeler.   
Filtrelenen yüksek önem dereceli olayları otomatik olarak high_events.csv dosyasına kaydeder.   
Hata Yönetimi ve Timeout: Sunucu kapalı olduğunda programın çökmesini engeller (URLError), yanlış endpoint çağrıldığında HTTP hatalarını yakalar (HTTPError) ve timeout=3 kuralı ile ağ donmalarına karşı koruma sağlar.    
## 4. Nasıl Çalıştırılır?    
Projeyi çalıştırmak için iki ayrı terminal penceresi açılması gerekmektedir.    
### Adım 1: Sunucuyu Başlatın   
İlk terminalde homework3 dizinine giderek sunucuyu çalıştırın:    
```Bash
python server.py
```
(Sunucu http://127.0.0.1:8081 adresinde dinlemeye başlayacaktır. Bu terminal açık bırakılmalıdır.)   
### Adım 2: İstemciyi Çalıştırın
İkinci bir terminal açarak istemci kodunu çalıştırın:
```Bash
python client.py
```
## 5. Örnek Çıktı
client.py başarıyla çalıştırıldığında konsolda aşağıdaki gibi bir çıktı elde edilir:
```Plaintext
API sunucusuna bağlanılıyor...
API bağlantısı başarılı.
Toplam olay: 8

Severity dağılımı:
LOW    : 3
MEDIUM : 2
HIGH   : 3

HIGH SEVERITY EVENTS
ID: 2
Type: bruteforce

ID: 5
Type: malware

ID: 8
Type: suspicious-login


Yüksek önem dereceli olaylar 'high_events.csv' dosyasına başarıyla kaydedildi.
```
## 6. Test Edilen Hata Senaryoları
Test 1 – Normal Çalışma: Server açıkken client.py çalıştırılır ve verilerin başarılı bir şekilde çekilerek CSV dosyasına yazıldığı doğrulanır.   
Test 2 – Yanlış Endpoint: Geçersiz bir URL (/api/abc) çağrıldığında sunucunun 404 durum kodu ve JSON hata mesajı döndürdüğü doğrulanır.   
Test 3 – Server Kapalı: Server kapalı durumdayken client çalıştırıldığında program çökmez; kullanıcıya anlamlı bir "API sunucusuna bağlanılamadı." bağlantı hatası gösterilir.   