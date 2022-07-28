# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
  atoms (1)      . soot (2)      , rice (3)      : peas (4)      ; marbles (5)      | golf balls (6)      L tennis balls (7)      # bowling balls (8)

 ■■■■■■■■ [1# a] tcp con to google                          #a (8: like website RTT     )     0.122793126107 [1] bowling balls a:      O(1) = excellent
 ■■■■■■■■ [1# a] tcp echo client                            #a (8: like website RTT     )     0.189628982544 [1] bowling balls a:      O(1) = excellent
    ■■■■■ [9; d] dns lookup google.com (cached prob)        ;d (5: like datacenter RTT  )        0.000915789604187 [9] marbles d:      O(1) = excellent
     ■■■■ [5: e] send 10k udp packets                       :e (4: like memory slice    )          0.0000518298149096 [5] peas e:      O(1) = excellent
     ■■■■ [2: e] send 100 b udp packets                     :e (4: like memory slice    )          0.0000299053192136 [2] peas e:      O(1) = excellent
     ■■■■ [2: e] send 1k udp packets                        :e (4: like memory slice    )          0.0000279064178464 [2] peas e:      O(1) = excellent
     ■■■■ [1: e] n in list[1000]                            :e (4: like memory slice    )          0.0000140520572666 [1] peas e:           O(n) = fair
      ■■■ [6, f] bind dgram sock                            ,f (3: like LAN send        )         0.00000697255134582 [6] rice f:      O(1) = excellent
      ■■■ [5, f] build stream sock                          ,f (3: like LAN send        )         0.00000597620010374 [5] rice f:      O(1) = excellent
      ■■■ [5, f] build dgram sock                           ,f (3: like LAN send        )         0.00000598001480102 [5] rice f:      O(1) = excellent
      ■■■ [2, f] create an async queue                      ,f (3: like LAN send        )         0.00000216451597184 [2] rice f:      O(1) = excellent
      ■■■ [2, f] n in list[100]                             ,f (3: like LAN send        )         0.00000202749180779 [2] rice f:           O(n) = fair
      ■■■ [2, f] ip bytes to ipaddress                      ,f (3: like LAN send        )          0.0000024115316864 [2] rice f:      O(1) = excellent
      ■■■ [1, f] time()                                     ,f (3: like LAN send        )         0.00000116483306886 [1] rice f:      O(1) = excellent
      ■■■ [1, f] add to an async queue                      ,f (3: like LAN send        )         0.00000112941336637 [1] rice f:      O(1) = excellent
      ■■■ [1, f] build async event                          ,f (3: like LAN send        )         0.00000115906953816 [1] rice f:      O(1) = excellent
      ■■■ [1, f] str in list[100]                           ,f (3: like LAN send        )         0.00000119600105288 [1] rice f:           O(n) = fair
       ■■ [9. g] get from an async queue                    .g (2: like 1KB compression )        0.000000950854301537 [9] soot g:      O(1) = excellent
       ■■ [8. g] n in list[10]                              .g (2: like 1KB compression )        0.000000808735847551 [8] soot g:           O(n) = fair
       ■■ [8. g] 1k bytes to str                            .g (2: like 1KB compression )        0.000000833257198411 [8] soot g:           O(n) = fair
       ■■ [7. g] set async event                            .g (2: like 1KB compression )        0.000000732600212165 [7] soot g:      O(1) = excellent
       ■■ [7. g] n in list[5]                               .g (2: like 1KB compression )        0.000000716044187603 [7] soot g:           O(n) = fair
       ■■ [7. g] str in list[10]                            .g (2: like 1KB compression )        0.000000724999904696 [7] soot g:           O(n) = fair
       ■■ [7. g] 1k str to bytes                            .g (2: like 1KB compression )        0.000000723023414671 [7] soot g:           O(n) = fair
       ■■ [6. g] list append small int                      .g (2: like 1KB compression )        0.000000636410474827 [6] soot g:      O(1) = excellent
       ■■ [6. g] overhead of a func call                    .g (2: like 1KB compression )        0.000000645185709053 [6] soot g:      O(1) = excellent
       ■■ [6. g] make a dic with one item                   .g (2: like 1KB compression )        0.000000620331049009 [6] soot g:      O(1) = excellent
       ■■ [6. g] dict key lookup from single item dic       .g (2: like 1KB compression )         0.00000063627123837 [6] soot g:      O(1) = excellent
       ■■ [6. g] make a dic with 4 items                    .g (2: like 1KB compression )        0.000000679139614154 [6] soot g:      O(1) = excellent
       ■■ [6. g] dict key lookup from 4 item dic            .g (2: like 1KB compression )        0.000000600421667156 [6] soot g:      O(1) = excellent
       ■■ [6. g] if x == n else ..                          .g (2: like 1KB compression )        0.000000619029760415 [6] soot g:      O(1) = excellent
       ■■ [6. g] str in list[5]                             .g (2: like 1KB compression )        0.000000659260511457 [6] soot g:           O(n) = fair
       ■■ [6. g] store ip tuple in dic                      .g (2: like 1KB compression )        0.000000627772569718 [6] soot g:      O(1) = excellent
 ```

