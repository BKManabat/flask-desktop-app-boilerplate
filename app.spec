# myapp.spec

import os
from pathlib import Path

app_dir = os.getcwd()
templates_dir = os.path.join(app_dir, 'templates')
static_dir = os.path.join(app_dir, 'static')

a = Analysis(['app.py'],
             pathex=[app_dir],
             binaries=[],
             datas=[(os.path.join(templates_dir, '**'), 'templates'), (os.path.join(static_dir, '**'), 'static')],
             hiddenimports=['app'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=None,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=None)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='myapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          upx_include=[],
          runtime_tmpdir=None,
          console=False )
