# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md

```
  atoms (1)      . soot (2)      , rice (3)      : peas (4)      ; marbles (5)      | golf balls (6)      L tennis balls (7)      # bowling balls (8)

 ■■■■■■■■ [1#] tcp con to google                        # (8: like website RTT     ) 0.1237130880355837 [1] bowling balls:                O(1) = excellent
 ■■■■■■■■ [1#] tcp echo client                          # (8: like website RTT     ) 0.1887878894805908 [1] bowling balls:                O(1) = excellent
    ■■■■■ [4;] dns lookup google.com (cached prob)      ; (5: like datacenter RTT  )   0.0004778861999511719 [4] marbles:                O(1) = excellent
     ■■■■ [4:] send 10k udp packets                     : (4: like memory slice    )     0.00004984521865844723 [4] peas:                O(1) = excellent
     ■■■■ [2:] send 100 b udp packets                   : (4: like memory slice    )     0.00002990055084228515 [2] peas:                O(1) = excellent
     ■■■■ [2:] send 1k udp packets                      : (4: like memory slice    )     0.00002690529823303221 [2] peas:                O(1) = excellent
     ■■■■ [1:] n in list[1000]                          : (4: like memory slice    )     0.00001435198783874497 [1] peas:                     O(n) = fair
      ■■■ [8,] bind dgram sock                          , (3: like LAN send        )    0.000008969783782958983 [8] rice:                O(1) = excellent
      ■■■ [5,] build stream sock                        , (3: like LAN send        )    0.000005980491638183594 [5] rice:                O(1) = excellent
      ■■■ [2,] create an async queue                    , (3: like LAN send        )     0.00000224156951904328 [2] rice:                O(1) = excellent
      ■■■ [2,] n in list[100]                           , (3: like LAN send        )    0.000002055997133255277 [2] rice:                     O(n) = fair
      ■■■ [2,] ip bytes to ipaddress                    , (3: like LAN send        )    0.000002355136156082513 [2] rice:                O(1) = excellent
      ■■■ [2,] build dgram sock                         , (3: like LAN send        )    0.000002989768981933593 [2] rice:                O(1) = excellent
      ■■■ [1,] time()                                   , (3: like LAN send        )    0.000001206345796585112 [1] rice:                O(1) = excellent
      ■■■ [1,] add to an async queue                    , (3: like LAN send        )     0.00000116366481781008 [1] rice:                O(1) = excellent
      ■■■ [1,] build async event                        , (3: like LAN send        )    0.000001178073644638086 [1] rice:                O(1) = excellent
      ■■■ [1,] str in list[100]                         , (3: like LAN send        )    0.000001191073179245019 [1] rice:                     O(n) = fair
       ■■ [9.] get from an async queue                  . (2: like 1KB compression )   0.0000009950804710387912 [9] soot:                O(1) = excellent
       ■■ [8.] 1k bytes to str                          . (2: like 1KB compression )   0.0000008176639080047389 [8] soot:                     O(n) = fair
       ■■ [7.] list append small int                    . (2: like 1KB compression )   0.0000007087996006011867 [7] soot:                O(1) = excellent
       ■■ [7.] set async event                          . (2: like 1KB compression )   0.0000007887718677520542 [7] soot:                O(1) = excellent
       ■■ [7.] n in list[5]                             . (2: like 1KB compression )     0.00000074463152885435 [7] soot:                     O(n) = fair
       ■■ [7.] n in list[10]                            . (2: like 1KB compression )   0.0000007902967929839875 [7] soot:                     O(n) = fair
       ■■ [7.] 1k str to bytes                          . (2: like 1KB compression )   0.0000007433254718780319 [7] soot:                     O(n) = fair
       ■■ [6.] overhead of a func call                  . (2: like 1KB compression )   0.0000006837174892425482 [6] soot:                O(1) = excellent
       ■■ [6.] make a dic with one item                 . (2: like 1KB compression )   0.0000006112818717956396 [6] soot:                O(1) = excellent
       ■■ [6.] dict key lookup from single item dic     . (2: like 1KB compression )   0.0000006618788242339915 [6] soot:                O(1) = excellent
       ■■ [6.] make a dic with 4 items                  . (2: like 1KB compression )   0.0000006766662597656071 [6] soot:                O(1) = excellent
       ■■ [6.] dict key lookup from 4 item dic          . (2: like 1KB compression )   0.0000006657655239105048 [6] soot:                O(1) = excellent
       ■■ [6.] if x == n else ..                        . (2: like 1KB compression )   0.0000006154954433441001 [6] soot:                O(1) = excellent
       ■■ [6.] str in list[5]                           . (2: like 1KB compression )   0.0000006851358413696109 [6] soot:                     O(n) = fair
       ■■ [6.] str in list[10]                          . (2: like 1KB compression )   0.0000006876409053802312 [6] soot:                     O(n) = fair
       ■■ [6.] store ip tuple in dic                    . (2: like 1KB compression )   0.0000006372539997100665 [6] soot:                O(1) = excellent
 ```

