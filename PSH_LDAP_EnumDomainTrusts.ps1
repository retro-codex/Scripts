$domain = (Get-ADDomain).DistinguishedName

Get-ADObject -SearchBase "CN=System,$domain" `
    -LDAPFilter "(objectClass=trustedDomain)" `
    -Properties * | Select-Object `
        Name,
        trustPartner,
        trustDirection,
        trustType,
        trustAttributes
