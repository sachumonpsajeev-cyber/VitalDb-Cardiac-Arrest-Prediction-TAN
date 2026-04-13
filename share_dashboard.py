# ╔══════════════════════════════════════════════════════════════════════╗
# ║  Cardiac Dashboard — Public Share Tool (Cloudflare Tunnel)           ║
# ║  Works on university networks — no account needed                    ║
# ║                                                                       ║
# ║  HOW TO USE:                                                          ║
# ║  1. Install cloudflared from:                                         ║
# ║     https://developers.cloudflare.com/cloudflare-one/connections/    ║
# ║     connect-networks/downloads/  (Windows 64-bit .msi)               ║
# ║  2. python share_dashboard.py                                         ║
# ║  3. Copy the https://...trycloudflare.com link and share it          ║
# ╚══════════════════════════════════════════════════════════════════════╝

import subprocess
import sys
import time
import os
import re
import webbrowser

STREAMLIT_PORT = 8501
SCRIPT_DIR     = os.path.dirname(os.path.abspath(__file__))
LAUNCHER_FILE  = os.path.join(SCRIPT_DIR, "cardiac_launcher.py")

def start_streamlit():
    print("\n🫀 Starting Cardiac Dashboard...")
    process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", LAUNCHER_FILE,
         "--server.port", str(STREAMLIT_PORT),
         "--server.headless", "true",
         "--server.enableCORS", "false",
         "--server.enableXsrfProtection", "false"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    print("  Waiting for dashboard to start", end="", flush=True)
    for _ in range(15):
        time.sleep(1)
        print(".", end="", flush=True)
        if process.poll() is not None:
            out, err = process.communicate()
            print(f"\n\n❌ Dashboard crashed. Error:\n{err.decode()}")
            sys.exit(1)
    print(" Ready!\n")
    return process

def start_cloudflare_tunnel():
    print("🌐 Creating public link via Cloudflare...")

    possible_paths = [
        "cloudflared",
        r"C:\Program Files\cloudflared\cloudflared.exe",
        r"C:\Program Files (x86)\cloudflared\cloudflared.exe",
        os.path.join(os.environ.get("LOCALAPPDATA",""), "cloudflared", "cloudflared.exe"),
        os.path.join(SCRIPT_DIR, "cloudflared.exe"),
    ]

    cloudflared_cmd = None
    for path in possible_paths:
        try:
            result = subprocess.run([path, "--version"], capture_output=True, timeout=5)
            if result.returncode == 0:
                cloudflared_cmd = path
                break
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue

    if not cloudflared_cmd:
        print("\n❌ cloudflared not found.")
        print("\n── How to install ─────────────────────────────────────")
        print("1. Go to this link in your browser:")
        print("   https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/")
        print("2. Download: Windows 64-bit .msi")
        print("3. Run the installer, then run this script again")
        print("\nOR download cloudflared.exe and place it here:")
        print(f"   {SCRIPT_DIR}")
        print("────────────────────────────────────────────────────────")
        return None, None

    tunnel_process = subprocess.Popen(
        [cloudflared_cmd, "tunnel", "--url", f"http://localhost:{STREAMLIT_PORT}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    public_url = None
    print("  Waiting for tunnel", end="", flush=True)
    for _ in range(40):
        time.sleep(1)
        print(".", end="", flush=True)
        line = tunnel_process.stdout.readline()
        match = re.search(r'https://[a-z0-9\-]+\.trycloudflare\.com', line)
        if match:
            public_url = match.group(0)
            break

    print()
    return tunnel_process, public_url

def print_summary(public_url):
    divider = "─" * 60
    print(divider)
    print("  🫀  CARDIAC ARREST RISK DASHBOARD — LIVE")
    print(divider)
    print()
    print(f"  📍 Local  (your laptop):    http://localhost:{STREAMLIT_PORT}")
    print(f"  🌐 Public (shareable link): {public_url}")
    print()
    print(divider)
    print("  ✅ Send the PUBLIC link to your supervisor/examiners.")
    print("  ✅ They open it in any browser — no install needed.")
    print()
    print("  ⚠️  Keep this window open while sharing.")
    print("  ⚠️  Link stops working when you press Ctrl+C.")
    print(divider)
    print()
    print("  Press Ctrl+C to stop sharing when done.")
    print()

if __name__ == "__main__":
    if not os.path.exists(LAUNCHER_FILE):
        print(f"\n❌ Cannot find cardiac_launcher.py in:\n   {SCRIPT_DIR}")
        sys.exit(1)

    streamlit_process = start_streamlit()
    tunnel_process, public_url = start_cloudflare_tunnel()

    if public_url:
        print_summary(public_url)
        webbrowser.open(f"http://localhost:{STREAMLIT_PORT}")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n  Stopping everything...")
            if tunnel_process:
                tunnel_process.terminate()
            streamlit_process.terminate()
            print("  Done. Link is now inactive.")
    else:
        print(f"\n  ⚠️  Could not get public URL.")
        print(f"  Your dashboard is running locally at:")
        print(f"  http://localhost:{STREAMLIT_PORT}")
        print("\n  Press Ctrl+C to stop.\n")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            if tunnel_process:
                tunnel_process.terminate()
            streamlit_process.terminate()
            print("\n  Stopped.")
