
@echo off
REM Remove the existing allure-latest-results directory if it exists
rmdir /s /q ".\allure-latest-results"

REM Create a new allure-latest-results directory
mkdir ".\allure-latest-results"

REM Start a local environment
setlocal

REM Save the current directory path
set "currentDir=%CD%"

REM Define directory paths
set "latestResultsDir=%currentDir%\allure-latest-results"
set "latestReportsDir=%currentDir%\allure-latest-reports"

REM Run pytest with allure results output directory
py.test --alluredir="%latestResultsDir%" .\src\tests\smoke\

REM Serve the allure report
allure serve --host localhost "%latestResultsDir%"

REM End the local environment
endlocal
