from speedtest import Speedtest



wifi = Speedtest()

print('Getting Download Speed....')
download_ = wifi.download()
print(f"Download: {download_ / 1024 / 1024:.2f} mps")

print('Getting Upload Speed....')
upload_ = wifi.upload()
print(f"Upload: {upload_ / 1024 / 1024:.2f} mps")
