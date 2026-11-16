from pathlib import Path

build = Path("Telegram/BUILD")
text = build.read_text()
old = (
    "    <key>CFBundleDisplayName</key>\n"
    "    <string>Telegram</string>\n"
    "    <key>CFBundleIdentifier</key>\n"
    "    <string>{telegram_bundle_id}</string>\n"
    "    <key>CFBundleName</key>\n"
    "    <string>Telegram</string>"
)
new = old.replace(">Telegram<", ">DoomGram<")
if old not in text:
    raise SystemExit("Telegram display name block was not found")
build.write_text(text.replace(old, new, 1))

icon = Path("Telegram/Telegram-iOS/Telegram.icon/icon.json")
icon_text = icon.read_text()
icon_text = icon_text.replace(
    "display-p3:0.21569,0.68627,0.89020,1.00000",
    "display-p3:0.18000,0.78000,0.42000,1.00000",
)
icon_text = icon_text.replace(
    "srgb:0.11373,0.57647,0.82353,1.00000",
    "srgb:0.05000,0.55000,0.28000,1.00000",
)
icon_text = icon_text.replace(
    "srgb:0.00000,0.47843,1.00000,1.00000",
    "srgb:0.00000,0.45000,0.22000,1.00000",
)
icon.write_text(icon_text)
print("DoomGram name and green icon applied")
