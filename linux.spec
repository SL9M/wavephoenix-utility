# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas = [
        ('resources/*', 'resources'),
        ('src/*', 'src'),
        ('openocd/*', 'openocd')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries + a.datas,
    exclude_binaries=False,
    name='wavephoenix-utility',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    icon='resources/icon.ico',
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)