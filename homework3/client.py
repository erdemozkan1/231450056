import urllib.request
import urllib.error
import json
import csv

def main():
    url = "http://127.0.0.1:8081/api/events"
    timeout_value = 3

    try:
        print("API sunucusuna bağlanılıyor")
        with urllib.request.urlopen(url,timeout=timeout_value) as response:

            response_data = response.read().decode('utf-8') # sunucudan bayt olarak gelen ham yanıtı decode et
            events = json.loads(response_data) #json verilerini listeye , sözlüüğe çevir
            print("API bağlantısı başarılı")

            #toplam olay sayısı
            total_events = len(events) # toplam olay sayısını bulduk
            print(f"Topalm olay : {total_events}\n")

            #low, medium, high hesaplama
            low_count = sum(1  for e in events if e.get("severity")=="low")
            medium_count = sum(1 for e in events if e.get("severity") =="medium")
            high_count = sum(1 for e in events if e.get("severity")=="high")

            print("Severity Dağılımı")
            print(f"LOW : {low_count}")
            print(f"MEDIUM: {medium_count}")
            print(f"HIGH: {high_count}\n")

            #yalnızca high severity olayları filtreleme
            high_events = [e for e in events if e.get("severity")=="high"]
            print("HIGH SEVERITY EVENTS")
            for event in high_events:
                print(f"ID: {event.get('id')}")
                print(f"type: {event.get('type')}\n")

            csv_file_name = "high_events.csv"
        with open(csv_file_name, mode="w",newline='',encoding='utf-8') as csv_file:
            fielnames = ['id','severity','type']
            writer = csv.DictWriter(csv_file, fieldnames=fielnames)

            writer.writeheader()
            for event in high_events:
                writer.writerow({
                    'id':event.get('id'),
                    'severity' : event.get('severity'),
                    'type': event.get('type')

                })
        print(f"Yüksek önem dereceli olaylar '{csv_file_name} dosyasına başarıyla kayıt edildi")
    except urllib.error.URLError as e:
        #Yanlış endpoint veya sunucu tarafı HTTP hataları yakalama örn: 404
        print(f"HTTP hatası : e.code")

    except urllib.error.URLError as e:
        #sunucuya bağlanamama
        print(f"Apu sunucusuna bağlanılamadı")
    except urllib.error.URLError as e:
        print("Beklenmeyen bir hata oluştu")


if __name__ == '__main__':
    main()











