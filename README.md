# python-benchmarking

I was interested in the performance cost of some common operations in Python. So here's some simple benchmarking results running on a 11th Gen Intel(R) Core(TM) i9-11980HK laptop. Run main.py to see how the results differ on your machine. You can get a sense of the relative cost of operations, anyway.

Open the raw file to view the data easier: https://raw.githubusercontent.com/robertsdotpm/python-benchmarking/main/README.md
```
 ■ atoms, ■■ soot, ■■■ rice, ■■■■ peas, ■■■■■ marbles, ■■■■■■ golf balls, ■■■■■■■ tennis balls, ■■■■■■■■ bowling balls

      ■■■ time()                                        0.0000012347133159637451171875 rice:                O(1) = excellent
       ■■ list append small int                          0.000000637637615203857421875 soot:                O(1) = excellent
       ■■ overhead of a func call                       0.0000006393167972564697265625 soot:                O(1) = excellent
       ■■ make a dic with one item                      0.0000007230675220489501953125 soot:                O(1) = excellent
       ■■ dict key lookup from single item dic            0.00000064790821075439453125 soot:                O(1) = excellent
       ■■ make a dic with 4 items                       0.0000006982791423797607421875 soot:                O(1) = excellent
       ■■ dict key lookup from 4 item dic               0.0000006570756435394287109375 soot:                O(1) = excellent
      ■■■ create an async queue                          0.000002245814800262451171875 rice:                O(1) = excellent
      ■■■ add to an async queue                         0.0000011237256526947021484375 rice:                O(1) = excellent
      ■■■ get from an async queue                        0.000001029907703399658203125 rice:                O(1) = excellent
      ■■■ build async event                               0.00000118044757843017578125 rice:                O(1) = excellent
       ■■ set async event                                     0.0000007658996582031250 soot:                O(1) = excellent
       ■■ if x == n else ..                             0.0000006013662815093994140625 soot:                O(1) = excellent
       ■■ n in list[5]                                  0.0000007066185474395751953125 soot:                     O(n) = fair
       ■■ n in list[10]                                 0.0000008140943050384521484375 soot:                     O(n) = fair
      ■■■ n in list[100]                                   0.0000019851398468017578125 rice:                     O(n) = fair
     ■■■■ n in list[1000]                                   0.000014376163482666015625 peas:                     O(n) = fair
       ■■ str in list[5]                                0.0000007002007961273193359375 soot:                     O(n) = fair
       ■■ str in list[10]                               0.0000007318937778472900390625 soot:                     O(n) = fair
      ■■■ str in list[100]                                0.00000120558643341064453125 rice:                     O(n) = fair
      ■■■ ip bytes to ipaddress                         0.0000023259594440460205078125 rice:                O(1) = excellent
       ■■ store ip tuple in dic                         0.0000006595852375030517578125 soot:                O(1) = excellent
       ■■ 1k str to bytes                                  0.0000006941089630126953125 soot:                     O(n) = fair
       ■■ 1k bytes to str                               0.0000008066885471343994140625 soot:                     O(n) = fair
      ■■■ build stream sock                                   0.0000039939880371093750 rice:                O(1) = excellent
      ■■■ build dgram sock                                   0.00000599384307861328125 rice:                O(1) = excellent
     ■■■■ bind dgram sock                                  0.0000159709453582763671875 peas:                O(1) = excellent
     ■■■■ send 100 b udp packets                           0.0000259697437286376953125 peas:                O(1) = excellent
     ■■■■ send 1k udp packets                              0.0000279529094696044921875 peas:                O(1) = excellent
     ■■■■ send 10k udp packets                               0.00004592800140380859375 peas:                O(1) = excellent
    ■■■■■ dns lookup google.com (cached prob)             0.00056226253509521484375 marbles:                O(1) = excellent
 ■■■■■■■■ tcp con to google                         0.12173469066619873046875 bowling balls:                O(1) = excellent
 ■■■■■■■■ tcp echo client                            0.1860974311828613281250 bowling balls:                O(1) = excellent
 ```

