function RunTshark() {
    & 'C:\Program Files\Wireshark\tshark.exe' `
    -i 3 `
    -n `
    -l `
    -T ek `
    -e _ws.col.Protocol `
    -e eth.dst `
    -e eth.src `
    -e ip.proto `
    -e ip.src `
    -e ip.dst `
    -e tcp.srcport `
    -e tcp.dstport `
    -e udp.srcport `
    -e udp.dstport `
    -f "(tcp or igmp or udp)" `
    
   
}


function PacketProcess($TPacketJson) {

    $TPacket = (ConvertFrom-Json $TPacketJson).layers

    if ($TPacket.ip_src) {
        if ($TPacket.tcp_srcport) {$SrcPort = $TPacket.tcp_srcport[0]} elseif ($TPacket.udp_srcport) {$SrcPort = $TPacket.udp_srcport[0]} else {$SrcPort = $null}
        if ($TPacket.tcp_dstport) {$DstPort = $TPacket.tcp_dstport[0]} elseif ($TPacket.udp_dstport) {$DstPort = $TPacket.udp_dstport[0]} else {$DstPort = $null}

        Switch ($TPacket.ip_proto) {
            1 { $Protocol = "ICMP"; break }
            2 { $Protocol = "IGMP"; break }
            6 { $Protocol = "TCP"; break }
            17 { $Protocol = "UDP"; break }
            default { $Protocol = $TPacket.ip_proto; break }
        }

        $Packet = New-Object -TypeName PSObject -Property @{
            SrcIP   = $TPacket.ip_src[0]
            DstIP   = $TPacket.ip_dst[0]
            Protocol = $Protocol
            SrcPort = $SrcPort
            DstPort = $DstPort
            SrcEth = $TPacket.eth_src[0]
            DstEth = $TPacket.eth_dst[0]
        }

        Write-Output $Packet | Select Protocol, SrcIP, SrcEth, SrcPort, DstIP, DstEth, DstPort
    }
}


RunTshark | % {PacketProcess $_}