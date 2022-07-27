# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
  atoms (1)      . soot (2)      , rice (3)      ; peas (4)      o marbles (5)      0 golf balls (6)      8 tennis balls (7)      # bowling balls (8)

 ■■■■■■■■ tcp echo client                          # (8: like website RTT     )   0.1881455421447753906250 (1) bowling balls:                O(1) = excellent
  ■■■■■■■ dns lookup google.com (cached prob)      8 (7: like gaming RTT      )    0.0805874347686767578125 (8) tennis balls:                O(1) = excellent
  ■■■■■■■ tcp con to google                        8 (7: like gaming RTT      )   0.02234952449798583984375 (2) tennis balls:                O(1) = excellent
     ■■■■ n in list[1000]                          ; (4: like memory slice    )        0.00001454451084136962890625 (1) peas:                     O(n) = fair
     ■■■■ send 100 b udp packets                   ; (4: like memory slice    )          0.000027948856353759765625 (2) peas:                O(1) = excellent
     ■■■■ send 1k udp packets                      ; (4: like memory slice    )         0.0000199639797210693359375 (1) peas:                O(1) = excellent
     ■■■■ send 10k udp packets                     ; (4: like memory slice    )           0.00005390644073486328125 (5) peas:                O(1) = excellent
      ■■■ time()                                   , (3: like LAN send        )      0.0000011982462406158447265625 (1) rice:                O(1) = excellent
      ■■■ create an async queue                    , (3: like LAN send        )       0.000002204707622528076171875 (2) rice:                O(1) = excellent
      ■■■ add to an async queue                    , (3: like LAN send        )      0.0000010872008800506591796875 (1) rice:                O(1) = excellent
      ■■■ get from an async queue                  , (3: like LAN send        )          0.000001011585235595703125 (1) rice:                O(1) = excellent
      ■■■ build async event                        , (3: like LAN send        )        0.00000117149639129638671875 (1) rice:                O(1) = excellent
      ■■■ n in list[100]                           , (3: like LAN send        )        0.00000204092502593994140625 (2) rice:                     O(n) = fair
      ■■■ str in list[100]                         , (3: like LAN send        )      0.0000011916148662567138671875 (1) rice:                     O(n) = fair
      ■■■ ip bytes to ipaddress                    , (3: like LAN send        )      0.0000023373339176177978515625 (2) rice:                O(1) = excellent
      ■■■ build stream sock                        , (3: like LAN send        )           0.00000398921966552734375 (3) rice:                O(1) = excellent
      ■■■ build dgram sock                         , (3: like LAN send        )         0.0000039899349212646484375 (3) rice:                O(1) = excellent
      ■■■ bind dgram sock                          , (3: like LAN send        )          0.000007987499237060546875 (7) rice:                O(1) = excellent
       ■■ list append small int                    . (2: like 1KB compression )          0.000000657611846923828125 (6) soot:                O(1) = excellent
       ■■ overhead of a func call                  . (2: like 1KB compression )      0.0000006468832492828369140625 (6) soot:                O(1) = excellent
       ■■ make a dic with one item                 . (2: like 1KB compression )      0.0000006409480571746826171875 (6) soot:                O(1) = excellent
       ■■ dict key lookup from single item dic     . (2: like 1KB compression )      0.0000006069147586822509765625 (6) soot:                O(1) = excellent
       ■■ make a dic with 4 items                  . (2: like 1KB compression )      0.0000006908242702484130859375 (6) soot:                O(1) = excellent
       ■■ dict key lookup from 4 item dic          . (2: like 1KB compression )        0.00000065827274322509765625 (6) soot:                O(1) = excellent
       ■■ set async event                          . (2: like 1KB compression )      0.0000008278291225433349609375 (8) soot:                O(1) = excellent
       ■■ if x == n else ..                        . (2: like 1KB compression )      0.0000006013524532318115234375 (6) soot:                O(1) = excellent
       ■■ n in list[5]                             . (2: like 1KB compression )      0.0000007472569942474365234375 (7) soot:                     O(n) = fair
       ■■ n in list[10]                            . (2: like 1KB compression )        0.00000076808643341064453125 (7) soot:                     O(n) = fair
       ■■ str in list[5]                           . (2: like 1KB compression )       0.000000689824581146240234375 (6) soot:                     O(n) = fair
       ■■ str in list[10]                          . (2: like 1KB compression )          0.000000665607452392578125 (6) soot:                     O(n) = fair
       ■■ store ip tuple in dic                    . (2: like 1KB compression )      0.0000006289389133453369140625 (6) soot:                O(1) = excellent
       ■■ 1k str to bytes                          . (2: like 1KB compression )      0.0000006944706439971923828125 (6) soot:                     O(n) = fair
       ■■ 1k bytes to str                          . (2: like 1KB compression )      0.0000008228013515472412109375 (8) soot:                     O(n) = fair
 ```

