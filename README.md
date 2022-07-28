# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
  atoms (1)      . soot (2)      , rice (3)      ; peas (4)      o marbles (5)      0 golf balls (6)      8 tennis balls (7)      # bowling balls (8)

 ■■■■■■■■ [1] tcp con to google                        # (8: like website RTT     ) 0.1229669332504273 [1] bowling balls:                O(1) = excellent
 ■■■■■■■■ [1] tcp echo client                          # (8: like website RTT     ) 0.1889734268188476 [1] bowling balls:                O(1) = excellent
    ■■■■■ [5] dns lookup google.com (cached prob)      o (5: like datacenter RTT  )   0.0005333423614501954 [5] marbles:                O(1) = excellent
     ■■■■ [4] send 10k udp packets                     ; (4: like memory slice    )     0.00004496312141418456 [4] peas:                O(1) = excellent
     ■■■■ [2] send 100 b udp packets                   ; (4: like memory slice    )     0.00002227282524108887 [2] peas:                O(1) = excellent
     ■■■■ [2] send 1k udp packets                      ; (4: like memory slice    )     0.00002356886863708495 [2] peas:                O(1) = excellent
     ■■■■ [1] n in list[1000]                          ; (4: like memory slice    )      0.0000143520355224608 [1] peas:                     O(n) = fair
      ■■■ [9] bind dgram sock                          , (3: like LAN send        )    0.000009870290756225586 [9] rice:                O(1) = excellent
      ■■■ [6] build stream sock                        , (3: like LAN send        )    0.000006406784057617186 [6] rice:                O(1) = excellent
      ■■■ [6] build dgram sock                         , (3: like LAN send        )    0.000006811380386352538 [6] rice:                O(1) = excellent
      ■■■ [2] create an async queue                    , (3: like LAN send        )    0.000002300775051117181 [2] rice:                O(1) = excellent
      ■■■ [2] n in list[100]                           , (3: like LAN send        )    0.000002094503164291597 [2] rice:                     O(n) = fair
      ■■■ [2] ip bytes to ipaddress                    , (3: like LAN send        )    0.000002473284959793313 [2] rice:                O(1) = excellent
      ■■■ [1] time()                                   , (3: like LAN send        )    0.000001216597080230732 [1] rice:                O(1) = excellent
      ■■■ [1] add to an async queue                    , (3: like LAN send        )    0.000001194925785064716 [1] rice:                O(1) = excellent
      ■■■ [1] get from an async queue                  , (3: like LAN send        )    0.000001036114692687967 [1] rice:                O(1) = excellent
      ■■■ [1] build async event                        , (3: like LAN send        )    0.000001226790189743058 [1] rice:                O(1) = excellent
      ■■■ [1] str in list[100]                         , (3: like LAN send        )    0.000001279877662658686 [1] rice:                     O(n) = fair
       ■■ [8] set async event                          . (2: like 1KB compression )   0.0000008355991840362325 [8] soot:                O(1) = excellent
       ■■ [8] n in list[10]                            . (2: like 1KB compression )   0.0000008142864704131869 [8] soot:                     O(n) = fair
       ■■ [8] 1k str to bytes                          . (2: like 1KB compression )   0.0000008477101325988693 [8] soot:                     O(n) = fair
       ■■ [8] 1k bytes to str                          . (2: like 1KB compression )   0.0000008749704360961871 [8] soot:                     O(n) = fair
       ■■ [7] list append small int                    . (2: like 1KB compression )   0.0000007111809253692467 [7] soot:                O(1) = excellent
       ■■ [7] make a dic with 4 items                  . (2: like 1KB compression )   0.0000007079343795776189 [7] soot:                O(1) = excellent
       ■■ [7] n in list[5]                             . (2: like 1KB compression )   0.0000007409768104553031 [7] soot:                     O(n) = fair
       ■■ [7] str in list[10]                          . (2: like 1KB compression )   0.0000007222461700439291 [7] soot:                     O(n) = fair
       ■■ [7] store ip tuple in dic                    . (2: like 1KB compression )   0.0000007375900745391758 [7] soot:                O(1) = excellent
       ■■ [6] overhead of a func call                  . (2: like 1KB compression )   0.0000006749403476714928 [6] soot:                O(1) = excellent
       ■■ [6] make a dic with one item                 . (2: like 1KB compression )   0.0000006400563716888275 [6] soot:                O(1) = excellent
       ■■ [6] dict key lookup from single item dic     . (2: like 1KB compression )   0.0000006504619121551347 [6] soot:                O(1) = excellent
       ■■ [6] dict key lookup from 4 item dic          . (2: like 1KB compression )   0.0000006545813083648515 [6] soot:                O(1) = excellent
       ■■ [6] if x == n else ..                        . (2: like 1KB compression )   0.0000006272678375243982 [6] soot:                O(1) = excellent
       ■■ [6] str in list[5]                           . (2: like 1KB compression )   0.0000006680550575256176 [6] soot:                     O(n) = fair
 ```

