import requests
from datetime import datetime, timezone

# List of URLs to keep alive
URLS = [
    "https://anti-india-detection.onrender.com",
    "https://mca-econsult-prototype.onrender.com",
    "https://testapp-wd1k.onrender.com"
    "https://parag.qzz.io"
]

def ping(url, timeout=10):
    """Send a GET request and return status info."""
    try:
        r = requests.get(url, timeout=timeout)
        return True, r.status_code, r.elapsed.total_seconds()
    except Exception as e:
        return False, str(e), None

def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"🕒 Ping run started at {now}\n")

    success_count = 0
    for url in URLS:
        print(f"🌐 Checking: {url}")
        ok, info, elapsed = ping(url)

        if ok:
            print(f"✅ UP | Status: {info} | Time: {elapsed:.2f}s\n")
            success_count += 1
        else:
            print(f"❌ DOWN | Error: {info}\n")

    print("🔁 Summary:")
    print(f"   {success_count}/{len(URLS)} sites responded successfully.\n")

    end_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"🏁 Ping run finished at {end_time}")

if __name__ == "__main__":
    main()
