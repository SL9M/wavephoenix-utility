#!/bin/bash
set -e

cd ..

if [ ! -f ./appimagetool.AppImage ]; then
  echo "Downloading appimagetool..."
  curl -LO https://github.com/AppImage/AppImageKit/releases/latest/download/appimagetool-x86_64.AppImage
  mv appimagetool-x86_64.AppImage appimagetool.AppImage
  chmod +x appimagetool.AppImage
fi

pyinstaller linux.spec

APPDIR=AppDir
mkdir -p "$APPDIR/usr/bin"

cat > "$APPDIR/wavephoenix-utility.desktop" <<EOF
[Desktop Entry]
Name=WavePhoenix Utility
Exec=wavephoenix-utility
Icon=icon
Type=Application
Categories=Utility;
EOF

cp dist/wavephoenix-utility "$APPDIR/usr/bin/"
cp resources/icon.png "$APPDIR/icon.png"

cat > "$APPDIR/AppRun" <<EOF
#!/bin/bash
exec "\$(dirname "\$0")/usr/bin/wavephoenix-utility" "\$@"
EOF
chmod +x "$APPDIR/AppRun"

./appimagetool.AppImage "$APPDIR" wavephoenix-utility.AppImage