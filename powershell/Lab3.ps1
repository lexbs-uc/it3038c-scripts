function getIP{
(get-netipaddress).ipv4address | Select-String "192*"
}
write-host(getIP)
$IP = getIP
$Vers = (Get-Variable PSVersionTable -ValueOnly).PSVersion
$Date = (Get-Date)


$Body = ("This machine's IP is $IP. User is $env:UserName. Hostname is $env:ComputerName. Powershell version is $Vers. Today's date is $Date")

Send-MailMessage -To "leonardf@ucmail.uc.edu" -From "daedlynwolf@gmail.com" -Subject "IT3038 Windows SysInfo" -Body $Body -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)