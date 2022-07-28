# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
 h atoms (1)      .g soot (2)      ,f rice (3)      :e peas (4)      ;d marbles (5)      |c golf balls (6)      Lb tennis balls (7)      #a bowling balls (8)
 1s 1000x > 1ms 1000x > 1µs 1000x > 1ns

 ■■■■■■■■ [⁰a 190 #] ms: tcp echo client                             slow #a (8: like website RTT     )    0.190159368515 [1⁰] bowling balls a:      O(1) = excellent
 ■■■■■■■■ [⁰a 140 #] ms: dns lookup google.com (cached prob)         slow #a (8: like website RTT     )    0.140346503258 [1⁰] bowling balls a:      O(1) = excellent
  ■■■■■■■ [¹b 23  L] ms: tcp con to google                           slow Lb (7: like gaming RTT      )    0.0237961053848 [2¹] tennis balls b:      O(1) = excellent
     ■■■■ [⁴e 46  :] µs: send 10k udp packets                       brisk :e (4: like memory slice    )         0.0000468430519092 [4⁴] peas e:      O(1) = excellent
     ■■■■ [⁴e 27  :] µs: send 1k udp packets                        brisk :e (4: like memory slice    )         0.0000279068946833 [2⁴] peas e:      O(1) = excellent
     ■■■■ [⁴e 22  :] µs: send 100 b udp packets                     brisk :e (4: like memory slice    )         0.0000224039554594 [2⁴] peas e:      O(1) = excellent
     ■■■■ [⁴e 14  :] µs: n in list[1000]                            brisk :e (4: like memory slice    )         0.0000143519878392 [1⁴] peas e:           O(n) = fair
      ■■■ [⁵f 7   ,] µs: build dgram sock                           brisk ,f (3: like LAN send        )        0.00000797271728514 [7⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 6   ,] µs: build stream sock                          brisk ,f (3: like LAN send        )        0.00000697636604308 [6⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 4   ,] µs: bind dgram sock                            brisk ,f (3: like LAN send        )        0.00000498247146607 [4⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 2   ,] µs: ip bytes to ipaddress                      brisk ,f (3: like LAN send        )        0.00000236171483951 [2⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 2   ,] µs: create an async queue                      brisk ,f (3: like LAN send        )        0.00000235852456026 [2⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 2   ,] µs: 1k bytes to str                            brisk ,f (3: like LAN send        )        0.00000212527322747 [2⁵] rice f:           O(n) = fair
      ■■■ [⁵f 2   ,] µs: n in list[100]                             brisk ,f (3: like LAN send        )        0.00000202596425987 [2⁵] rice f:           O(n) = fair
      ■■■ [⁵f 2   ,] µs: 1k str to bytes                            brisk ,f (3: like LAN send        )        0.00000201060461971 [2⁵] rice f:           O(n) = fair
      ■■■ [⁵f 1   ,] µs: build async event                          brisk ,f (3: like LAN send        )        0.00000120729970933 [1⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 1   ,] µs: str in list[100]                           brisk ,f (3: like LAN send        )        0.00000120620274544 [1⁵] rice f:           O(n) = fair
      ■■■ [⁵f 1   ,] µs: add to an async queue                      brisk ,f (3: like LAN send        )        0.00000118769288048 [1⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 1   ,] µs: time()                                     brisk ,f (3: like LAN send        )        0.00000116114020354 [1⁵] rice f:      O(1) = excellent
      ■■■ [⁵f 1   ,] µs: get from an async queue                    brisk ,f (3: like LAN send        )         0.0000011018276214 [1⁵] rice f:      O(1) = excellent
       ■■ [⁶g 852 .] ns: n in list[10]                               fast .g (2: like 1KB compression )       0.000000852153539726 [8⁶] soot g:           O(n) = fair
       ■■ [⁶g 755 .] ns: set async event                             fast .g (2: like 1KB compression )       0.000000755170822204 [7⁶] soot g:      O(1) = excellent
       ■■ [⁶g 743 .] ns: n in list[5]                                fast .g (2: like 1KB compression )       0.000000743911027969 [7⁶] soot g:           O(n) = fair
       ■■ [⁶g 722 .] ns: make a dic with 4 items                     fast .g (2: like 1KB compression )       0.000000722963333124 [7⁶] soot g:      O(1) = excellent
       ■■ [⁶g 711 .] ns: dict key lookup from 4 item dic             fast .g (2: like 1KB compression )       0.000000711860418336 [7⁶] soot g:      O(1) = excellent
       ■■ [⁶g 694 .] ns: str in list[10]                             fast .g (2: like 1KB compression )        0.00000069463634498 [6⁶] soot g:           O(n) = fair
       ■■ [⁶g 683 .] ns: str in list[5]                              fast .g (2: like 1KB compression )       0.000000683158397733 [6⁶] soot g:           O(n) = fair
       ■■ [⁶g 659 .] ns: dict key lookup from single item dic        fast .g (2: like 1KB compression )       0.000000659031152778 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 652 .] ns: overhead of a func call                     fast .g (2: like 1KB compression )       0.000000652029514357 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 632 .] ns: if x == n else ..                           fast .g (2: like 1KB compression )       0.000000632991313993 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 630 .] ns: list append small int                       fast .g (2: like 1KB compression )       0.000000630065679606 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 629 .] ns: make a dic with one item                    fast .g (2: like 1KB compression )       0.000000629672288964 [6⁶] soot g:      O(1) = excellent
       ■■ [⁶g 623 .] ns: store ip tuple in dic                       fast .g (2: like 1KB compression )       0.000000623999595701 [6⁶] soot g:      O(1) = excellent
 ```

