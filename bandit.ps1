if (-not $env:VIRTUAL_ENV) {
    ./.venv/Scripts/Activate.ps1
}

Copy-Item -Path .\pre-commit -Destination .\.git\hooks\pre-commit -Force