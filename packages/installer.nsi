!define PRODUCT_NAME "CyPyTest"
!define PRODUCT_EXE "cy_py_test.exe"

OutFile "${PRODUCT_NAME}_Installer.exe"
InstallDir "$PROGRAMFILES\${PRODUCT_NAME}"

Page directory
Page instfiles

Section
  SetOutPath "$INSTDIR"
  File "dist\cy_py_test\cy_py_test.exe"
  CreateShortcut "$DESKTOP\${PRODUCT_NAME}.lnk" "$INSTDIR\${PRODUCT_EXE}"
SectionEnd
