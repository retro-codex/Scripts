$forest = Get-ADForest

$forest.Domains | ForEach-Object {
    Get-ADTrust -Filter * -Server $_ | Select-Object `
        @{Name="QueriedDomain";Expression={$_}},
        Name,
        Source,
        Target,
        Direction,
        TrustType
}
