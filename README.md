# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
 h atoms (1)      .g soot (2)      ,f rice (3)      :e peas (4)      ;d marbles (5)      |c golf balls (6)      Lb tennis balls (7)      #a bowling balls (8)
 1s 1000x > 1ms 1000x > 1µs 1000x > 1ns

 ■■■■■■■■ [⁰a 187 #] ms: tcp echo client                            #a (8: like website RTT     )    0.187500715256 [1⁰] bowling balls a:      O(1) = excellent
  ■■■■■■■ [¹b 961 L] ms: tcp con to google                          Lb (7: like gaming RTT      )    0.0961748361588 [9¹] tennis balls b:      O(1) = excellent
    ■■■■■ [³d 494 ;] µs: dns lookup google.com (cached prob)        ;d (5: like datacenter RTT  )       0.000494384765625 [4³] marbles d:      O(1) = excellent
     ■■■■ [⁴e 468 :] µs: send 10k udp packets                       :e (4: like memory slice    )         0.0000468394756305 [4⁴] peas e:      O(1) = excellent
     ■■■■ [⁴e 229 :] µs: send 100 b udp packets                     :e (4: like memory slice    )         0.0000229246616361 [2⁴] peas e:      O(1) = excellent
     ■■■■ [⁴e 142 :] µs: n in list[1000]                            :e (4: like memory slice    )         0.0000142563104633 [1⁴] peas e:           O(n) = fair
     ■■■■ [⁴e 119 :] µs: bind dgram sock                            :e (4: like memory slice    )         0.0000119590759277 [1⁴] peas e:      O(1) = excellent
     ■■■■ [⁴e 194 :] µs: send 1k udp packets                        :e (4: like memory slice    )         0.0000194425582884 [1⁴] peas e:      O(1) = excellent
      ■■■ [⁵f 597 ,] µs: build stream sock                          ,f (3: like LAN send        )        0.00000597977638244 [5⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 246 ,] µs: create an async queue                      ,f (3: like LAN send        )         0.0000024615094657 [2⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 207 ,] µs: n in list[100]                             ,f (3: like LAN send        )        0.00000207245278332 [2⁵] rice f:           O(n) = fair
      ■■■ [⁵f 234 ,] µs: ip bytes to ipaddress                      ,f (3: like LAN send        )        0.00000234844446154 [2⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 299 ,] µs: build dgram sock                           ,f (3: like LAN send        )         0.0000029902458191 [2⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 115 ,] µs: time()                                     ,f (3: like LAN send        )        0.00000115557599074 [1⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 126 ,] µs: add to an async queue                      ,f (3: like LAN send        )        0.00000126496720308 [1⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 111 ,] µs: build async event                          ,f (3: like LAN send        )        0.00000111772203454 [1⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 118 ,] µs: str in list[100]                           ,f (3: like LAN send        )        0.00000118474745754 [1⁵] rice f:           O(n) = fair
       ■■ [⁶g 977 .] ns: get from an async queue                    .g (2: like 1KB compression )       0.000000977082967836 [9⁶] soot g:      O(1) = excellent
       ■■ [⁶g 800 .] ns: set async event                            .g (2: like 1KB compression )       0.000000800107956012 [8⁶] soot g:      O(1) = excellent
       ■■ [⁶g 851 .] ns: n in list[10]                              .g (2: like 1KB compression )       0.000000851855754849 [8⁶] soot g:           O(n) = fair
       ■■ [⁶g 702 .] ns: make a dic with 4 items                    .g (2: like 1KB compression )         0.0000007028055191 [7⁶] soot g:      O(1) = excellent
       ■■ [⁶g 783 .] ns: n in list[5]                               .g (2: like 1KB compression )       0.000000783831357972 [7⁶] soot g:           O(n) = fair
       ■■ [⁶g 732 .] ns: str in list[10]                            .g (2: like 1KB compression )       0.000000732957840046 [7⁶] soot g:           O(n) = fair
       ■■ [⁶g 703 .] ns: 1k str to bytes                            .g (2: like 1KB compression )       0.000000703740596837 [7⁶] soot g:           O(n) = fair
       ■■ [⁶g 779 .] ns: 1k bytes to str                            .g (2: like 1KB compression )       0.000000779015779578 [7⁶] soot g:           O(n) = fair
       ■■ [⁶g 675 .] ns: list append small int                      .g (2: like 1KB compression )       0.000000675343751954 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 643 .] ns: overhead of a func call                    .g (2: like 1KB compression )       0.000000643025875155 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 632 .] ns: make a dic with one item                   .g (2: like 1KB compression )       0.000000632129430807 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 697 .] ns: dict key lookup from single item dic       .g (2: like 1KB compression )       0.000000697077274319 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 686 .] ns: dict key lookup from 4 item dic            .g (2: like 1KB compression )       0.000000686251401917 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 622 .] ns: if x == n else ..                          .g (2: like 1KB compression )       0.000000622621297892 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 659 .] ns: str in list[5]                             .g (2: like 1KB compression )       0.000000659553289479 [6⁶] soot g:           O(n) = fair
       ■■ [⁶g 621 .] ns: store ip tuple in dic                      .g (2: like 1KB compression )       0.000000621436357554 [6⁶] soot g:      O(1) = excellent
 ```

