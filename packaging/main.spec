# main.spec
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'sympy.core',
        'sympy.functions',
        'sympy.simplify',
        'sympy.solvers',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'pandas',
        'scipy',
        'numpy',
        'sympy.tests',
        'sympy.categories',
        'sympy.diffgeom',
        'sympy.crypto',
        'sympy.stats',
        'sympy.sandbox',
        'PyQt6',
        'PyQt5'
    ],
    noarchive=False,
    optimize=2  # 字节码优化
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # 启用 UPX
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='main.ico'  # 可执行文件的图标
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,  # 对二进制文件也启用 UPX 压缩
    upx_exclude=[],
    name='main'  # 输出文件夹名称
)