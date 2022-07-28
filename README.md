# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
 h atoms (1)      .g soot (2)      ,f rice (3)      :e peas (4)      ;d marbles (5)      |c golf balls (6)      Lb tennis balls (7)      #a bowling balls (8)

 ■■■■■■■■ [a1⁰ #] tcp echo client                            #a (8: like website RTT     )    0.188316106796 [1⁰] bowling balls a:      O(1) = excellent
  ■■■■■■■ [b7¹ L] dns lookup google.com (cached prob)        Lb (7: like gaming RTT      )    0.0786361217499 [7¹] tennis balls b:      O(1) = excellent
  ■■■■■■■ [b2¹ L] tcp con to google                          Lb (7: like gaming RTT      )    0.0233625888826 [2¹] tennis balls b:      O(1) = excellent
     ■■■■ [e4⁴ :] send 10k udp packets                       :e (4: like memory slice    )         0.0000498330593097 [4⁴] peas e:      O(1) = excellent
     ■■■■ [e2⁴ :] send 100 b udp packets                     :e (4: like memory slice    )         0.0000259127616877 [2⁴] peas e:      O(1) = excellent
     ■■■■ [e2⁴ :] send 1k udp packets                        :e (4: like memory slice    )         0.0000289039611811 [2⁴] peas e:      O(1) = excellent
     ■■■■ [e1⁴ :] n in list[1000]                            :e (4: like memory slice    )          0.000013654351235 [1⁴] peas e:           O(n) = fair
      ■■■ [f9⁵ ,] bind dgram sock                            ,f (3: like LAN send        )        0.00000996685028074 [9⁵] rice f:      O(1) = excellent
      ■■■ [f4⁵ ,] build stream sock                          ,f (3: like LAN send        )        0.00000498342514038 [4⁵] rice f:      O(1) = excellent
      ■■■ [f4⁵ ,] build dgram sock                           ,f (3: like LAN send        )        0.00000498342514038 [4⁵] rice f:      O(1) = excellent
      ■■■ [f2⁵ ,] create an async queue                      ,f (3: like LAN send        )        0.00000220578455923 [2⁵] rice f:      O(1) = excellent
      ■■■ [f2⁵ ,] n in list[100]                             ,f (3: like LAN send        )        0.00000202223539349 [2⁵] rice f:           O(n) = fair
      ■■■ [f2⁵ ,] ip bytes to ipaddress                      ,f (3: like LAN send        )        0.00000236460542667 [2⁵] rice f:      O(1) = excellent
      ■■■ [f2⁵ ,] 1k str to bytes                            ,f (3: like LAN send        )        0.00000208463025098 [2⁵] rice f:           O(n) = fair
      ■■■ [f2⁵ ,] 1k bytes to str                            ,f (3: like LAN send        )        0.00000214853715907 [2⁵] rice f:           O(n) = fair
      ■■■ [f1⁵ ,] time()                                     ,f (3: like LAN send        )        0.00000114843153968 [1⁵] rice f:      O(1) = excellent
      ■■■ [f1⁵ ,] add to an async queue                      ,f (3: like LAN send        )        0.00000109091687219 [1⁵] rice f:      O(1) = excellent
      ■■■ [f1⁵ ,] get from an async queue                    ,f (3: like LAN send        )        0.00000100463581101 [1⁵] rice f:      O(1) = excellent
      ■■■ [f1⁵ ,] build async event                          ,f (3: like LAN send        )        0.00000116221714033 [1⁵] rice f:      O(1) = excellent
      ■■■ [f1⁵ ,] str in list[100]                           ,f (3: like LAN send        )        0.00000122454547894 [1⁵] rice f:           O(n) = fair
       ■■ [g8⁶ .] n in list[10]                              .g (2: like 1KB compression )       0.000000806324482098 [8⁶] soot g:           O(n) = fair
       ■■ [g7⁶ .] set async event                            .g (2: like 1KB compression )        0.00000077389359487 [7⁶] soot g:      O(1) = excellent
       ■■ [g6⁶ .] list append small int                      .g (2: like 1KB compression )       0.000000665235757927 [6⁶] soot g:      O(1) = excellent
       ■■ [g6⁶ .] overhead of a func call                    .g (2: like 1KB compression )       0.000000671293497188 [6⁶] soot g:      O(1) = excellent
       ■■ [g6⁶ .] make a dic with one item                   .g (2: like 1KB compression )       0.000000647165775396 [6⁶] soot g:      O(1) = excellent
       ■■ [g6⁶ .] dict key lookup from single item dic       .g (2: like 1KB compression )       0.000000604201555348 [6⁶] soot g:      O(1) = excellent
       ■■ [g6⁶ .] make a dic with 4 items                    .g (2: like 1KB compression )       0.000000690963983638 [6⁶] soot g:      O(1) = excellent
       ■■ [g6⁶ .] dict key lookup from 4 item dic            .g (2: like 1KB compression )       0.000000643095016578 [6⁶] soot g:      O(1) = excellent
       ■■ [g6⁶ .] if x == n else ..                          .g (2: like 1KB compression )       0.000000604360580536 [6⁶] soot g:      O(1) = excellent
       ■■ [g6⁶ .] n in list[5]                               .g (2: like 1KB compression )       0.000000692735672107 [6⁶] soot g:           O(n) = fair
       ■■ [g6⁶ .] str in list[5]                             .g (2: like 1KB compression )       0.000000676540136437 [6⁶] soot g:           O(n) = fair
       ■■ [g6⁶ .] str in list[10]                            .g (2: like 1KB compression )       0.000000690455675236 [6⁶] soot g:           O(n) = fair
       ■■ [g6⁶ .] store ip tuple in dic                      .g (2: like 1KB compression )       0.000000651237011059 [6⁶] soot g:      O(1) = excellent
 ```

