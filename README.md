# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
  atoms (1)      . soot (2)      , rice (3)      : peas (4)      ; marbles (5)      | golf balls (6)      L tennis balls (7)      # bowling balls (8)

 ■■■■■■■■ [1a #] tcp echo client                            #a (8: like website RTT     )     0.188696670532 [1] bowling balls a:      O(1) = excellent
  ■■■■■■■ [7b L] dns lookup google.com (cached prob)        Lb (7: like gaming RTT      )     0.0763056278229 [7] tennis balls b:      O(1) = excellent
  ■■■■■■■ [2b L] tcp con to google                          Lb (7: like gaming RTT      )     0.0223058223724 [2] tennis balls b:      O(1) = excellent
     ■■■■ [5e :] send 10k udp packets                       :e (4: like memory slice    )          0.0000538222789759 [5] peas e:      O(1) = excellent
     ■■■■ [3e :] send 1k udp packets                        :e (4: like memory slice    )          0.0000328967571257 [3] peas e:      O(1) = excellent
     ■■■■ [2e :] send 100 b udp packets                     :e (4: like memory slice    )          0.0000249207019805 [2] peas e:      O(1) = excellent
     ■■■■ [1e :] n in list[1000]                            :e (4: like memory slice    )          0.0000144517898566 [1] peas e:           O(n) = fair
     ■■■■ [1e :] bind dgram sock                            :e (4: like memory slice    )          0.0000109620094299 [1] peas e:      O(1) = excellent
      ■■■ [5f ,] build dgram sock                           ,f (3: like LAN send        )         0.00000598359107971 [5] rice f:      O(1) = excellent
      ■■■ [3f ,] build stream sock                          ,f (3: like LAN send        )         0.00000398707389831 [3] rice f:      O(1) = excellent
      ■■■ [2f ,] create an async queue                      ,f (3: like LAN send        )         0.00000233536243393 [2] rice f:      O(1) = excellent
      ■■■ [2f ,] n in list[100]                             ,f (3: like LAN send        )         0.00000207922744726 [2] rice f:           O(n) = fair
      ■■■ [2f ,] ip bytes to ipaddress                      ,f (3: like LAN send        )         0.00000238977050744 [2] rice f:      O(1) = excellent
      ■■■ [1f ,] time()                                     ,f (3: like LAN send        )         0.00000127546715738 [1] rice f:      O(1) = excellent
      ■■■ [1f ,] add to an async queue                      ,f (3: like LAN send        )         0.00000117303323741 [1] rice f:      O(1) = excellent
      ■■■ [1f ,] get from an async queue                    ,f (3: like LAN send        )         0.00000101852607727 [1] rice f:      O(1) = excellent
      ■■■ [1f ,] build async event                          ,f (3: like LAN send        )         0.00000127411794661 [1] rice f:      O(1) = excellent
      ■■■ [1f ,] str in list[100]                           ,f (3: like LAN send        )         0.00000118250846867 [1] rice f:           O(n) = fair
       ■■ [8g .] set async event                            .g (2: like 1KB compression )         0.00000088778686526 [8] soot g:      O(1) = excellent
       ■■ [8g .] n in list[10]                              .g (2: like 1KB compression )        0.000000869704484933 [8] soot g:           O(n) = fair
       ■■ [7g .] list append small int                      .g (2: like 1KB compression )        0.000000751696825036 [7] soot g:      O(1) = excellent
       ■■ [7g .] make a dic with 4 items                    .g (2: like 1KB compression )        0.000000717749118812 [7] soot g:      O(1) = excellent
       ■■ [7g .] n in list[5]                               .g (2: like 1KB compression )        0.000000764899730682 [7] soot g:           O(n) = fair
       ■■ [7g .] str in list[10]                            .g (2: like 1KB compression )        0.000000718265533504 [7] soot g:           O(n) = fair
       ■■ [7g .] 1k str to bytes                            .g (2: like 1KB compression )        0.000000747452974382 [7] soot g:           O(n) = fair
       ■■ [7g .] 1k bytes to str                            .g (2: like 1KB compression )        0.000000793936014212 [7] soot g:           O(n) = fair
       ■■ [6g .] overhead of a func call                    .g (2: like 1KB compression )        0.000000662959814089 [6] soot g:      O(1) = excellent
       ■■ [6g .] make a dic with one item                   .g (2: like 1KB compression )        0.000000603074312241 [6] soot g:      O(1) = excellent
       ■■ [6g .] dict key lookup from single item dic       .g (2: like 1KB compression )        0.000000634622812281 [6] soot g:      O(1) = excellent
       ■■ [6g .] dict key lookup from 4 item dic            .g (2: like 1KB compression )        0.000000645556688318 [6] soot g:      O(1) = excellent
       ■■ [6g .] str in list[5]                             .g (2: like 1KB compression )        0.000000687805652668 [6] soot g:           O(n) = fair
       ■■ [6g .] store ip tuple in dic                      .g (2: like 1KB compression )        0.000000665157079742 [6] soot g:      O(1) = excellent
       ■■ [5g .] if x == n else ..                          .g (2: like 1KB compression )        0.000000587586641362 [5] soot g:      O(1) = excellent
 ```

