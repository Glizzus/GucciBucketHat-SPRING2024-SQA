$forensics = "https://github.com/paser-group/continuous-secsoft/raw/master/sqa-spring2024/project/MLForensics.zip"

if (-not (Test-Path .\MLForensics)) {
    Invoke-WebRequest -Uri $forensics -OutFile .\MLForensics.zip
    Expand-Archive -Path .\MLForensics.zip -DestinationPath .\
    Remove-Item .\MLForensics.zip
}
