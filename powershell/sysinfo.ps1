function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}
$User = $env:Username
$IP = getIP
$ver = $PSVersionTable.PSVersion.Major
$DATE = getDate
$HOSTname = $env:COMPUTERNAME

$SMTPServer = "smtp.gmail.com"
$SenderEmail = "seanmcderment@gmail.com"
$RecipientEmail = "seanmcderment@gmail.com"

$BODY = "This machine's IP is $IP. User is $User. Hostname is $HOSTname. PowerShell $ver. Today's Date is $DATE."

Send-MailMessage -To "seanmcderment@gmail.com" -From "seanmcderment@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential) 
