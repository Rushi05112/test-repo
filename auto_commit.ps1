# Create timestamp
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"

# File name
$filename = "auto_" + $timestamp + ".txt"

# Create file with content
"This is auto commit at $timestamp" | Out-File $filename

#Git add
git add .

# git commit
git commit -m "Auto commit at $timestamp"

# Git Push
git push origin main

Write-Host "Auto commit completed."