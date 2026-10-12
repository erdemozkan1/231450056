# Homework 3 - Mini Security Event API

## Ödevin Amacı
Bu ödevin amacı; Python'da yerleşik `http.server` ve `urllib` kütüphanelerini kullanarak yerel bir REST API sunucusu (server) ve bu sunucuyla HTTP üzerinden haberleşen bir istemci (client) geliştirmektir. Bu projede HTTP metotları, REST mimarisi, JSON veri formatı, HTTP durum kodları (status codes) ve hata yönetimi (exception handling) gibi web teknolojileri uygulamalı olarak kullanılmıştır.

## Kullanılan Endpoint'ler
Sunucu (Server) uygulaması aşağıdaki HTTP GET endpoint'lerini desteklemektedir:

* **`/api/events`**: Tüm güvenlik olaylarını JSON formatında döndürür.
* **`/api/events/high`**: Yalnızca `severity` (önem) değeri "high" olan güvenlik olaylarını döndürür.
* **`/api/summary`**: Güvenlik olaylarının (low, medium, high) sayıca dağılımını içeren özet bilgiyi döndürür.

## Kurulum ve Çalıştırma
Sistemin doğru çalışabilmesi için Server ve Client uygulamalarının eşzamanlı olarak çalışması gerekmektedir. İki farklı terminal penceresi kullanınız.

**1. Sunucuyu (Server) Başlatmak:**
Birinci terminali açın, `homework3` klasörüne gidin ve sunucuyu başlatın:
```bash
python server.py
```
(Sunucu terminalini açık bırakın.)
2. İstemciyi (Client) Başlatmak:
İkinci bir terminal açın, homework3 klasörüne gidin ve istemciyi çalıştırın:
```Bash
python client.py
```
Örnek Çıktı
Client başarıyla çalıştığında terminalde aşağıdaki gibi bir çıktı verir ve yüksek önem dereceli olayları high_events.csv dosyasına kaydeder:
Plaintext   
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
Hata Yönetimi ve Test Edilen Senaryolar   
Programın kararlı çalışması için aşağıdaki senaryolar try/except blokları ile test edilmiş ve yönetilmiştir:   
Bağlantı Hatası (Sunucu Kapalı): Sunucu çalıştırılmadan Client çalıştırıldığında programın çökmesi engellenmiş, kullanıcıya API sunucusuna bağlanılamadı. şeklinde bir uyarı verilmesi sağlanmıştır. Ayrıca Client tarafında olası gecikmeler için timeout yapılandırılmıştır.    
Yanlış Endpoint (HTTP 404): İstemci tarafından geçersiz bir adrese (örn. /api/abc) istek gönderildiğinde, sunucu 404 durum kodu ve {"error": "Endpoint not found"} JSON mesajı döndürmektedir. Client bu durumu yakalayarak HTTP hatası: 404 çıktısı üretir.    