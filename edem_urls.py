import csv, requests


with open("2020.csv", newline="") as f:
    """newline="" - пустая строка позволяет корректно считывать строки
    из файла вне зависимости от операционной системы."""
    reader = csv.reader(f)
    for url in reader:
        #print(url)
        try:
            if "http" in url[0]:
                #print(url[0])
                r = requests.get(url[0])
                print(r.url)
        except Exception:
            print("Something wrong\n")