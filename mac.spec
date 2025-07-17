# -*- mode: python ; coding: utf-8 -*-

import os
project_path = os.path.abspath('.')

a = Analysis(
    ['main.py'],
    pathex=[project_path],
    binaries=[],
    datas=[
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
    [],
    exclude_binaries=True,
    name='wavephoenix-utility',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    icon='resources/icon.icns',
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='wavephoenix-utility',
)

bundle = BUNDLE(
    coll,
    name='wavephoenix-utility.app',
    icon='resources/icon.icns',
    bundle_identifier='com.yourdomain.wavephoenixutility',
)
