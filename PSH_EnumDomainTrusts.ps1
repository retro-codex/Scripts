Get-ADTrust -Filter * | ForEach-Object {
    [PSCustomObject]@{
        Name              = $_.Name
        SourceDomain      = $_.Source
        TargetDomain      = $_.Target
        Direction         = $_.Direction
        TrustType         = $_.TrustType
        IsTransitive      = $_.IsTransitive
        SIDFiltering      = $_.SIDFilteringForestAware
        SelectiveAuth     = $_.SelectiveAuthentication
    }
}
