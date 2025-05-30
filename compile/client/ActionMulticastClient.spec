# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['..\\..\\src\\client\\ActionMulticastClient.py'],
    pathex=['../../.venv/Lib/site-packages', '../../'],
    binaries=[],
    datas=[('../../resources/config_client.yml', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ActionMulticast-client-win32',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=True,
)