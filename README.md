# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
  atoms (1)      . soot (2)      , rice (3)      ; peas (4)      o marbles (5)      0 golf balls (6)      8 tennis balls (7)      # bowling balls (8)

 ■■■■■■■■ tcp echo client                          # (8: like website RTT     )   0.1885454654693603515625 (1) bowling balls:                O(1) = excellent
  ■■■■■■■ tcp con to google                        8 (7: like gaming RTT      )    0.0927736759185791015625 (9) tennis balls:                O(1) = excellent
    ■■■■■ dns lookup google.com (cached prob)      o (5: like datacenter RTT  )        0.00048086643218994140625 (4) marbles:                O(1) = excellent
     ■■■■ send 10k udp packets                     ; (4: like memory slice    )           0.00005183315277099609375 (5) peas:                O(1) = excellent
     ■■■■ send 100 b udp packets                   ; (4: like memory slice    )         0.0000219566822052001953125 (2) peas:                O(1) = excellent
     ■■■■ send 1k udp packets                      ; (4: like memory slice    )            0.0000219688415527343750 (2) peas:                O(1) = excellent
     ■■■■ n in list[1000]                          ; (4: like memory slice    )            0.0000150455474853515625 (1) peas:                     O(n) = fair
      ■■■ build stream sock                        , (3: like LAN send        )          0.000005982875823974609375 (5) rice:                O(1) = excellent
      ■■■ build dgram sock                         , (3: like LAN send        )         0.0000059964656829833984375 (5) rice:                O(1) = excellent
      ■■■ bind dgram sock                          , (3: like LAN send        )          0.000005972385406494140625 (5) rice:                O(1) = excellent
      ■■■ create an async queue                    , (3: like LAN send        )      0.0000022400701045989990234375 (2) rice:                O(1) = excellent
      ■■■ ip bytes to ipaddress                    , (3: like LAN send        )      0.0000023076479434967041015625 (2) rice:                O(1) = excellent
      ■■■ time()                                   , (3: like LAN send        )          0.000001212268829345703125 (1) rice:                O(1) = excellent
      ■■■ add to an async queue                    , (3: like LAN send        )        0.00000116480350494384765625 (1) rice:                O(1) = excellent
      ■■■ build async event                        , (3: like LAN send        )      0.0000011592772006988525390625 (1) rice:                O(1) = excellent
      ■■■ n in list[100]                           , (3: like LAN send        )      0.0000019873769283294677734375 (1) rice:                     O(n) = fair
      ■■■ str in list[100]                         , (3: like LAN send        )        0.00000120564746856689453125 (1) rice:                     O(n) = fair
       ■■ get from an async queue                  . (2: like 1KB compression )       0.000000964486598968505859375 (9) soot:                O(1) = excellent
       ■■ n in list[10]                            . (2: like 1KB compression )        0.00000083655261993408203125 (8) soot:                     O(n) = fair
       ■■ set async event                          . (2: like 1KB compression )        0.00000077172565460205078125 (7) soot:                O(1) = excellent
       ■■ n in list[5]                             . (2: like 1KB compression )      0.0000007133848667144775390625 (7) soot:                     O(n) = fair
       ■■ 1k bytes to str                          . (2: like 1KB compression )      0.0000007895748615264892578125 (7) soot:                     O(n) = fair
       ■■ list append small int                    . (2: like 1KB compression )      0.0000006581590175628662109375 (6) soot:                O(1) = excellent
       ■■ overhead of a func call                  . (2: like 1KB compression )       0.000000660897731781005859375 (6) soot:                O(1) = excellent
       ■■ make a dic with one item                 . (2: like 1KB compression )      0.0000006192595958709716796875 (6) soot:                O(1) = excellent
       ■■ dict key lookup from single item dic     . (2: like 1KB compression )      0.0000006652538776397705078125 (6) soot:                O(1) = excellent
       ■■ make a dic with 4 items                  . (2: like 1KB compression )        0.00000068299961090087890625 (6) soot:                O(1) = excellent
       ■■ dict key lookup from 4 item dic          . (2: like 1KB compression )       0.000000647033214569091796875 (6) soot:                O(1) = excellent
       ■■ if x == n else ..                        . (2: like 1KB compression )       0.000000625382900238037109375 (6) soot:                O(1) = excellent
       ■■ str in list[5]                           . (2: like 1KB compression )           0.00000068470001220703125 (6) soot:                     O(n) = fair
       ■■ str in list[10]                          . (2: like 1KB compression )       0.000000688507556915283203125 (6) soot:                     O(n) = fair
       ■■ store ip tuple in dic                    . (2: like 1KB compression )      0.0000006693451404571533203125 (6) soot:                O(1) = excellent
       ■■ 1k str to bytes                          . (2: like 1KB compression )      0.0000006932704448699951171875 (6) soot:                     O(n) = fair
 ```

