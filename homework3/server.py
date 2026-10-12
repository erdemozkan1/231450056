from http.server import BaseHTTPRequestHandler, HTTPServer
import json

events = [
    {"id": 1,"severity":"low","type":"config-change"},# güvenlik duvarı yapılandırması
    {"id": 2,"severity":"high","type":"bruteforce"}, # Kullanıcı adına arka arkaya şifresini yanlış girerek deneme-yanılma yoluyla şifresini kırma
    {"id": 3,"severity":"high","type":"malware-detected"}, # Sistemde veya dosyalarda kötü amaçlı yazılım
    {"id": 4,"severity":"high","type":"sql-injection"}, # veritabanına yetkisiz erişim
    {"id": 5,"severity":"high","type":"suspicious-login"}, # normal dışı coğrafyadan ya da normal dışı saatte yapılan oturum açma işlemi
    {"id": 6,"severity":"medium","type":"unauth-acces"}, # yetkisiz birisinin yada IP kısıtlı bir dosyaya ya da sisteme erişmeye çalışması
    {"id": 7,"severity":"medium","type":"port-scan"}, # Dış IP adresinin sunucudaki açık portları ve servisleri listelemek için tarama yapması
    {"id": 8,"severity":"medum","type":"high-cpu-usage"},# sunucu kaynaklarını yüksek seviyede sömürmesi
    {"id": 9,"severity":"medium","type":"rate-limit-exceeded"}, # istek sınırının aşılması
    {"id": 10,"severity":"low","type":"connection-timeout"}, # bağlantı zaman aşımı
    {"id": 11,"severity":"low","type":"service-rest"}, # kritik olmayan bir servisin yeniden başlatılması
]

class SecurityEventServer(BaseHTTPRequestHandler):
    def send_json_response(self,data,status_code):
        response_body = json.dumps(data).encode('utf-8') # sözlük verisini JSON'a çevirdik ardından bytes formatına dönüştürdük,
        self.send_response(status_code) # HTTP protokolüne uygun olarak tarayıcıya yanıt durum kodunu gönderir Örn: 200 OK
        self.send_header('Content-Type','application/json') # karşı tarafa json göndereceğimizi söylüyoruz
        self.send_header('Content-Length',str(len(response_body)))# göndereceğimiz verinin bayt cinsinden uzunluğunu HTTP başlığına ekleriz Böylece alıcı verinin ne kadar süreece geleceğini veya bittiğini bilir
        self.end_headers() #    http başlıklarının bittiğini bundan sonra gövde kısmının geleceğini söyleriz
        self.wfile.write(response_body) # bayt cinsindeki yanıt verisinin istemciye göndeririz

    def do_GET(self): # istemciden get isteği geldiğinde otomatik olarak tetiklenir
        #Endpoint yönlendirmeleri
        if self.path == '/api/events': #istemcisinin hangi adrese istek attığını tutar örn:
            self.send_json_response(events,200)
        elif self.path == '/api/events/high':
            high_events = [e for e in events if e ["severity"] == "high"]
            self.send_json_response(high_events,200)
        elif self.path == "api/summary":
            total = len(events)
            low_count = sum(1 for e in events if e["severity"]=="low")
            medium_count = sum(1 for e in events if e["severity"]=="medium")
            high_count = sum(1 for e in events if e["severity"]=="high")

            summary = {
                "total":total,
                "low": low_count,
                "medium" :medium_count,
                "high": high_count
            }
            self.send_json_response(summary,200)
        else:
            #Tanımlanmamış endpointler için 404 ve JSON hata mesajı
            error_response = {"error":"Endpoint bulunamadı"}
            self.send_json_response(error_response,404)

def run():
    server_address = ("127.0.0.1",8081)
    httpd = HTTPServer(server_address,SecurityEventServer)
    print(f"Sunucu Çalışıyor : http://{server_address[0]}:{server_address[1]}")
    httpd.serve_forever()
if __name__ == '__main__':
    run()


















