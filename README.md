# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
  atoms (1)      . soot (2)      , rice (3)      ; peas (4)      o marbles (5)      0 golf balls (6)      8 tennis balls (7)      # bowling balls (8)

 ■■■■■■■■ tcp con to google                        # (8: like website RTT     )   0.1311063289642333984375 bowling balls:                O(1) = excellent
 ■■■■■■■■ tcp echo client                          # (8: like website RTT     )   0.1882236003875732421875 bowling balls:                O(1) = excellent
    ■■■■■ dns lookup google.com (cached prob)      o (5: like datacenter RTT  )        0.00076539516448974609375 marbles:                O(1) = excellent
     ■■■■ n in list[1000]                          ; (4: like memory slice    )         0.0000147751331329345703125 peas:                     O(n) = fair
     ■■■■ send 100 b udp packets                   ; (4: like memory slice    )         0.0000259563922882080078125 peas:                O(1) = excellent
     ■■■■ send 1k udp packets                      ; (4: like memory slice    )         0.0000279543399810791015625 peas:                O(1) = excellent
     ■■■■ send 10k udp packets                     ; (4: like memory slice    )         0.0000459291934967041015625 peas:                O(1) = excellent
      ■■■ time()                                   , (3: like LAN send        )        0.00000119509029388427734375 rice:                O(1) = excellent
      ■■■ create an async queue                    , (3: like LAN send        )         0.0000022507457733154296875 rice:                O(1) = excellent
      ■■■ add to an async queue                    , (3: like LAN send        )       0.000001151882648468017578125 rice:                O(1) = excellent
      ■■■ build async event                        , (3: like LAN send        )      0.0000012413203716278076171875 rice:                O(1) = excellent
      ■■■ n in list[100]                           , (3: like LAN send        )         0.0000020178241729736328125 rice:                     O(n) = fair
      ■■■ str in list[100]                         , (3: like LAN send        )        0.00000126682186126708984375 rice:                     O(n) = fair
      ■■■ ip bytes to ipaddress                    , (3: like LAN send        )      0.0000023219172954559326171875 rice:                O(1) = excellent
      ■■■ build stream sock                        , (3: like LAN send        )         0.0000079877376556396484375 rice:                O(1) = excellent
      ■■■ build dgram sock                         , (3: like LAN send        )         0.0000079886913299560546875 rice:                O(1) = excellent
      ■■■ bind dgram sock                          , (3: like LAN send        )         0.0000039923191070556640625 rice:                O(1) = excellent
       ■■ list append small int                    . (2: like 1KB compression )      0.0000006709063053131103515625 soot:                O(1) = excellent
       ■■ overhead of a func call                  . (2: like 1KB compression )       0.000000640750408172607421875 soot:                O(1) = excellent
       ■■ make a dic with one item                 . (2: like 1KB compression )      0.0000006249525547027587890625 soot:                O(1) = excellent
       ■■ dict key lookup from single item dic     . (2: like 1KB compression )      0.0000006310336589813232421875 soot:                O(1) = excellent
       ■■ make a dic with 4 items                  . (2: like 1KB compression )      0.0000006671059131622314453125 soot:                O(1) = excellent
       ■■ dict key lookup from 4 item dic          . (2: like 1KB compression )        0.00000060701656341552734375 soot:                O(1) = excellent
       ■■ get from an async queue                  . (2: like 1KB compression )       0.000000973964214324951171875 soot:                O(1) = excellent
       ■■ set async event                          . (2: like 1KB compression )      0.0000007653181552886962890625 soot:                O(1) = excellent
       ■■ if x == n else ..                        . (2: like 1KB compression )      0.0000006139853000640869140625 soot:                O(1) = excellent
       ■■ n in list[5]                             . (2: like 1KB compression )      0.0000006913235187530517578125 soot:                     O(n) = fair
       ■■ n in list[10]                            . (2: like 1KB compression )           0.00000075882720947265625 soot:                     O(n) = fair
       ■■ str in list[5]                           . (2: like 1KB compression )          0.000000694484710693359375 soot:                     O(n) = fair
       ■■ str in list[10]                          . (2: like 1KB compression )         0.0000006686000823974609375 soot:                     O(n) = fair
       ■■ store ip tuple in dic                    . (2: like 1KB compression )      0.0000006300361156463623046875 soot:                O(1) = excellent
       ■■ 1k str to bytes                          . (2: like 1KB compression )           0.00000078884124755859375 soot:                     O(n) = fair
       ■■ 1k bytes to str                          . (2: like 1KB compression )         0.0000008470745086669921875 soot:                     O(n) = fair
 ```

