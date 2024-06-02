# glovedatahub.spec

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
version = '/version.txt'

a = Analysis(
    ['GUI/gui_main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('Data-Acquisition/*', 'Data-Acquisition'),
        ('API/*.py', 'API'),
        ('GUI/images/*', 'GUI/images'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='glovedatahub',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon=['GUI\\images\\GDH.ico']
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='glovedatahub',
)