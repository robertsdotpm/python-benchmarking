# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
 h atoms (1)      .g soot (2)      ,f rice (3)      :e peas (4)      ;d marbles (5)      |c golf balls (6)      Lb tennis balls (7)      #a bowling balls (8)
 1s 1000x > 1ms 1000x > 1µs 1000x > 1ns

 ■■■■■■■■ [⁰a 106 #] ms: dns lookup google.com (cached prob)        #a (8: like website RTT     )    0.106448888778 [1⁰] bowling balls a:      O(1) = excellent
 ■■■■■■■■ [⁰a 188 #] ms: tcp echo client                            #a (8: like website RTT     )    0.188036775589 [1⁰] bowling balls a:      O(1) = excellent
  ■■■■■■■ [¹b 22  L] ms: tcp con to google                          Lb (7: like gaming RTT      )    0.0229234457018 [2¹] tennis balls b:      O(1) = excellent
     ■■■■ [⁴e 50  :] µs: send 10k udp packets                       :e (4: like memory slice    )          0.000050833463668 [5⁴] peas e:      O(1) = excellent
     ■■■■ [⁴e 30  :] µs: send 100 b udp packets                     :e (4: like memory slice    )         0.0000309000015258 [3⁴] peas e:      O(1) = excellent
     ■■■■ [⁴e 29  :] µs: send 1k udp packets                        :e (4: like memory slice    )         0.0000298998355864 [2⁴] peas e:      O(1) = excellent
     ■■■■ [⁴e 14  :] µs: n in list[1000]                            :e (4: like memory slice    )         0.0000145513296127 [1⁴] peas e:           O(n) = fair
      ■■■ [⁵f 5   ,] µs: bind dgram sock                            ,f (3: like LAN send        )        0.00000597953796386 [5⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 4   ,] µs: build dgram sock                           ,f (3: like LAN send        )        0.00000498461723328 [4⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 3   ,] µs: build stream sock                          ,f (3: like LAN send        )        0.00000398707389832 [3⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 2   ,] µs: create an async queue                      ,f (3: like LAN send        )        0.00000219090914682 [2⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 2   ,] µs: n in list[100]                             ,f (3: like LAN send        )        0.00000206553554503 [2⁵] rice f:           O(n) = fair
      ■■■ [⁵f 2   ,] µs: ip bytes to ipaddress                      ,f (3: like LAN send        )        0.00000234719800903 [2⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 1   ,] µs: time()                                     ,f (3: like LAN send        )        0.00000122823667519 [1⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 1   ,] µs: add to an async queue                      ,f (3: like LAN send        )        0.00000119613361362 [1⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 1   ,] µs: build async event                          ,f (3: like LAN send        )        0.00000117882537842 [1⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 1   ,] µs: str in list[100]                           ,f (3: like LAN send        )        0.00000122375082974 [1⁵] rice f:           O(n) = fair
       ■■ [⁶g 939 .] ns: get from an async queue                    .g (2: like 1KB compression )       0.000000939646482532 [9⁶] soot g:      O(1) = excellent
       ■■ [⁶g 818 .] ns: n in list[10]                              .g (2: like 1KB compression )       0.000000818305969318 [8⁶] soot g:           O(n) = fair
       ■■ [⁶g 808 .] ns: 1k bytes to str                            .g (2: like 1KB compression )       0.000000808801174229 [8⁶] soot g:           O(n) = fair
       ■■ [⁶g 782 .] ns: set async event                            .g (2: like 1KB compression )       0.000000782751560263 [7⁶] soot g:      O(1) = excellent
       ■■ [⁶g 749 .] ns: n in list[5]                               .g (2: like 1KB compression )       0.000000749145507889 [7⁶] soot g:           O(n) = fair
       ■■ [⁶g 704 .] ns: str in list[10]                            .g (2: like 1KB compression )       0.000000704548597394 [7⁶] soot g:           O(n) = fair
       ■■ [⁶g 726 .] ns: 1k str to bytes                            .g (2: like 1KB compression )       0.000000726617336328 [7⁶] soot g:           O(n) = fair
       ■■ [⁶g 676 .] ns: list append small int                      .g (2: like 1KB compression )       0.000000676083564809 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 628 .] ns: overhead of a func call                    .g (2: like 1KB compression )       0.000000628982782418 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 655 .] ns: make a dic with one item                   .g (2: like 1KB compression )       0.000000655885934885 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 641 .] ns: dict key lookup from single item dic       .g (2: like 1KB compression )       0.000000641970396062 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 661 .] ns: make a dic with 4 items                    .g (2: like 1KB compression )       0.000000661128282586 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 619 .] ns: dict key lookup from 4 item dic            .g (2: like 1KB compression )       0.000000619813203842 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 648 .] ns: if x == n else ..                          .g (2: like 1KB compression )       0.000000648170948074 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 689 .] ns: str in list[5]                             .g (2: like 1KB compression )       0.000000689481258474 [6⁶] soot g:           O(n) = fair
       ■■ [⁶g 620 .] ns: store ip tuple in dic                      .g (2: like 1KB compression )       0.000000620451927237 [6⁶] soot g:      O(1) = excellent
 ```

