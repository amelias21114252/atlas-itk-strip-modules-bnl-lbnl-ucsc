# category C BNL

#!/usr/bin/env python3

import re

RAW_TEXT = """


Module: SN20USBHX2002099
--------------------------------------------------------------------------------
Module total values: 442

File: SN20USBHX2002099_01.json
Stream: under
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_02.json
Stream: under
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_03.json
Stream: under
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_04.json
Stream: under
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_05.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_06.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_07.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_08.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_09.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_10.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_11.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_12.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_13.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_14.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_15.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_16.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_17.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_18.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_19.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_20.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_21.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_22.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_23.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_24.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_25.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_01.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_02.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_03.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_04.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_05.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_06.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_07.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_08.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_09.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_10.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_11.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_12.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_13.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_14.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_15.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_16.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_17.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_18.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_19.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_20.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_21.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_22.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_23.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_24.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002099_25.json
Stream: away
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2002301
--------------------------------------------------------------------------------
Module total values: 48

File: SN20USBHX2002301_02.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_03.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_04.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_05.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_06.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_07.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_08.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_09.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_10.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_11.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_12.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_13.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_14.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_15.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_16.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_17.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_18.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_19.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_20.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_21.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_22.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_23.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_24.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_25.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_02.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_03.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_04.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_05.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_06.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_07.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_08.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_09.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_10.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_11.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_12.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_13.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_14.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_15.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_16.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_17.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_18.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_19.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_20.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_21.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_22.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_23.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_24.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002301_25.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2002303
--------------------------------------------------------------------------------
Module total values: 42

File: SN20USBHX2002303_05.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_06.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_07.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_08.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_09.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_10.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_11.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_12.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_13.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_14.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_15.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_16.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_17.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_18.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_19.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_20.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_21.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_22.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_23.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_24.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_25.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_05.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_06.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_07.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_08.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_09.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_10.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_11.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_12.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_13.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_14.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_15.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_16.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_17.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_18.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_19.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_20.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_21.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_22.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_23.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_24.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002303_25.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2002587
--------------------------------------------------------------------------------
Module total values: 16

File: SN20USBHX2002587_22.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002587_23.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002587_24.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002587_25.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002587_22.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002587_23.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002587_24.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002587_25.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]


Module: SN20USBHX2002588
--------------------------------------------------------------------------------
Module total values: 60

File: SN20USBHX2002588_11.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_12.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_13.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_14.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_15.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_16.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_17.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_18.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_19.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_20.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_21.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_22.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_23.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_24.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_25.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_11.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_12.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_13.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_14.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_15.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_16.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_17.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_18.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_19.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_20.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_21.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_22.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_23.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_24.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002588_25.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]


Module: SN20USBHX2002592
--------------------------------------------------------------------------------
Module total values: 562

File: SN20USBHX2002592_01.json
Stream: under
Low count: 1
Low values: [376.9166259765625]

File: SN20USBHX2002592_02.json
Stream: under
Low count: 1
Low values: [335.12152099609375]

File: SN20USBHX2002592_03.json
Stream: under
Low count: 1
Low values: [323.7219543457031]

File: SN20USBHX2002592_04.json
Stream: under
Low count: 1
Low values: [366.59375]

File: SN20USBHX2002592_05.json
Stream: under
Low count: 1
Low values: [339.8546142578125]

File: SN20USBHX2002592_06.json
Stream: under
Low count: 1
Low values: [381.877685546875]

File: SN20USBHX2002592_07.json
Stream: under
Low count: 1
Low values: [337.5286865234375]

File: SN20USBHX2002592_08.json
Stream: under
Low count: 1
Low values: [376.7206115722656]

File: SN20USBHX2002592_09.json
Stream: under
Low count: 1
Low values: [333.2250061035156]

File: SN20USBHX2002592_10.json
Stream: under
Low count: 1
Low values: [374.8917541503906]

File: SN20USBHX2002592_11.json
Stream: under
Low count: 1
Low values: [333.59417724609375]

File: SN20USBHX2002592_12.json
Stream: under
Low count: 1
Low values: [367.99188232421875]

File: SN20USBHX2002592_13.json
Stream: under
Low count: 1
Low values: [335.23760986328125]

File: SN20USBHX2002592_14.json
Stream: under
Low count: 1
Low values: [374.4814758300781]

File: SN20USBHX2002592_15.json
Stream: under
Low count: 1
Low values: [332.6537170410156]

File: SN20USBHX2002592_16.json
Stream: under
Low count: 1
Low values: [385.3248596191406]

File: SN20USBHX2002592_17.json
Stream: under
Low count: 1
Low values: [339.89019775390625]

File: SN20USBHX2002592_18.json
Stream: under
Low count: 1
Low values: [374.9822082519531]

File: SN20USBHX2002592_19.json
Stream: under
Low count: 1
Low values: [336.0409240722656]

File: SN20USBHX2002592_20.json
Stream: under
Low count: 1
Low values: [374.1568603515625]

File: SN20USBHX2002592_21.json
Stream: under
Low count: 1
Low values: [344.1947937011719]

File: SN20USBHX2002592_22.json
Stream: under
Low count: 210
Low values: [0.0, 0.0, 307.4964599609375, 0.0, 484.3179626464844, 0.0, 0.11818188428878784, 0.0, 0.0, 0.0, 139.027587890625, 409.78460693359375, 0.0, 0.0, 0.0, 291.593017578125, 0.0, 0.0, 270.2583312988281, 0.0, 0.0, 0.0, 0.0, 189.32167053222656, 0.0, 0.0, 0.0, 0.028217531740665436, 0.0025024430360645056, 0.0, 0.0, 80.4842300415039, 113.31561279296875, 394.03375244140625, 0.0, 0.0, 498.0917053222656, 0.0, 0.0, 274.5360107421875, 236.1494140625, 0.0023285725619643927, 457.48828125, 0.0, 447.974365234375, 0.0, 7.543721675872803, 0.0037025813944637775, 0.0, 0.0, 0.0, 11.180647850036621, 0.05654311180114746, 208.54771423339844, 0.0, 450.2246398925781, 515.5545654296875, 0.0, 173.6005859375, 0.0, 407.19488525390625, 361.02685546875, 0.0, 0.0, 0.0, 0.04793122038245201, 0.11109306663274765, 0.0, 0.0, 4.908905506134033, 45.24326705932617, 584.22265625, 0.0, 457.0439147949219, 394.290283203125, 0.0, 593.9625854492188, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 214.21022033691406, 243.1955108642578, 336.7558898925781, 0.0, 370.1629638671875, 0.0, 0.0, 0.0, 435.92633056640625, 0.0, 0.0, 1.6201491355895996, 393.6839904785156, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 32.62594985961914, 0.0, 0.0, 0.0, 0.0, 425.26837158203125, 0.0, 0.0, 0.0, 492.986328125, 574.4417114257812, 486.66973876953125, 343.5789489746094, 577.1463623046875, 546.3202514648438, 588.8623046875, 594.6016845703125, 488.1178894042969, 592.9390258789062, 0.0, 18.461376190185547, 395.85198974609375, 441.9080505371094, 582.580078125, 341.74017333984375, 530.965087890625, 496.749267578125, 561.9257202148438, 0.0, 0.0, 373.7153015136719, 495.2207946777344, 330.2457580566406, 349.7161865234375, 0.0, 321.7257080078125, 507.807373046875, 562.2250366210938, 564.130615234375, 417.9915466308594, 469.9459533691406, 25.10860252380371, 153.49725341796875, 484.6988220214844, 357.6729736328125, 582.9429931640625, 479.48651123046875, 477.80859375, 500.275634765625, 476.50775146484375, 484.31103515625, 439.1365051269531, 456.9203186035156, 498.549560546875, 466.1294860839844, 575.1688232421875, 512.507568359375, 450.2720031738281, 535.3112182617188, 511.3630065917969, 456.1014099121094, 467.0870056152344, 455.8751220703125, 459.7196044921875, 535.3028564453125, 313.4619445800781, 518.5008544921875, 468.01556396484375, 580.2882080078125, 433.40087890625, 532.230712890625, 431.5215759277344, 511.1917724609375, 321.1384582519531, 0.0, 0.0, 379.38427734375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 64.57091522216797, 6.454570293426514, 363.79962158203125, 30.556224822998047, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 91.33678436279297, 343.4433288574219, 360.7939147949219]

File: SN20USBHX2002592_23.json
Stream: under
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 339.1548156738281]

File: SN20USBHX2002592_24.json
Stream: under
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 335.13372802734375]

File: SN20USBHX2002592_25.json
Stream: under
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 384.9148864746094]

File: SN20USBHX2002592_22.json
Stream: away
Low count: 304
Low values: [0.0, 0.0, 0.0, 0.0, 296.2464599609375, 0.0, 3.422079563140869, 0.0, 204.7001190185547, 0.0, 448.0463562011719, 0.0, 3.0429344177246094, 0.0, 0.0, 0.0, 6.791556358337402, 0.0, 0.0, 307.5281066894531, 0.0, 0.0, 0.0, 566.1350708007812, 0.0, 0.0, 0.0, 0.0, 363.6528625488281, 0.0, 0.0, 0.0, 0.0, 0.0, 9.996790885925293, 0.0, 302.245361328125, 0.0, 0.0, 0.0, 0.0, 340.5819091796875, 12.728286743164062, 207.84910583496094, 438.3942565917969, 0.0, 370.60382080078125, 0.0, 0.0, 599.0867309570312, 265.3096008300781, 0.0, 3.301715135574341, 0.0, 0.0009301140089519322, 0.023471413180232048, 0.0, 0.0, 0.045472402125597, 0.06892255693674088, 589.4457397460938, 116.81513977050781, 0.0027951919473707676, 568.0120849609375, 0.0, 0.0006546311196871102, 0.0, 0.0, 0.0, 230.9311065673828, 43.20072555541992, 0.0, 372.7017822265625, 0.0, 0.0, 151.62132263183594, 7.403024673461914, 281.3215637207031, 483.5285949707031, 290.0122375488281, 0.0, 9.186744689941406, 0.0, 0.0, 0.0, 0.0, 0.0, 505.7428283691406, 0.0, 0.0, 0.0, 0.0, 350.62286376953125, 0.0, 373.27911376953125, 0.0, 2.552760362625122, 526.9393310546875, 0.0, 0.0, 0.0, 2.8230159282684326, 0.0, 0.0, 0.0, 303.84857177734375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 367.8978271484375, 0.0, 0.0, 0.0, 448.8602294921875, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 420.288330078125, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 174.31057739257812, 0.0, 463.7690734863281, 470.0368347167969, 454.3843994140625, 468.0726318359375, 451.61492919921875, 328.01885986328125, 460.8150329589844, 460.3802185058594, 451.64166259765625, 470.19195556640625, 462.2911071777344, 475.6004333496094, 0.0, 473.4491882324219, 460.4899597167969, 105.96197509765625, 453.2286376953125, 465.62335205078125, 470.391357421875, 336.1478576660156, 351.1747741699219, 447.46038818359375, 484.4723815917969, 0.0, 0.0, 204.0905303955078, 464.51544189453125, 449.5724792480469, 442.82257080078125, 441.3193359375, 480.0684814453125, 455.58282470703125, 473.358642578125, 473.5082092285156, 0.0, 456.5700378417969, 446.92840576171875, 441.0097351074219, 194.91583251953125, 432.7479553222656, 445.97406005859375, 447.4288024902344, 447.21160888671875, 447.8251037597656, 570.564697265625, 448.4141540527344, 468.22314453125, 469.31292724609375, 379.64093017578125, 560.5833740234375, 497.9767150878906, 522.6405029296875, 334.5940246582031, 502.7618103027344, 543.328369140625, 341.5652770996094, 427.2577819824219, 448.47747802734375, 473.528564453125, 457.09735107421875, 586.2420654296875, 246.6304473876953, 243.19566345214844, 518.1409912109375, 432.90673828125, 447.57220458984375, 481.01324462890625, 449.4319152832031, 457.1335754394531, 434.99884033203125, 455.24365234375, 438.7598571777344, 398.8184509277344, 436.8266906738281, 438.05084228515625, 451.4226379394531, 440.27349853515625, 442.4407653808594, 338.0158996582031, 292.6605224609375, 436.6083984375, 444.25689697265625, 453.2253723144531, 535.2274780273438, 441.2948303222656, 438.9992370605469, 444.6326904296875, 427.3379821777344, 442.3604431152344, 420.48895263671875, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 374.9200744628906, 0.0, 423.713623046875, 0.0, 0.0, 0.0, 22.26203155517578, 552.2462158203125, 0.0, 415.61199951171875, 0.0, 0.0, 0.0, 549.1661376953125, 158.06431579589844, 0.0, 111.52224731445312, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 459.9185485839844, 0.0, 0.0, 66.74771118164062, 0.0, 0.0, 0.0, 0.06418773531913757, 0.024950845167040825, 563.79443359375, 0.0, 0.0, 424.1065979003906, 0.0, 375.1783752441406, 260.2541198730469, 0.0, 271.39208984375, 432.12591552734375, 0.0, 0.0, 0.0, 0.0, 479.9234924316406, 468.993408203125, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 362.0752868652344]

File: SN20USBHX2002592_23.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002592_24.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002592_25.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2002593
--------------------------------------------------------------------------------
Module total values: 10

File: SN20USBHX2002593_21.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002593_22.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002593_23.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002593_24.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002593_25.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]


Module: SN20USBHX2002594
--------------------------------------------------------------------------------
Module total values: 110

File: SN20USBHX2002594_01.json
Stream: under
Low count: 4
Low values: [385.21026611328125, 373.73150634765625, 374.6399841308594, 369.6800231933594]

File: SN20USBHX2002594_02.json
Stream: under
Low count: 4
Low values: [362.240234375, 333.5816345214844, 350.1844177246094, 341.38818359375]

File: SN20USBHX2002594_03.json
Stream: under
Low count: 4
Low values: [355.21099853515625, 348.6365051269531, 341.30352783203125, 357.9775390625]

File: SN20USBHX2002594_04.json
Stream: under
Low count: 4
Low values: [379.3785705566406, 378.5726013183594, 386.0939636230469, 364.9965515136719]

File: SN20USBHX2002594_05.json
Stream: under
Low count: 4
Low values: [348.0806579589844, 348.2672119140625, 338.5586853027344, 330.6883850097656]

File: SN20USBHX2002594_06.json
Stream: under
Low count: 4
Low values: [381.40240478515625, 374.36767578125, 374.8807067871094, 366.0714111328125]

File: SN20USBHX2002594_07.json
Stream: under
Low count: 4
Low values: [347.9287414550781, 337.8755798339844, 352.557373046875, 347.8238220214844]

File: SN20USBHX2002594_08.json
Stream: under
Low count: 4
Low values: [359.6143798828125, 372.2395935058594, 369.5702819824219, 374.0065002441406]

File: SN20USBHX2002594_09.json
Stream: under
Low count: 4
Low values: [346.2488708496094, 356.1334228515625, 367.76092529296875, 358.440185546875]

File: SN20USBHX2002594_10.json
Stream: under
Low count: 4
Low values: [367.4663391113281, 369.72821044921875, 383.2418212890625, 377.17047119140625]

File: SN20USBHX2002594_11.json
Stream: under
Low count: 4
Low values: [356.4283447265625, 334.6320495605469, 354.347900390625, 341.44830322265625]

File: SN20USBHX2002594_12.json
Stream: under
Low count: 4
Low values: [384.1120300292969, 383.6446838378906, 376.4271545410156, 382.1260986328125]

File: SN20USBHX2002594_13.json
Stream: under
Low count: 4
Low values: [343.1730651855469, 361.56756591796875, 353.2434997558594, 348.94403076171875]

File: SN20USBHX2002594_14.json
Stream: under
Low count: 4
Low values: [382.8467712402344, 379.3466491699219, 381.78485107421875, 375.4825134277344]

File: SN20USBHX2002594_15.json
Stream: under
Low count: 4
Low values: [361.9762268066406, 351.8753967285156, 348.3381652832031, 334.7243347167969]

File: SN20USBHX2002594_16.json
Stream: under
Low count: 4
Low values: [372.6873779296875, 383.1199951171875, 375.6300048828125, 376.6070251464844]

File: SN20USBHX2002594_17.json
Stream: under
Low count: 4
Low values: [355.5508728027344, 340.7869873046875, 350.6882019042969, 342.6788024902344]

File: SN20USBHX2002594_18.json
Stream: under
Low count: 4
Low values: [382.722900390625, 385.92657470703125, 377.6437072753906, 366.48907470703125]

File: SN20USBHX2002594_19.json
Stream: under
Low count: 4
Low values: [337.7152404785156, 356.91845703125, 348.4781188964844, 340.95208740234375]

File: SN20USBHX2002594_20.json
Stream: under
Low count: 4
Low values: [387.0834045410156, 367.87969970703125, 391.5545654296875, 376.4215393066406]

File: SN20USBHX2002594_21.json
Stream: under
Low count: 6
Low values: [355.4406433105469, 354.7424011230469, 353.0682373046875, 356.1847839355469, 0.0, 0.0]

File: SN20USBHX2002594_22.json
Stream: under
Low count: 6
Low values: [373.3351745605469, 358.0534973144531, 369.0184631347656, 373.5101013183594, 0.0, 0.0]

File: SN20USBHX2002594_23.json
Stream: under
Low count: 6
Low values: [323.6888122558594, 360.8050537109375, 349.33355712890625, 343.29400634765625, 0.0, 0.0]

File: SN20USBHX2002594_24.json
Stream: under
Low count: 6
Low values: [349.0455017089844, 351.74835205078125, 349.9601135253906, 341.9459533691406, 0.0, 0.0]

File: SN20USBHX2002594_25.json
Stream: under
Low count: 6
Low values: [375.6607360839844, 374.6891174316406, 388.6921081542969, 369.61529541015625, 0.0, 0.0]


Module: SN20USBHX2002598
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2002598_01.json
Stream: under
Low count: 1
Low values: [387.7159118652344]

File: SN20USBHX2002598_02.json
Stream: under
Low count: 1
Low values: [333.7998962402344]

File: SN20USBHX2002598_03.json
Stream: under
Low count: 1
Low values: [358.828125]

File: SN20USBHX2002598_04.json
Stream: under
Low count: 1
Low values: [382.41741943359375]

File: SN20USBHX2002598_05.json
Stream: under
Low count: 1
Low values: [343.34539794921875]

File: SN20USBHX2002598_06.json
Stream: under
Low count: 1
Low values: [380.66412353515625]

File: SN20USBHX2002598_07.json
Stream: under
Low count: 1
Low values: [339.08001708984375]

File: SN20USBHX2002598_08.json
Stream: under
Low count: 1
Low values: [373.77227783203125]

File: SN20USBHX2002598_09.json
Stream: under
Low count: 1
Low values: [341.2684020996094]

File: SN20USBHX2002598_10.json
Stream: under
Low count: 1
Low values: [379.6276550292969]

File: SN20USBHX2002598_11.json
Stream: under
Low count: 1
Low values: [348.93206787109375]

File: SN20USBHX2002598_12.json
Stream: under
Low count: 1
Low values: [375.47833251953125]

File: SN20USBHX2002598_13.json
Stream: under
Low count: 1
Low values: [337.78125]

File: SN20USBHX2002598_14.json
Stream: under
Low count: 1
Low values: [385.94793701171875]

File: SN20USBHX2002598_15.json
Stream: under
Low count: 1
Low values: [349.833251953125]

File: SN20USBHX2002598_16.json
Stream: under
Low count: 1
Low values: [396.4549255371094]

File: SN20USBHX2002598_17.json
Stream: under
Low count: 1
Low values: [342.1222839355469]

File: SN20USBHX2002598_18.json
Stream: under
Low count: 1
Low values: [384.89202880859375]

File: SN20USBHX2002598_19.json
Stream: under
Low count: 1
Low values: [342.7579345703125]

File: SN20USBHX2002598_20.json
Stream: under
Low count: 1
Low values: [380.8211364746094]

File: SN20USBHX2002598_21.json
Stream: under
Low count: 1
Low values: [341.4438781738281]

File: SN20USBHX2002598_22.json
Stream: under
Low count: 1
Low values: [397.66943359375]

File: SN20USBHX2002598_23.json
Stream: under
Low count: 1
Low values: [346.8270568847656]

File: SN20USBHX2002598_24.json
Stream: under
Low count: 1
Low values: [333.2058410644531]

File: SN20USBHX2002598_25.json
Stream: under
Low count: 1
Low values: [383.59161376953125]


Module: SN20USBHX2002627
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2002627_01.json
Stream: under
Low count: 1
Low values: [386.87237548828125]

File: SN20USBHX2002627_02.json
Stream: under
Low count: 1
Low values: [322.70660400390625]

File: SN20USBHX2002627_03.json
Stream: under
Low count: 1
Low values: [340.49591064453125]

File: SN20USBHX2002627_04.json
Stream: under
Low count: 1
Low values: [383.96435546875]

File: SN20USBHX2002627_05.json
Stream: under
Low count: 1
Low values: [338.11944580078125]

File: SN20USBHX2002627_06.json
Stream: under
Low count: 1
Low values: [394.59600830078125]

File: SN20USBHX2002627_07.json
Stream: under
Low count: 1
Low values: [338.26556396484375]

File: SN20USBHX2002627_08.json
Stream: under
Low count: 1
Low values: [399.20477294921875]

File: SN20USBHX2002627_09.json
Stream: under
Low count: 1
Low values: [343.6694641113281]

File: SN20USBHX2002627_10.json
Stream: under
Low count: 1
Low values: [381.07452392578125]

File: SN20USBHX2002627_11.json
Stream: under
Low count: 1
Low values: [337.2077331542969]

File: SN20USBHX2002627_12.json
Stream: under
Low count: 1
Low values: [387.8922119140625]

File: SN20USBHX2002627_13.json
Stream: under
Low count: 1
Low values: [332.61053466796875]

File: SN20USBHX2002627_14.json
Stream: under
Low count: 1
Low values: [376.91632080078125]

File: SN20USBHX2002627_15.json
Stream: under
Low count: 1
Low values: [343.49658203125]

File: SN20USBHX2002627_16.json
Stream: under
Low count: 1
Low values: [376.88079833984375]

File: SN20USBHX2002627_17.json
Stream: under
Low count: 1
Low values: [349.4642639160156]

File: SN20USBHX2002627_18.json
Stream: under
Low count: 1
Low values: [380.1692810058594]

File: SN20USBHX2002627_19.json
Stream: under
Low count: 1
Low values: [338.02642822265625]

File: SN20USBHX2002627_20.json
Stream: under
Low count: 1
Low values: [373.9139404296875]

File: SN20USBHX2002627_21.json
Stream: under
Low count: 1
Low values: [354.5751647949219]

File: SN20USBHX2002627_22.json
Stream: under
Low count: 1
Low values: [376.34552001953125]

File: SN20USBHX2002627_23.json
Stream: under
Low count: 1
Low values: [340.66192626953125]

File: SN20USBHX2002627_24.json
Stream: under
Low count: 1
Low values: [343.882080078125]

File: SN20USBHX2002627_25.json
Stream: under
Low count: 1
Low values: [393.7532653808594]


Module: SN20USBHX2002652
--------------------------------------------------------------------------------
Module total values: 166

File: SN20USBHX2002652_05.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002652_06.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002652_07.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_08.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_09.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_10.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_11.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_12.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_13.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_14.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_15.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_16.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_17.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_18.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_19.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_20.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_21.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_22.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_23.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_24.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_25.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_02.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_03.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_04.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002652_05.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002652_06.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002652_07.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_08.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_09.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_10.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_11.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_12.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_13.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_14.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_15.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_16.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_17.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_18.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_19.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_20.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_21.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_22.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_23.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_24.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002652_25.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2002653
--------------------------------------------------------------------------------
Module total values: 138

File: SN20USBHX2002653_13.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_14.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_15.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_16.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_17.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_18.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_19.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_20.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_21.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_22.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_23.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_24.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_25.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_13.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002653_14.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002653_15.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002653_16.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002653_17.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_18.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_19.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_20.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_21.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_22.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_23.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_24.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002653_25.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2002654
--------------------------------------------------------------------------------
Module total values: 18

File: SN20USBHX2002654_17.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_18.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_19.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_20.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_21.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_22.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_23.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_24.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_25.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_17.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_18.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_19.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_20.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_21.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_22.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_23.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_24.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002654_25.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2002655
--------------------------------------------------------------------------------
Module total values: 232

File: SN20USBHX2002655_02.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002655_03.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_04.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_05.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_06.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_07.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_08.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_09.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_10.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_11.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_12.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_13.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_14.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_15.json
Stream: under
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_16.json
Stream: under
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_17.json
Stream: under
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_18.json
Stream: under
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_19.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_20.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_21.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_22.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_23.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_24.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_25.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_03.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002655_04.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002655_05.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002655_06.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002655_07.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002655_08.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002655_09.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_10.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_11.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_12.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_13.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_14.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_15.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_16.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_17.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_18.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_19.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_20.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_21.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_22.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_23.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_24.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002655_25.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2002656
--------------------------------------------------------------------------------
Module total values: 92

File: SN20USBHX2002656_01.json
Stream: under
Low count: 2
Low values: [379.4102478027344, 377.55230712890625]

File: SN20USBHX2002656_02.json
Stream: under
Low count: 2
Low values: [320.0478820800781, 343.3160095214844]

File: SN20USBHX2002656_03.json
Stream: under
Low count: 2
Low values: [343.4026184082031, 347.79833984375]

File: SN20USBHX2002656_04.json
Stream: under
Low count: 2
Low values: [374.38287353515625, 366.5093688964844]

File: SN20USBHX2002656_05.json
Stream: under
Low count: 2
Low values: [339.1021728515625, 354.56884765625]

File: SN20USBHX2002656_06.json
Stream: under
Low count: 2
Low values: [363.1334533691406, 389.0586853027344]

File: SN20USBHX2002656_07.json
Stream: under
Low count: 2
Low values: [347.2503356933594, 337.7398681640625]

File: SN20USBHX2002656_08.json
Stream: under
Low count: 2
Low values: [387.8669738769531, 380.470703125]

File: SN20USBHX2002656_09.json
Stream: under
Low count: 2
Low values: [352.18389892578125, 342.8469543457031]

File: SN20USBHX2002656_10.json
Stream: under
Low count: 2
Low values: [384.0228271484375, 395.3269348144531]

File: SN20USBHX2002656_11.json
Stream: under
Low count: 2
Low values: [348.5596008300781, 352.5171813964844]

File: SN20USBHX2002656_12.json
Stream: under
Low count: 2
Low values: [370.6483154296875, 370.94964599609375]

File: SN20USBHX2002656_13.json
Stream: under
Low count: 2
Low values: [339.24322509765625, 332.53619384765625]

File: SN20USBHX2002656_14.json
Stream: under
Low count: 2
Low values: [384.76873779296875, 383.39337158203125]

File: SN20USBHX2002656_15.json
Stream: under
Low count: 2
Low values: [344.4147644042969, 341.5358581542969]

File: SN20USBHX2002656_16.json
Stream: under
Low count: 2
Low values: [372.8927001953125, 378.6304016113281]

File: SN20USBHX2002656_17.json
Stream: under
Low count: 4
Low values: [331.69158935546875, 340.72412109375, 0.0, 0.0]

File: SN20USBHX2002656_18.json
Stream: under
Low count: 4
Low values: [362.8603820800781, 373.0765075683594, 0.0, 0.0]

File: SN20USBHX2002656_19.json
Stream: under
Low count: 4
Low values: [345.4410705566406, 343.4666748046875, 0.0, 0.0]

File: SN20USBHX2002656_20.json
Stream: under
Low count: 4
Low values: [386.7333984375, 367.6443176269531, 0.0, 0.0]

File: SN20USBHX2002656_21.json
Stream: under
Low count: 7
Low values: [0.0, 0.0, 330.21923828125, 342.7721252441406, 0.0, 0.0, 0.0]

File: SN20USBHX2002656_22.json
Stream: under
Low count: 7
Low values: [0.0, 0.0, 383.4088439941406, 390.8680114746094, 0.0, 0.0, 0.0]

File: SN20USBHX2002656_23.json
Stream: under
Low count: 7
Low values: [0.0, 0.0, 332.6089172363281, 351.1954650878906, 0.0, 0.0, 0.0]

File: SN20USBHX2002656_24.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 337.1288757324219, 345.63568115234375, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002656_25.json
Stream: under
Low count: 9
Low values: [0.0, 0.0, 379.9583740234375, 382.7550048828125, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002656_21.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002656_22.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002656_23.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002656_24.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002656_25.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2002677
--------------------------------------------------------------------------------
Module total values: 272

File: SN20USBHX2002677_07.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002677_08.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002677_09.json
Stream: under
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_10.json
Stream: under
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_11.json
Stream: under
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_12.json
Stream: under
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_13.json
Stream: under
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_14.json
Stream: under
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_15.json
Stream: under
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_16.json
Stream: under
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_17.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_18.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_19.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_20.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_21.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_22.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_23.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_24.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_25.json
Stream: under
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_07.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_08.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_09.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_10.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_11.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_12.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_13.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_14.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_15.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_16.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_17.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_18.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_19.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_20.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_21.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_22.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_23.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_24.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002677_25.json
Stream: away
Low count: 8
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2002678
--------------------------------------------------------------------------------
Module total values: 52

File: SN20USBHX2002678_11.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_12.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_13.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_14.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_15.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002678_16.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002678_17.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002678_18.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002678_19.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002678_20.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002678_21.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002678_22.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002678_23.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002678_24.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002678_25.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002678_11.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_12.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_13.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_14.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_15.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_16.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_17.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_18.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_19.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_20.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_21.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_22.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_23.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_24.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002678_25.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2002679
--------------------------------------------------------------------------------
Module total values: 128

File: SN20USBHX2002679_07.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_08.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_09.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_10.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_11.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_12.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_13.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_14.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_15.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_16.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_17.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_18.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_19.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_20.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_21.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_22.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_23.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002679_24.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002679_25.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002679_02.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002679_03.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002679_04.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002679_05.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002679_06.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002679_07.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002679_08.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002679_09.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_10.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_11.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_12.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_13.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_14.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_15.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_16.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_17.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_18.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_19.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_20.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_21.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_22.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_23.json
Stream: away
Low count: 5
Low values: [0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_24.json
Stream: away
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002679_25.json
Stream: away
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2002680
--------------------------------------------------------------------------------
Module total values: 138

File: SN20USBHX2002680_17.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002680_18.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002680_19.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002680_20.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002680_21.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002680_22.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002680_23.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002680_24.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002680_25.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002680_01.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_02.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_03.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_04.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_05.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_06.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_07.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_08.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_09.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_10.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_11.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_12.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_13.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_14.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_15.json
Stream: away
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_16.json
Stream: away
Low count: 6
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_17.json
Stream: away
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_18.json
Stream: away
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_19.json
Stream: away
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_20.json
Stream: away
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_21.json
Stream: away
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_22.json
Stream: away
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_23.json
Stream: away
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_24.json
Stream: away
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002680_25.json
Stream: away
Low count: 7
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2002684
--------------------------------------------------------------------------------
Module total values: 18

File: SN20USBHX2002684_17.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002684_18.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002684_19.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002684_20.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002684_21.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002684_22.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002684_23.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002684_24.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002684_25.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]


Module: SN20USBHX2002685
--------------------------------------------------------------------------------
Module total values: 46

File: SN20USBHX2002685_03.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_04.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_05.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_06.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_07.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_08.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_09.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_10.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_11.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_12.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_13.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_14.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_15.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_16.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_17.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_18.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_19.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_20.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_21.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_22.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_23.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_24.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_25.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_03.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_04.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_05.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_06.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_07.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_08.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_09.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_10.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_11.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_12.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_13.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_14.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_15.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_16.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_17.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_18.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_19.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_20.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_21.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_22.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_23.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_24.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002685_25.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2002691
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2002691_01.json
Stream: under
Low count: 1
Low values: [369.2320556640625]

File: SN20USBHX2002691_02.json
Stream: under
Low count: 1
Low values: [319.4494934082031]

File: SN20USBHX2002691_03.json
Stream: under
Low count: 1
Low values: [326.04736328125]

File: SN20USBHX2002691_04.json
Stream: under
Low count: 1
Low values: [384.0440673828125]

File: SN20USBHX2002691_05.json
Stream: under
Low count: 1
Low values: [327.6197814941406]

File: SN20USBHX2002691_06.json
Stream: under
Low count: 1
Low values: [396.2476806640625]

File: SN20USBHX2002691_07.json
Stream: under
Low count: 1
Low values: [330.91802978515625]

File: SN20USBHX2002691_08.json
Stream: under
Low count: 1
Low values: [386.77386474609375]

File: SN20USBHX2002691_09.json
Stream: under
Low count: 1
Low values: [329.8138427734375]

File: SN20USBHX2002691_10.json
Stream: under
Low count: 1
Low values: [382.0418701171875]

File: SN20USBHX2002691_11.json
Stream: under
Low count: 1
Low values: [331.2413024902344]

File: SN20USBHX2002691_12.json
Stream: under
Low count: 1
Low values: [361.4172668457031]

File: SN20USBHX2002691_13.json
Stream: under
Low count: 1
Low values: [331.4938659667969]

File: SN20USBHX2002691_14.json
Stream: under
Low count: 1
Low values: [375.3954772949219]

File: SN20USBHX2002691_15.json
Stream: under
Low count: 1
Low values: [339.1162414550781]

File: SN20USBHX2002691_16.json
Stream: under
Low count: 1
Low values: [385.96795654296875]

File: SN20USBHX2002691_17.json
Stream: under
Low count: 1
Low values: [346.8785705566406]

File: SN20USBHX2002691_18.json
Stream: under
Low count: 1
Low values: [371.8212890625]

File: SN20USBHX2002691_19.json
Stream: under
Low count: 1
Low values: [326.3542785644531]

File: SN20USBHX2002691_20.json
Stream: under
Low count: 1
Low values: [394.7746276855469]

File: SN20USBHX2002691_21.json
Stream: under
Low count: 1
Low values: [340.46875]

File: SN20USBHX2002691_22.json
Stream: under
Low count: 1
Low values: [368.25390625]

File: SN20USBHX2002691_23.json
Stream: under
Low count: 1
Low values: [335.0682067871094]

File: SN20USBHX2002691_24.json
Stream: under
Low count: 1
Low values: [327.6119079589844]

File: SN20USBHX2002691_25.json
Stream: under
Low count: 1
Low values: [375.4156188964844]


Module: SN20USBHX2002692
--------------------------------------------------------------------------------
Module total values: 44

File: SN20USBHX2002692_05.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_06.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_07.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_08.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_09.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_10.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_11.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_12.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_13.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_14.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_15.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_16.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_17.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_18.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_19.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_20.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_21.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_22.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_23.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_24.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002692_25.json
Stream: under
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002692_25.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2002695
--------------------------------------------------------------------------------
Module total values: 42

File: SN20USBHX2002695_05.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_06.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_07.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_08.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_09.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_10.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_11.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_12.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_13.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_14.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_15.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_16.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_17.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_18.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_19.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_20.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_21.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_22.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_23.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_24.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_25.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_05.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_06.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_07.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_08.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_09.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_10.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_11.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_12.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_13.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_14.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_15.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_16.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_17.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_18.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_19.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_20.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_21.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_22.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_23.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_24.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2002695_25.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2002712
--------------------------------------------------------------------------------
Module total values: 72

File: SN20USBHX2002712_08.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_09.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_10.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_11.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_12.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_13.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_14.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_15.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_16.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_17.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_18.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_19.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_20.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_21.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_22.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_23.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_24.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002712_25.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2002713
--------------------------------------------------------------------------------
Module total values: 38

File: SN20USBHX2002713_07.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_08.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_09.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_10.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_11.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_12.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_13.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_14.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_15.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_16.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_17.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_18.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_19.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_20.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_21.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_22.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_23.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_24.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002713_25.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]


Module: SN20USBHX2002938
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2002938_01.json
Stream: under
Low count: 1
Low values: [375.3376159667969]

File: SN20USBHX2002938_02.json
Stream: under
Low count: 1
Low values: [336.55047607421875]

File: SN20USBHX2002938_03.json
Stream: under
Low count: 1
Low values: [345.460693359375]

File: SN20USBHX2002938_04.json
Stream: under
Low count: 1
Low values: [391.9453125]

File: SN20USBHX2002938_05.json
Stream: under
Low count: 1
Low values: [331.4820556640625]

File: SN20USBHX2002938_06.json
Stream: under
Low count: 1
Low values: [358.9056701660156]

File: SN20USBHX2002938_07.json
Stream: under
Low count: 1
Low values: [351.79022216796875]

File: SN20USBHX2002938_08.json
Stream: under
Low count: 1
Low values: [364.7907409667969]

File: SN20USBHX2002938_09.json
Stream: under
Low count: 1
Low values: [329.871826171875]

File: SN20USBHX2002938_10.json
Stream: under
Low count: 1
Low values: [383.3154296875]

File: SN20USBHX2002938_11.json
Stream: under
Low count: 1
Low values: [342.2851867675781]

File: SN20USBHX2002938_12.json
Stream: under
Low count: 1
Low values: [391.78759765625]

File: SN20USBHX2002938_13.json
Stream: under
Low count: 1
Low values: [338.66033935546875]

File: SN20USBHX2002938_14.json
Stream: under
Low count: 1
Low values: [379.5426940917969]

File: SN20USBHX2002938_15.json
Stream: under
Low count: 1
Low values: [326.00360107421875]

File: SN20USBHX2002938_16.json
Stream: under
Low count: 1
Low values: [389.8060607910156]

File: SN20USBHX2002938_17.json
Stream: under
Low count: 1
Low values: [330.53228759765625]

File: SN20USBHX2002938_18.json
Stream: under
Low count: 1
Low values: [379.43408203125]

File: SN20USBHX2002938_19.json
Stream: under
Low count: 1
Low values: [339.76800537109375]

File: SN20USBHX2002938_20.json
Stream: under
Low count: 1
Low values: [374.4273681640625]

File: SN20USBHX2002938_21.json
Stream: under
Low count: 1
Low values: [340.3414001464844]

File: SN20USBHX2002938_22.json
Stream: under
Low count: 1
Low values: [381.2370300292969]

File: SN20USBHX2002938_23.json
Stream: under
Low count: 1
Low values: [335.9787902832031]

File: SN20USBHX2002938_24.json
Stream: under
Low count: 1
Low values: [342.1583251953125]

File: SN20USBHX2002938_25.json
Stream: under
Low count: 1
Low values: [375.3074951171875]


Module: SN20USBHX2002940
--------------------------------------------------------------------------------
Module total values: 56

File: SN20USBHX2002940_11.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002940_12.json
Stream: under
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002940_13.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002940_14.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002940_15.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002940_16.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002940_17.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002940_18.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002940_19.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002940_20.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002940_21.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002940_22.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002940_23.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002940_24.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002940_25.json
Stream: under
Low count: 4
Low values: [0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2002943
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2002943_01.json
Stream: away
Low count: 1
Low values: [377.7726745605469]

File: SN20USBHX2002943_02.json
Stream: away
Low count: 1
Low values: [354.2491760253906]

File: SN20USBHX2002943_03.json
Stream: away
Low count: 1
Low values: [351.5348205566406]

File: SN20USBHX2002943_04.json
Stream: away
Low count: 1
Low values: [381.572265625]

File: SN20USBHX2002943_05.json
Stream: away
Low count: 1
Low values: [333.46063232421875]

File: SN20USBHX2002943_06.json
Stream: away
Low count: 1
Low values: [378.8609313964844]

File: SN20USBHX2002943_07.json
Stream: away
Low count: 1
Low values: [333.9211730957031]

File: SN20USBHX2002943_08.json
Stream: away
Low count: 1
Low values: [374.9405212402344]

File: SN20USBHX2002943_09.json
Stream: away
Low count: 1
Low values: [351.9991760253906]

File: SN20USBHX2002943_10.json
Stream: away
Low count: 1
Low values: [381.20574951171875]

File: SN20USBHX2002943_11.json
Stream: away
Low count: 1
Low values: [329.61187744140625]

File: SN20USBHX2002943_12.json
Stream: away
Low count: 1
Low values: [389.039794921875]

File: SN20USBHX2002943_13.json
Stream: away
Low count: 1
Low values: [333.24273681640625]

File: SN20USBHX2002943_14.json
Stream: away
Low count: 1
Low values: [384.33917236328125]

File: SN20USBHX2002943_15.json
Stream: away
Low count: 1
Low values: [326.85009765625]

File: SN20USBHX2002943_16.json
Stream: away
Low count: 1
Low values: [375.541259765625]

File: SN20USBHX2002943_17.json
Stream: away
Low count: 1
Low values: [328.52362060546875]

File: SN20USBHX2002943_18.json
Stream: away
Low count: 1
Low values: [396.9159851074219]

File: SN20USBHX2002943_19.json
Stream: away
Low count: 1
Low values: [341.64013671875]

File: SN20USBHX2002943_20.json
Stream: away
Low count: 1
Low values: [384.11468505859375]

File: SN20USBHX2002943_21.json
Stream: away
Low count: 1
Low values: [345.4071044921875]

File: SN20USBHX2002943_22.json
Stream: away
Low count: 1
Low values: [372.0532531738281]

File: SN20USBHX2002943_23.json
Stream: away
Low count: 1
Low values: [358.12591552734375]

File: SN20USBHX2002943_24.json
Stream: away
Low count: 1
Low values: [333.11767578125]

File: SN20USBHX2002943_25.json
Stream: away
Low count: 1
Low values: [382.4371032714844]


Module: SN20USBHX2002957
--------------------------------------------------------------------------------
Module total values: 282

File: SN20USBHX2002957_01.json
Stream: under
Low count: 1
Low values: [367.97283935546875]

File: SN20USBHX2002957_02.json
Stream: under
Low count: 1
Low values: [337.7287292480469]

File: SN20USBHX2002957_03.json
Stream: under
Low count: 1
Low values: [339.0854797363281]

File: SN20USBHX2002957_04.json
Stream: under
Low count: 1
Low values: [373.4632263183594]

File: SN20USBHX2002957_05.json
Stream: under
Low count: 1
Low values: [349.8678283691406]

File: SN20USBHX2002957_06.json
Stream: under
Low count: 1
Low values: [364.6476135253906]

File: SN20USBHX2002957_07.json
Stream: under
Low count: 1
Low values: [341.28814697265625]

File: SN20USBHX2002957_08.json
Stream: under
Low count: 1
Low values: [375.9397888183594]

File: SN20USBHX2002957_09.json
Stream: under
Low count: 1
Low values: [329.8074035644531]

File: SN20USBHX2002957_10.json
Stream: under
Low count: 1
Low values: [385.36126708984375]

File: SN20USBHX2002957_11.json
Stream: under
Low count: 1
Low values: [345.55975341796875]

File: SN20USBHX2002957_12.json
Stream: under
Low count: 1
Low values: [368.35894775390625]

File: SN20USBHX2002957_13.json
Stream: under
Low count: 1
Low values: [337.0871887207031]

File: SN20USBHX2002957_14.json
Stream: under
Low count: 1
Low values: [365.9167785644531]

File: SN20USBHX2002957_15.json
Stream: under
Low count: 1
Low values: [344.263916015625]

File: SN20USBHX2002957_16.json
Stream: under
Low count: 1
Low values: [369.0524597167969]

File: SN20USBHX2002957_17.json
Stream: under
Low count: 1
Low values: [339.0566711425781]

File: SN20USBHX2002957_18.json
Stream: under
Low count: 1
Low values: [367.47711181640625]

File: SN20USBHX2002957_19.json
Stream: under
Low count: 1
Low values: [332.8476257324219]

File: SN20USBHX2002957_20.json
Stream: under
Low count: 1
Low values: [366.74395751953125]

File: SN20USBHX2002957_21.json
Stream: under
Low count: 1
Low values: [335.9456481933594]

File: SN20USBHX2002957_22.json
Stream: under
Low count: 104
Low values: [101.0085678100586, 0.0, 0.0, 0.0, 0.0, 0.0, 597.5215454101562, 558.3040771484375, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 379.2411804199219, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002957_23.json
Stream: under
Low count: 1
Low values: [339.29052734375]

File: SN20USBHX2002957_24.json
Stream: under
Low count: 1
Low values: [340.90576171875]

File: SN20USBHX2002957_25.json
Stream: under
Low count: 1
Low values: [390.4936218261719]

File: SN20USBHX2002957_22.json
Stream: away
Low count: 154
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 103.40459442138672, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2002960
--------------------------------------------------------------------------------
Module total values: 50

File: SN20USBHX2002960_01.json
Stream: away
Low count: 2
Low values: [388.1717529296875, 371.0157775878906]

File: SN20USBHX2002960_02.json
Stream: away
Low count: 2
Low values: [334.4687805175781, 323.2434387207031]

File: SN20USBHX2002960_03.json
Stream: away
Low count: 2
Low values: [347.2294616699219, 340.6602783203125]

File: SN20USBHX2002960_04.json
Stream: away
Low count: 2
Low values: [390.951904296875, 377.73968505859375]

File: SN20USBHX2002960_05.json
Stream: away
Low count: 2
Low values: [328.07427978515625, 339.34796142578125]

File: SN20USBHX2002960_06.json
Stream: away
Low count: 2
Low values: [369.061767578125, 378.41571044921875]

File: SN20USBHX2002960_07.json
Stream: away
Low count: 2
Low values: [346.4017028808594, 326.4405212402344]

File: SN20USBHX2002960_08.json
Stream: away
Low count: 2
Low values: [378.6877746582031, 376.66363525390625]

File: SN20USBHX2002960_09.json
Stream: away
Low count: 2
Low values: [329.361572265625, 335.3903503417969]

File: SN20USBHX2002960_10.json
Stream: away
Low count: 2
Low values: [381.01934814453125, 372.4822082519531]

File: SN20USBHX2002960_11.json
Stream: away
Low count: 2
Low values: [343.17584228515625, 330.2913818359375]

File: SN20USBHX2002960_12.json
Stream: away
Low count: 2
Low values: [370.1105651855469, 366.4925842285156]

File: SN20USBHX2002960_13.json
Stream: away
Low count: 2
Low values: [346.4610595703125, 336.6968078613281]

File: SN20USBHX2002960_14.json
Stream: away
Low count: 2
Low values: [379.65570068359375, 368.6830139160156]

File: SN20USBHX2002960_15.json
Stream: away
Low count: 2
Low values: [329.7211608886719, 329.6789855957031]

File: SN20USBHX2002960_16.json
Stream: away
Low count: 2
Low values: [386.8173828125, 379.9418029785156]

File: SN20USBHX2002960_17.json
Stream: away
Low count: 2
Low values: [331.3547668457031, 325.55462646484375]

File: SN20USBHX2002960_18.json
Stream: away
Low count: 2
Low values: [387.0751953125, 383.0130310058594]

File: SN20USBHX2002960_19.json
Stream: away
Low count: 2
Low values: [339.9776916503906, 333.3285217285156]

File: SN20USBHX2002960_20.json
Stream: away
Low count: 2
Low values: [386.7160949707031, 380.9822692871094]

File: SN20USBHX2002960_21.json
Stream: away
Low count: 2
Low values: [343.6284484863281, 343.1169738769531]

File: SN20USBHX2002960_22.json
Stream: away
Low count: 2
Low values: [388.1668701171875, 387.360107421875]

File: SN20USBHX2002960_23.json
Stream: away
Low count: 2
Low values: [336.0994567871094, 349.9168395996094]

File: SN20USBHX2002960_24.json
Stream: away
Low count: 2
Low values: [327.80584716796875, 332.9079284667969]

File: SN20USBHX2002960_25.json
Stream: away
Low count: 2
Low values: [383.5533142089844, 377.78729248046875]


Module: SN20USBHX2002964
--------------------------------------------------------------------------------
Module total values: 64

File: SN20USBHX2002964_11.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_12.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_13.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_14.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_15.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_16.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_17.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_18.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_19.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_20.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_21.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_22.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_23.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_24.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_25.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2002964_09.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002964_10.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2002964_11.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_12.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_13.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_14.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_15.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_16.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_17.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_18.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_19.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_20.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_21.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_22.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_23.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_24.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]

File: SN20USBHX2002964_25.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 0.0]


Module: SN20USBHX2002965
--------------------------------------------------------------------------------
Module total values: 299

File: SN20USBHX2002965_01.json
Stream: under
Low count: 11
Low values: [373.305419921875, 380.0566101074219, 393.61578369140625, 397.5981750488281, 384.3458557128906, 384.77685546875, 391.0663146972656, 377.0263366699219, 383.9669189453125, 381.6352844238281, 385.4055480957031]

File: SN20USBHX2002965_02.json
Stream: under
Low count: 11
Low values: [362.7820129394531, 341.74407958984375, 359.9025573730469, 360.1113586425781, 339.48138427734375, 350.97320556640625, 342.8455810546875, 343.9474792480469, 331.3690185546875, 350.2088623046875, 344.4112243652344]

File: SN20USBHX2002965_03.json
Stream: under
Low count: 11
Low values: [346.78961181640625, 352.5122375488281, 355.0035705566406, 363.2454528808594, 355.7012634277344, 360.209716796875, 339.8437194824219, 359.155517578125, 356.63629150390625, 356.4812927246094, 355.75244140625]

File: SN20USBHX2002965_04.json
Stream: under
Low count: 11
Low values: [380.4980163574219, 373.4451904296875, 390.4729919433594, 387.33697509765625, 384.8879699707031, 389.6933288574219, 375.7607116699219, 387.3467712402344, 383.61114501953125, 388.7073059082031, 393.5632019042969]

File: SN20USBHX2002965_05.json
Stream: under
Low count: 11
Low values: [368.0262145996094, 356.8318786621094, 349.39141845703125, 337.79559326171875, 345.46478271484375, 339.7475280761719, 344.69769287109375, 348.2231750488281, 358.2116394042969, 340.36639404296875, 348.3563232421875]

File: SN20USBHX2002965_06.json
Stream: under
Low count: 11
Low values: [372.882080078125, 392.38824462890625, 382.0320129394531, 375.6618347167969, 373.5972595214844, 387.70355224609375, 363.48895263671875, 383.43878173828125, 376.4888000488281, 379.8053283691406, 401.8030700683594]

File: SN20USBHX2002965_07.json
Stream: under
Low count: 11
Low values: [351.7016296386719, 336.1624450683594, 362.03912353515625, 369.5355529785156, 358.75079345703125, 349.1777648925781, 352.8525390625, 346.7779235839844, 332.2242736816406, 343.2729797363281, 348.2310791015625]

File: SN20USBHX2002965_08.json
Stream: under
Low count: 11
Low values: [407.0457763671875, 393.767333984375, 391.7213134765625, 389.76983642578125, 382.7094421386719, 379.7220153808594, 374.4322509765625, 390.0376892089844, 377.6309509277344, 391.3881530761719, 391.6949768066406]

File: SN20USBHX2002965_09.json
Stream: under
Low count: 11
Low values: [359.8996276855469, 344.70745849609375, 335.5038146972656, 334.6652526855469, 343.84747314453125, 347.083251953125, 340.4585876464844, 332.33502197265625, 347.2908020019531, 351.63330078125, 354.97125244140625]

File: SN20USBHX2002965_10.json
Stream: under
Low count: 11
Low values: [365.1820373535156, 382.6434326171875, 384.4205627441406, 383.4925842285156, 390.3660888671875, 381.39019775390625, 392.9234619140625, 373.2608337402344, 377.4287109375, 380.180419921875, 385.05865478515625]

File: SN20USBHX2002965_11.json
Stream: under
Low count: 11
Low values: [346.05401611328125, 359.06842041015625, 341.27117919921875, 355.158935546875, 336.3711853027344, 347.1612243652344, 343.9010314941406, 335.5002136230469, 341.98138427734375, 352.91845703125, 360.1981506347656]

File: SN20USBHX2002965_12.json
Stream: under
Low count: 11
Low values: [388.697265625, 374.926513671875, 385.1368713378906, 390.2606201171875, 379.193359375, 369.9674377441406, 382.8496398925781, 384.10711669921875, 383.28802490234375, 385.13671875, 389.5824890136719]

File: SN20USBHX2002965_13.json
Stream: under
Low count: 12
Low values: [0.0, 339.624267578125, 348.5594482421875, 366.6794128417969, 344.3047180175781, 344.9284362792969, 350.2491455078125, 347.85467529296875, 355.46673583984375, 331.462158203125, 345.6312561035156, 326.9036560058594]

File: SN20USBHX2002965_14.json
Stream: under
Low count: 12
Low values: [0.0, 379.8219909667969, 385.4454650878906, 383.90283203125, 366.9807434082031, 370.6190185546875, 386.0101013183594, 374.17559814453125, 393.5309753417969, 386.2055358886719, 383.6452941894531, 371.9779968261719]

File: SN20USBHX2002965_15.json
Stream: under
Low count: 12
Low values: [0.0, 353.08001708984375, 352.8387756347656, 340.4459533691406, 345.44244384765625, 341.202880859375, 360.96319580078125, 343.80694580078125, 355.0987854003906, 360.191162109375, 355.1822509765625, 342.4081726074219]

File: SN20USBHX2002965_16.json
Stream: under
Low count: 12
Low values: [0.0, 389.3677062988281, 381.9566650390625, 394.1664733886719, 388.603515625, 385.97027587890625, 381.25054931640625, 387.532958984375, 391.0115051269531, 383.60302734375, 373.1139221191406, 374.43524169921875]

File: SN20USBHX2002965_17.json
Stream: under
Low count: 12
Low values: [0.0, 345.986083984375, 347.29571533203125, 337.8219909667969, 342.9309997558594, 347.9150085449219, 352.3695983886719, 347.5520935058594, 355.2853698730469, 349.1998291015625, 362.39141845703125, 351.22064208984375]

File: SN20USBHX2002965_18.json
Stream: under
Low count: 12
Low values: [0.0, 379.0729675292969, 364.75335693359375, 397.0222473144531, 389.0761413574219, 389.9554443359375, 383.1354064941406, 372.4320068359375, 388.2833557128906, 377.7217712402344, 398.3802490234375, 373.3876953125]

File: SN20USBHX2002965_19.json
Stream: under
Low count: 12
Low values: [0.0, 342.582275390625, 362.0894470214844, 336.9547424316406, 335.1177062988281, 330.2887268066406, 356.23834228515625, 349.0522766113281, 339.504638671875, 363.7033386230469, 353.27569580078125, 342.9732666015625]

File: SN20USBHX2002965_01.json
Stream: away
Low count: 4
Low values: [392.1028137207031, 396.425537109375, 0.0, 0.0]

File: SN20USBHX2002965_02.json
Stream: away
Low count: 4
Low values: [357.25860595703125, 339.5047912597656, 0.0, 0.0]

File: SN20USBHX2002965_03.json
Stream: away
Low count: 4
Low values: [353.0852355957031, 355.61865234375, 0.0, 0.0]

File: SN20USBHX2002965_04.json
Stream: away
Low count: 4
Low values: [389.0081481933594, 388.4471435546875, 0.0, 0.0]

File: SN20USBHX2002965_05.json
Stream: away
Low count: 4
Low values: [357.26544189453125, 347.87908935546875, 0.0, 0.0]

File: SN20USBHX2002965_06.json
Stream: away
Low count: 4
Low values: [378.3153381347656, 378.8362121582031, 0.0, 0.0]

File: SN20USBHX2002965_07.json
Stream: away
Low count: 4
Low values: [353.1978454589844, 347.80010986328125, 0.0, 0.0]

File: SN20USBHX2002965_08.json
Stream: away
Low count: 4
Low values: [396.92877197265625, 379.779541015625, 0.0, 0.0]

File: SN20USBHX2002965_09.json
Stream: away
Low count: 4
Low values: [333.8307189941406, 352.70062255859375, 0.0, 0.0]

File: SN20USBHX2002965_10.json
Stream: away
Low count: 4
Low values: [373.1827392578125, 375.9071350097656, 0.0, 0.0]

File: SN20USBHX2002965_11.json
Stream: away
Low count: 4
Low values: [356.79681396484375, 349.0624084472656, 0.0, 0.0]

File: SN20USBHX2002965_12.json
Stream: away
Low count: 4
Low values: [384.53546142578125, 371.588623046875, 0.0, 0.0]

File: SN20USBHX2002965_13.json
Stream: away
Low count: 5
Low values: [0.0, 346.3587341308594, 352.4604797363281, 0.0, 0.0]

File: SN20USBHX2002965_14.json
Stream: away
Low count: 5
Low values: [0.0, 382.8126220703125, 389.306884765625, 0.0, 0.0]

File: SN20USBHX2002965_15.json
Stream: away
Low count: 5
Low values: [0.0, 342.8486633300781, 357.1366882324219, 0.0, 0.0]

File: SN20USBHX2002965_16.json
Stream: away
Low count: 5
Low values: [0.0, 378.8111572265625, 387.1204833984375, 0.0, 0.0]

File: SN20USBHX2002965_17.json
Stream: away
Low count: 5
Low values: [0.0, 333.50811767578125, 342.3710021972656, 0.0, 0.0]

File: SN20USBHX2002965_18.json
Stream: away
Low count: 5
Low values: [0.0, 370.5143127441406, 375.5951843261719, 0.0, 0.0]

File: SN20USBHX2002965_19.json
Stream: away
Low count: 5
Low values: [0.0, 352.7447204589844, 339.65740966796875, 0.0, 0.0]


Module: SN20USBHX2002968
--------------------------------------------------------------------------------
Module total values: 281

File: SN20USBHX2002968_25.json
Stream: under
Low count: 129
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2002968_25.json
Stream: away
Low count: 152
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2002971
--------------------------------------------------------------------------------
Module total values: 43

File: SN20USBHX2002971_01.json
Stream: away
Low count: 1
Low values: [370.3578186035156]

File: SN20USBHX2002971_02.json
Stream: away
Low count: 1
Low values: [327.1632385253906]

File: SN20USBHX2002971_03.json
Stream: away
Low count: 1
Low values: [335.2873229980469]

File: SN20USBHX2002971_04.json
Stream: away
Low count: 1
Low values: [372.9046325683594]

File: SN20USBHX2002971_05.json
Stream: away
Low count: 1
Low values: [324.93701171875]

File: SN20USBHX2002971_06.json
Stream: away
Low count: 1
Low values: [369.8916320800781]

File: SN20USBHX2002971_07.json
Stream: away
Low count: 1
Low values: [334.7666320800781]

File: SN20USBHX2002971_08.json
Stream: away
Low count: 1
Low values: [377.1575622558594]

File: SN20USBHX2002971_09.json
Stream: away
Low count: 1
Low values: [333.27996826171875]

File: SN20USBHX2002971_10.json
Stream: away
Low count: 1
Low values: [361.8241271972656]

File: SN20USBHX2002971_11.json
Stream: away
Low count: 1
Low values: [343.103515625]

File: SN20USBHX2002971_12.json
Stream: away
Low count: 1
Low values: [375.7928771972656]

File: SN20USBHX2002971_13.json
Stream: away
Low count: 1
Low values: [338.50836181640625]

File: SN20USBHX2002971_14.json
Stream: away
Low count: 1
Low values: [373.6805725097656]

File: SN20USBHX2002971_15.json
Stream: away
Low count: 1
Low values: [316.9711608886719]

File: SN20USBHX2002971_16.json
Stream: away
Low count: 1
Low values: [373.3115234375]

File: SN20USBHX2002971_17.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 322.0970153808594]

File: SN20USBHX2002971_18.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 356.044189453125]

File: SN20USBHX2002971_19.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 332.982666015625]

File: SN20USBHX2002971_20.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 361.72735595703125]

File: SN20USBHX2002971_21.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 328.3368835449219]

File: SN20USBHX2002971_22.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 363.6431884765625]

File: SN20USBHX2002971_23.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 339.178466796875]

File: SN20USBHX2002971_24.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 327.05572509765625]

File: SN20USBHX2002971_25.json
Stream: away
Low count: 3
Low values: [0.0, 0.0, 358.9784851074219]


Module: SN20USBHX2003036
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003036_01.json
Stream: under
Low count: 1
Low values: [369.21624755859375]

File: SN20USBHX2003036_02.json
Stream: under
Low count: 1
Low values: [312.1361389160156]

File: SN20USBHX2003036_03.json
Stream: under
Low count: 1
Low values: [313.879150390625]

File: SN20USBHX2003036_04.json
Stream: under
Low count: 1
Low values: [375.79736328125]

File: SN20USBHX2003036_05.json
Stream: under
Low count: 1
Low values: [320.27752685546875]

File: SN20USBHX2003036_06.json
Stream: under
Low count: 1
Low values: [360.0903625488281]

File: SN20USBHX2003036_07.json
Stream: under
Low count: 1
Low values: [333.708984375]

File: SN20USBHX2003036_08.json
Stream: under
Low count: 1
Low values: [363.9217834472656]

File: SN20USBHX2003036_09.json
Stream: under
Low count: 1
Low values: [311.68304443359375]

File: SN20USBHX2003036_10.json
Stream: under
Low count: 1
Low values: [371.6455383300781]

File: SN20USBHX2003036_11.json
Stream: under
Low count: 1
Low values: [328.4667053222656]

File: SN20USBHX2003036_12.json
Stream: under
Low count: 1
Low values: [358.5736999511719]

File: SN20USBHX2003036_13.json
Stream: under
Low count: 1
Low values: [315.567626953125]

File: SN20USBHX2003036_14.json
Stream: under
Low count: 1
Low values: [361.5404357910156]

File: SN20USBHX2003036_15.json
Stream: under
Low count: 1
Low values: [306.5552673339844]

File: SN20USBHX2003036_16.json
Stream: under
Low count: 1
Low values: [371.6884460449219]

File: SN20USBHX2003036_17.json
Stream: under
Low count: 1
Low values: [334.86480712890625]

File: SN20USBHX2003036_18.json
Stream: under
Low count: 1
Low values: [359.18170166015625]

File: SN20USBHX2003036_19.json
Stream: under
Low count: 1
Low values: [316.58868408203125]

File: SN20USBHX2003036_20.json
Stream: under
Low count: 1
Low values: [379.59930419921875]

File: SN20USBHX2003036_21.json
Stream: under
Low count: 1
Low values: [323.6621398925781]

File: SN20USBHX2003036_22.json
Stream: under
Low count: 1
Low values: [363.7191467285156]

File: SN20USBHX2003036_23.json
Stream: under
Low count: 1
Low values: [329.1922302246094]

File: SN20USBHX2003036_24.json
Stream: under
Low count: 1
Low values: [318.34332275390625]

File: SN20USBHX2003036_25.json
Stream: under
Low count: 1
Low values: [366.79644775390625]


Module: SN20USBHX2003042
--------------------------------------------------------------------------------
Module total values: 9

File: SN20USBHX2003042_01.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003042_04.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003042_06.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003042_07.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003042_10.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003042_16.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003042_19.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003042_24.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003042_25.json
Stream: under
Low count: 1
Low values: [0.0]


Module: SN20USBHX2003058
--------------------------------------------------------------------------------
Module total values: 300

File: SN20USBHX2003058_01.json
Stream: under
Low count: 12
Low values: [376.108154296875, 377.11822509765625, 403.83892822265625, 370.66180419921875, 381.81634521484375, 387.3766174316406, 377.91033935546875, 377.0606994628906, 402.4351501464844, 368.56768798828125, 382.15478515625, 380.9049377441406]

File: SN20USBHX2003058_02.json
Stream: under
Low count: 12
Low values: [350.6887512207031, 332.91680908203125, 347.60693359375, 335.5115051269531, 346.8724670410156, 351.0553894042969, 338.399658203125, 325.6083984375, 338.10498046875, 346.5945129394531, 349.0033264160156, 332.0777282714844]

File: SN20USBHX2003058_03.json
Stream: under
Low count: 12
Low values: [344.9717102050781, 350.9042663574219, 365.2236022949219, 333.0224914550781, 345.72576904296875, 342.499267578125, 354.801513671875, 351.07891845703125, 348.5342712402344, 352.9481201171875, 339.4241027832031, 343.5340881347656]

File: SN20USBHX2003058_04.json
Stream: under
Low count: 12
Low values: [371.5498962402344, 392.36187744140625, 384.8085021972656, 377.26898193359375, 381.1075439453125, 373.7545471191406, 371.0441589355469, 375.388427734375, 382.2352294921875, 379.8416748046875, 381.6007080078125, 398.0073547363281]

File: SN20USBHX2003058_05.json
Stream: under
Low count: 12
Low values: [335.0897216796875, 338.44976806640625, 344.7687072753906, 334.6070556640625, 331.96630859375, 333.0932922363281, 354.49810791015625, 350.2352294921875, 342.439697265625, 343.08221435546875, 330.2245178222656, 333.5928649902344]

File: SN20USBHX2003058_06.json
Stream: under
Low count: 12
Low values: [383.08489990234375, 392.2489013671875, 395.2517395019531, 397.89886474609375, 392.56182861328125, 375.1066589355469, 369.6636962890625, 378.79168701171875, 385.0518493652344, 387.7605895996094, 396.64532470703125, 379.8802185058594]

File: SN20USBHX2003058_07.json
Stream: under
Low count: 12
Low values: [332.4357604980469, 346.1301574707031, 346.2215881347656, 347.7253112792969, 346.1860656738281, 331.0267639160156, 347.0155334472656, 344.5369873046875, 338.91754150390625, 344.9057922363281, 343.497802734375, 337.657470703125]

File: SN20USBHX2003058_08.json
Stream: under
Low count: 12
Low values: [378.6399841308594, 368.76385498046875, 385.77081298828125, 375.4306945800781, 364.26922607421875, 382.73016357421875, 384.5348815917969, 394.5207214355469, 387.7139892578125, 373.5286560058594, 373.7147521972656, 377.07037353515625]

File: SN20USBHX2003058_09.json
Stream: under
Low count: 12
Low values: [336.5851745605469, 328.56634521484375, 338.16162109375, 346.7835693359375, 338.7354736328125, 330.3499755859375, 342.9687805175781, 334.4070739746094, 324.5166931152344, 344.5327453613281, 321.1708984375, 352.2549133300781]

File: SN20USBHX2003058_10.json
Stream: under
Low count: 12
Low values: [384.4530334472656, 378.0554504394531, 369.3809814453125, 400.7156982421875, 371.90081787109375, 379.410400390625, 385.6637268066406, 380.440673828125, 377.934814453125, 371.23101806640625, 384.9028015136719, 375.5014953613281]

File: SN20USBHX2003058_11.json
Stream: under
Low count: 12
Low values: [342.91107177734375, 343.8609924316406, 338.86285400390625, 338.7369079589844, 337.0212707519531, 327.9889831542969, 334.25054931640625, 343.8083190917969, 351.2356262207031, 341.85870361328125, 344.7004699707031, 340.902099609375]

File: SN20USBHX2003058_12.json
Stream: under
Low count: 12
Low values: [394.2466125488281, 368.25537109375, 385.06219482421875, 385.0657043457031, 395.3780822753906, 384.18212890625, 379.3123779296875, 390.5868835449219, 388.23828125, 398.8726501464844, 371.1377258300781, 370.3218078613281]

File: SN20USBHX2003058_13.json
Stream: under
Low count: 12
Low values: [346.518798828125, 347.9508972167969, 346.3440856933594, 342.1979675292969, 335.4106140136719, 350.8138122558594, 350.6074523925781, 348.1407165527344, 347.322998046875, 337.7332458496094, 336.5685729980469, 336.6417236328125]

File: SN20USBHX2003058_14.json
Stream: under
Low count: 12
Low values: [369.9192199707031, 371.6511535644531, 372.66796875, 384.3080139160156, 375.3973693847656, 386.46746826171875, 369.1109619140625, 382.04742431640625, 384.65350341796875, 382.5623474121094, 362.47808837890625, 388.18109130859375]

File: SN20USBHX2003058_15.json
Stream: under
Low count: 12
Low values: [344.4223937988281, 329.0135498046875, 339.6926574707031, 333.8759765625, 335.5858154296875, 347.7816467285156, 336.2497253417969, 342.96710205078125, 330.1632385253906, 336.8808288574219, 341.54241943359375, 337.3791809082031]

File: SN20USBHX2003058_16.json
Stream: under
Low count: 12
Low values: [386.2451171875, 379.41009521484375, 378.1165466308594, 382.8726501464844, 381.69012451171875, 387.1890563964844, 366.7188720703125, 378.942138671875, 390.4020690917969, 379.86944580078125, 389.84136962890625, 376.8329772949219]

File: SN20USBHX2003058_17.json
Stream: under
Low count: 12
Low values: [340.02398681640625, 337.3288269042969, 334.913818359375, 335.40521240234375, 339.4559326171875, 336.820556640625, 345.0690612792969, 336.8791809082031, 349.8743591308594, 352.38861083984375, 331.83282470703125, 340.550048828125]

File: SN20USBHX2003058_18.json
Stream: under
Low count: 12
Low values: [383.66949462890625, 368.228759765625, 399.3562316894531, 392.3332824707031, 378.5560302734375, 384.80291748046875, 384.3117980957031, 380.21002197265625, 393.56451416015625, 378.1173095703125, 370.9903564453125, 372.883544921875]

File: SN20USBHX2003058_19.json
Stream: under
Low count: 12
Low values: [327.8555603027344, 346.28533935546875, 333.9026794433594, 333.0583190917969, 333.4610900878906, 352.6365661621094, 335.0472412109375, 338.1165466308594, 329.0736083984375, 344.5877990722656, 349.9864807128906, 331.8789978027344]

File: SN20USBHX2003058_20.json
Stream: under
Low count: 12
Low values: [363.6847229003906, 375.1331481933594, 387.2150573730469, 382.22625732421875, 383.7208557128906, 387.4945983886719, 398.309814453125, 373.02838134765625, 385.9408874511719, 382.0180969238281, 376.075927734375, 375.57373046875]

File: SN20USBHX2003058_21.json
Stream: under
Low count: 12
Low values: [343.8547058105469, 336.720458984375, 343.0758056640625, 338.8447265625, 336.8863830566406, 351.0763244628906, 341.4381408691406, 338.607177734375, 340.7640686035156, 333.49462890625, 351.1671142578125, 337.7301025390625]

File: SN20USBHX2003058_22.json
Stream: under
Low count: 12
Low values: [378.14227294921875, 384.6068420410156, 391.81976318359375, 378.28778076171875, 377.4546203613281, 402.8626708984375, 386.7702331542969, 369.0150451660156, 387.5351867675781, 384.0300598144531, 389.17730712890625, 382.97027587890625]

File: SN20USBHX2003058_23.json
Stream: under
Low count: 12
Low values: [351.8327941894531, 362.83148193359375, 340.3916015625, 337.48126220703125, 359.8587646484375, 352.785888671875, 344.7284851074219, 341.9280700683594, 351.82220458984375, 332.4938659667969, 328.0605773925781, 348.4658508300781]

File: SN20USBHX2003058_24.json
Stream: under
Low count: 12
Low values: [336.68890380859375, 337.4369812011719, 355.6611328125, 335.3403625488281, 334.1980285644531, 338.8110046386719, 339.0791931152344, 334.98748779296875, 348.7433776855469, 353.2650451660156, 339.7890319824219, 336.73077392578125]

File: SN20USBHX2003058_25.json
Stream: under
Low count: 12
Low values: [387.0595397949219, 388.9997863769531, 385.88153076171875, 386.7038879394531, 373.8923645019531, 379.62481689453125, 370.4544372558594, 385.53717041015625, 380.1263732910156, 390.7222595214844, 378.2071838378906, 364.8931884765625]


Module: SN20USBHX2003130
--------------------------------------------------------------------------------
Module total values: 50

File: SN20USBHX2003130_01.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_02.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_03.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_04.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_05.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_06.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_07.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_08.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_09.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_10.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_11.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_12.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_13.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_14.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_15.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_16.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_17.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_18.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_19.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_20.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_21.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_22.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_23.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_24.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_25.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_01.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_02.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_03.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_04.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_05.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_06.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_07.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_08.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_09.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_10.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_11.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_12.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_13.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_14.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_15.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_16.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_17.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_18.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_19.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_20.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_21.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_22.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_23.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_24.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2003130_25.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2003237
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003237_01.json
Stream: under
Low count: 1
Low values: [372.8826599121094]

File: SN20USBHX2003237_02.json
Stream: under
Low count: 1
Low values: [350.77679443359375]

File: SN20USBHX2003237_03.json
Stream: under
Low count: 1
Low values: [333.32086181640625]

File: SN20USBHX2003237_04.json
Stream: under
Low count: 1
Low values: [380.78179931640625]

File: SN20USBHX2003237_05.json
Stream: under
Low count: 1
Low values: [332.5690612792969]

File: SN20USBHX2003237_06.json
Stream: under
Low count: 1
Low values: [377.75244140625]

File: SN20USBHX2003237_07.json
Stream: under
Low count: 1
Low values: [343.36334228515625]

File: SN20USBHX2003237_08.json
Stream: under
Low count: 1
Low values: [379.0486755371094]

File: SN20USBHX2003237_09.json
Stream: under
Low count: 1
Low values: [324.84130859375]

File: SN20USBHX2003237_10.json
Stream: under
Low count: 1
Low values: [362.6156311035156]

File: SN20USBHX2003237_11.json
Stream: under
Low count: 1
Low values: [334.6346435546875]

File: SN20USBHX2003237_12.json
Stream: under
Low count: 1
Low values: [372.7718811035156]

File: SN20USBHX2003237_13.json
Stream: under
Low count: 1
Low values: [350.53118896484375]

File: SN20USBHX2003237_14.json
Stream: under
Low count: 1
Low values: [379.9317321777344]

File: SN20USBHX2003237_15.json
Stream: under
Low count: 1
Low values: [349.6494140625]

File: SN20USBHX2003237_16.json
Stream: under
Low count: 1
Low values: [385.6515808105469]

File: SN20USBHX2003237_17.json
Stream: under
Low count: 1
Low values: [336.2442626953125]

File: SN20USBHX2003237_18.json
Stream: under
Low count: 1
Low values: [384.88525390625]

File: SN20USBHX2003237_19.json
Stream: under
Low count: 1
Low values: [327.1291809082031]

File: SN20USBHX2003237_20.json
Stream: under
Low count: 1
Low values: [383.5575866699219]

File: SN20USBHX2003237_21.json
Stream: under
Low count: 1
Low values: [343.7330017089844]

File: SN20USBHX2003237_22.json
Stream: under
Low count: 1
Low values: [384.1965637207031]

File: SN20USBHX2003237_23.json
Stream: under
Low count: 1
Low values: [355.6258850097656]

File: SN20USBHX2003237_24.json
Stream: under
Low count: 1
Low values: [326.1518249511719]

File: SN20USBHX2003237_25.json
Stream: under
Low count: 1
Low values: [377.1360778808594]


Module: SN20USBHX2003244
--------------------------------------------------------------------------------
Module total values: 75

File: SN20USBHX2003244_01.json
Stream: under
Low count: 3
Low values: [386.47808837890625, 385.3154602050781, 381.04888916015625]

File: SN20USBHX2003244_02.json
Stream: under
Low count: 3
Low values: [333.3196105957031, 331.90283203125, 346.372802734375]

File: SN20USBHX2003244_03.json
Stream: under
Low count: 3
Low values: [343.2382507324219, 328.6667175292969, 335.3934020996094]

File: SN20USBHX2003244_04.json
Stream: under
Low count: 3
Low values: [378.99517822265625, 386.6259460449219, 387.3365478515625]

File: SN20USBHX2003244_05.json
Stream: under
Low count: 3
Low values: [357.7283935546875, 337.0788269042969, 340.57012939453125]

File: SN20USBHX2003244_06.json
Stream: under
Low count: 3
Low values: [382.588623046875, 383.7885437011719, 387.8223571777344]

File: SN20USBHX2003244_07.json
Stream: under
Low count: 3
Low values: [333.66888427734375, 345.343505859375, 338.3497009277344]

File: SN20USBHX2003244_08.json
Stream: under
Low count: 3
Low values: [378.6990051269531, 387.56512451171875, 384.8905334472656]

File: SN20USBHX2003244_09.json
Stream: under
Low count: 3
Low values: [332.29718017578125, 340.3849792480469, 345.2674865722656]

File: SN20USBHX2003244_10.json
Stream: under
Low count: 3
Low values: [383.4514465332031, 366.1174621582031, 379.2670593261719]

File: SN20USBHX2003244_11.json
Stream: under
Low count: 3
Low values: [338.978271484375, 342.98736572265625, 327.1372985839844]

File: SN20USBHX2003244_12.json
Stream: under
Low count: 3
Low values: [384.0108337402344, 377.9965515136719, 384.5953063964844]

File: SN20USBHX2003244_13.json
Stream: under
Low count: 3
Low values: [332.04388427734375, 335.9798278808594, 340.3576354980469]

File: SN20USBHX2003244_14.json
Stream: under
Low count: 3
Low values: [373.6537780761719, 378.1431579589844, 384.9070739746094]

File: SN20USBHX2003244_15.json
Stream: under
Low count: 3
Low values: [328.7078552246094, 340.6815185546875, 328.79608154296875]

File: SN20USBHX2003244_16.json
Stream: under
Low count: 3
Low values: [370.7931823730469, 385.9367980957031, 380.1610412597656]

File: SN20USBHX2003244_17.json
Stream: under
Low count: 3
Low values: [338.108642578125, 332.24285888671875, 337.43280029296875]

File: SN20USBHX2003244_18.json
Stream: under
Low count: 3
Low values: [391.7702331542969, 374.97503662109375, 392.73016357421875]

File: SN20USBHX2003244_19.json
Stream: under
Low count: 3
Low values: [334.93646240234375, 339.1216125488281, 351.2890319824219]

File: SN20USBHX2003244_20.json
Stream: under
Low count: 3
Low values: [384.47430419921875, 380.7760925292969, 391.29327392578125]

File: SN20USBHX2003244_21.json
Stream: under
Low count: 3
Low values: [341.921875, 335.28363037109375, 327.7610778808594]

File: SN20USBHX2003244_22.json
Stream: under
Low count: 3
Low values: [383.2377624511719, 404.572265625, 381.07354736328125]

File: SN20USBHX2003244_23.json
Stream: under
Low count: 3
Low values: [343.7372131347656, 333.9493713378906, 349.8468017578125]

File: SN20USBHX2003244_24.json
Stream: under
Low count: 3
Low values: [334.614501953125, 341.5150451660156, 339.52880859375]

File: SN20USBHX2003244_25.json
Stream: under
Low count: 3
Low values: [389.7801818847656, 386.4393310546875, 383.4541015625]


Module: SN20USBHX2003545
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003545_01.json
Stream: away
Low count: 1
Low values: [377.9342041015625]

File: SN20USBHX2003545_02.json
Stream: away
Low count: 1
Low values: [349.19927978515625]

File: SN20USBHX2003545_03.json
Stream: away
Low count: 1
Low values: [351.6348571777344]

File: SN20USBHX2003545_04.json
Stream: away
Low count: 1
Low values: [390.3948669433594]

File: SN20USBHX2003545_05.json
Stream: away
Low count: 1
Low values: [333.4176330566406]

File: SN20USBHX2003545_06.json
Stream: away
Low count: 1
Low values: [397.3115539550781]

File: SN20USBHX2003545_07.json
Stream: away
Low count: 1
Low values: [357.33514404296875]

File: SN20USBHX2003545_08.json
Stream: away
Low count: 1
Low values: [384.8717956542969]

File: SN20USBHX2003545_09.json
Stream: away
Low count: 1
Low values: [328.03082275390625]

File: SN20USBHX2003545_10.json
Stream: away
Low count: 1
Low values: [390.8889465332031]

File: SN20USBHX2003545_11.json
Stream: away
Low count: 1
Low values: [348.62115478515625]

File: SN20USBHX2003545_12.json
Stream: away
Low count: 1
Low values: [367.5054016113281]

File: SN20USBHX2003545_13.json
Stream: away
Low count: 1
Low values: [337.2171325683594]

File: SN20USBHX2003545_14.json
Stream: away
Low count: 1
Low values: [363.56072998046875]

File: SN20USBHX2003545_15.json
Stream: away
Low count: 1
Low values: [339.1599426269531]

File: SN20USBHX2003545_16.json
Stream: away
Low count: 1
Low values: [391.7470703125]

File: SN20USBHX2003545_17.json
Stream: away
Low count: 1
Low values: [345.7159729003906]

File: SN20USBHX2003545_18.json
Stream: away
Low count: 1
Low values: [379.2467346191406]

File: SN20USBHX2003545_19.json
Stream: away
Low count: 1
Low values: [345.4359130859375]

File: SN20USBHX2003545_20.json
Stream: away
Low count: 1
Low values: [380.4573669433594]

File: SN20USBHX2003545_21.json
Stream: away
Low count: 1
Low values: [362.9654235839844]

File: SN20USBHX2003545_22.json
Stream: away
Low count: 1
Low values: [384.6168212890625]

File: SN20USBHX2003545_23.json
Stream: away
Low count: 1
Low values: [325.2674865722656]

File: SN20USBHX2003545_24.json
Stream: away
Low count: 1
Low values: [341.0767822265625]

File: SN20USBHX2003545_25.json
Stream: away
Low count: 1
Low values: [401.6379699707031]


Module: SN20USBHX2003548
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003548_01.json
Stream: under
Low count: 1
Low values: [376.0489807128906]

File: SN20USBHX2003548_02.json
Stream: under
Low count: 1
Low values: [332.7443542480469]

File: SN20USBHX2003548_03.json
Stream: under
Low count: 1
Low values: [367.5210876464844]

File: SN20USBHX2003548_04.json
Stream: under
Low count: 1
Low values: [387.8843994140625]

File: SN20USBHX2003548_05.json
Stream: under
Low count: 1
Low values: [346.96282958984375]

File: SN20USBHX2003548_06.json
Stream: under
Low count: 1
Low values: [378.48858642578125]

File: SN20USBHX2003548_07.json
Stream: under
Low count: 1
Low values: [338.8375549316406]

File: SN20USBHX2003548_08.json
Stream: under
Low count: 1
Low values: [376.2036437988281]

File: SN20USBHX2003548_09.json
Stream: under
Low count: 1
Low values: [351.5931396484375]

File: SN20USBHX2003548_10.json
Stream: under
Low count: 1
Low values: [388.44866943359375]

File: SN20USBHX2003548_11.json
Stream: under
Low count: 1
Low values: [347.3157958984375]

File: SN20USBHX2003548_12.json
Stream: under
Low count: 1
Low values: [380.0953674316406]

File: SN20USBHX2003548_13.json
Stream: under
Low count: 1
Low values: [349.5216979980469]

File: SN20USBHX2003548_14.json
Stream: under
Low count: 1
Low values: [383.9441833496094]

File: SN20USBHX2003548_15.json
Stream: under
Low count: 1
Low values: [343.3804931640625]

File: SN20USBHX2003548_16.json
Stream: under
Low count: 1
Low values: [382.22015380859375]

File: SN20USBHX2003548_17.json
Stream: under
Low count: 1
Low values: [340.6231384277344]

File: SN20USBHX2003548_18.json
Stream: under
Low count: 1
Low values: [384.28546142578125]

File: SN20USBHX2003548_19.json
Stream: under
Low count: 1
Low values: [351.01715087890625]

File: SN20USBHX2003548_20.json
Stream: under
Low count: 1
Low values: [375.6024169921875]

File: SN20USBHX2003548_21.json
Stream: under
Low count: 1
Low values: [349.0440673828125]

File: SN20USBHX2003548_22.json
Stream: under
Low count: 1
Low values: [406.5660400390625]

File: SN20USBHX2003548_23.json
Stream: under
Low count: 1
Low values: [349.69158935546875]

File: SN20USBHX2003548_24.json
Stream: under
Low count: 1
Low values: [353.1818542480469]

File: SN20USBHX2003548_25.json
Stream: under
Low count: 1
Low values: [391.93719482421875]


Module: SN20USBHX2003549
--------------------------------------------------------------------------------
Module total values: 50

File: SN20USBHX2003549_01.json
Stream: under
Low count: 2
Low values: [384.1025695800781, 394.8154296875]

File: SN20USBHX2003549_02.json
Stream: under
Low count: 2
Low values: [349.30389404296875, 343.42730712890625]

File: SN20USBHX2003549_03.json
Stream: under
Low count: 2
Low values: [362.4012756347656, 353.7865905761719]

File: SN20USBHX2003549_04.json
Stream: under
Low count: 2
Low values: [393.08685302734375, 399.9026184082031]

File: SN20USBHX2003549_05.json
Stream: under
Low count: 2
Low values: [346.7798156738281, 341.85296630859375]

File: SN20USBHX2003549_06.json
Stream: under
Low count: 2
Low values: [386.0915832519531, 397.20086669921875]

File: SN20USBHX2003549_07.json
Stream: under
Low count: 2
Low values: [334.8404541015625, 344.1164245605469]

File: SN20USBHX2003549_08.json
Stream: under
Low count: 2
Low values: [396.5881042480469, 388.8359069824219]

File: SN20USBHX2003549_09.json
Stream: under
Low count: 2
Low values: [343.30328369140625, 353.63818359375]

File: SN20USBHX2003549_10.json
Stream: under
Low count: 2
Low values: [385.8173828125, 388.7562255859375]

File: SN20USBHX2003549_11.json
Stream: under
Low count: 2
Low values: [342.875732421875, 341.7088623046875]

File: SN20USBHX2003549_12.json
Stream: under
Low count: 2
Low values: [389.0995178222656, 376.4493408203125]

File: SN20USBHX2003549_13.json
Stream: under
Low count: 2
Low values: [346.3172607421875, 351.554443359375]

File: SN20USBHX2003549_14.json
Stream: under
Low count: 2
Low values: [382.76861572265625, 392.2356872558594]

File: SN20USBHX2003549_15.json
Stream: under
Low count: 2
Low values: [341.0965576171875, 340.85137939453125]

File: SN20USBHX2003549_16.json
Stream: under
Low count: 2
Low values: [385.0838928222656, 375.96746826171875]

File: SN20USBHX2003549_17.json
Stream: under
Low count: 2
Low values: [342.4972839355469, 352.1700439453125]

File: SN20USBHX2003549_18.json
Stream: under
Low count: 2
Low values: [384.45538330078125, 379.25372314453125]

File: SN20USBHX2003549_19.json
Stream: under
Low count: 2
Low values: [348.97796630859375, 326.46356201171875]

File: SN20USBHX2003549_20.json
Stream: under
Low count: 2
Low values: [383.6190490722656, 390.4460754394531]

File: SN20USBHX2003549_21.json
Stream: under
Low count: 2
Low values: [336.205078125, 341.4548034667969]

File: SN20USBHX2003549_22.json
Stream: under
Low count: 2
Low values: [379.8570251464844, 383.9491271972656]

File: SN20USBHX2003549_23.json
Stream: under
Low count: 2
Low values: [337.59820556640625, 353.8681945800781]

File: SN20USBHX2003549_24.json
Stream: under
Low count: 2
Low values: [336.2966613769531, 330.0932922363281]

File: SN20USBHX2003549_25.json
Stream: under
Low count: 2
Low values: [389.0904846191406, 385.8825378417969]


Module: SN20USBHX2003562
--------------------------------------------------------------------------------
Module total values: 1

File: SN20USBHX2003562_21.json
Stream: away
Low count: 1
Low values: [464.758056640625]


Module: SN20USBHX2003645
--------------------------------------------------------------------------------
Module total values: 125

File: SN20USBHX2003645_01.json
Stream: under
Low count: 5
Low values: [384.3110656738281, 387.76995849609375, 369.4521484375, 369.0750732421875, 386.8045959472656]

File: SN20USBHX2003645_02.json
Stream: under
Low count: 5
Low values: [341.24658203125, 350.6005554199219, 338.9536437988281, 341.0543518066406, 339.0541076660156]

File: SN20USBHX2003645_03.json
Stream: under
Low count: 5
Low values: [339.9733581542969, 344.0278625488281, 337.3652648925781, 346.955322265625, 345.6398010253906]

File: SN20USBHX2003645_04.json
Stream: under
Low count: 5
Low values: [380.40252685546875, 392.7256774902344, 376.80364990234375, 376.36248779296875, 391.5235290527344]

File: SN20USBHX2003645_05.json
Stream: under
Low count: 5
Low values: [321.8184509277344, 336.69207763671875, 340.0304870605469, 326.6041564941406, 334.7629089355469]

File: SN20USBHX2003645_06.json
Stream: under
Low count: 5
Low values: [366.40350341796875, 378.4485168457031, 372.57452392578125, 368.4644470214844, 390.3750915527344]

File: SN20USBHX2003645_07.json
Stream: under
Low count: 5
Low values: [333.2069396972656, 328.17926025390625, 339.8832092285156, 352.1220397949219, 336.6087341308594]

File: SN20USBHX2003645_08.json
Stream: under
Low count: 5
Low values: [380.05926513671875, 385.80316162109375, 377.93182373046875, 382.62744140625, 385.4300231933594]

File: SN20USBHX2003645_09.json
Stream: under
Low count: 5
Low values: [343.3645324707031, 327.0472412109375, 335.62396240234375, 335.298583984375, 353.4480895996094]

File: SN20USBHX2003645_10.json
Stream: under
Low count: 5
Low values: [380.1770324707031, 380.662353515625, 373.6761169433594, 385.60552978515625, 382.460205078125]

File: SN20USBHX2003645_11.json
Stream: under
Low count: 5
Low values: [331.9433898925781, 349.0690612792969, 350.5992736816406, 332.86419677734375, 345.6813049316406]

File: SN20USBHX2003645_12.json
Stream: under
Low count: 5
Low values: [369.9214782714844, 386.6068115234375, 372.97943115234375, 369.8396911621094, 383.4759826660156]

File: SN20USBHX2003645_13.json
Stream: under
Low count: 5
Low values: [330.4362487792969, 346.1849060058594, 332.8385009765625, 336.92291259765625, 335.0458679199219]

File: SN20USBHX2003645_14.json
Stream: under
Low count: 5
Low values: [374.4193420410156, 388.8004150390625, 381.2064208984375, 386.7983093261719, 378.84454345703125]

File: SN20USBHX2003645_15.json
Stream: under
Low count: 5
Low values: [331.40252685546875, 324.6819763183594, 344.86212158203125, 336.00531005859375, 334.1363525390625]

File: SN20USBHX2003645_16.json
Stream: under
Low count: 5
Low values: [391.8121337890625, 393.83392333984375, 382.10418701171875, 375.1619567871094, 385.33831787109375]

File: SN20USBHX2003645_17.json
Stream: under
Low count: 5
Low values: [340.94500732421875, 339.5943908691406, 339.3573913574219, 356.99334716796875, 353.7135009765625]

File: SN20USBHX2003645_18.json
Stream: under
Low count: 5
Low values: [387.16241455078125, 380.92291259765625, 375.94793701171875, 390.43853759765625, 375.9859313964844]

File: SN20USBHX2003645_19.json
Stream: under
Low count: 5
Low values: [336.5923156738281, 337.3350830078125, 332.9684753417969, 346.9206848144531, 336.9455871582031]

File: SN20USBHX2003645_20.json
Stream: under
Low count: 5
Low values: [382.2105712890625, 393.8130798339844, 387.74688720703125, 380.1441345214844, 377.9398498535156]

File: SN20USBHX2003645_21.json
Stream: under
Low count: 5
Low values: [335.59820556640625, 339.0468444824219, 350.385009765625, 336.72198486328125, 346.6065979003906]

File: SN20USBHX2003645_22.json
Stream: under
Low count: 5
Low values: [384.5234069824219, 390.5076904296875, 376.2679443359375, 376.6604919433594, 385.62689208984375]

File: SN20USBHX2003645_23.json
Stream: under
Low count: 5
Low values: [337.4696044921875, 347.5987243652344, 333.7140808105469, 348.6886901855469, 348.27734375]

File: SN20USBHX2003645_24.json
Stream: under
Low count: 5
Low values: [340.9808044433594, 330.4076232910156, 344.2401123046875, 340.9007873535156, 334.5953063964844]

File: SN20USBHX2003645_25.json
Stream: under
Low count: 5
Low values: [396.1087951660156, 377.6645812988281, 389.10595703125, 377.63641357421875, 387.5545349121094]


Module: SN20USBHX2003654
--------------------------------------------------------------------------------
Module total values: 75

File: SN20USBHX2003654_01.json
Stream: away
Low count: 3
Low values: [374.4396667480469, 387.30462646484375, 378.78350830078125]

File: SN20USBHX2003654_02.json
Stream: away
Low count: 3
Low values: [318.5319519042969, 345.87774658203125, 328.49090576171875]

File: SN20USBHX2003654_03.json
Stream: away
Low count: 3
Low values: [322.9336853027344, 341.12249755859375, 344.06298828125]

File: SN20USBHX2003654_04.json
Stream: away
Low count: 3
Low values: [387.9924011230469, 387.8540344238281, 372.6741943359375]

File: SN20USBHX2003654_05.json
Stream: away
Low count: 3
Low values: [310.0007019042969, 322.4706115722656, 340.4412841796875]

File: SN20USBHX2003654_06.json
Stream: away
Low count: 3
Low values: [378.7734375, 376.40802001953125, 375.5219421386719]

File: SN20USBHX2003654_07.json
Stream: away
Low count: 3
Low values: [315.3778076171875, 350.62652587890625, 339.75982666015625]

File: SN20USBHX2003654_08.json
Stream: away
Low count: 3
Low values: [373.7638244628906, 380.8663024902344, 395.6343994140625]

File: SN20USBHX2003654_09.json
Stream: away
Low count: 3
Low values: [340.304931640625, 339.5552673339844, 331.3734130859375]

File: SN20USBHX2003654_10.json
Stream: away
Low count: 3
Low values: [381.59808349609375, 378.1853332519531, 381.93499755859375]

File: SN20USBHX2003654_11.json
Stream: away
Low count: 3
Low values: [338.1226501464844, 342.98895263671875, 329.2059631347656]

File: SN20USBHX2003654_12.json
Stream: away
Low count: 3
Low values: [362.43646240234375, 395.9181213378906, 378.6845703125]

File: SN20USBHX2003654_13.json
Stream: away
Low count: 3
Low values: [324.83258056640625, 337.1575927734375, 333.4959411621094]

File: SN20USBHX2003654_14.json
Stream: away
Low count: 3
Low values: [373.7658386230469, 365.2145690917969, 382.3521728515625]

File: SN20USBHX2003654_15.json
Stream: away
Low count: 3
Low values: [313.18304443359375, 337.9970703125, 339.1269226074219]

File: SN20USBHX2003654_16.json
Stream: away
Low count: 3
Low values: [372.6796569824219, 381.6349792480469, 371.2369384765625]

File: SN20USBHX2003654_17.json
Stream: away
Low count: 3
Low values: [315.22509765625, 335.5763244628906, 321.1377868652344]

File: SN20USBHX2003654_18.json
Stream: away
Low count: 3
Low values: [379.3498229980469, 365.826171875, 386.06182861328125]

File: SN20USBHX2003654_19.json
Stream: away
Low count: 3
Low values: [324.02252197265625, 343.2135314941406, 340.6723327636719]

File: SN20USBHX2003654_20.json
Stream: away
Low count: 3
Low values: [369.1400146484375, 378.54144287109375, 375.09857177734375]

File: SN20USBHX2003654_21.json
Stream: away
Low count: 3
Low values: [323.38427734375, 326.1101379394531, 327.54010009765625]

File: SN20USBHX2003654_22.json
Stream: away
Low count: 3
Low values: [365.9418640136719, 387.4161071777344, 383.0639343261719]

File: SN20USBHX2003654_23.json
Stream: away
Low count: 3
Low values: [320.5469970703125, 333.0381164550781, 359.8352355957031]

File: SN20USBHX2003654_24.json
Stream: away
Low count: 3
Low values: [329.3502502441406, 328.6324462890625, 330.290771484375]

File: SN20USBHX2003654_25.json
Stream: away
Low count: 3
Low values: [369.1914367675781, 391.6497497558594, 378.8683166503906]


Module: SN20USBHX2003662
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003662_01.json
Stream: away
Low count: 1
Low values: [391.15045166015625]

File: SN20USBHX2003662_02.json
Stream: away
Low count: 1
Low values: [337.0163269042969]

File: SN20USBHX2003662_03.json
Stream: away
Low count: 1
Low values: [340.43170166015625]

File: SN20USBHX2003662_04.json
Stream: away
Low count: 1
Low values: [360.9233093261719]

File: SN20USBHX2003662_05.json
Stream: away
Low count: 1
Low values: [349.77447509765625]

File: SN20USBHX2003662_06.json
Stream: away
Low count: 1
Low values: [390.81756591796875]

File: SN20USBHX2003662_07.json
Stream: away
Low count: 1
Low values: [346.08697509765625]

File: SN20USBHX2003662_08.json
Stream: away
Low count: 1
Low values: [380.8674011230469]

File: SN20USBHX2003662_09.json
Stream: away
Low count: 1
Low values: [345.6455383300781]

File: SN20USBHX2003662_10.json
Stream: away
Low count: 1
Low values: [394.5398864746094]

File: SN20USBHX2003662_11.json
Stream: away
Low count: 1
Low values: [351.49957275390625]

File: SN20USBHX2003662_12.json
Stream: away
Low count: 1
Low values: [368.1732482910156]

File: SN20USBHX2003662_13.json
Stream: away
Low count: 1
Low values: [337.2982482910156]

File: SN20USBHX2003662_14.json
Stream: away
Low count: 1
Low values: [381.18646240234375]

File: SN20USBHX2003662_15.json
Stream: away
Low count: 1
Low values: [340.354736328125]

File: SN20USBHX2003662_16.json
Stream: away
Low count: 1
Low values: [381.5832214355469]

File: SN20USBHX2003662_17.json
Stream: away
Low count: 1
Low values: [357.15655517578125]

File: SN20USBHX2003662_18.json
Stream: away
Low count: 1
Low values: [375.0927429199219]

File: SN20USBHX2003662_19.json
Stream: away
Low count: 1
Low values: [318.8880615234375]

File: SN20USBHX2003662_20.json
Stream: away
Low count: 1
Low values: [379.2605895996094]

File: SN20USBHX2003662_21.json
Stream: away
Low count: 1
Low values: [343.80865478515625]

File: SN20USBHX2003662_22.json
Stream: away
Low count: 1
Low values: [348.8515319824219]

File: SN20USBHX2003662_23.json
Stream: away
Low count: 1
Low values: [337.6177978515625]

File: SN20USBHX2003662_24.json
Stream: away
Low count: 1
Low values: [328.5325012207031]

File: SN20USBHX2003662_25.json
Stream: away
Low count: 1
Low values: [369.50299072265625]


Module: SN20USBHX2003663
--------------------------------------------------------------------------------
Module total values: 50

File: SN20USBHX2003663_01.json
Stream: under
Low count: 2
Low values: [367.1712951660156, 408.342041015625]

File: SN20USBHX2003663_02.json
Stream: under
Low count: 2
Low values: [329.0376281738281, 350.86920166015625]

File: SN20USBHX2003663_03.json
Stream: under
Low count: 2
Low values: [320.93426513671875, 352.917724609375]

File: SN20USBHX2003663_04.json
Stream: under
Low count: 2
Low values: [369.7412109375, 399.6480712890625]

File: SN20USBHX2003663_05.json
Stream: under
Low count: 2
Low values: [336.99957275390625, 367.43438720703125]

File: SN20USBHX2003663_06.json
Stream: under
Low count: 2
Low values: [360.30126953125, 398.4615173339844]

File: SN20USBHX2003663_07.json
Stream: under
Low count: 2
Low values: [331.2694091796875, 353.5691223144531]

File: SN20USBHX2003663_08.json
Stream: under
Low count: 2
Low values: [375.7410888671875, 409.4457702636719]

File: SN20USBHX2003663_09.json
Stream: under
Low count: 2
Low values: [333.6507263183594, 348.0185546875]

File: SN20USBHX2003663_10.json
Stream: under
Low count: 2
Low values: [367.00048828125, 391.1152038574219]

File: SN20USBHX2003663_11.json
Stream: under
Low count: 2
Low values: [343.2420959472656, 341.7559814453125]

File: SN20USBHX2003663_12.json
Stream: under
Low count: 2
Low values: [375.4416809082031, 415.004638671875]

File: SN20USBHX2003663_13.json
Stream: under
Low count: 2
Low values: [329.9169006347656, 338.4417724609375]

File: SN20USBHX2003663_14.json
Stream: under
Low count: 2
Low values: [372.0238952636719, 385.65545654296875]

File: SN20USBHX2003663_15.json
Stream: under
Low count: 2
Low values: [335.2519836425781, 357.4596252441406]

File: SN20USBHX2003663_16.json
Stream: under
Low count: 2
Low values: [367.70263671875, 385.17169189453125]

File: SN20USBHX2003663_17.json
Stream: under
Low count: 2
Low values: [337.927978515625, 344.28607177734375]

File: SN20USBHX2003663_18.json
Stream: under
Low count: 2
Low values: [360.05572509765625, 389.9124755859375]

File: SN20USBHX2003663_19.json
Stream: under
Low count: 2
Low values: [324.4358215332031, 342.53668212890625]

File: SN20USBHX2003663_20.json
Stream: under
Low count: 2
Low values: [366.0343017578125, 382.1104431152344]

File: SN20USBHX2003663_21.json
Stream: under
Low count: 2
Low values: [327.8058776855469, 347.1826171875]

File: SN20USBHX2003663_22.json
Stream: under
Low count: 2
Low values: [348.6761779785156, 381.4021911621094]

File: SN20USBHX2003663_23.json
Stream: under
Low count: 2
Low values: [326.7950744628906, 354.25262451171875]

File: SN20USBHX2003663_24.json
Stream: under
Low count: 2
Low values: [331.8379821777344, 336.68975830078125]

File: SN20USBHX2003663_25.json
Stream: under
Low count: 2
Low values: [379.2968444824219, 387.48077392578125]


Module: SN20USBHX2003664
--------------------------------------------------------------------------------
Module total values: 50

File: SN20USBHX2003664_01.json
Stream: away
Low count: 3
Low values: [0.0, 354.8539123535156, 382.8277282714844]

File: SN20USBHX2003664_02.json
Stream: away
Low count: 2
Low values: [333.2830810546875, 348.8876953125]

File: SN20USBHX2003664_03.json
Stream: away
Low count: 3
Low values: [0.0, 383.1299133300781, 376.5775451660156]

File: SN20USBHX2003664_04.json
Stream: away
Low count: 2
Low values: [314.1590881347656, 333.5632629394531]

File: SN20USBHX2003664_05.json
Stream: away
Low count: 3
Low values: [0.0, 379.6637878417969, 358.5861511230469]

File: SN20USBHX2003664_06.json
Stream: away
Low count: 2
Low values: [317.4884948730469, 326.8788757324219]

File: SN20USBHX2003664_07.json
Stream: away
Low count: 3
Low values: [0.0, 350.2746276855469, 387.3590393066406]

File: SN20USBHX2003664_08.json
Stream: away
Low count: 2
Low values: [316.68182373046875, 329.310546875]

File: SN20USBHX2003664_09.json
Stream: away
Low count: 3
Low values: [0.0, 384.7708435058594, 384.2527770996094]

File: SN20USBHX2003664_10.json
Stream: away
Low count: 2
Low values: [308.8935546875, 329.3706970214844]

File: SN20USBHX2003664_11.json
Stream: away
Low count: 3
Low values: [0.0, 372.1629638671875, 376.8798522949219]

File: SN20USBHX2003664_12.json
Stream: away
Low count: 2
Low values: [331.8697204589844, 323.20306396484375]

File: SN20USBHX2003664_13.json
Stream: away
Low count: 3
Low values: [0.0, 376.2278747558594, 370.7706298828125]

File: SN20USBHX2003664_14.json
Stream: away
Low count: 2
Low values: [311.51934814453125, 338.04180908203125]

File: SN20USBHX2003664_15.json
Stream: away
Low count: 3
Low values: [0.0, 364.533935546875, 355.90191650390625]

File: SN20USBHX2003664_16.json
Stream: away
Low count: 2
Low values: [311.9809875488281, 342.1610107421875]

File: SN20USBHX2003664_17.json
Stream: away
Low count: 3
Low values: [0.0, 365.3164978027344, 374.19537353515625]

File: SN20USBHX2003664_18.json
Stream: away
Low count: 2
Low values: [340.60614013671875, 341.81036376953125]

File: SN20USBHX2003664_19.json
Stream: away
Low count: 2
Low values: [331.1729431152344, 337.7059326171875]

File: SN20USBHX2003664_20.json
Stream: away
Low count: 3
Low values: [0.0, 360.5726318359375, 375.65771484375]


Module: SN20USBHX2003667
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003667_01.json
Stream: away
Low count: 1
Low values: [359.8743591308594]

File: SN20USBHX2003667_02.json
Stream: away
Low count: 1
Low values: [313.2471008300781]

File: SN20USBHX2003667_03.json
Stream: away
Low count: 1
Low values: [330.02227783203125]

File: SN20USBHX2003667_04.json
Stream: away
Low count: 1
Low values: [371.0847473144531]

File: SN20USBHX2003667_05.json
Stream: away
Low count: 1
Low values: [342.4804382324219]

File: SN20USBHX2003667_06.json
Stream: away
Low count: 1
Low values: [367.9378662109375]

File: SN20USBHX2003667_07.json
Stream: away
Low count: 1
Low values: [335.56182861328125]

File: SN20USBHX2003667_08.json
Stream: away
Low count: 1
Low values: [361.9465637207031]

File: SN20USBHX2003667_09.json
Stream: away
Low count: 1
Low values: [338.177001953125]

File: SN20USBHX2003667_10.json
Stream: away
Low count: 1
Low values: [374.640380859375]

File: SN20USBHX2003667_11.json
Stream: away
Low count: 1
Low values: [313.10382080078125]

File: SN20USBHX2003667_12.json
Stream: away
Low count: 1
Low values: [378.109375]

File: SN20USBHX2003667_13.json
Stream: away
Low count: 1
Low values: [323.1980895996094]

File: SN20USBHX2003667_14.json
Stream: away
Low count: 1
Low values: [362.56903076171875]

File: SN20USBHX2003667_15.json
Stream: away
Low count: 1
Low values: [324.82989501953125]

File: SN20USBHX2003667_16.json
Stream: away
Low count: 1
Low values: [369.20819091796875]

File: SN20USBHX2003667_17.json
Stream: away
Low count: 1
Low values: [324.94049072265625]

File: SN20USBHX2003667_18.json
Stream: away
Low count: 1
Low values: [372.1469421386719]

File: SN20USBHX2003667_19.json
Stream: away
Low count: 1
Low values: [333.8304748535156]

File: SN20USBHX2003667_20.json
Stream: away
Low count: 1
Low values: [369.8415222167969]

File: SN20USBHX2003667_21.json
Stream: away
Low count: 1
Low values: [324.31982421875]

File: SN20USBHX2003667_22.json
Stream: away
Low count: 1
Low values: [371.342529296875]

File: SN20USBHX2003667_23.json
Stream: away
Low count: 1
Low values: [317.2215881347656]

File: SN20USBHX2003667_24.json
Stream: away
Low count: 1
Low values: [307.09893798828125]

File: SN20USBHX2003667_25.json
Stream: away
Low count: 1
Low values: [359.0215759277344]


Module: SN20USBHX2003669
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003669_01.json
Stream: under
Low count: 1
Low values: [380.2232360839844]

File: SN20USBHX2003669_02.json
Stream: under
Low count: 1
Low values: [324.5167541503906]

File: SN20USBHX2003669_03.json
Stream: under
Low count: 1
Low values: [348.3490295410156]

File: SN20USBHX2003669_04.json
Stream: under
Low count: 1
Low values: [388.6878967285156]

File: SN20USBHX2003669_05.json
Stream: under
Low count: 1
Low values: [337.7660827636719]

File: SN20USBHX2003669_06.json
Stream: under
Low count: 1
Low values: [382.644287109375]

File: SN20USBHX2003669_07.json
Stream: under
Low count: 1
Low values: [335.8549499511719]

File: SN20USBHX2003669_08.json
Stream: under
Low count: 1
Low values: [375.3092346191406]

File: SN20USBHX2003669_09.json
Stream: under
Low count: 1
Low values: [338.5195617675781]

File: SN20USBHX2003669_10.json
Stream: under
Low count: 1
Low values: [376.8055725097656]

File: SN20USBHX2003669_11.json
Stream: under
Low count: 1
Low values: [336.1408996582031]

File: SN20USBHX2003669_12.json
Stream: under
Low count: 1
Low values: [374.50225830078125]

File: SN20USBHX2003669_13.json
Stream: under
Low count: 1
Low values: [345.56304931640625]

File: SN20USBHX2003669_14.json
Stream: under
Low count: 1
Low values: [391.3861999511719]

File: SN20USBHX2003669_15.json
Stream: under
Low count: 1
Low values: [336.5382080078125]

File: SN20USBHX2003669_16.json
Stream: under
Low count: 1
Low values: [370.0992431640625]

File: SN20USBHX2003669_17.json
Stream: under
Low count: 1
Low values: [340.53619384765625]

File: SN20USBHX2003669_18.json
Stream: under
Low count: 1
Low values: [376.9580078125]

File: SN20USBHX2003669_19.json
Stream: under
Low count: 1
Low values: [329.4452819824219]

File: SN20USBHX2003669_20.json
Stream: under
Low count: 1
Low values: [384.6522521972656]

File: SN20USBHX2003669_21.json
Stream: under
Low count: 1
Low values: [322.2353515625]

File: SN20USBHX2003669_22.json
Stream: under
Low count: 1
Low values: [381.681396484375]

File: SN20USBHX2003669_23.json
Stream: under
Low count: 1
Low values: [350.3354797363281]

File: SN20USBHX2003669_24.json
Stream: under
Low count: 1
Low values: [344.3107604980469]

File: SN20USBHX2003669_25.json
Stream: under
Low count: 1
Low values: [382.99261474609375]


Module: SN20USBHX2003856
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003856_01.json
Stream: under
Low count: 1
Low values: [356.9549560546875]

File: SN20USBHX2003856_02.json
Stream: under
Low count: 1
Low values: [319.5877685546875]

File: SN20USBHX2003856_03.json
Stream: under
Low count: 1
Low values: [326.9110107421875]

File: SN20USBHX2003856_04.json
Stream: under
Low count: 1
Low values: [358.9737243652344]

File: SN20USBHX2003856_05.json
Stream: under
Low count: 1
Low values: [342.3659973144531]

File: SN20USBHX2003856_06.json
Stream: under
Low count: 1
Low values: [372.6951904296875]

File: SN20USBHX2003856_07.json
Stream: under
Low count: 1
Low values: [329.2369079589844]

File: SN20USBHX2003856_08.json
Stream: under
Low count: 1
Low values: [364.3891296386719]

File: SN20USBHX2003856_09.json
Stream: under
Low count: 1
Low values: [328.1983642578125]

File: SN20USBHX2003856_10.json
Stream: under
Low count: 1
Low values: [354.2589111328125]

File: SN20USBHX2003856_11.json
Stream: under
Low count: 1
Low values: [323.2854919433594]

File: SN20USBHX2003856_12.json
Stream: under
Low count: 1
Low values: [364.9355773925781]

File: SN20USBHX2003856_13.json
Stream: under
Low count: 1
Low values: [333.7088623046875]

File: SN20USBHX2003856_14.json
Stream: under
Low count: 1
Low values: [372.6181335449219]

File: SN20USBHX2003856_15.json
Stream: under
Low count: 1
Low values: [333.5119934082031]

File: SN20USBHX2003856_16.json
Stream: under
Low count: 1
Low values: [364.8365783691406]

File: SN20USBHX2003856_17.json
Stream: under
Low count: 1
Low values: [324.48492431640625]

File: SN20USBHX2003856_18.json
Stream: under
Low count: 1
Low values: [365.0810852050781]

File: SN20USBHX2003856_19.json
Stream: under
Low count: 1
Low values: [307.5636901855469]

File: SN20USBHX2003856_20.json
Stream: under
Low count: 1
Low values: [372.2211608886719]

File: SN20USBHX2003856_21.json
Stream: under
Low count: 1
Low values: [335.9721374511719]

File: SN20USBHX2003856_22.json
Stream: under
Low count: 1
Low values: [358.9326477050781]

File: SN20USBHX2003856_23.json
Stream: under
Low count: 1
Low values: [329.3630676269531]

File: SN20USBHX2003856_24.json
Stream: under
Low count: 1
Low values: [326.6473693847656]

File: SN20USBHX2003856_25.json
Stream: under
Low count: 1
Low values: [363.3739013671875]


Module: SN20USBHX2003859
--------------------------------------------------------------------------------
Module total values: 75

File: SN20USBHX2003859_01.json
Stream: under
Low count: 3
Low values: [372.3740234375, 391.6094970703125, 389.36761474609375]

File: SN20USBHX2003859_02.json
Stream: under
Low count: 3
Low values: [330.5553894042969, 332.0889892578125, 335.2380676269531]

File: SN20USBHX2003859_03.json
Stream: under
Low count: 3
Low values: [334.4468688964844, 360.16644287109375, 337.67730712890625]

File: SN20USBHX2003859_04.json
Stream: under
Low count: 3
Low values: [375.5911560058594, 375.07977294921875, 380.0799255371094]

File: SN20USBHX2003859_05.json
Stream: under
Low count: 3
Low values: [330.1258239746094, 340.2144775390625, 335.4834899902344]

File: SN20USBHX2003859_06.json
Stream: under
Low count: 3
Low values: [386.18389892578125, 393.14691162109375, 378.0790100097656]

File: SN20USBHX2003859_07.json
Stream: under
Low count: 3
Low values: [321.8841247558594, 346.2813415527344, 338.77154541015625]

File: SN20USBHX2003859_08.json
Stream: under
Low count: 3
Low values: [371.3724365234375, 380.3931579589844, 386.1397399902344]

File: SN20USBHX2003859_09.json
Stream: under
Low count: 3
Low values: [330.8965759277344, 322.4505920410156, 325.78424072265625]

File: SN20USBHX2003859_10.json
Stream: under
Low count: 3
Low values: [364.2343444824219, 376.599853515625, 369.0353698730469]

File: SN20USBHX2003859_11.json
Stream: under
Low count: 3
Low values: [340.9156188964844, 335.7647705078125, 343.844482421875]

File: SN20USBHX2003859_12.json
Stream: under
Low count: 3
Low values: [391.4395446777344, 379.6484375, 378.1952209472656]

File: SN20USBHX2003859_13.json
Stream: under
Low count: 3
Low values: [325.49139404296875, 341.0254211425781, 326.4320373535156]

File: SN20USBHX2003859_14.json
Stream: under
Low count: 3
Low values: [377.1858215332031, 379.9262390136719, 368.5401611328125]

File: SN20USBHX2003859_15.json
Stream: under
Low count: 3
Low values: [331.3358459472656, 332.0590515136719, 330.61444091796875]

File: SN20USBHX2003859_16.json
Stream: under
Low count: 3
Low values: [378.79248046875, 371.6246032714844, 391.57855224609375]

File: SN20USBHX2003859_17.json
Stream: under
Low count: 3
Low values: [333.9379577636719, 340.3498229980469, 332.04754638671875]

File: SN20USBHX2003859_18.json
Stream: under
Low count: 3
Low values: [375.56304931640625, 385.0240478515625, 389.8438415527344]

File: SN20USBHX2003859_19.json
Stream: under
Low count: 3
Low values: [325.27081298828125, 351.0276184082031, 332.1548767089844]

File: SN20USBHX2003859_20.json
Stream: under
Low count: 3
Low values: [382.5121154785156, 391.2287292480469, 381.74029541015625]

File: SN20USBHX2003859_21.json
Stream: under
Low count: 3
Low values: [328.0888366699219, 345.4604187011719, 328.2783508300781]

File: SN20USBHX2003859_22.json
Stream: under
Low count: 3
Low values: [385.660400390625, 384.1710205078125, 385.8912048339844]

File: SN20USBHX2003859_23.json
Stream: under
Low count: 3
Low values: [338.5974426269531, 342.75311279296875, 340.47222900390625]

File: SN20USBHX2003859_24.json
Stream: under
Low count: 3
Low values: [322.8376159667969, 331.97979736328125, 336.80712890625]

File: SN20USBHX2003859_25.json
Stream: under
Low count: 3
Low values: [379.0698547363281, 371.07684326171875, 389.4949035644531]


Module: SN20USBHX2003860
--------------------------------------------------------------------------------
Module total values: 175

File: SN20USBHX2003860_01.json
Stream: away
Low count: 7
Low values: [360.1458740234375, 356.37261962890625, 356.85736083984375, 371.25958251953125, 361.46392822265625, 352.7001037597656, 366.43365478515625]

File: SN20USBHX2003860_02.json
Stream: away
Low count: 7
Low values: [316.76373291015625, 319.2815856933594, 327.03961181640625, 309.42950439453125, 310.1988220214844, 331.54791259765625, 317.7989807128906]

File: SN20USBHX2003860_03.json
Stream: away
Low count: 7
Low values: [334.6521911621094, 333.98956298828125, 324.5792541503906, 323.4827575683594, 321.3630065917969, 337.0095520019531, 327.97528076171875]

File: SN20USBHX2003860_04.json
Stream: away
Low count: 7
Low values: [371.08380126953125, 360.6241760253906, 362.9857482910156, 372.3559875488281, 372.04595947265625, 363.5770568847656, 374.0924072265625]

File: SN20USBHX2003860_05.json
Stream: away
Low count: 7
Low values: [319.6269226074219, 322.0284729003906, 318.0835266113281, 320.5042419433594, 321.0519714355469, 323.90692138671875, 336.21038818359375]

File: SN20USBHX2003860_06.json
Stream: away
Low count: 7
Low values: [372.3236389160156, 349.5177917480469, 353.3529052734375, 363.29681396484375, 351.2880554199219, 360.96148681640625, 359.94952392578125]

File: SN20USBHX2003860_07.json
Stream: away
Low count: 7
Low values: [330.9952087402344, 337.1888732910156, 324.1238098144531, 316.36505126953125, 335.555908203125, 332.5494384765625, 324.9830322265625]

File: SN20USBHX2003860_08.json
Stream: away
Low count: 7
Low values: [363.4234313964844, 364.0209655761719, 366.31097412109375, 365.6113586425781, 367.056396484375, 362.4465026855469, 356.6831359863281]

File: SN20USBHX2003860_09.json
Stream: away
Low count: 7
Low values: [315.66925048828125, 322.8318176269531, 325.2309265136719, 316.781982421875, 327.7517395019531, 321.0528869628906, 331.97930908203125]

File: SN20USBHX2003860_10.json
Stream: away
Low count: 7
Low values: [356.1719665527344, 359.1046142578125, 363.2540283203125, 348.2192077636719, 361.8762512207031, 363.42767333984375, 360.52740478515625]

File: SN20USBHX2003860_11.json
Stream: away
Low count: 7
Low values: [310.219482421875, 322.4483642578125, 317.6639099121094, 327.019287109375, 331.974365234375, 324.1044006347656, 324.5017395019531]

File: SN20USBHX2003860_12.json
Stream: away
Low count: 7
Low values: [370.7710876464844, 350.68316650390625, 367.16949462890625, 367.002685546875, 362.2723083496094, 373.78179931640625, 355.6479797363281]

File: SN20USBHX2003860_13.json
Stream: away
Low count: 7
Low values: [308.8984375, 321.5096435546875, 317.75396728515625, 314.81134033203125, 332.48101806640625, 324.5359802246094, 320.87994384765625]

File: SN20USBHX2003860_14.json
Stream: away
Low count: 7
Low values: [368.4258728027344, 374.5695495605469, 360.4042053222656, 358.70208740234375, 347.4949645996094, 365.1444396972656, 363.2652893066406]

File: SN20USBHX2003860_15.json
Stream: away
Low count: 7
Low values: [312.4267272949219, 324.0968322753906, 303.99603271484375, 335.21136474609375, 318.7743835449219, 328.2345275878906, 318.8255615234375]

File: SN20USBHX2003860_16.json
Stream: away
Low count: 7
Low values: [361.135498046875, 381.581298828125, 359.47821044921875, 370.4557189941406, 365.1481018066406, 363.2028503417969, 375.57598876953125]

File: SN20USBHX2003860_17.json
Stream: away
Low count: 7
Low values: [319.7405700683594, 321.3388366699219, 338.579833984375, 330.4875183105469, 326.3544921875, 342.42596435546875, 330.9777526855469]

File: SN20USBHX2003860_18.json
Stream: away
Low count: 7
Low values: [344.8902893066406, 369.59857177734375, 354.6223449707031, 368.18359375, 373.6459655761719, 375.2846374511719, 366.2838439941406]

File: SN20USBHX2003860_19.json
Stream: away
Low count: 7
Low values: [326.8753662109375, 325.7207946777344, 326.3509826660156, 326.9294128417969, 331.49273681640625, 322.6110534667969, 339.92901611328125]

File: SN20USBHX2003860_20.json
Stream: away
Low count: 7
Low values: [363.0482177734375, 377.7718811035156, 360.6842956542969, 378.9997253417969, 356.1095275878906, 360.7624816894531, 363.6900939941406]

File: SN20USBHX2003860_21.json
Stream: away
Low count: 7
Low values: [328.6345520019531, 322.9483947753906, 319.41314697265625, 320.0080871582031, 327.667724609375, 316.3919982910156, 330.4729919433594]

File: SN20USBHX2003860_22.json
Stream: away
Low count: 7
Low values: [361.1549377441406, 370.8066711425781, 361.63311767578125, 374.3709716796875, 353.09002685546875, 367.144775390625, 361.82373046875]

File: SN20USBHX2003860_23.json
Stream: away
Low count: 7
Low values: [327.9974670410156, 333.88238525390625, 336.0110778808594, 330.8882751464844, 323.6745910644531, 323.837158203125, 337.489013671875]

File: SN20USBHX2003860_24.json
Stream: away
Low count: 7
Low values: [328.25579833984375, 321.4921875, 314.9771423339844, 322.95556640625, 317.0638427734375, 335.5247497558594, 332.93017578125]

File: SN20USBHX2003860_25.json
Stream: away
Low count: 7
Low values: [357.9623718261719, 367.1425476074219, 361.9439392089844, 370.3764953613281, 343.193603515625, 370.4360656738281, 351.6946716308594]


Module: SN20USBHX2003863
--------------------------------------------------------------------------------
Module total values: 50

File: SN20USBHX2003863_01.json
Stream: under
Low count: 2
Low values: [380.684814453125, 382.7623291015625]

File: SN20USBHX2003863_02.json
Stream: under
Low count: 2
Low values: [336.76593017578125, 338.8147888183594]

File: SN20USBHX2003863_03.json
Stream: under
Low count: 2
Low values: [342.9833984375, 337.6143798828125]

File: SN20USBHX2003863_04.json
Stream: under
Low count: 2
Low values: [378.10009765625, 365.802490234375]

File: SN20USBHX2003863_05.json
Stream: under
Low count: 2
Low values: [335.1891784667969, 332.4305725097656]

File: SN20USBHX2003863_06.json
Stream: under
Low count: 2
Low values: [377.5415954589844, 382.5835266113281]

File: SN20USBHX2003863_07.json
Stream: under
Low count: 2
Low values: [337.5737609863281, 360.49884033203125]

File: SN20USBHX2003863_08.json
Stream: under
Low count: 2
Low values: [405.73974609375, 371.66766357421875]

File: SN20USBHX2003863_09.json
Stream: under
Low count: 2
Low values: [338.1276550292969, 345.0898742675781]

File: SN20USBHX2003863_10.json
Stream: under
Low count: 2
Low values: [373.999267578125, 389.2329406738281]

File: SN20USBHX2003863_11.json
Stream: under
Low count: 2
Low values: [325.70343017578125, 345.9866638183594]

File: SN20USBHX2003863_12.json
Stream: under
Low count: 2
Low values: [379.3973083496094, 393.0152282714844]

File: SN20USBHX2003863_13.json
Stream: under
Low count: 2
Low values: [340.3223876953125, 328.8446350097656]

File: SN20USBHX2003863_14.json
Stream: under
Low count: 2
Low values: [392.5470886230469, 380.4194641113281]

File: SN20USBHX2003863_15.json
Stream: under
Low count: 2
Low values: [346.561279296875, 350.215087890625]

File: SN20USBHX2003863_16.json
Stream: under
Low count: 2
Low values: [374.1319274902344, 375.703857421875]

File: SN20USBHX2003863_17.json
Stream: under
Low count: 2
Low values: [334.3332214355469, 333.0861511230469]

File: SN20USBHX2003863_18.json
Stream: under
Low count: 2
Low values: [385.9376220703125, 396.3478698730469]

File: SN20USBHX2003863_19.json
Stream: under
Low count: 2
Low values: [326.4036865234375, 347.9832763671875]

File: SN20USBHX2003863_20.json
Stream: under
Low count: 2
Low values: [365.1899719238281, 384.9095764160156]

File: SN20USBHX2003863_21.json
Stream: under
Low count: 2
Low values: [325.5060729980469, 336.5932312011719]

File: SN20USBHX2003863_22.json
Stream: under
Low count: 2
Low values: [379.1608581542969, 381.50128173828125]

File: SN20USBHX2003863_23.json
Stream: under
Low count: 2
Low values: [346.62921142578125, 334.3666076660156]

File: SN20USBHX2003863_24.json
Stream: under
Low count: 2
Low values: [344.9085998535156, 362.7272644042969]

File: SN20USBHX2003863_25.json
Stream: under
Low count: 2
Low values: [369.4051818847656, 390.3965759277344]


Module: SN20USBHX2003866
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003866_01.json
Stream: away
Low count: 1
Low values: [361.0378723144531]

File: SN20USBHX2003866_02.json
Stream: away
Low count: 1
Low values: [343.360595703125]

File: SN20USBHX2003866_03.json
Stream: away
Low count: 1
Low values: [329.91925048828125]

File: SN20USBHX2003866_04.json
Stream: away
Low count: 1
Low values: [360.1622009277344]

File: SN20USBHX2003866_05.json
Stream: away
Low count: 1
Low values: [338.7320251464844]

File: SN20USBHX2003866_06.json
Stream: away
Low count: 1
Low values: [366.5445861816406]

File: SN20USBHX2003866_07.json
Stream: away
Low count: 1
Low values: [334.887451171875]

File: SN20USBHX2003866_08.json
Stream: away
Low count: 1
Low values: [361.77978515625]

File: SN20USBHX2003866_09.json
Stream: away
Low count: 1
Low values: [346.6105041503906]

File: SN20USBHX2003866_10.json
Stream: away
Low count: 1
Low values: [372.499267578125]

File: SN20USBHX2003866_11.json
Stream: away
Low count: 1
Low values: [342.1049499511719]

File: SN20USBHX2003866_12.json
Stream: away
Low count: 1
Low values: [362.9191589355469]

File: SN20USBHX2003866_13.json
Stream: away
Low count: 1
Low values: [326.2938537597656]

File: SN20USBHX2003866_14.json
Stream: away
Low count: 1
Low values: [358.1391906738281]

File: SN20USBHX2003866_15.json
Stream: away
Low count: 1
Low values: [333.7879333496094]

File: SN20USBHX2003866_16.json
Stream: away
Low count: 1
Low values: [369.2255859375]

File: SN20USBHX2003866_17.json
Stream: away
Low count: 1
Low values: [331.898193359375]

File: SN20USBHX2003866_18.json
Stream: away
Low count: 1
Low values: [364.4179382324219]

File: SN20USBHX2003866_19.json
Stream: away
Low count: 1
Low values: [337.9627685546875]

File: SN20USBHX2003866_20.json
Stream: away
Low count: 1
Low values: [377.3117370605469]

File: SN20USBHX2003866_21.json
Stream: away
Low count: 1
Low values: [339.38409423828125]

File: SN20USBHX2003866_22.json
Stream: away
Low count: 1
Low values: [385.2597351074219]

File: SN20USBHX2003866_23.json
Stream: away
Low count: 1
Low values: [321.1669921875]

File: SN20USBHX2003866_24.json
Stream: away
Low count: 1
Low values: [342.1033935546875]

File: SN20USBHX2003866_25.json
Stream: away
Low count: 1
Low values: [374.2787170410156]


Module: SN20USBHX2003868
--------------------------------------------------------------------------------
Module total values: 150

File: SN20USBHX2003868_01.json
Stream: under
Low count: 6
Low values: [355.39996337890625, 382.4373474121094, 358.30035400390625, 382.5611572265625, 379.7789611816406, 374.2231140136719]

File: SN20USBHX2003868_02.json
Stream: under
Low count: 6
Low values: [333.2552795410156, 339.0412902832031, 333.39727783203125, 345.9607238769531, 325.7952575683594, 324.2110290527344]

File: SN20USBHX2003868_03.json
Stream: under
Low count: 6
Low values: [330.0621032714844, 329.3477783203125, 346.459716796875, 334.7213134765625, 323.2984924316406, 335.7048034667969]

File: SN20USBHX2003868_04.json
Stream: under
Low count: 6
Low values: [384.80859375, 366.3006286621094, 373.99908447265625, 354.7066345214844, 383.1724853515625, 365.58306884765625]

File: SN20USBHX2003868_05.json
Stream: under
Low count: 6
Low values: [335.89739990234375, 325.98150634765625, 339.7242126464844, 326.4309997558594, 326.7038879394531, 311.650634765625]

File: SN20USBHX2003868_06.json
Stream: under
Low count: 6
Low values: [383.3171691894531, 370.2364807128906, 369.6703186035156, 361.2280578613281, 373.0542297363281, 378.1531982421875]

File: SN20USBHX2003868_07.json
Stream: under
Low count: 6
Low values: [341.8875732421875, 324.0989074707031, 338.5799560546875, 319.8426208496094, 328.46160888671875, 322.0252990722656]

File: SN20USBHX2003868_08.json
Stream: under
Low count: 6
Low values: [344.7367248535156, 382.52764892578125, 371.6848449707031, 365.2115173339844, 373.04217529296875, 369.2063293457031]

File: SN20USBHX2003868_09.json
Stream: under
Low count: 6
Low values: [321.82269287109375, 346.9578857421875, 318.9754333496094, 322.5865478515625, 332.39935302734375, 322.59405517578125]

File: SN20USBHX2003868_10.json
Stream: under
Low count: 6
Low values: [374.2610778808594, 387.1181945800781, 380.48345947265625, 383.08245849609375, 375.7835388183594, 376.78900146484375]

File: SN20USBHX2003868_11.json
Stream: under
Low count: 6
Low values: [317.3018798828125, 323.117431640625, 323.7698669433594, 318.7588806152344, 322.0042419433594, 325.7308044433594]

File: SN20USBHX2003868_12.json
Stream: under
Low count: 6
Low values: [359.220703125, 365.8946838378906, 386.89239501953125, 372.2618713378906, 352.2366027832031, 369.3807067871094]

File: SN20USBHX2003868_13.json
Stream: under
Low count: 6
Low values: [329.8941345214844, 327.9365234375, 333.6543273925781, 334.5080261230469, 338.56829833984375, 332.5179138183594]

File: SN20USBHX2003868_14.json
Stream: under
Low count: 6
Low values: [364.370361328125, 363.8861999511719, 376.5269470214844, 381.3601379394531, 373.56683349609375, 364.5475158691406]

File: SN20USBHX2003868_15.json
Stream: under
Low count: 6
Low values: [318.699951171875, 319.2561950683594, 339.43096923828125, 318.9075622558594, 333.5848083496094, 325.0353698730469]

File: SN20USBHX2003868_16.json
Stream: under
Low count: 6
Low values: [372.7052917480469, 377.75762939453125, 368.5942077636719, 380.6137390136719, 385.572265625, 376.0300598144531]

File: SN20USBHX2003868_17.json
Stream: under
Low count: 6
Low values: [344.76727294921875, 324.97930908203125, 341.9858703613281, 323.33843994140625, 340.1982421875, 331.0298156738281]

File: SN20USBHX2003868_18.json
Stream: under
Low count: 6
Low values: [363.7056579589844, 375.6402282714844, 375.2843322753906, 375.9145202636719, 374.4043273925781, 364.2991638183594]

File: SN20USBHX2003868_19.json
Stream: under
Low count: 6
Low values: [324.25128173828125, 313.6811218261719, 327.5664367675781, 330.61334228515625, 328.8663024902344, 329.7882995605469]

File: SN20USBHX2003868_20.json
Stream: under
Low count: 6
Low values: [376.77886962890625, 362.782470703125, 367.2436218261719, 372.927978515625, 373.03045654296875, 372.51129150390625]

File: SN20USBHX2003868_21.json
Stream: under
Low count: 6
Low values: [328.4390563964844, 336.0740051269531, 336.32421875, 343.183837890625, 321.6710205078125, 321.30950927734375]

File: SN20USBHX2003868_22.json
Stream: under
Low count: 6
Low values: [367.63055419921875, 348.15869140625, 384.3924560546875, 378.8347473144531, 359.4457092285156, 369.5979919433594]

File: SN20USBHX2003868_23.json
Stream: under
Low count: 6
Low values: [345.1101989746094, 340.68804931640625, 341.7433166503906, 339.65960693359375, 334.5585021972656, 322.47998046875]

File: SN20USBHX2003868_24.json
Stream: under
Low count: 6
Low values: [328.2083740234375, 320.24957275390625, 337.8433837890625, 326.0426025390625, 337.0831604003906, 329.9243469238281]

File: SN20USBHX2003868_25.json
Stream: under
Low count: 6
Low values: [355.01129150390625, 359.48828125, 382.2737731933594, 361.9388122558594, 376.3740234375, 369.55926513671875]


Module: SN20USBHX2003872
--------------------------------------------------------------------------------
Module total values: 100

File: SN20USBHX2003872_01.json
Stream: under
Low count: 2
Low values: [380.7904052734375, 369.6789245605469]

File: SN20USBHX2003872_02.json
Stream: under
Low count: 2
Low values: [331.51055908203125, 327.1020202636719]

File: SN20USBHX2003872_03.json
Stream: under
Low count: 2
Low values: [335.26611328125, 329.727294921875]

File: SN20USBHX2003872_04.json
Stream: under
Low count: 2
Low values: [365.1073303222656, 373.5225524902344]

File: SN20USBHX2003872_05.json
Stream: under
Low count: 2
Low values: [334.82073974609375, 340.7847595214844]

File: SN20USBHX2003872_06.json
Stream: under
Low count: 2
Low values: [370.03741455078125, 353.79449462890625]

File: SN20USBHX2003872_07.json
Stream: under
Low count: 2
Low values: [326.4002685546875, 322.5197448730469]

File: SN20USBHX2003872_08.json
Stream: under
Low count: 2
Low values: [379.0263671875, 373.9930725097656]

File: SN20USBHX2003872_09.json
Stream: under
Low count: 2
Low values: [333.23382568359375, 331.7525634765625]

File: SN20USBHX2003872_10.json
Stream: under
Low count: 2
Low values: [357.5406494140625, 379.102783203125]

File: SN20USBHX2003872_11.json
Stream: under
Low count: 2
Low values: [324.5805969238281, 321.85760498046875]

File: SN20USBHX2003872_12.json
Stream: under
Low count: 2
Low values: [365.4339904785156, 374.3567199707031]

File: SN20USBHX2003872_13.json
Stream: under
Low count: 2
Low values: [334.2727966308594, 342.7838439941406]

File: SN20USBHX2003872_14.json
Stream: under
Low count: 2
Low values: [368.2095947265625, 374.9669189453125]

File: SN20USBHX2003872_15.json
Stream: under
Low count: 2
Low values: [328.4818420410156, 330.7162780761719]

File: SN20USBHX2003872_16.json
Stream: under
Low count: 2
Low values: [368.4283447265625, 370.9145812988281]

File: SN20USBHX2003872_17.json
Stream: under
Low count: 2
Low values: [338.09967041015625, 344.6237487792969]

File: SN20USBHX2003872_18.json
Stream: under
Low count: 2
Low values: [381.6353454589844, 371.59881591796875]

File: SN20USBHX2003872_19.json
Stream: under
Low count: 2
Low values: [338.17626953125, 341.6778564453125]

File: SN20USBHX2003872_20.json
Stream: under
Low count: 2
Low values: [368.6281433105469, 361.2430419921875]

File: SN20USBHX2003872_21.json
Stream: under
Low count: 2
Low values: [338.02655029296875, 330.1282653808594]

File: SN20USBHX2003872_22.json
Stream: under
Low count: 2
Low values: [374.5693359375, 366.281982421875]

File: SN20USBHX2003872_23.json
Stream: under
Low count: 2
Low values: [336.7843322753906, 333.7970275878906]

File: SN20USBHX2003872_24.json
Stream: under
Low count: 2
Low values: [329.01708984375, 342.35272216796875]

File: SN20USBHX2003872_25.json
Stream: under
Low count: 2
Low values: [380.3662414550781, 362.7560119628906]

File: SN20USBHX2003872_01.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_02.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_03.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_04.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_05.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_06.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_07.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_08.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_09.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_10.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_11.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_12.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_13.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_14.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_15.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_16.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_17.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_18.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_19.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_20.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_21.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_22.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_23.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_24.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2003872_25.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]


Module: SN20USBHX2003873
--------------------------------------------------------------------------------
Module total values: 1

File: SN20USBHX2003873_04.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2003904
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003904_01.json
Stream: under
Low count: 1
Low values: [379.6908874511719]

File: SN20USBHX2003904_02.json
Stream: under
Low count: 1
Low values: [328.09100341796875]

File: SN20USBHX2003904_03.json
Stream: under
Low count: 1
Low values: [336.9752197265625]

File: SN20USBHX2003904_04.json
Stream: under
Low count: 1
Low values: [376.7264404296875]

File: SN20USBHX2003904_05.json
Stream: under
Low count: 1
Low values: [336.3179626464844]

File: SN20USBHX2003904_06.json
Stream: under
Low count: 1
Low values: [373.5513610839844]

File: SN20USBHX2003904_07.json
Stream: under
Low count: 1
Low values: [347.4474792480469]

File: SN20USBHX2003904_08.json
Stream: under
Low count: 1
Low values: [396.93402099609375]

File: SN20USBHX2003904_09.json
Stream: under
Low count: 1
Low values: [337.7051696777344]

File: SN20USBHX2003904_10.json
Stream: under
Low count: 1
Low values: [387.6358947753906]

File: SN20USBHX2003904_11.json
Stream: under
Low count: 1
Low values: [330.1537780761719]

File: SN20USBHX2003904_12.json
Stream: under
Low count: 1
Low values: [374.92205810546875]

File: SN20USBHX2003904_13.json
Stream: under
Low count: 1
Low values: [322.2669677734375]

File: SN20USBHX2003904_14.json
Stream: under
Low count: 1
Low values: [368.949951171875]

File: SN20USBHX2003904_15.json
Stream: under
Low count: 1
Low values: [318.009765625]

File: SN20USBHX2003904_16.json
Stream: under
Low count: 1
Low values: [385.18585205078125]

File: SN20USBHX2003904_17.json
Stream: under
Low count: 1
Low values: [340.3361511230469]

File: SN20USBHX2003904_18.json
Stream: under
Low count: 1
Low values: [383.9873352050781]

File: SN20USBHX2003904_19.json
Stream: under
Low count: 1
Low values: [339.0093994140625]

File: SN20USBHX2003904_20.json
Stream: under
Low count: 1
Low values: [378.3925476074219]

File: SN20USBHX2003904_21.json
Stream: under
Low count: 1
Low values: [336.3792724609375]

File: SN20USBHX2003904_22.json
Stream: under
Low count: 1
Low values: [375.3255920410156]

File: SN20USBHX2003904_23.json
Stream: under
Low count: 1
Low values: [336.0798645019531]

File: SN20USBHX2003904_24.json
Stream: under
Low count: 1
Low values: [335.5554504394531]

File: SN20USBHX2003904_25.json
Stream: under
Low count: 1
Low values: [371.038818359375]


Module: SN20USBHX2003905
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003905_01.json
Stream: away
Low count: 1
Low values: [382.7803039550781]

File: SN20USBHX2003905_02.json
Stream: away
Low count: 1
Low values: [333.6535339355469]

File: SN20USBHX2003905_03.json
Stream: away
Low count: 1
Low values: [337.9772644042969]

File: SN20USBHX2003905_04.json
Stream: away
Low count: 1
Low values: [377.4454650878906]

File: SN20USBHX2003905_05.json
Stream: away
Low count: 1
Low values: [314.9100341796875]

File: SN20USBHX2003905_06.json
Stream: away
Low count: 1
Low values: [387.10491943359375]

File: SN20USBHX2003905_07.json
Stream: away
Low count: 1
Low values: [332.0928649902344]

File: SN20USBHX2003905_08.json
Stream: away
Low count: 1
Low values: [390.9646911621094]

File: SN20USBHX2003905_09.json
Stream: away
Low count: 1
Low values: [345.92755126953125]

File: SN20USBHX2003905_10.json
Stream: away
Low count: 1
Low values: [380.1091613769531]

File: SN20USBHX2003905_11.json
Stream: away
Low count: 1
Low values: [341.79949951171875]

File: SN20USBHX2003905_12.json
Stream: away
Low count: 1
Low values: [379.3351745605469]

File: SN20USBHX2003905_13.json
Stream: away
Low count: 1
Low values: [340.89715576171875]

File: SN20USBHX2003905_14.json
Stream: away
Low count: 1
Low values: [390.0810852050781]

File: SN20USBHX2003905_15.json
Stream: away
Low count: 1
Low values: [340.5049743652344]

File: SN20USBHX2003905_16.json
Stream: away
Low count: 1
Low values: [373.7353515625]

File: SN20USBHX2003905_17.json
Stream: away
Low count: 1
Low values: [336.6371154785156]

File: SN20USBHX2003905_18.json
Stream: away
Low count: 1
Low values: [377.096923828125]

File: SN20USBHX2003905_19.json
Stream: away
Low count: 1
Low values: [339.30419921875]

File: SN20USBHX2003905_20.json
Stream: away
Low count: 1
Low values: [375.693603515625]

File: SN20USBHX2003905_21.json
Stream: away
Low count: 1
Low values: [345.5010681152344]

File: SN20USBHX2003905_22.json
Stream: away
Low count: 1
Low values: [395.2127380371094]

File: SN20USBHX2003905_23.json
Stream: away
Low count: 1
Low values: [329.6272277832031]

File: SN20USBHX2003905_24.json
Stream: away
Low count: 1
Low values: [314.63824462890625]

File: SN20USBHX2003905_25.json
Stream: away
Low count: 1
Low values: [384.3828125]


Module: SN20USBHX2003994
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003994_01.json
Stream: under
Low count: 1
Low values: [388.36822509765625]

File: SN20USBHX2003994_02.json
Stream: under
Low count: 1
Low values: [348.8000793457031]

File: SN20USBHX2003994_03.json
Stream: under
Low count: 1
Low values: [337.7607727050781]

File: SN20USBHX2003994_04.json
Stream: under
Low count: 1
Low values: [384.1370849609375]

File: SN20USBHX2003994_05.json
Stream: under
Low count: 1
Low values: [345.7601623535156]

File: SN20USBHX2003994_06.json
Stream: under
Low count: 1
Low values: [388.5559387207031]

File: SN20USBHX2003994_07.json
Stream: under
Low count: 1
Low values: [340.1149597167969]

File: SN20USBHX2003994_08.json
Stream: under
Low count: 1
Low values: [391.2943420410156]

File: SN20USBHX2003994_09.json
Stream: under
Low count: 1
Low values: [341.36859130859375]

File: SN20USBHX2003994_10.json
Stream: under
Low count: 1
Low values: [393.39630126953125]

File: SN20USBHX2003994_11.json
Stream: under
Low count: 1
Low values: [363.03631591796875]

File: SN20USBHX2003994_12.json
Stream: under
Low count: 1
Low values: [381.36639404296875]

File: SN20USBHX2003994_13.json
Stream: under
Low count: 1
Low values: [341.6847839355469]

File: SN20USBHX2003994_14.json
Stream: under
Low count: 1
Low values: [399.0045471191406]

File: SN20USBHX2003994_15.json
Stream: under
Low count: 1
Low values: [343.8092346191406]

File: SN20USBHX2003994_16.json
Stream: under
Low count: 1
Low values: [386.811767578125]

File: SN20USBHX2003994_17.json
Stream: under
Low count: 1
Low values: [358.8565979003906]

File: SN20USBHX2003994_18.json
Stream: under
Low count: 1
Low values: [389.8442077636719]

File: SN20USBHX2003994_19.json
Stream: under
Low count: 1
Low values: [353.418701171875]

File: SN20USBHX2003994_20.json
Stream: under
Low count: 1
Low values: [383.5519104003906]

File: SN20USBHX2003994_21.json
Stream: under
Low count: 1
Low values: [342.16009521484375]

File: SN20USBHX2003994_22.json
Stream: under
Low count: 1
Low values: [393.54876708984375]

File: SN20USBHX2003994_23.json
Stream: under
Low count: 1
Low values: [346.3522033691406]

File: SN20USBHX2003994_24.json
Stream: under
Low count: 1
Low values: [343.69757080078125]

File: SN20USBHX2003994_25.json
Stream: under
Low count: 1
Low values: [382.52435302734375]


Module: SN20USBHX2004018
--------------------------------------------------------------------------------
Module total values: 50

File: SN20USBHX2004018_01.json
Stream: under
Low count: 2
Low values: [365.95697021484375, 361.6342468261719]

File: SN20USBHX2004018_02.json
Stream: under
Low count: 2
Low values: [326.0276794433594, 321.39642333984375]

File: SN20USBHX2004018_03.json
Stream: under
Low count: 2
Low values: [331.0989990234375, 330.1045227050781]

File: SN20USBHX2004018_04.json
Stream: under
Low count: 2
Low values: [385.8900146484375, 363.69268798828125]

File: SN20USBHX2004018_05.json
Stream: under
Low count: 2
Low values: [328.0826721191406, 320.9344787597656]

File: SN20USBHX2004018_06.json
Stream: under
Low count: 2
Low values: [382.9528503417969, 377.2987060546875]

File: SN20USBHX2004018_07.json
Stream: under
Low count: 2
Low values: [319.4356994628906, 341.64837646484375]

File: SN20USBHX2004018_08.json
Stream: under
Low count: 2
Low values: [362.3742980957031, 374.6937255859375]

File: SN20USBHX2004018_09.json
Stream: under
Low count: 2
Low values: [337.76910400390625, 334.8027038574219]

File: SN20USBHX2004018_10.json
Stream: under
Low count: 2
Low values: [378.0543518066406, 360.3462219238281]

File: SN20USBHX2004018_11.json
Stream: under
Low count: 2
Low values: [348.4001770019531, 324.2536315917969]

File: SN20USBHX2004018_12.json
Stream: under
Low count: 2
Low values: [366.436279296875, 374.644775390625]

File: SN20USBHX2004018_13.json
Stream: under
Low count: 2
Low values: [331.0335693359375, 336.8685607910156]

File: SN20USBHX2004018_14.json
Stream: under
Low count: 2
Low values: [372.3030700683594, 386.8083190917969]

File: SN20USBHX2004018_15.json
Stream: under
Low count: 2
Low values: [338.90728759765625, 359.9437561035156]

File: SN20USBHX2004018_16.json
Stream: under
Low count: 2
Low values: [380.7121887207031, 376.24151611328125]

File: SN20USBHX2004018_17.json
Stream: under
Low count: 2
Low values: [350.6062927246094, 333.5131530761719]

File: SN20USBHX2004018_18.json
Stream: under
Low count: 2
Low values: [389.3332214355469, 356.62750244140625]

File: SN20USBHX2004018_19.json
Stream: under
Low count: 2
Low values: [337.983642578125, 320.1782531738281]

File: SN20USBHX2004018_20.json
Stream: under
Low count: 2
Low values: [373.03350830078125, 384.99896240234375]

File: SN20USBHX2004018_21.json
Stream: under
Low count: 2
Low values: [322.67633056640625, 333.26776123046875]

File: SN20USBHX2004018_22.json
Stream: under
Low count: 2
Low values: [366.3409729003906, 376.0867919921875]

File: SN20USBHX2004018_23.json
Stream: under
Low count: 2
Low values: [338.147705078125, 334.3253173828125]

File: SN20USBHX2004018_24.json
Stream: under
Low count: 2
Low values: [336.4988098144531, 336.7753601074219]

File: SN20USBHX2004018_25.json
Stream: under
Low count: 2
Low values: [382.1230773925781, 375.4787902832031]


Module: SN20USBHX2004020
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2004020_01.json
Stream: away
Low count: 1
Low values: [391.1294860839844]

File: SN20USBHX2004020_02.json
Stream: away
Low count: 1
Low values: [332.29730224609375]

File: SN20USBHX2004020_03.json
Stream: away
Low count: 1
Low values: [334.7083740234375]

File: SN20USBHX2004020_04.json
Stream: away
Low count: 1
Low values: [375.2572021484375]

File: SN20USBHX2004020_05.json
Stream: away
Low count: 1
Low values: [342.0749816894531]

File: SN20USBHX2004020_06.json
Stream: away
Low count: 1
Low values: [371.6555480957031]

File: SN20USBHX2004020_07.json
Stream: away
Low count: 1
Low values: [331.2015075683594]

File: SN20USBHX2004020_08.json
Stream: away
Low count: 1
Low values: [379.8437805175781]

File: SN20USBHX2004020_09.json
Stream: away
Low count: 1
Low values: [330.4881591796875]

File: SN20USBHX2004020_10.json
Stream: away
Low count: 1
Low values: [367.5028381347656]

File: SN20USBHX2004020_11.json
Stream: away
Low count: 1
Low values: [341.408203125]

File: SN20USBHX2004020_12.json
Stream: away
Low count: 1
Low values: [369.21099853515625]

File: SN20USBHX2004020_13.json
Stream: away
Low count: 1
Low values: [335.7449035644531]

File: SN20USBHX2004020_14.json
Stream: away
Low count: 1
Low values: [381.13043212890625]

File: SN20USBHX2004020_15.json
Stream: away
Low count: 1
Low values: [342.4273986816406]

File: SN20USBHX2004020_16.json
Stream: away
Low count: 1
Low values: [378.4972839355469]

File: SN20USBHX2004020_17.json
Stream: away
Low count: 1
Low values: [347.6024475097656]

File: SN20USBHX2004020_18.json
Stream: away
Low count: 1
Low values: [386.4782409667969]

File: SN20USBHX2004020_19.json
Stream: away
Low count: 1
Low values: [342.2564697265625]

File: SN20USBHX2004020_20.json
Stream: away
Low count: 1
Low values: [367.9775695800781]

File: SN20USBHX2004020_21.json
Stream: away
Low count: 1
Low values: [342.9295959472656]

File: SN20USBHX2004020_22.json
Stream: away
Low count: 1
Low values: [376.1631774902344]

File: SN20USBHX2004020_23.json
Stream: away
Low count: 1
Low values: [336.4495849609375]

File: SN20USBHX2004020_24.json
Stream: away
Low count: 1
Low values: [337.8448791503906]

File: SN20USBHX2004020_25.json
Stream: away
Low count: 1
Low values: [371.5912780761719]


Module: SN20USBHX2004021
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2004021_01.json
Stream: under
Low count: 1
Low values: [379.3783264160156]

File: SN20USBHX2004021_02.json
Stream: under
Low count: 1
Low values: [340.2444763183594]

File: SN20USBHX2004021_03.json
Stream: under
Low count: 1
Low values: [348.571044921875]

File: SN20USBHX2004021_04.json
Stream: under
Low count: 1
Low values: [395.76043701171875]

File: SN20USBHX2004021_05.json
Stream: under
Low count: 1
Low values: [334.3205261230469]

File: SN20USBHX2004021_06.json
Stream: under
Low count: 1
Low values: [386.8601379394531]

File: SN20USBHX2004021_07.json
Stream: under
Low count: 1
Low values: [338.56292724609375]

File: SN20USBHX2004021_08.json
Stream: under
Low count: 1
Low values: [378.988525390625]

File: SN20USBHX2004021_09.json
Stream: under
Low count: 1
Low values: [326.2529602050781]

File: SN20USBHX2004021_10.json
Stream: under
Low count: 1
Low values: [384.62127685546875]

File: SN20USBHX2004021_11.json
Stream: under
Low count: 1
Low values: [344.2881774902344]

File: SN20USBHX2004021_12.json
Stream: under
Low count: 1
Low values: [372.6732482910156]

File: SN20USBHX2004021_13.json
Stream: under
Low count: 1
Low values: [335.87945556640625]

File: SN20USBHX2004021_14.json
Stream: under
Low count: 1
Low values: [380.7837219238281]

File: SN20USBHX2004021_15.json
Stream: under
Low count: 1
Low values: [340.17108154296875]

File: SN20USBHX2004021_16.json
Stream: under
Low count: 1
Low values: [391.5010070800781]

File: SN20USBHX2004021_17.json
Stream: under
Low count: 1
Low values: [345.52154541015625]

File: SN20USBHX2004021_18.json
Stream: under
Low count: 1
Low values: [384.6806640625]

File: SN20USBHX2004021_19.json
Stream: under
Low count: 1
Low values: [344.51947021484375]

File: SN20USBHX2004021_20.json
Stream: under
Low count: 1
Low values: [388.3182373046875]

File: SN20USBHX2004021_21.json
Stream: under
Low count: 1
Low values: [348.8303527832031]

File: SN20USBHX2004021_22.json
Stream: under
Low count: 1
Low values: [382.689697265625]

File: SN20USBHX2004021_23.json
Stream: under
Low count: 1
Low values: [350.8985290527344]

File: SN20USBHX2004021_24.json
Stream: under
Low count: 1
Low values: [336.7129821777344]

File: SN20USBHX2004021_25.json
Stream: under
Low count: 1
Low values: [380.3202819824219]


Module: SN20USBHX2004159
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2004159_01.json
Stream: away
Low count: 1
Low values: [375.6661376953125]

File: SN20USBHX2004159_02.json
Stream: away
Low count: 1
Low values: [328.39056396484375]

File: SN20USBHX2004159_03.json
Stream: away
Low count: 1
Low values: [330.2976379394531]

File: SN20USBHX2004159_04.json
Stream: away
Low count: 1
Low values: [374.56634521484375]

File: SN20USBHX2004159_05.json
Stream: away
Low count: 1
Low values: [322.7008972167969]

File: SN20USBHX2004159_06.json
Stream: away
Low count: 1
Low values: [373.1352233886719]

File: SN20USBHX2004159_07.json
Stream: away
Low count: 1
Low values: [317.76220703125]

File: SN20USBHX2004159_08.json
Stream: away
Low count: 1
Low values: [362.3617248535156]

File: SN20USBHX2004159_09.json
Stream: away
Low count: 1
Low values: [326.6747741699219]

File: SN20USBHX2004159_10.json
Stream: away
Low count: 1
Low values: [375.0511169433594]

File: SN20USBHX2004159_11.json
Stream: away
Low count: 1
Low values: [342.3540344238281]

File: SN20USBHX2004159_12.json
Stream: away
Low count: 1
Low values: [367.953369140625]

File: SN20USBHX2004159_13.json
Stream: away
Low count: 1
Low values: [324.5297546386719]

File: SN20USBHX2004159_14.json
Stream: away
Low count: 1
Low values: [366.1027526855469]

File: SN20USBHX2004159_15.json
Stream: away
Low count: 1
Low values: [337.01788330078125]

File: SN20USBHX2004159_16.json
Stream: away
Low count: 1
Low values: [358.2366638183594]

File: SN20USBHX2004159_17.json
Stream: away
Low count: 1
Low values: [324.1234436035156]

File: SN20USBHX2004159_18.json
Stream: away
Low count: 1
Low values: [363.3747863769531]

File: SN20USBHX2004159_19.json
Stream: away
Low count: 1
Low values: [327.76318359375]

File: SN20USBHX2004159_20.json
Stream: away
Low count: 1
Low values: [370.88519287109375]

File: SN20USBHX2004159_21.json
Stream: away
Low count: 1
Low values: [329.7605285644531]

File: SN20USBHX2004159_22.json
Stream: away
Low count: 1
Low values: [372.56201171875]

File: SN20USBHX2004159_23.json
Stream: away
Low count: 1
Low values: [336.17095947265625]

File: SN20USBHX2004159_24.json
Stream: away
Low count: 1
Low values: [319.30010986328125]

File: SN20USBHX2004159_25.json
Stream: away
Low count: 1
Low values: [371.3931579589844]


Module: SN20USBHX2004160
--------------------------------------------------------------------------------
Module total values: 256

File: SN20USBHX2004160_05.json
Stream: under
Low count: 128
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

File: SN20USBHX2004160_05.json
Stream: away
Low count: 128
Low values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


Module: SN20USBHX2004167
--------------------------------------------------------------------------------
Module total values: 100

File: SN20USBHX2004167_01.json
Stream: under
Low count: 3
Low values: [359.9295349121094, 375.6889343261719, 373.28253173828125]

File: SN20USBHX2004167_02.json
Stream: under
Low count: 3
Low values: [334.3975830078125, 340.8230285644531, 320.5147399902344]

File: SN20USBHX2004167_03.json
Stream: under
Low count: 3
Low values: [326.0968933105469, 347.9407653808594, 324.4166259765625]

File: SN20USBHX2004167_04.json
Stream: under
Low count: 3
Low values: [368.1977844238281, 368.96337890625, 369.4935607910156]

File: SN20USBHX2004167_05.json
Stream: under
Low count: 3
Low values: [338.3600769042969, 343.4096984863281, 326.88189697265625]

File: SN20USBHX2004167_06.json
Stream: under
Low count: 3
Low values: [373.5025939941406, 378.15869140625, 360.9374694824219]

File: SN20USBHX2004167_07.json
Stream: under
Low count: 3
Low values: [336.9571228027344, 332.9790344238281, 324.01727294921875]

File: SN20USBHX2004167_08.json
Stream: under
Low count: 3
Low values: [375.2678527832031, 368.4495849609375, 361.79931640625]

File: SN20USBHX2004167_09.json
Stream: under
Low count: 3
Low values: [324.62042236328125, 326.99664306640625, 314.74822998046875]

File: SN20USBHX2004167_10.json
Stream: under
Low count: 3
Low values: [378.75775146484375, 369.25177001953125, 373.4666442871094]

File: SN20USBHX2004167_11.json
Stream: under
Low count: 3
Low values: [336.95758056640625, 336.51397705078125, 330.4737854003906]

File: SN20USBHX2004167_12.json
Stream: under
Low count: 3
Low values: [374.3384704589844, 377.6943054199219, 368.6531066894531]

File: SN20USBHX2004167_13.json
Stream: under
Low count: 3
Low values: [328.21209716796875, 332.336181640625, 321.72882080078125]

File: SN20USBHX2004167_14.json
Stream: under
Low count: 3
Low values: [377.52545166015625, 368.4006042480469, 366.3777770996094]

File: SN20USBHX2004167_15.json
Stream: under
Low count: 3
Low values: [330.92425537109375, 326.8641357421875, 326.3588562011719]

File: SN20USBHX2004167_16.json
Stream: under
Low count: 3
Low values: [366.7191162109375, 387.4853210449219, 362.5846862792969]

File: SN20USBHX2004167_17.json
Stream: under
Low count: 3
Low values: [331.0445251464844, 331.28082275390625, 333.4806823730469]

File: SN20USBHX2004167_18.json
Stream: under
Low count: 3
Low values: [352.57330322265625, 376.98333740234375, 365.51202392578125]

File: SN20USBHX2004167_19.json
Stream: under
Low count: 3
Low values: [326.7239074707031, 335.3401794433594, 317.9468994140625]

File: SN20USBHX2004167_20.json
Stream: under
Low count: 3
Low values: [364.73138427734375, 372.8180236816406, 367.79058837890625]

File: SN20USBHX2004167_21.json
Stream: under
Low count: 3
Low values: [333.5245666503906, 341.6063537597656, 308.56396484375]

File: SN20USBHX2004167_22.json
Stream: under
Low count: 3
Low values: [373.40576171875, 373.156982421875, 356.16552734375]

File: SN20USBHX2004167_23.json
Stream: under
Low count: 3
Low values: [325.0855407714844, 350.0502624511719, 318.7794494628906]

File: SN20USBHX2004167_24.json
Stream: under
Low count: 3
Low values: [339.1767883300781, 327.1041259765625, 315.0621032714844]

File: SN20USBHX2004167_25.json
Stream: under
Low count: 3
Low values: [369.4915771484375, 361.67535400390625, 361.49249267578125]

File: SN20USBHX2004167_01.json
Stream: away
Low count: 1
Low values: [360.1285400390625]

File: SN20USBHX2004167_02.json
Stream: away
Low count: 1
Low values: [328.7076416015625]

File: SN20USBHX2004167_03.json
Stream: away
Low count: 1
Low values: [331.17108154296875]

File: SN20USBHX2004167_04.json
Stream: away
Low count: 1
Low values: [373.32525634765625]

File: SN20USBHX2004167_05.json
Stream: away
Low count: 1
Low values: [337.7658386230469]

File: SN20USBHX2004167_06.json
Stream: away
Low count: 1
Low values: [375.0653076171875]

File: SN20USBHX2004167_07.json
Stream: away
Low count: 1
Low values: [331.2317810058594]

File: SN20USBHX2004167_08.json
Stream: away
Low count: 1
Low values: [360.4026184082031]

File: SN20USBHX2004167_09.json
Stream: away
Low count: 1
Low values: [319.1171875]

File: SN20USBHX2004167_10.json
Stream: away
Low count: 1
Low values: [382.70855712890625]

File: SN20USBHX2004167_11.json
Stream: away
Low count: 1
Low values: [333.44281005859375]

File: SN20USBHX2004167_12.json
Stream: away
Low count: 1
Low values: [357.2721862792969]

File: SN20USBHX2004167_13.json
Stream: away
Low count: 1
Low values: [331.4504089355469]

File: SN20USBHX2004167_14.json
Stream: away
Low count: 1
Low values: [364.3797302246094]

File: SN20USBHX2004167_15.json
Stream: away
Low count: 1
Low values: [346.0127258300781]

File: SN20USBHX2004167_16.json
Stream: away
Low count: 1
Low values: [381.4237365722656]

File: SN20USBHX2004167_17.json
Stream: away
Low count: 1
Low values: [318.4898376464844]

File: SN20USBHX2004167_18.json
Stream: away
Low count: 1
Low values: [360.5631408691406]

File: SN20USBHX2004167_19.json
Stream: away
Low count: 1
Low values: [315.624267578125]

File: SN20USBHX2004167_20.json
Stream: away
Low count: 1
Low values: [363.83233642578125]

File: SN20USBHX2004167_21.json
Stream: away
Low count: 1
Low values: [317.7385559082031]

File: SN20USBHX2004167_22.json
Stream: away
Low count: 1
Low values: [373.68017578125]

File: SN20USBHX2004167_23.json
Stream: away
Low count: 1
Low values: [337.90643310546875]

File: SN20USBHX2004167_24.json
Stream: away
Low count: 1
Low values: [338.4239501953125]

File: SN20USBHX2004167_25.json
Stream: away
Low count: 1
Low values: [366.9954833984375]


Module: SN20USBHX2004168
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2004168_01.json
Stream: under
Low count: 1
Low values: [379.5183410644531]

File: SN20USBHX2004168_02.json
Stream: under
Low count: 1
Low values: [351.9434814453125]

File: SN20USBHX2004168_03.json
Stream: under
Low count: 1
Low values: [361.1265563964844]

File: SN20USBHX2004168_04.json
Stream: under
Low count: 1
Low values: [373.2882385253906]

File: SN20USBHX2004168_05.json
Stream: under
Low count: 1
Low values: [329.7261962890625]

File: SN20USBHX2004168_06.json
Stream: under
Low count: 1
Low values: [384.923095703125]

File: SN20USBHX2004168_07.json
Stream: under
Low count: 1
Low values: [338.1983642578125]

File: SN20USBHX2004168_08.json
Stream: under
Low count: 1
Low values: [388.0196838378906]

File: SN20USBHX2004168_09.json
Stream: under
Low count: 1
Low values: [343.1163330078125]

File: SN20USBHX2004168_10.json
Stream: under
Low count: 1
Low values: [385.9440002441406]

File: SN20USBHX2004168_11.json
Stream: under
Low count: 1
Low values: [322.8553771972656]

File: SN20USBHX2004168_12.json
Stream: under
Low count: 1
Low values: [379.4869384765625]

File: SN20USBHX2004168_13.json
Stream: under
Low count: 1
Low values: [348.53253173828125]

File: SN20USBHX2004168_14.json
Stream: under
Low count: 1
Low values: [370.94171142578125]

File: SN20USBHX2004168_15.json
Stream: under
Low count: 1
Low values: [328.0871276855469]

File: SN20USBHX2004168_16.json
Stream: under
Low count: 1
Low values: [385.2055358886719]

File: SN20USBHX2004168_17.json
Stream: under
Low count: 1
Low values: [345.85943603515625]

File: SN20USBHX2004168_18.json
Stream: under
Low count: 1
Low values: [381.3818664550781]

File: SN20USBHX2004168_19.json
Stream: under
Low count: 1
Low values: [335.31231689453125]

File: SN20USBHX2004168_20.json
Stream: under
Low count: 1
Low values: [377.43756103515625]

File: SN20USBHX2004168_21.json
Stream: under
Low count: 1
Low values: [328.246826171875]

File: SN20USBHX2004168_22.json
Stream: under
Low count: 1
Low values: [387.283447265625]

File: SN20USBHX2004168_23.json
Stream: under
Low count: 1
Low values: [341.5447692871094]

File: SN20USBHX2004168_24.json
Stream: under
Low count: 1
Low values: [334.9928283691406]

File: SN20USBHX2004168_25.json
Stream: under
Low count: 1
Low values: [378.3330993652344]


Module: SN20USBHX2004169
--------------------------------------------------------------------------------
Module total values: 75

File: SN20USBHX2004169_01.json
Stream: under
Low count: 3
Low values: [379.07464599609375, 372.0311584472656, 369.8923034667969]

File: SN20USBHX2004169_02.json
Stream: under
Low count: 3
Low values: [337.0861511230469, 343.5809326171875, 325.9825439453125]

File: SN20USBHX2004169_03.json
Stream: under
Low count: 3
Low values: [342.8326721191406, 335.9608459472656, 348.1848449707031]

File: SN20USBHX2004169_04.json
Stream: under
Low count: 3
Low values: [386.8572998046875, 376.5590515136719, 381.3193664550781]

File: SN20USBHX2004169_05.json
Stream: under
Low count: 3
Low values: [333.7052917480469, 343.1541442871094, 335.5812683105469]

File: SN20USBHX2004169_06.json
Stream: under
Low count: 3
Low values: [366.8436584472656, 380.3023681640625, 366.69097900390625]

File: SN20USBHX2004169_07.json
Stream: under
Low count: 3
Low values: [351.1294250488281, 318.9424743652344, 331.86358642578125]

File: SN20USBHX2004169_08.json
Stream: under
Low count: 3
Low values: [392.11016845703125, 366.36895751953125, 381.60809326171875]

File: SN20USBHX2004169_09.json
Stream: under
Low count: 3
Low values: [336.3283996582031, 327.6214294433594, 332.20068359375]

File: SN20USBHX2004169_10.json
Stream: under
Low count: 3
Low values: [377.595703125, 374.89862060546875, 366.110107421875]

File: SN20USBHX2004169_11.json
Stream: under
Low count: 3
Low values: [345.7622985839844, 339.7547912597656, 337.3789367675781]

File: SN20USBHX2004169_12.json
Stream: under
Low count: 3
Low values: [382.7999267578125, 373.7827453613281, 369.5166320800781]

File: SN20USBHX2004169_13.json
Stream: under
Low count: 3
Low values: [330.14959716796875, 321.86883544921875, 325.6361389160156]

File: SN20USBHX2004169_14.json
Stream: under
Low count: 3
Low values: [369.6129150390625, 372.479248046875, 370.0146484375]

File: SN20USBHX2004169_15.json
Stream: under
Low count: 3
Low values: [339.8119201660156, 330.5046691894531, 339.9654235839844]

File: SN20USBHX2004169_16.json
Stream: under
Low count: 3
Low values: [372.1153564453125, 371.2359313964844, 365.2039489746094]

File: SN20USBHX2004169_17.json
Stream: under
Low count: 3
Low values: [344.2514343261719, 338.35113525390625, 339.5364685058594]

File: SN20USBHX2004169_18.json
Stream: under
Low count: 3
Low values: [383.7991027832031, 377.0624084472656, 374.21942138671875]

File: SN20USBHX2004169_19.json
Stream: under
Low count: 3
Low values: [334.9357604980469, 333.01129150390625, 338.53912353515625]

File: SN20USBHX2004169_20.json
Stream: under
Low count: 3
Low values: [363.4326171875, 372.0318908691406, 371.40679931640625]

File: SN20USBHX2004169_21.json
Stream: under
Low count: 3
Low values: [334.4584655761719, 329.7800598144531, 335.9224853515625]

File: SN20USBHX2004169_22.json
Stream: under
Low count: 3
Low values: [376.6912536621094, 371.1199951171875, 371.4764404296875]

File: SN20USBHX2004169_23.json
Stream: under
Low count: 3
Low values: [358.5652160644531, 341.6390075683594, 334.37542724609375]

File: SN20USBHX2004169_24.json
Stream: under
Low count: 3
Low values: [331.4137878417969, 332.226806640625, 338.33477783203125]

File: SN20USBHX2004169_25.json
Stream: under
Low count: 3
Low values: [377.1912841796875, 375.07989501953125, 377.3813171386719]


Module: SN20USBHX2004172
--------------------------------------------------------------------------------
Module total values: 100

File: SN20USBHX2004172_01.json
Stream: under
Low count: 3
Low values: [364.1956481933594, 361.8276062011719, 383.0595397949219]

File: SN20USBHX2004172_02.json
Stream: under
Low count: 3
Low values: [347.3800048828125, 336.9989929199219, 322.06280517578125]

File: SN20USBHX2004172_03.json
Stream: under
Low count: 3
Low values: [342.82684326171875, 343.3163757324219, 340.8682556152344]

File: SN20USBHX2004172_04.json
Stream: under
Low count: 3
Low values: [380.1456604003906, 377.5954284667969, 382.0201110839844]

File: SN20USBHX2004172_05.json
Stream: under
Low count: 3
Low values: [326.2081604003906, 353.6391906738281, 325.7630920410156]

File: SN20USBHX2004172_06.json
Stream: under
Low count: 3
Low values: [389.9234619140625, 392.8564147949219, 374.4870910644531]

File: SN20USBHX2004172_07.json
Stream: under
Low count: 3
Low values: [336.3977966308594, 340.2759094238281, 333.97894287109375]

File: SN20USBHX2004172_08.json
Stream: under
Low count: 3
Low values: [385.05169677734375, 387.48040771484375, 365.986572265625]

File: SN20USBHX2004172_09.json
Stream: under
Low count: 3
Low values: [323.04449462890625, 329.255615234375, 346.1919860839844]

File: SN20USBHX2004172_10.json
Stream: under
Low count: 3
Low values: [371.783935546875, 374.6346740722656, 365.11474609375]

File: SN20USBHX2004172_11.json
Stream: under
Low count: 3
Low values: [331.4618225097656, 337.2742919921875, 346.4332580566406]

File: SN20USBHX2004172_12.json
Stream: under
Low count: 3
Low values: [366.1476745605469, 383.27197265625, 374.5396423339844]

File: SN20USBHX2004172_13.json
Stream: under
Low count: 3
Low values: [329.6227111816406, 326.80889892578125, 339.8553161621094]

File: SN20USBHX2004172_14.json
Stream: under
Low count: 3
Low values: [379.23895263671875, 383.1769104003906, 378.95098876953125]

File: SN20USBHX2004172_15.json
Stream: under
Low count: 3
Low values: [341.6924743652344, 337.2737731933594, 344.608642578125]

File: SN20USBHX2004172_16.json
Stream: under
Low count: 3
Low values: [378.6750183105469, 383.0788269042969, 377.3340759277344]

File: SN20USBHX2004172_17.json
Stream: under
Low count: 3
Low values: [335.99945068359375, 329.09149169921875, 339.35162353515625]

File: SN20USBHX2004172_18.json
Stream: under
Low count: 3
Low values: [379.42236328125, 390.6651916503906, 382.2269592285156]

File: SN20USBHX2004172_19.json
Stream: under
Low count: 3
Low values: [331.2760925292969, 337.283935546875, 335.5693359375]

File: SN20USBHX2004172_20.json
Stream: under
Low count: 3
Low values: [368.8046875, 376.5071105957031, 377.24139404296875]

File: SN20USBHX2004172_21.json
Stream: under
Low count: 3
Low values: [312.32476806640625, 345.8609313964844, 337.36785888671875]

File: SN20USBHX2004172_22.json
Stream: under
Low count: 3
Low values: [372.9657287597656, 376.49920654296875, 378.6931457519531]

File: SN20USBHX2004172_23.json
Stream: under
Low count: 3
Low values: [349.92645263671875, 340.2771911621094, 350.1128845214844]

File: SN20USBHX2004172_24.json
Stream: under
Low count: 3
Low values: [338.9259338378906, 338.7113037109375, 339.6991271972656]

File: SN20USBHX2004172_25.json
Stream: under
Low count: 3
Low values: [383.0755920410156, 383.245849609375, 395.0010070800781]

File: SN20USBHX2004172_01.json
Stream: away
Low count: 1
Low values: [378.6748962402344]

File: SN20USBHX2004172_02.json
Stream: away
Low count: 1
Low values: [338.1507568359375]

File: SN20USBHX2004172_03.json
Stream: away
Low count: 1
Low values: [357.3181457519531]

File: SN20USBHX2004172_04.json
Stream: away
Low count: 1
Low values: [382.30889892578125]

File: SN20USBHX2004172_05.json
Stream: away
Low count: 1
Low values: [334.46160888671875]

File: SN20USBHX2004172_06.json
Stream: away
Low count: 1
Low values: [380.1348876953125]

File: SN20USBHX2004172_07.json
Stream: away
Low count: 1
Low values: [345.65643310546875]

File: SN20USBHX2004172_08.json
Stream: away
Low count: 1
Low values: [396.1023254394531]

File: SN20USBHX2004172_09.json
Stream: away
Low count: 1
Low values: [315.2575988769531]

File: SN20USBHX2004172_10.json
Stream: away
Low count: 1
Low values: [389.6102600097656]

File: SN20USBHX2004172_11.json
Stream: away
Low count: 1
Low values: [339.15325927734375]

File: SN20USBHX2004172_12.json
Stream: away
Low count: 1
Low values: [368.838134765625]

File: SN20USBHX2004172_13.json
Stream: away
Low count: 1
Low values: [333.4317321777344]

File: SN20USBHX2004172_14.json
Stream: away
Low count: 1
Low values: [360.1307067871094]

File: SN20USBHX2004172_15.json
Stream: away
Low count: 1
Low values: [342.5915222167969]

File: SN20USBHX2004172_16.json
Stream: away
Low count: 1
Low values: [371.1839599609375]

File: SN20USBHX2004172_17.json
Stream: away
Low count: 1
Low values: [335.7601318359375]

File: SN20USBHX2004172_18.json
Stream: away
Low count: 1
Low values: [369.5998840332031]

File: SN20USBHX2004172_19.json
Stream: away
Low count: 1
Low values: [331.7259826660156]

File: SN20USBHX2004172_20.json
Stream: away
Low count: 1
Low values: [368.4811096191406]

File: SN20USBHX2004172_21.json
Stream: away
Low count: 1
Low values: [333.83087158203125]

File: SN20USBHX2004172_22.json
Stream: away
Low count: 1
Low values: [372.1729736328125]

File: SN20USBHX2004172_23.json
Stream: away
Low count: 1
Low values: [334.2804870605469]

File: SN20USBHX2004172_24.json
Stream: away
Low count: 1
Low values: [342.2506408691406]

File: SN20USBHX2004172_25.json
Stream: away
Low count: 1
Low values: [378.14813232421875]


Module: SN20USBHX2004174
--------------------------------------------------------------------------------
Module total values: 68

File: SN20USBHX2004174_01.json
Stream: under
Low count: 2
Low values: [377.6978759765625, 0.0]

File: SN20USBHX2004174_02.json
Stream: under
Low count: 3
Low values: [318.14349365234375, 0.0, 0.0]

File: SN20USBHX2004174_03.json
Stream: under
Low count: 4
Low values: [322.0764465332031, 0.0, 0.0, 0.0]

File: SN20USBHX2004174_04.json
Stream: under
Low count: 2
Low values: [370.6986083984375, 0.0]

File: SN20USBHX2004174_05.json
Stream: under
Low count: 4
Low values: [337.86456298828125, 0.0, 0.0, 0.0]

File: SN20USBHX2004174_06.json
Stream: under
Low count: 2
Low values: [350.46551513671875, 0.0]

File: SN20USBHX2004174_07.json
Stream: under
Low count: 4
Low values: [323.5709533691406, 0.0, 0.0, 0.0]

File: SN20USBHX2004174_08.json
Stream: under
Low count: 2
Low values: [382.9844665527344, 0.0]

File: SN20USBHX2004174_09.json
Stream: under
Low count: 3
Low values: [330.4927978515625, 0.0, 0.0]

File: SN20USBHX2004174_10.json
Stream: under
Low count: 1
Low values: [356.4606018066406]

File: SN20USBHX2004174_11.json
Stream: under
Low count: 4
Low values: [315.8577880859375, 0.0, 0.0, 0.0]

File: SN20USBHX2004174_12.json
Stream: under
Low count: 2
Low values: [366.78009033203125, 0.0]

File: SN20USBHX2004174_13.json
Stream: under
Low count: 3
Low values: [320.29852294921875, 0.0, 0.0]

File: SN20USBHX2004174_14.json
Stream: under
Low count: 2
Low values: [383.2066345214844, 0.0]

File: SN20USBHX2004174_15.json
Stream: under
Low count: 4
Low values: [330.07574462890625, 0.0, 0.0, 0.0]

File: SN20USBHX2004174_16.json
Stream: under
Low count: 1
Low values: [357.7794494628906]

File: SN20USBHX2004174_17.json
Stream: under
Low count: 4
Low values: [331.87030029296875, 0.0, 0.0, 0.0]

File: SN20USBHX2004174_18.json
Stream: under
Low count: 2
Low values: [359.56500244140625, 0.0]

File: SN20USBHX2004174_19.json
Stream: under
Low count: 2
Low values: [318.2453918457031, 0.0]

File: SN20USBHX2004174_20.json
Stream: under
Low count: 2
Low values: [364.6203918457031, 0.0]

File: SN20USBHX2004174_21.json
Stream: under
Low count: 4
Low values: [333.5051574707031, 0.0, 0.0, 0.0]

File: SN20USBHX2004174_22.json
Stream: under
Low count: 2
Low values: [373.70672607421875, 0.0]

File: SN20USBHX2004174_23.json
Stream: under
Low count: 3
Low values: [333.825439453125, 0.0, 0.0]

File: SN20USBHX2004174_24.json
Stream: under
Low count: 4
Low values: [317.8343811035156, 0.0, 0.0, 0.0]

File: SN20USBHX2004174_25.json
Stream: under
Low count: 2
Low values: [355.2725830078125, 0.0]


Module: SN20USBHX2004175
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2004175_01.json
Stream: away
Low count: 1
Low values: [365.9957275390625]

File: SN20USBHX2004175_02.json
Stream: away
Low count: 1
Low values: [341.1307373046875]

File: SN20USBHX2004175_03.json
Stream: away
Low count: 1
Low values: [342.4907531738281]

File: SN20USBHX2004175_04.json
Stream: away
Low count: 1
Low values: [368.6700744628906]

File: SN20USBHX2004175_05.json
Stream: away
Low count: 1
Low values: [326.28936767578125]

File: SN20USBHX2004175_06.json
Stream: away
Low count: 1
Low values: [367.9286193847656]

File: SN20USBHX2004175_07.json
Stream: away
Low count: 1
Low values: [330.1007385253906]

File: SN20USBHX2004175_08.json
Stream: away
Low count: 1
Low values: [363.0489501953125]

File: SN20USBHX2004175_09.json
Stream: away
Low count: 1
Low values: [339.0762023925781]

File: SN20USBHX2004175_10.json
Stream: away
Low count: 1
Low values: [361.158203125]

File: SN20USBHX2004175_11.json
Stream: away
Low count: 1
Low values: [336.749267578125]

File: SN20USBHX2004175_12.json
Stream: away
Low count: 1
Low values: [363.78778076171875]

File: SN20USBHX2004175_13.json
Stream: away
Low count: 1
Low values: [344.1712646484375]

File: SN20USBHX2004175_14.json
Stream: away
Low count: 1
Low values: [362.41705322265625]

File: SN20USBHX2004175_15.json
Stream: away
Low count: 1
Low values: [323.11431884765625]

File: SN20USBHX2004175_16.json
Stream: away
Low count: 1
Low values: [356.550048828125]

File: SN20USBHX2004175_17.json
Stream: away
Low count: 1
Low values: [344.80291748046875]

File: SN20USBHX2004175_18.json
Stream: away
Low count: 1
Low values: [372.989990234375]

File: SN20USBHX2004175_19.json
Stream: away
Low count: 1
Low values: [330.5021057128906]

File: SN20USBHX2004175_20.json
Stream: away
Low count: 1
Low values: [358.58990478515625]

File: SN20USBHX2004175_21.json
Stream: away
Low count: 1
Low values: [325.23956298828125]

File: SN20USBHX2004175_22.json
Stream: away
Low count: 1
Low values: [372.8158264160156]

File: SN20USBHX2004175_23.json
Stream: away
Low count: 1
Low values: [341.032470703125]

File: SN20USBHX2004175_24.json
Stream: away
Low count: 1
Low values: [336.24334716796875]

File: SN20USBHX2004175_25.json
Stream: away
Low count: 1
Low values: [383.80841064453125]


Module: SN20USBHX2004481
--------------------------------------------------------------------------------
Module total values: 8

File: SN20USBHX2004481_01.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004481_08.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004481_12.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004481_13.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004481_14.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004481_15.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004481_17.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004481_19.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2004484
--------------------------------------------------------------------------------
Module total values: 225

File: SN20USBHX2004484_01.json
Stream: under
Low count: 1
Low values: [389.26544189453125]

File: SN20USBHX2004484_02.json
Stream: under
Low count: 1
Low values: [353.37066650390625]

File: SN20USBHX2004484_03.json
Stream: under
Low count: 1
Low values: [348.5347900390625]

File: SN20USBHX2004484_04.json
Stream: under
Low count: 1
Low values: [387.8835754394531]

File: SN20USBHX2004484_05.json
Stream: under
Low count: 1
Low values: [326.1339111328125]

File: SN20USBHX2004484_06.json
Stream: under
Low count: 1
Low values: [377.7435607910156]

File: SN20USBHX2004484_07.json
Stream: under
Low count: 1
Low values: [345.7176513671875]

File: SN20USBHX2004484_08.json
Stream: under
Low count: 1
Low values: [376.36590576171875]

File: SN20USBHX2004484_09.json
Stream: under
Low count: 1
Low values: [352.3627624511719]

File: SN20USBHX2004484_10.json
Stream: under
Low count: 1
Low values: [396.9635009765625]

File: SN20USBHX2004484_11.json
Stream: under
Low count: 1
Low values: [346.66094970703125]

File: SN20USBHX2004484_12.json
Stream: under
Low count: 1
Low values: [387.0405578613281]

File: SN20USBHX2004484_13.json
Stream: under
Low count: 1
Low values: [346.6787414550781]

File: SN20USBHX2004484_14.json
Stream: under
Low count: 1
Low values: [378.35662841796875]

File: SN20USBHX2004484_15.json
Stream: under
Low count: 1
Low values: [351.7285461425781]

File: SN20USBHX2004484_16.json
Stream: under
Low count: 1
Low values: [383.5690002441406]

File: SN20USBHX2004484_17.json
Stream: under
Low count: 1
Low values: [360.1399841308594]

File: SN20USBHX2004484_18.json
Stream: under
Low count: 1
Low values: [358.8027648925781]

File: SN20USBHX2004484_19.json
Stream: under
Low count: 1
Low values: [342.9075012207031]

File: SN20USBHX2004484_20.json
Stream: under
Low count: 1
Low values: [388.050048828125]

File: SN20USBHX2004484_21.json
Stream: under
Low count: 1
Low values: [357.250732421875]

File: SN20USBHX2004484_22.json
Stream: under
Low count: 1
Low values: [378.859130859375]

File: SN20USBHX2004484_23.json
Stream: under
Low count: 1
Low values: [356.1296081542969]

File: SN20USBHX2004484_24.json
Stream: under
Low count: 1
Low values: [352.35400390625]

File: SN20USBHX2004484_25.json
Stream: under
Low count: 1
Low values: [394.9878845214844]

File: SN20USBHX2004484_01.json
Stream: away
Low count: 8
Low values: [382.52227783203125, 369.76434326171875, 381.72467041015625, 369.386474609375, 372.83111572265625, 365.1742858886719, 374.9276428222656, 382.9143981933594]

File: SN20USBHX2004484_02.json
Stream: away
Low count: 8
Low values: [349.5975341796875, 340.7115173339844, 336.521484375, 342.56866455078125, 344.4765625, 339.0793762207031, 340.0747985839844, 344.7598876953125]

File: SN20USBHX2004484_03.json
Stream: away
Low count: 8
Low values: [362.4641418457031, 362.31842041015625, 356.8572082519531, 335.3306579589844, 348.92108154296875, 351.62469482421875, 346.46942138671875, 348.46905517578125]

File: SN20USBHX2004484_04.json
Stream: away
Low count: 8
Low values: [373.138671875, 372.53387451171875, 383.99072265625, 380.6859130859375, 375.3095397949219, 381.38165283203125, 387.9995422363281, 379.6385498046875]

File: SN20USBHX2004484_05.json
Stream: away
Low count: 8
Low values: [342.3799743652344, 333.6945495605469, 331.7262268066406, 313.589599609375, 338.8255615234375, 336.95556640625, 341.91607666015625, 335.703125]

File: SN20USBHX2004484_06.json
Stream: away
Low count: 8
Low values: [375.945556640625, 372.1121520996094, 384.044677734375, 381.733154296875, 395.2545471191406, 378.48974609375, 376.9155578613281, 382.372314453125]

File: SN20USBHX2004484_07.json
Stream: away
Low count: 8
Low values: [340.0042724609375, 333.7511291503906, 336.20233154296875, 341.1297912597656, 331.5325622558594, 350.34881591796875, 339.5393981933594, 346.09222412109375]

File: SN20USBHX2004484_08.json
Stream: away
Low count: 8
Low values: [369.1679382324219, 379.711181640625, 371.38446044921875, 366.8678283691406, 380.81280517578125, 381.1458435058594, 365.5663146972656, 375.42138671875]

File: SN20USBHX2004484_09.json
Stream: away
Low count: 8
Low values: [355.7059020996094, 329.1939697265625, 339.5294494628906, 341.92523193359375, 331.33587646484375, 319.1995544433594, 342.0971374511719, 339.4698791503906]

File: SN20USBHX2004484_10.json
Stream: away
Low count: 8
Low values: [396.4037780761719, 402.0995788574219, 379.1653747558594, 387.2654113769531, 362.5988464355469, 369.5685729980469, 377.9922790527344, 379.3924255371094]

File: SN20USBHX2004484_11.json
Stream: away
Low count: 8
Low values: [344.1509094238281, 328.4566345214844, 325.0639953613281, 345.5193786621094, 345.3614196777344, 345.8486022949219, 342.3255615234375, 338.67169189453125]

File: SN20USBHX2004484_12.json
Stream: away
Low count: 8
Low values: [374.81097412109375, 378.7345275878906, 385.5850830078125, 367.4889831542969, 390.6083984375, 369.8199768066406, 369.04351806640625, 377.9422302246094]

File: SN20USBHX2004484_13.json
Stream: away
Low count: 8
Low values: [339.9002685546875, 345.06842041015625, 335.30145263671875, 346.278076171875, 341.6116027832031, 338.6214294433594, 343.8277587890625, 364.2528991699219]

File: SN20USBHX2004484_14.json
Stream: away
Low count: 8
Low values: [374.86529541015625, 382.0469665527344, 386.1383972167969, 368.47479248046875, 388.4717712402344, 375.6165466308594, 376.7532958984375, 378.6842041015625]

File: SN20USBHX2004484_15.json
Stream: away
Low count: 8
Low values: [349.5921936035156, 337.6253662109375, 342.6089782714844, 335.9759216308594, 335.60906982421875, 344.1654357910156, 335.4269714355469, 333.57891845703125]

File: SN20USBHX2004484_16.json
Stream: away
Low count: 8
Low values: [376.946044921875, 378.23809814453125, 369.1937561035156, 380.6379699707031, 379.6481628417969, 369.9165954589844, 358.1930847167969, 385.1378173828125]

File: SN20USBHX2004484_17.json
Stream: away
Low count: 8
Low values: [341.00439453125, 330.2210998535156, 349.2495422363281, 343.68792724609375, 342.96728515625, 332.52813720703125, 333.6286926269531, 338.99664306640625]

File: SN20USBHX2004484_18.json
Stream: away
Low count: 8
Low values: [363.1712341308594, 362.3011779785156, 388.7966003417969, 362.9366760253906, 382.7071533203125, 383.4500732421875, 374.1958923339844, 374.3349304199219]

File: SN20USBHX2004484_19.json
Stream: away
Low count: 8
Low values: [348.3130187988281, 348.32598876953125, 342.1963195800781, 333.95550537109375, 347.2820739746094, 320.9122314453125, 331.6983337402344, 346.97955322265625]

File: SN20USBHX2004484_20.json
Stream: away
Low count: 8
Low values: [390.30963134765625, 357.9732360839844, 364.3269958496094, 398.3652038574219, 387.9840087890625, 377.6500549316406, 385.4461975097656, 381.4630432128906]

File: SN20USBHX2004484_21.json
Stream: away
Low count: 8
Low values: [339.8431396484375, 327.9715270996094, 354.45635986328125, 342.5009460449219, 346.8725891113281, 340.4922180175781, 340.607421875, 351.4289245605469]

File: SN20USBHX2004484_22.json
Stream: away
Low count: 8
Low values: [369.20941162109375, 360.932373046875, 377.1549377441406, 377.5451965332031, 377.7177429199219, 377.5591735839844, 377.56512451171875, 377.0108947753906]

File: SN20USBHX2004484_23.json
Stream: away
Low count: 8
Low values: [343.0787658691406, 348.2832336425781, 357.9294738769531, 356.3145446777344, 355.0693054199219, 351.7359313964844, 341.9097900390625, 352.65020751953125]

File: SN20USBHX2004484_24.json
Stream: away
Low count: 8
Low values: [346.6207275390625, 343.6740417480469, 344.58404541015625, 339.614501953125, 338.1453857421875, 354.69940185546875, 355.5437316894531, 330.593994140625]

File: SN20USBHX2004484_25.json
Stream: away
Low count: 8
Low values: [374.47515869140625, 376.287841796875, 385.2835693359375, 392.419921875, 386.83746337890625, 374.0285339355469, 371.45916748046875, 383.5932312011719]


Module: SN20USBHX2004489
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2004489_01.json
Stream: under
Low count: 1
Low values: [381.34075927734375]

File: SN20USBHX2004489_02.json
Stream: under
Low count: 1
Low values: [336.423828125]

File: SN20USBHX2004489_03.json
Stream: under
Low count: 1
Low values: [337.4532165527344]

File: SN20USBHX2004489_04.json
Stream: under
Low count: 1
Low values: [372.73004150390625]

File: SN20USBHX2004489_05.json
Stream: under
Low count: 1
Low values: [337.2427062988281]

File: SN20USBHX2004489_06.json
Stream: under
Low count: 1
Low values: [377.7867431640625]

File: SN20USBHX2004489_07.json
Stream: under
Low count: 1
Low values: [337.813720703125]

File: SN20USBHX2004489_08.json
Stream: under
Low count: 1
Low values: [384.0441589355469]

File: SN20USBHX2004489_09.json
Stream: under
Low count: 1
Low values: [338.1858825683594]

File: SN20USBHX2004489_10.json
Stream: under
Low count: 1
Low values: [375.0798034667969]

File: SN20USBHX2004489_11.json
Stream: under
Low count: 1
Low values: [334.61480712890625]

File: SN20USBHX2004489_12.json
Stream: under
Low count: 1
Low values: [375.5901184082031]

File: SN20USBHX2004489_13.json
Stream: under
Low count: 1
Low values: [324.3650817871094]

File: SN20USBHX2004489_14.json
Stream: under
Low count: 1
Low values: [383.39520263671875]

File: SN20USBHX2004489_15.json
Stream: under
Low count: 1
Low values: [337.90777587890625]

File: SN20USBHX2004489_16.json
Stream: under
Low count: 1
Low values: [367.2675476074219]

File: SN20USBHX2004489_17.json
Stream: under
Low count: 1
Low values: [337.6700744628906]

File: SN20USBHX2004489_18.json
Stream: under
Low count: 1
Low values: [368.03314208984375]

File: SN20USBHX2004489_19.json
Stream: under
Low count: 1
Low values: [327.8229064941406]

File: SN20USBHX2004489_20.json
Stream: under
Low count: 1
Low values: [368.2450866699219]

File: SN20USBHX2004489_21.json
Stream: under
Low count: 1
Low values: [316.3295593261719]

File: SN20USBHX2004489_22.json
Stream: under
Low count: 1
Low values: [383.3682861328125]

File: SN20USBHX2004489_23.json
Stream: under
Low count: 1
Low values: [333.2428283691406]

File: SN20USBHX2004489_24.json
Stream: under
Low count: 1
Low values: [337.18914794921875]

File: SN20USBHX2004489_25.json
Stream: under
Low count: 1
Low values: [367.9459533691406]


Module: SN20USBHX2004505
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2004505_01.json
Stream: away
Low count: 1
Low values: [363.1091613769531]

File: SN20USBHX2004505_02.json
Stream: away
Low count: 1
Low values: [338.453857421875]

File: SN20USBHX2004505_03.json
Stream: away
Low count: 1
Low values: [342.02392578125]

File: SN20USBHX2004505_04.json
Stream: away
Low count: 1
Low values: [376.6437683105469]

File: SN20USBHX2004505_05.json
Stream: away
Low count: 1
Low values: [321.6625061035156]

File: SN20USBHX2004505_06.json
Stream: away
Low count: 1
Low values: [372.5992736816406]

File: SN20USBHX2004505_07.json
Stream: away
Low count: 1
Low values: [334.6546936035156]

File: SN20USBHX2004505_08.json
Stream: away
Low count: 1
Low values: [373.98162841796875]

File: SN20USBHX2004505_09.json
Stream: away
Low count: 1
Low values: [339.5914306640625]

File: SN20USBHX2004505_10.json
Stream: away
Low count: 1
Low values: [372.87847900390625]

File: SN20USBHX2004505_11.json
Stream: away
Low count: 1
Low values: [333.07281494140625]

File: SN20USBHX2004505_12.json
Stream: away
Low count: 1
Low values: [364.0130310058594]

File: SN20USBHX2004505_13.json
Stream: away
Low count: 1
Low values: [334.69561767578125]

File: SN20USBHX2004505_14.json
Stream: away
Low count: 1
Low values: [372.20367431640625]

File: SN20USBHX2004505_15.json
Stream: away
Low count: 1
Low values: [334.3153991699219]

File: SN20USBHX2004505_16.json
Stream: away
Low count: 1
Low values: [374.2171936035156]

File: SN20USBHX2004505_17.json
Stream: away
Low count: 1
Low values: [332.81268310546875]

File: SN20USBHX2004505_18.json
Stream: away
Low count: 1
Low values: [381.0315246582031]

File: SN20USBHX2004505_19.json
Stream: away
Low count: 1
Low values: [328.4552917480469]

File: SN20USBHX2004505_20.json
Stream: away
Low count: 1
Low values: [363.2495422363281]

File: SN20USBHX2004505_21.json
Stream: away
Low count: 1
Low values: [340.78826904296875]

File: SN20USBHX2004505_22.json
Stream: away
Low count: 1
Low values: [381.3541259765625]

File: SN20USBHX2004505_23.json
Stream: away
Low count: 1
Low values: [353.3351745605469]

File: SN20USBHX2004505_24.json
Stream: away
Low count: 1
Low values: [342.259521484375]

File: SN20USBHX2004505_25.json
Stream: away
Low count: 1
Low values: [388.9200439453125]


Module: SN20USBHX2004509
--------------------------------------------------------------------------------
Module total values: 119

File: SN20USBHX2004509_01.json
Stream: under
Low count: 4
Low values: [392.2294006347656, 362.5561828613281, 367.8653869628906, 386.8101806640625]

File: SN20USBHX2004509_02.json
Stream: under
Low count: 4
Low values: [343.9773864746094, 336.2164611816406, 336.0085144042969, 354.4128723144531]

File: SN20USBHX2004509_03.json
Stream: under
Low count: 4
Low values: [338.368408203125, 336.1727294921875, 342.6667785644531, 347.35638427734375]

File: SN20USBHX2004509_04.json
Stream: under
Low count: 4
Low values: [379.7485656738281, 373.8405456542969, 369.7522888183594, 392.8222961425781]

File: SN20USBHX2004509_05.json
Stream: under
Low count: 4
Low values: [339.7799987792969, 338.7815856933594, 328.630615234375, 346.1961669921875]

File: SN20USBHX2004509_06.json
Stream: under
Low count: 4
Low values: [382.4307556152344, 373.2510070800781, 377.85406494140625, 378.5793762207031]

File: SN20USBHX2004509_07.json
Stream: under
Low count: 4
Low values: [343.7021789550781, 327.2894592285156, 344.8348083496094, 335.0858154296875]

File: SN20USBHX2004509_08.json
Stream: under
Low count: 4
Low values: [373.9880065917969, 380.60345458984375, 358.467041015625, 389.36834716796875]

File: SN20USBHX2004509_09.json
Stream: under
Low count: 4
Low values: [337.16510009765625, 328.6808166503906, 338.8902282714844, 359.7962646484375]

File: SN20USBHX2004509_10.json
Stream: under
Low count: 4
Low values: [371.38385009765625, 375.0325622558594, 384.88543701171875, 383.3883972167969]

File: SN20USBHX2004509_11.json
Stream: under
Low count: 4
Low values: [376.80718994140625, 375.92999267578125, 377.5718994140625, 389.7799987792969]

File: SN20USBHX2004509_12.json
Stream: under
Low count: 4
Low values: [364.90423583984375, 368.52301025390625, 380.2637023925781, 382.05322265625]

File: SN20USBHX2004509_13.json
Stream: under
Low count: 4
Low values: [376.9466552734375, 379.4168701171875, 387.1340637207031, 371.9225158691406]

File: SN20USBHX2004509_14.json
Stream: under
Low count: 4
Low values: [374.3036804199219, 386.2864990234375, 366.4089050292969, 385.9356994628906]

File: SN20USBHX2004509_15.json
Stream: under
Low count: 4
Low values: [383.69384765625, 374.57757568359375, 374.9980773925781, 388.1815185546875]

File: SN20USBHX2004509_16.json
Stream: under
Low count: 4
Low values: [362.2238464355469, 374.99114990234375, 382.7253112792969, 384.9913330078125]

File: SN20USBHX2004509_17.json
Stream: under
Low count: 4
Low values: [383.2601013183594, 374.36199951171875, 383.00079345703125, 381.0365905761719]

File: SN20USBHX2004509_01.json
Stream: away
Low count: 3
Low values: [381.571044921875, 378.9489440917969, 374.66253662109375]

File: SN20USBHX2004509_02.json
Stream: away
Low count: 3
Low values: [325.82672119140625, 336.8486022949219, 331.0689697265625]

File: SN20USBHX2004509_03.json
Stream: away
Low count: 3
Low values: [334.7618408203125, 349.974609375, 336.9710693359375]

File: SN20USBHX2004509_04.json
Stream: away
Low count: 3
Low values: [385.56219482421875, 378.4144287109375, 376.8183288574219]

File: SN20USBHX2004509_05.json
Stream: away
Low count: 3
Low values: [339.6143798828125, 328.79522705078125, 333.6577453613281]

File: SN20USBHX2004509_06.json
Stream: away
Low count: 3
Low values: [378.413330078125, 378.7580871582031, 370.1133728027344]

File: SN20USBHX2004509_07.json
Stream: away
Low count: 3
Low values: [345.975830078125, 342.6365966796875, 322.7001647949219]

File: SN20USBHX2004509_08.json
Stream: away
Low count: 3
Low values: [382.7498474121094, 380.3196716308594, 374.15008544921875]

File: SN20USBHX2004509_09.json
Stream: away
Low count: 3
Low values: [336.2226867675781, 327.0017395019531, 332.150146484375]

File: SN20USBHX2004509_10.json
Stream: away
Low count: 3
Low values: [390.9231872558594, 386.7200012207031, 367.724853515625]

File: SN20USBHX2004509_11.json
Stream: away
Low count: 3
Low values: [373.82940673828125, 382.6416015625, 377.63079833984375]

File: SN20USBHX2004509_12.json
Stream: away
Low count: 3
Low values: [374.23681640625, 371.1775207519531, 375.39190673828125]

File: SN20USBHX2004509_13.json
Stream: away
Low count: 3
Low values: [373.7146911621094, 370.0439147949219, 377.8086242675781]

File: SN20USBHX2004509_14.json
Stream: away
Low count: 3
Low values: [387.6683044433594, 381.5912170410156, 374.9285888671875]

File: SN20USBHX2004509_15.json
Stream: away
Low count: 3
Low values: [370.3676452636719, 376.7953796386719, 381.316650390625]

File: SN20USBHX2004509_16.json
Stream: away
Low count: 3
Low values: [373.5224609375, 375.6511535644531, 374.8072814941406]

File: SN20USBHX2004509_17.json
Stream: away
Low count: 3
Low values: [393.4010925292969, 387.84429931640625, 373.6828918457031]


Module: SN20USBHX2004510
--------------------------------------------------------------------------------
Module total values: 50

File: SN20USBHX2004510_01.json
Stream: under
Low count: 2
Low values: [388.9161682128906, 376.2929382324219]

File: SN20USBHX2004510_02.json
Stream: under
Low count: 2
Low values: [354.59222412109375, 350.3989562988281]

File: SN20USBHX2004510_03.json
Stream: under
Low count: 2
Low values: [347.4010925292969, 342.83721923828125]

File: SN20USBHX2004510_04.json
Stream: under
Low count: 2
Low values: [398.9024353027344, 385.3715515136719]

File: SN20USBHX2004510_05.json
Stream: under
Low count: 2
Low values: [353.6857604980469, 334.1271057128906]

File: SN20USBHX2004510_06.json
Stream: under
Low count: 2
Low values: [393.8118896484375, 366.1663513183594]

File: SN20USBHX2004510_07.json
Stream: under
Low count: 2
Low values: [354.5238037109375, 336.19195556640625]

File: SN20USBHX2004510_08.json
Stream: under
Low count: 2
Low values: [383.0983581542969, 379.4788818359375]

File: SN20USBHX2004510_09.json
Stream: under
Low count: 2
Low values: [352.2565002441406, 338.1614990234375]

File: SN20USBHX2004510_10.json
Stream: under
Low count: 2
Low values: [402.6302795410156, 369.0563049316406]

File: SN20USBHX2004510_11.json
Stream: under
Low count: 2
Low values: [357.671630859375, 333.9795837402344]

File: SN20USBHX2004510_12.json
Stream: under
Low count: 2
Low values: [409.7845153808594, 377.8546447753906]

File: SN20USBHX2004510_13.json
Stream: under
Low count: 2
Low values: [373.48333740234375, 334.44818115234375]

File: SN20USBHX2004510_14.json
Stream: under
Low count: 2
Low values: [402.1499328613281, 375.447998046875]

File: SN20USBHX2004510_15.json
Stream: under
Low count: 2
Low values: [369.9679260253906, 333.6445617675781]

File: SN20USBHX2004510_16.json
Stream: under
Low count: 2
Low values: [398.4482116699219, 382.3678283691406]

File: SN20USBHX2004510_17.json
Stream: under
Low count: 2
Low values: [349.38531494140625, 344.1590576171875]

File: SN20USBHX2004510_18.json
Stream: under
Low count: 2
Low values: [393.59393310546875, 368.889892578125]

File: SN20USBHX2004510_19.json
Stream: under
Low count: 2
Low values: [370.0712585449219, 346.19091796875]

File: SN20USBHX2004510_20.json
Stream: under
Low count: 2
Low values: [387.25347900390625, 385.4834289550781]

File: SN20USBHX2004510_21.json
Stream: under
Low count: 2
Low values: [335.6924133300781, 348.21783447265625]

File: SN20USBHX2004510_22.json
Stream: under
Low count: 2
Low values: [392.4969177246094, 391.5054626464844]

File: SN20USBHX2004510_23.json
Stream: under
Low count: 2
Low values: [350.7783508300781, 347.59619140625]

File: SN20USBHX2004510_24.json
Stream: under
Low count: 2
Low values: [342.84295654296875, 340.3511657714844]

File: SN20USBHX2004510_25.json
Stream: under
Low count: 2
Low values: [401.3004150390625, 390.048828125]


Module: SN20USBHX2004511
--------------------------------------------------------------------------------
Module total values: 5

File: SN20USBHX2004511_06.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004511_10.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004511_16.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004511_18.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004511_20.json
Stream: under
Low count: 1
Low values: [0.0]


Module: SN20USBHX2004513
--------------------------------------------------------------------------------
Module total values: 50

File: SN20USBHX2004513_01.json
Stream: under
Low count: 2
Low values: [388.805419921875, 373.44580078125]

File: SN20USBHX2004513_02.json
Stream: under
Low count: 2
Low values: [330.4370422363281, 345.455322265625]

File: SN20USBHX2004513_03.json
Stream: under
Low count: 2
Low values: [343.9241943359375, 348.2962341308594]

File: SN20USBHX2004513_04.json
Stream: under
Low count: 2
Low values: [362.2275390625, 387.31268310546875]

File: SN20USBHX2004513_05.json
Stream: under
Low count: 2
Low values: [351.4449768066406, 347.1856689453125]

File: SN20USBHX2004513_06.json
Stream: under
Low count: 2
Low values: [376.0458068847656, 370.8501892089844]

File: SN20USBHX2004513_07.json
Stream: under
Low count: 2
Low values: [334.49163818359375, 335.8953857421875]

File: SN20USBHX2004513_08.json
Stream: under
Low count: 2
Low values: [378.4281921386719, 380.3067626953125]

File: SN20USBHX2004513_09.json
Stream: under
Low count: 2
Low values: [324.6037292480469, 330.2665100097656]

File: SN20USBHX2004513_10.json
Stream: under
Low count: 2
Low values: [370.2615661621094, 390.75518798828125]

File: SN20USBHX2004513_11.json
Stream: under
Low count: 2
Low values: [327.34930419921875, 329.407470703125]

File: SN20USBHX2004513_12.json
Stream: under
Low count: 2
Low values: [382.1539611816406, 395.26763916015625]

File: SN20USBHX2004513_13.json
Stream: under
Low count: 2
Low values: [325.33026123046875, 329.6052551269531]

File: SN20USBHX2004513_14.json
Stream: under
Low count: 2
Low values: [376.4215393066406, 373.3433532714844]

File: SN20USBHX2004513_15.json
Stream: under
Low count: 2
Low values: [322.5511779785156, 336.9411315917969]

File: SN20USBHX2004513_16.json
Stream: under
Low count: 2
Low values: [389.9069519042969, 368.528076171875]

File: SN20USBHX2004513_17.json
Stream: under
Low count: 2
Low values: [331.5959777832031, 331.88092041015625]

File: SN20USBHX2004513_18.json
Stream: under
Low count: 2
Low values: [387.86114501953125, 380.28521728515625]

File: SN20USBHX2004513_19.json
Stream: under
Low count: 2
Low values: [354.78546142578125, 331.1529235839844]

File: SN20USBHX2004513_20.json
Stream: under
Low count: 2
Low values: [376.1771240234375, 376.8931579589844]

File: SN20USBHX2004513_21.json
Stream: under
Low count: 2
Low values: [329.44195556640625, 333.5533447265625]

File: SN20USBHX2004513_22.json
Stream: under
Low count: 2
Low values: [379.9002380371094, 374.4089660644531]

File: SN20USBHX2004513_23.json
Stream: under
Low count: 2
Low values: [320.62396240234375, 345.79913330078125]

File: SN20USBHX2004513_24.json
Stream: under
Low count: 2
Low values: [339.29150390625, 328.172607421875]

File: SN20USBHX2004513_25.json
Stream: under
Low count: 2
Low values: [382.7904968261719, 377.4048767089844]


Module: SN20USBHX2004859
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2004859_01.json
Stream: under
Low count: 1
Low values: [373.7839660644531]

File: SN20USBHX2004859_02.json
Stream: under
Low count: 1
Low values: [324.6165771484375]

File: SN20USBHX2004859_03.json
Stream: under
Low count: 1
Low values: [343.2064514160156]

File: SN20USBHX2004859_04.json
Stream: under
Low count: 1
Low values: [370.2333984375]

File: SN20USBHX2004859_05.json
Stream: under
Low count: 1
Low values: [331.7441711425781]

File: SN20USBHX2004859_06.json
Stream: under
Low count: 1
Low values: [375.718505859375]

File: SN20USBHX2004859_07.json
Stream: under
Low count: 1
Low values: [338.0876770019531]

File: SN20USBHX2004859_08.json
Stream: under
Low count: 1
Low values: [373.4263916015625]

File: SN20USBHX2004859_09.json
Stream: under
Low count: 1
Low values: [337.40380859375]

File: SN20USBHX2004859_10.json
Stream: under
Low count: 1
Low values: [370.9831848144531]

File: SN20USBHX2004859_11.json
Stream: under
Low count: 1
Low values: [336.06927490234375]

File: SN20USBHX2004859_12.json
Stream: under
Low count: 1
Low values: [364.0728454589844]

File: SN20USBHX2004859_13.json
Stream: under
Low count: 1
Low values: [334.33599853515625]

File: SN20USBHX2004859_14.json
Stream: under
Low count: 1
Low values: [383.96820068359375]

File: SN20USBHX2004859_15.json
Stream: under
Low count: 1
Low values: [328.49151611328125]

File: SN20USBHX2004859_16.json
Stream: under
Low count: 1
Low values: [363.7001647949219]

File: SN20USBHX2004859_17.json
Stream: under
Low count: 1
Low values: [341.6846618652344]

File: SN20USBHX2004859_18.json
Stream: under
Low count: 1
Low values: [367.008056640625]

File: SN20USBHX2004859_19.json
Stream: under
Low count: 1
Low values: [322.1902160644531]

File: SN20USBHX2004859_20.json
Stream: under
Low count: 1
Low values: [347.0450744628906]

File: SN20USBHX2004859_21.json
Stream: under
Low count: 1
Low values: [331.9578857421875]

File: SN20USBHX2004859_22.json
Stream: under
Low count: 1
Low values: [378.3832092285156]

File: SN20USBHX2004859_23.json
Stream: under
Low count: 1
Low values: [338.20574951171875]

File: SN20USBHX2004859_24.json
Stream: under
Low count: 1
Low values: [331.2726745605469]

File: SN20USBHX2004859_25.json
Stream: under
Low count: 1
Low values: [366.853759765625]


Module: SN20USBHX2004870
--------------------------------------------------------------------------------
Module total values: 50

File: SN20USBHX2004870_01.json
Stream: under
Low count: 2
Low values: [373.4115295410156, 379.8102722167969]

File: SN20USBHX2004870_02.json
Stream: under
Low count: 2
Low values: [330.4306335449219, 346.0422058105469]

File: SN20USBHX2004870_03.json
Stream: under
Low count: 2
Low values: [340.408203125, 353.0003662109375]

File: SN20USBHX2004870_04.json
Stream: under
Low count: 2
Low values: [354.21783447265625, 387.94635009765625]

File: SN20USBHX2004870_05.json
Stream: under
Low count: 2
Low values: [334.4876708984375, 354.6369934082031]

File: SN20USBHX2004870_06.json
Stream: under
Low count: 2
Low values: [369.2987060546875, 391.0442810058594]

File: SN20USBHX2004870_07.json
Stream: under
Low count: 2
Low values: [331.47601318359375, 347.6597595214844]

File: SN20USBHX2004870_08.json
Stream: under
Low count: 2
Low values: [377.598876953125, 374.1954650878906]

File: SN20USBHX2004870_09.json
Stream: under
Low count: 2
Low values: [335.8387145996094, 358.4057312011719]

File: SN20USBHX2004870_10.json
Stream: under
Low count: 2
Low values: [368.3548278808594, 387.0973205566406]

File: SN20USBHX2004870_11.json
Stream: under
Low count: 2
Low values: [331.5939636230469, 348.1925048828125]

File: SN20USBHX2004870_12.json
Stream: under
Low count: 2
Low values: [370.9839782714844, 377.24725341796875]

File: SN20USBHX2004870_13.json
Stream: under
Low count: 2
Low values: [328.94677734375, 343.9256896972656]

File: SN20USBHX2004870_14.json
Stream: under
Low count: 2
Low values: [366.16302490234375, 380.0998229980469]

File: SN20USBHX2004870_15.json
Stream: under
Low count: 2
Low values: [322.4891662597656, 345.8016052246094]

File: SN20USBHX2004870_16.json
Stream: under
Low count: 2
Low values: [375.0750427246094, 395.146484375]

File: SN20USBHX2004870_17.json
Stream: under
Low count: 2
Low values: [329.7583923339844, 350.5874328613281]

File: SN20USBHX2004870_18.json
Stream: under
Low count: 2
Low values: [353.92376708984375, 386.1412353515625]

File: SN20USBHX2004870_19.json
Stream: under
Low count: 2
Low values: [341.6077880859375, 358.6405334472656]

File: SN20USBHX2004870_20.json
Stream: under
Low count: 2
Low values: [375.91314697265625, 385.0050964355469]

File: SN20USBHX2004870_21.json
Stream: under
Low count: 2
Low values: [330.66107177734375, 342.3435974121094]

File: SN20USBHX2004870_22.json
Stream: under
Low count: 2
Low values: [378.7342224121094, 381.31146240234375]

File: SN20USBHX2004870_23.json
Stream: under
Low count: 2
Low values: [333.5837097167969, 351.4909362792969]

File: SN20USBHX2004870_24.json
Stream: under
Low count: 2
Low values: [335.8757019042969, 345.81866455078125]

File: SN20USBHX2004870_25.json
Stream: under
Low count: 2
Low values: [365.5913391113281, 379.42706298828125]


Module: SN20USBHX2005137
--------------------------------------------------------------------------------
Module total values: 37

File: SN20USBHX2005137_01.json
Stream: under
Low count: 1
Low values: [372.756103515625]

File: SN20USBHX2005137_02.json
Stream: under
Low count: 1
Low values: [344.1643981933594]

File: SN20USBHX2005137_03.json
Stream: under
Low count: 1
Low values: [334.0586242675781]

File: SN20USBHX2005137_04.json
Stream: under
Low count: 1
Low values: [373.43597412109375]

File: SN20USBHX2005137_05.json
Stream: under
Low count: 1
Low values: [332.6119689941406]

File: SN20USBHX2005137_06.json
Stream: under
Low count: 1
Low values: [376.2284851074219]

File: SN20USBHX2005137_07.json
Stream: under
Low count: 1
Low values: [328.1324157714844]

File: SN20USBHX2005137_08.json
Stream: under
Low count: 1
Low values: [363.6601257324219]

File: SN20USBHX2005137_09.json
Stream: under
Low count: 1
Low values: [317.43218994140625]

File: SN20USBHX2005137_10.json
Stream: under
Low count: 1
Low values: [379.17620849609375]

File: SN20USBHX2005137_11.json
Stream: under
Low count: 1
Low values: [319.15362548828125]

File: SN20USBHX2005137_12.json
Stream: under
Low count: 1
Low values: [376.0777893066406]

File: SN20USBHX2005137_13.json
Stream: under
Low count: 1
Low values: [329.807373046875]

File: SN20USBHX2005137_14.json
Stream: under
Low count: 1
Low values: [380.6281433105469]

File: SN20USBHX2005137_15.json
Stream: under
Low count: 1
Low values: [333.10638427734375]

File: SN20USBHX2005137_16.json
Stream: under
Low count: 1
Low values: [373.58026123046875]

File: SN20USBHX2005137_17.json
Stream: under
Low count: 1
Low values: [314.7771911621094]

File: SN20USBHX2005137_18.json
Stream: under
Low count: 1
Low values: [376.8381042480469]

File: SN20USBHX2005137_19.json
Stream: under
Low count: 1
Low values: [316.52587890625]

File: SN20USBHX2005137_20.json
Stream: under
Low count: 1
Low values: [381.3226013183594]

File: SN20USBHX2005137_21.json
Stream: under
Low count: 1
Low values: [332.46771240234375]

File: SN20USBHX2005137_22.json
Stream: under
Low count: 1
Low values: [390.4912414550781]

File: SN20USBHX2005137_23.json
Stream: under
Low count: 1
Low values: [344.2972106933594]

File: SN20USBHX2005137_24.json
Stream: under
Low count: 1
Low values: [322.6755676269531]

File: SN20USBHX2005137_25.json
Stream: under
Low count: 1
Low values: [357.636962890625]

File: SN20USBHX2005137_01.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2005137_04.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2005137_06.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2005137_08.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2005137_10.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2005137_12.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2005137_14.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2005137_16.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2005137_18.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2005137_20.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2005137_22.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2005137_25.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2005140
--------------------------------------------------------------------------------
Module total values: 17

File: SN20USBHX2005140_01.json
Stream: away
Low count: 1
Low values: [373.18206787109375]

File: SN20USBHX2005140_02.json
Stream: away
Low count: 1
Low values: [335.1532897949219]

File: SN20USBHX2005140_03.json
Stream: away
Low count: 1
Low values: [340.6995849609375]

File: SN20USBHX2005140_04.json
Stream: away
Low count: 1
Low values: [377.6282653808594]

File: SN20USBHX2005140_05.json
Stream: away
Low count: 1
Low values: [335.8003234863281]

File: SN20USBHX2005140_06.json
Stream: away
Low count: 1
Low values: [368.83123779296875]

File: SN20USBHX2005140_07.json
Stream: away
Low count: 1
Low values: [331.0378723144531]

File: SN20USBHX2005140_08.json
Stream: away
Low count: 1
Low values: [383.1450500488281]

File: SN20USBHX2005140_09.json
Stream: away
Low count: 1
Low values: [332.6188049316406]

File: SN20USBHX2005140_10.json
Stream: away
Low count: 1
Low values: [368.0079650878906]

File: SN20USBHX2005140_11.json
Stream: away
Low count: 1
Low values: [318.1548156738281]

File: SN20USBHX2005140_12.json
Stream: away
Low count: 1
Low values: [370.7162780761719]

File: SN20USBHX2005140_13.json
Stream: away
Low count: 1
Low values: [333.8562316894531]

File: SN20USBHX2005140_14.json
Stream: away
Low count: 1
Low values: [390.9414367675781]

File: SN20USBHX2005140_15.json
Stream: away
Low count: 1
Low values: [344.5868835449219]

File: SN20USBHX2005140_16.json
Stream: away
Low count: 1
Low values: [362.1643371582031]

File: SN20USBHX2005140_17.json
Stream: away
Low count: 1
Low values: [352.60528564453125]


================================================================================
CATEGORY D — files skipped, empty, missing, or unreadable
================================================================================
Total entries: 0

None

================================================================================
CATEGORY E — script did not run for entire module / no valid histogram plotted
================================================================================
Total entries: 0

None


"""

# Find all module names like:

# Module: SN20USBHX2003961

modules = re.findall(r"Module:\s*SN(\S+)", RAW_TEXT)

# Remove duplicates while preserving order

seen = set()

unique_modules = []

for module in modules:

    if module not in seen:

        seen.add(module)

        unique_modules.append(module)

# Print formatted output

for module in unique_modules:

    print(f'"{module}",\n')