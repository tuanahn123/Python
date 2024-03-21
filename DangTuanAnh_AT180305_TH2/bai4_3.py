import nmap
import asyncio

async def async_scan(host, arguments):
    scanner = nmap.PortScannerAsync()
    await scanner.scan(hosts=host, arguments=arguments)
    # handle scan result after await

# Định nghĩa hàm main để chạy quét bất đồng bộ
async def main():
    await asyncio.gather(
        async_scan('scanme.nmap.org', '-p 21'),
        async_scan('scanme.nmap.org', '-p 22'),
        async_scan('scanme.nmap.org', '-p 23'),
        async_scan('scanme.nmap.org', '-p 80'),
    )
    print("Scanning done.")

# Chạy hàm main bằng event loop
asyncio.run(main())
