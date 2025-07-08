# cy_py_test.spec
# Replace "your_script.py" with the actual entry point of your package
block_cipher = None

import os
script_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'src', 'my_cy', '__main__.py'))

a = Analysis(
    [script_path],
    pathex=['.'],
    binaries=[],
    datas=[],
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
    name='cy_py_test',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='cy_py_test'
)

bundle = BUNDLE(
    exe,
    name='cy_py_test.app',
    ),
)