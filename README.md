# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
 h atoms (1)      .g soot (2)      ,f rice (3)      :e peas (4)      ;d marbles (5)      |c golf balls (6)      Lb tennis balls (7)      #a bowling balls (8)

 ■■■■■■■■ [a1 #] tcp con to google                          #a (8: like website RTT     )     0.123720383642 [1] bowling balls a:      O(1) = excellent
 ■■■■■■■■ [a1 #] tcp echo client                            #a (8: like website RTT     )     0.188721704483 [1] bowling balls a:      O(1) = excellent
    ■■■■■ [d5 ;] dns lookup google.com (cached prob)        ;d (5: like datacenter RTT  )        0.000516033172607 [5] marbles d:      O(1) = excellent
     ■■■■ [e4 :] send 10k udp packets                       :e (4: like memory slice    )          0.0000468435287472 [4] peas e:      O(1) = excellent
     ■■■■ [e2 :] send 100 b udp packets                     :e (4: like memory slice    )          0.0000288951396941 [2] peas e:      O(1) = excellent
     ■■■■ [e2 :] send 1k udp packets                        :e (4: like memory slice    )          0.0000249238014218 [2] peas e:      O(1) = excellent
     ■■■■ [e1 :] n in list[1000]                            :e (4: like memory slice    )          0.0000139808893206 [1] peas e:           O(n) = fair
      ■■■ [f9 ,] bind dgram sock                            ,f (3: like LAN send        )         0.00000996804237365 [9] rice f:      O(1) = excellent
      ■■■ [f4 ,] build stream sock                          ,f (3: like LAN send        )         0.00000497865676881 [4] rice f:      O(1) = excellent
      ■■■ [f2 ,] create an async queue                      ,f (3: like LAN send        )         0.00000223852753593 [2] rice f:      O(1) = excellent
      ■■■ [f2 ,] n in list[100]                             ,f (3: like LAN send        )         0.00000206167054145 [2] rice f:           O(n) = fair
      ■■■ [f2 ,] ip bytes to ipaddress                      ,f (3: like LAN send        )         0.00000235897350279 [2] rice f:      O(1) = excellent
      ■■■ [f2 ,] build dgram sock                           ,f (3: like LAN send        )         0.00000299119949342 [2] rice f:      O(1) = excellent
      ■■■ [f1 ,] time()                                     ,f (3: like LAN send        )         0.00000119708418846 [1] rice f:      O(1) = excellent
      ■■■ [f1 ,] add to an async queue                      ,f (3: like LAN send        )         0.00000117393422122 [1] rice f:      O(1) = excellent
      ■■■ [f1 ,] build async event                          ,f (3: like LAN send        )         0.00000121178770059 [1] rice f:      O(1) = excellent
      ■■■ [f1 ,] str in list[100]                           ,f (3: like LAN send        )         0.00000123694205279 [1] rice f:           O(n) = fair
       ■■ [g9 .] get from an async queue                    .g (2: like 1KB compression )        0.000000967635870029 [9] soot g:      O(1) = excellent
       ■■ [g8 .] n in list[10]                              .g (2: like 1KB compression )        0.000000832880497022 [8] soot g:           O(n) = fair
       ■■ [g8 .] 1k bytes to str                            .g (2: like 1KB compression )        0.000000839214801832 [8] soot g:           O(n) = fair
       ■■ [g7 .] set async event                            .g (2: like 1KB compression )        0.000000791539907495 [7] soot g:      O(1) = excellent
       ■■ [g7 .] n in list[5]                               .g (2: like 1KB compression )        0.000000717027902619 [7] soot g:           O(n) = fair
       ■■ [g7 .] 1k str to bytes                            .g (2: like 1KB compression )        0.000000764803886426 [7] soot g:           O(n) = fair
       ■■ [g6 .] list append small int                      .g (2: like 1KB compression )        0.000000647662639643 [6] soot g:      O(1) = excellent
       ■■ [g6 .] overhead of a func call                    .g (2: like 1KB compression )        0.000000671195268656 [6] soot g:      O(1) = excellent
       ■■ [g6 .] make a dic with one item                   .g (2: like 1KB compression )        0.000000675966739695 [6] soot g:      O(1) = excellent
       ■■ [g6 .] dict key lookup from single item dic       .g (2: like 1KB compression )        0.000000635638237037 [6] soot g:      O(1) = excellent
       ■■ [g6 .] make a dic with 4 items                    .g (2: like 1KB compression )        0.000000690726518675 [6] soot g:      O(1) = excellent
       ■■ [g6 .] dict key lookup from 4 item dic            .g (2: like 1KB compression )        0.000000630423545861 [6] soot g:      O(1) = excellent
       ■■ [g6 .] if x == n else ..                          .g (2: like 1KB compression )        0.000000632575988795 [6] soot g:      O(1) = excellent
       ■■ [g6 .] str in list[5]                             .g (2: like 1KB compression )        0.000000681256055862 [6] soot g:           O(n) = fair
       ■■ [g6 .] str in list[10]                            .g (2: like 1KB compression )        0.000000680866003067 [6] soot g:           O(n) = fair
       ■■ [g6 .] store ip tuple in dic                      .g (2: like 1KB compression )        0.000000667348861725 [6] soot g:      O(1) = excellent
 ```

