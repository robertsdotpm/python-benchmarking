# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
  atoms (1)      . soot (2)      , rice (3)      ; peas (4)      o marbles (5)      0 golf balls (6)      8 tennis balls (7)      # bowling balls (8)

 ■■■■■■■■ tcp con to google                        # (8)   0.1233331203460693359375 bowling balls:                O(1) = excellent
 ■■■■■■■■ tcp echo client                          # (8)   0.1899780750274658203125 bowling balls:                O(1) = excellent
    ■■■■■ dns lookup google.com (cached prob)      o (5)        0.00052382946014404296875 marbles:                O(1) = excellent
     ■■■■ n in list[1000]                          ; (4)        0.00001417677402496337890625 peas:                     O(n) = fair
     ■■■■ send 100 b udp packets                   ; (4)         0.0000139510631561279296875 peas:                O(1) = excellent
     ■■■■ send 1k udp packets                      ; (4)            0.0000218238830566406250 peas:                O(1) = excellent
     ■■■■ send 10k udp packets                     ; (4)          0.000051909923553466796875 peas:                O(1) = excellent
      ■■■ time()                                   , (3)       0.000001173039913177490234375 rice:                O(1) = excellent
      ■■■ create an async queue                    , (3)      0.0000021734731197357177734375 rice:                O(1) = excellent
      ■■■ add to an async queue                    , (3)      0.0000011550176143646240234375 rice:                O(1) = excellent
      ■■■ build async event                        , (3)        0.00000117263507843017578125 rice:                O(1) = excellent
      ■■■ n in list[100]                           , (3)      0.0000020131666660308837890625 rice:                     O(n) = fair
      ■■■ str in list[100]                         , (3)       0.000001232528209686279296875 rice:                     O(n) = fair
      ■■■ ip bytes to ipaddress                    , (3)       0.000002352914333343505859375 rice:                O(1) = excellent
      ■■■ build stream sock                        , (3)         0.0000019943714141845703125 rice:                O(1) = excellent
      ■■■ build dgram sock                         , (3)           0.00000998783111572265625 rice:                O(1) = excellent
      ■■■ bind dgram sock                          , (3)         0.0000079762935638427734375 rice:                O(1) = excellent
       ■■ list append small int                    . (2)      0.0000006749250888824462890625 soot:                O(1) = excellent
       ■■ overhead of a func call                  . (2)      0.0000006090385913848876953125 soot:                O(1) = excellent
       ■■ make a dic with one item                 . (2)       0.000000596550464630126953125 soot:                O(1) = excellent
       ■■ dict key lookup from single item dic     . (2)        0.00000061519336700439453125 soot:                O(1) = excellent
       ■■ make a dic with 4 items                  . (2)      0.0000006949174404144287109375 soot:                O(1) = excellent
       ■■ dict key lookup from 4 item dic          . (2)       0.000000613524913787841796875 soot:                O(1) = excellent
       ■■ get from an async queue                  . (2)       0.000000989290714263916015625 soot:                O(1) = excellent
       ■■ set async event                          . (2)      0.0000007928383350372314453125 soot:                O(1) = excellent
       ■■ if x == n else ..                        . (2)      0.0000006306874752044677734375 soot:                O(1) = excellent
       ■■ n in list[5]                             . (2)      0.0000007090160846710205078125 soot:                     O(n) = fair
       ■■ n in list[10]                            . (2)      0.0000007679574489593505859375 soot:                     O(n) = fair
       ■■ str in list[5]                           . (2)       0.000000657414913177490234375 soot:                     O(n) = fair
       ■■ str in list[10]                          . (2)        0.00000069303607940673828125 soot:                     O(n) = fair
       ■■ store ip tuple in dic                    . (2)      0.0000005951354503631591796875 soot:                O(1) = excellent
       ■■ 1k str to bytes                          . (2)      0.0000006817123889923095703125 soot:                     O(n) = fair
       ■■ 1k bytes to str                          . (2)      0.0000007892301082611083984375 soot:                     O(n) = fair
 ```

