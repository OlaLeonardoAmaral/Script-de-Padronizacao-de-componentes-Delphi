@echo off
echo Limpando arquivos temporarios do projeto Delphi...

rem Remove arquivos comuns de build
del /f /q *.dcu
del /f /q *.~*
del /f /q *.dsk
del /f /q *.cfg
del /f /q *.dof
del /f /q *.map
del /f /q *.tds
del /f /q *.local

echo.
echo Arquivos temporarios removidos com sucesso.
pause
