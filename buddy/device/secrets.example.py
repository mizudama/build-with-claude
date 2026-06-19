"""Template for secrets.py — copy to secrets.py and fill in your values.

secrets.py is gitignored. Each developer can also add a deny rule
in .claude/settings.local.json so Claude can't read/edit/write it.
Put real credentials in secrets.py, never here.

Used by wifi_event.py at boot. If secrets.py is missing on the device,
wifi_event.py falls back to the public event WiFi.
"""

WIFI_SSID = "your-ssid"
WIFI_PASSWORD = "your-password"
