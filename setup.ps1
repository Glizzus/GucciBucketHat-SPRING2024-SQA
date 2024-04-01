$forensics = "https://github.com/paser-group/continuous-secsoft/raw/master/sqa-spring2024/project/MLForensics.zip"

if (-not (Test-Path .\MLForensics-farzana)) {
    Invoke-WebRequest -Uri $forensics -OutFile .\MLForensics.zip
    Expand-Archive -Path .\MLForensics.zip -DestinationPath .\
    Remove-Item .\MLForensics.zip
}

python -m venv .\.venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
