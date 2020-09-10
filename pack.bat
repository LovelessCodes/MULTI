pyinstaller -F -i=multi.ico multi.py
copy dist\multi.exe .\
rename multi.exe MultiTool.exe
rmdir dist /q /s
rmdir build /q /s
rmdir __pycache__ /q /s
del multi.spec