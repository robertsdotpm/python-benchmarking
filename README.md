# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
 h atoms (1)      .g soot (2)      ,f rice (3)      :e peas (4)      ;d marbles (5)      |c golf balls (6)      Lb tennis balls (7)      #a bowling balls (8)
 1s 1000x > 1ms 1000x > 1µs 1000x > 1ns

 ■■■■■■■■ [⁰a 189 #] ms: tcp echo client                            #a (8: like website RTT     )    0.189165687561 [1⁰] bowling balls a:      O(1) = excellent
  ■■■■■■■ [¹b 80  L] ms: dns lookup google.com (cached prob)        Lb (7: like gaming RTT      )    0.0807644844055 [8¹] tennis balls b:      O(1) = excellent
  ■■■■■■■ [¹b 23  L] ms: tcp con to google                          Lb (7: like gaming RTT      )    0.0237143993378 [2¹] tennis balls b:      O(1) = excellent
     ■■■■ [⁴e 46  :] µs: send 10k udp packets                       :e (4: like memory slice    )         0.0000468444824207 [4⁴] peas e:      O(1) = excellent
     ■■■■ [⁴e 29  :] µs: send 100 b udp packets                     :e (4: like memory slice    )         0.0000299005508417 [2⁴] peas e:      O(1) = excellent
     ■■■■ [⁴e 27  :] µs: send 1k udp packets                        :e (4: like memory slice    )         0.0000279064178461 [2⁴] peas e:      O(1) = excellent
     ■■■■ [⁴e 13  :] µs: n in list[1000]                            :e (4: like memory slice    )         0.0000136542797093 [1⁴] peas e:           O(n) = fair
     ■■■■ [⁴e 11  :] µs: bind dgram sock                            :e (4: like memory slice    )          0.000011960029602 [1⁴] peas e:      O(1) = excellent
      ■■■ [⁵f 6   ,] µs: build dgram sock                           ,f (3: like LAN send        )        0.00000697684288024 [6⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 3   ,] µs: build stream sock                          ,f (3: like LAN send        )        0.00000398707389832 [3⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 2   ,] µs: ip bytes to ipaddress                      ,f (3: like LAN send        )        0.00000235885667788 [2⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 2   ,] µs: create an async queue                      ,f (3: like LAN send        )        0.00000226145529739 [2⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 2   ,] µs: n in list[100]                             ,f (3: like LAN send        )         0.0000021057250499 [2⁵] rice f:           O(n) = fair
      ■■■ [⁵f 1   ,] µs: time()                                     ,f (3: like LAN send        )        0.00000121691107761 [1⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 1   ,] µs: str in list[100]                           ,f (3: like LAN send        )        0.00000120235872282 [1⁵] rice f:           O(n) = fair
      ■■■ [⁵f 1   ,] µs: build async event                          ,f (3: like LAN send        )        0.00000118703246131 [1⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 1   ,] µs: add to an async queue                      ,f (3: like LAN send        )        0.00000115136599553 [1⁵] rice f:      O(1) = excellent
       ■■ [⁶g 960 .] ns: get from an async queue                    .g (2: like 1KB compression )        0.00000096086478249 [9⁶] soot g:      O(1) = excellent
       ■■ [⁶g 825 .] ns: set async event                            .g (2: like 1KB compression )       0.000000825977087154 [8⁶] soot g:      O(1) = excellent
       ■■ [⁶g 808 .] ns: n in list[10]                              .g (2: like 1KB compression )       0.000000808643818041 [8⁶] soot g:           O(n) = fair
       ■■ [⁶g 787 .] ns: 1k bytes to str                            .g (2: like 1KB compression )       0.000000787573337685 [7⁶] soot g:           O(n) = fair
       ■■ [⁶g 769 .] ns: n in list[5]                               .g (2: like 1KB compression )       0.000000769555091986 [7⁶] soot g:           O(n) = fair
       ■■ [⁶g 762 .] ns: 1k str to bytes                            .g (2: like 1KB compression )       0.000000762054443476 [7⁶] soot g:           O(n) = fair
       ■■ [⁶g 689 .] ns: str in list[5]                             .g (2: like 1KB compression )       0.000000689933300121 [6⁶] soot g:           O(n) = fair
       ■■ [⁶g 689 .] ns: dict key lookup from single item dic       .g (2: like 1KB compression )       0.000000689284324755 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 676 .] ns: str in list[10]                            .g (2: like 1KB compression )       0.000000676942110175 [6⁶] soot g:           O(n) = fair
       ■■ [⁶g 674 .] ns: list append small int                      .g (2: like 1KB compression )       0.000000674686193562 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 674 .] ns: make a dic with 4 items                    .g (2: like 1KB compression )       0.000000674427032576 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 659 .] ns: dict key lookup from 4 item dic            .g (2: like 1KB compression )       0.000000659515857803 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 656 .] ns: store ip tuple in dic                      .g (2: like 1KB compression )       0.000000656919717892 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 641 .] ns: if x == n else ..                          .g (2: like 1KB compression )       0.000000641301632023 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 633 .] ns: overhead of a func call                    .g (2: like 1KB compression )       0.000000633456707096 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 628 .] ns: make a dic with one item                   .g (2: like 1KB compression )       0.000000628479719255 [6⁶] soot g:      O(1) = excellent
 ```

