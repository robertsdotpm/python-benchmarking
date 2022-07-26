# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md
```
        atoms (8)      . soot (7)      , rice (6)      ; peas (5)      o marbles (4)      0 golf balls (3)      8 tennis balls (2)      # bowling balls (1)

      ■■■ time()                                   ,      0.0000011669290065765380859375 rice:                O(1) = excellent
       ■■ list append small int                    .       0.000000692196369171142578125 soot:                O(1) = excellent
       ■■ overhead of a func call                  .      0.0000006407163143157958984375 soot:                O(1) = excellent
       ■■ make a dic with one item                 .        0.00000063958644866943359375 soot:                O(1) = excellent
       ■■ dict key lookup from single item dic     .      0.0000006313445568084716796875 soot:                O(1) = excellent
       ■■ make a dic with 4 items                  .        0.00000070595073699951171875 soot:                O(1) = excellent
       ■■ dict key lookup from 4 item dic          .       0.000000669296741485595703125 soot:                O(1) = excellent
      ■■■ create an async queue                    ,          0.000002254360198974609375 rice:                O(1) = excellent
      ■■■ add to an async queue                    ,       0.000001162513256072998046875 rice:                O(1) = excellent
       ■■ get from an async queue                  .        0.00000098680973052978515625 soot:                O(1) = excellent
      ■■■ build async event                        ,      0.0000011526954174041748046875 rice:                O(1) = excellent
       ■■ set async event                          .      0.0000008217403888702392578125 soot:                O(1) = excellent
       ■■ if x == n else ..                        .       0.000000623041629791259765625 soot:                O(1) = excellent
       ■■ n in list[5]                             .      0.0000007171633243560791015625 soot:                     O(n) = fair
       ■■ n in list[10]                            .         0.0000008075351715087890625 soot:                     O(n) = fair
      ■■■ n in list[100]                           ,          0.000002048152923583984375 rice:                     O(n) = fair
     ■■■■ n in list[1000]                          ;        0.00001435339450836181640625 peas:                     O(n) = fair
       ■■ str in list[5]                           .       0.000000672167301177978515625 soot:                     O(n) = fair
       ■■ str in list[10]                          .       0.000000686926364898681640625 soot:                     O(n) = fair
      ■■■ str in list[100]                         ,            0.0000012375030517578125 rice:                     O(n) = fair
      ■■■ ip bytes to ipaddress                    ,        0.00000233835124969482421875 rice:                O(1) = excellent
       ■■ store ip tuple in dic                    .      0.0000006325690746307373046875 soot:                O(1) = excellent
       ■■ 1k str to bytes                          .       0.000000738755702972412109375 soot:                     O(n) = fair
       ■■ 1k bytes to str                          .        0.00000084706211090087890625 soot:                     O(n) = fair
      ■■■ build stream sock                        ,          0.000006976604461669921875 rice:                O(1) = excellent
      ■■■ build dgram sock                         ,            0.0000029888153076171875 rice:                O(1) = excellent
     ■■■■ bind dgram sock                          ;          0.000010966777801513671875 peas:                O(1) = excellent
     ■■■■ send 100 b udp packets                   ;         0.0000289862155914306640625 peas:                O(1) = excellent
     ■■■■ send 1k udp packets                      ;            0.0000289020538330078125 peas:                O(1) = excellent
     ■■■■ send 10k udp packets                     ;         0.0000538151264190673828125 peas:                O(1) = excellent
  ■■■■■■■ dns lookup google.com (cached prob)      8    0.0802800655364990234375 tennis balls:                O(1) = excellent
  ■■■■■■■ tcp con to google                        8   0.02267887592315673828125 tennis balls:                O(1) = excellent
 ■■■■■■■■ tcp echo client                          #   0.1879781723022460937500 bowling balls:                O(1) = excellent
 ```

