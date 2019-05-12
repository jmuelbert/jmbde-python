# -*- mode: python -*-

block_cipher = None

a = Analysis(['jmbde/__main__.py'],
            pathex=['.'],
            binaries=[],
            datas=[],
            hiddenimports=[],
            hookspath=[],
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)

app = BUNDLE(exe,
         name='jmbde.app',
         icon=None,
         bundle_identifier=None)

exe = EXE(pyz,
        a.scripts,
        exclude_binaries=True,
        name='jmbde',
        debug=False,
        strip=False,
        upx=False,
        console=False)

coll = COLLECT(exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        name='jmbde')