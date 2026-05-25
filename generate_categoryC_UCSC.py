#!/usr/bin/env python3

import re

RAW_TEXT = """


================================================================================
CATEGORY C — low input noise values less than 600
================================================================================
Total entries: 441
Total values: 672


Module: SN20USBHX2003619
--------------------------------------------------------------------------------
Module total values: 175

File: SN20USBHX2003619_01.json
Stream: away
Low count: 7
Low values: [370.02667236328125, 381.73541259765625, 383.7731018066406, 390.8004150390625, 371.4160461425781, 393.002685546875, 387.1858825683594]

File: SN20USBHX2003619_02.json
Stream: away
Low count: 7
Low values: [343.7392883300781, 358.8944396972656, 351.4591979980469, 352.8162536621094, 354.6593322753906, 356.9330749511719, 355.2536926269531]

File: SN20USBHX2003619_03.json
Stream: away
Low count: 7
Low values: [354.4566650390625, 350.3120422363281, 357.6756286621094, 360.67315673828125, 343.11907958984375, 352.95257568359375, 355.71673583984375]

File: SN20USBHX2003619_04.json
Stream: away
Low count: 7
Low values: [380.5254211425781, 402.0334777832031, 397.95208740234375, 369.3782043457031, 393.3066101074219, 372.35382080078125, 411.6325378417969]

File: SN20USBHX2003619_05.json
Stream: away
Low count: 7
Low values: [361.49688720703125, 350.3538513183594, 348.29400634765625, 346.10345458984375, 353.2828369140625, 350.9620666503906, 360.3039855957031]

File: SN20USBHX2003619_06.json
Stream: away
Low count: 7
Low values: [403.70281982421875, 409.9639892578125, 390.7123107910156, 393.4908447265625, 382.64581298828125, 395.12060546875, 392.768798828125]

File: SN20USBHX2003619_07.json
Stream: away
Low count: 7
Low values: [330.26318359375, 353.3181457519531, 341.714111328125, 354.9363098144531, 343.04522705078125, 347.9626159667969, 355.1410827636719]

File: SN20USBHX2003619_08.json
Stream: away
Low count: 7
Low values: [378.0023193359375, 381.7024841308594, 392.86248779296875, 386.5304870605469, 380.2382507324219, 386.1382751464844, 377.9183044433594]

File: SN20USBHX2003619_09.json
Stream: away
Low count: 7
Low values: [349.8606262207031, 347.0963439941406, 351.3043518066406, 360.6568298339844, 348.2456359863281, 339.4376220703125, 342.86053466796875]

File: SN20USBHX2003619_10.json
Stream: away
Low count: 7
Low values: [385.1095886230469, 396.56182861328125, 390.97283935546875, 386.3277587890625, 390.2867736816406, 397.8099670410156, 382.742431640625]

File: SN20USBHX2003619_11.json
Stream: away
Low count: 7
Low values: [342.45074462890625, 355.3377685546875, 352.36370849609375, 339.28704833984375, 348.1992492675781, 338.7829284667969, 352.827392578125]

File: SN20USBHX2003619_12.json
Stream: away
Low count: 7
Low values: [379.1685791015625, 395.78424072265625, 391.0532531738281, 375.9269714355469, 395.79095458984375, 399.67547607421875, 399.8449401855469]

File: SN20USBHX2003619_13.json
Stream: away
Low count: 7
Low values: [343.2485656738281, 349.6036071777344, 345.9466247558594, 355.8599548339844, 346.3826904296875, 332.3606872558594, 346.00518798828125]

File: SN20USBHX2003619_14.json
Stream: away
Low count: 7
Low values: [381.9713134765625, 397.0954895019531, 393.7210998535156, 370.3873596191406, 386.4721374511719, 387.07952880859375, 380.1041564941406]

File: SN20USBHX2003619_15.json
Stream: away
Low count: 7
Low values: [337.37713623046875, 362.7515563964844, 338.6311950683594, 346.162353515625, 355.0577697753906, 340.96270751953125, 358.5468444824219]

File: SN20USBHX2003619_16.json
Stream: away
Low count: 7
Low values: [373.5608215332031, 387.41497802734375, 390.9068298339844, 386.7843322753906, 399.1618347167969, 378.97210693359375, 395.7524108886719]

File: SN20USBHX2003619_17.json
Stream: away
Low count: 7
Low values: [362.0036926269531, 366.5435791015625, 334.4383544921875, 348.38446044921875, 351.5697326660156, 351.9740295410156, 358.8486633300781]

File: SN20USBHX2003619_18.json
Stream: away
Low count: 7
Low values: [375.5311584472656, 379.281494140625, 385.7976379394531, 382.2517395019531, 376.8447265625, 402.97637939453125, 386.550048828125]

File: SN20USBHX2003619_19.json
Stream: away
Low count: 7
Low values: [349.2595520019531, 353.88775634765625, 337.9714050292969, 345.46832275390625, 337.66241455078125, 357.1616516113281, 339.6453552246094]

File: SN20USBHX2003619_20.json
Stream: away
Low count: 7
Low values: [398.1455993652344, 384.947021484375, 383.806884765625, 392.9005432128906, 391.69256591796875, 387.8598937988281, 381.0036926269531]

File: SN20USBHX2003619_21.json
Stream: away
Low count: 7
Low values: [332.3702087402344, 349.8379821777344, 355.48199462890625, 350.3511047363281, 336.34820556640625, 345.1689758300781, 348.6921691894531]

File: SN20USBHX2003619_22.json
Stream: away
Low count: 7
Low values: [384.3623046875, 400.72052001953125, 379.8050231933594, 380.93994140625, 403.3046875, 396.7158203125, 390.8547668457031]

File: SN20USBHX2003619_23.json
Stream: away
Low count: 7
Low values: [349.4930725097656, 366.5540466308594, 352.8055114746094, 367.4065856933594, 350.61932373046875, 358.2765197753906, 350.287353515625]

File: SN20USBHX2003619_24.json
Stream: away
Low count: 7
Low values: [343.23529052734375, 355.40655517578125, 354.52545166015625, 347.6381530761719, 345.3208923339844, 352.1482238769531, 349.8005065917969]

File: SN20USBHX2003619_25.json
Stream: away
Low count: 7
Low values: [383.3143005371094, 385.05914306640625, 398.24169921875, 395.2841796875, 381.09375, 393.9537048339844, 406.9464416503906]


Module: SN20USBHX2003764
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2003764_01.json
Stream: away
Low count: 1
Low values: [391.0494384765625]

File: SN20USBHX2003764_02.json
Stream: away
Low count: 1
Low values: [344.13519287109375]

File: SN20USBHX2003764_03.json
Stream: away
Low count: 1
Low values: [361.16119384765625]

File: SN20USBHX2003764_04.json
Stream: away
Low count: 1
Low values: [389.874267578125]

File: SN20USBHX2003764_05.json
Stream: away
Low count: 1
Low values: [346.8126525878906]

File: SN20USBHX2003764_06.json
Stream: away
Low count: 1
Low values: [388.2572937011719]

File: SN20USBHX2003764_07.json
Stream: away
Low count: 1
Low values: [349.2693176269531]

File: SN20USBHX2003764_08.json
Stream: away
Low count: 1
Low values: [384.7138671875]

File: SN20USBHX2003764_09.json
Stream: away
Low count: 1
Low values: [353.4908142089844]

File: SN20USBHX2003764_10.json
Stream: away
Low count: 1
Low values: [388.9836730957031]

File: SN20USBHX2003764_11.json
Stream: away
Low count: 1
Low values: [354.33074951171875]

File: SN20USBHX2003764_12.json
Stream: away
Low count: 1
Low values: [385.5757141113281]

File: SN20USBHX2003764_13.json
Stream: away
Low count: 1
Low values: [349.4183044433594]

File: SN20USBHX2003764_14.json
Stream: away
Low count: 1
Low values: [393.0913391113281]

File: SN20USBHX2003764_15.json
Stream: away
Low count: 1
Low values: [354.50872802734375]

File: SN20USBHX2003764_16.json
Stream: away
Low count: 1
Low values: [390.6466064453125]

File: SN20USBHX2003764_17.json
Stream: away
Low count: 1
Low values: [333.8876647949219]

File: SN20USBHX2003764_18.json
Stream: away
Low count: 1
Low values: [394.87103271484375]

File: SN20USBHX2003764_19.json
Stream: away
Low count: 1
Low values: [340.7046813964844]

File: SN20USBHX2003764_20.json
Stream: away
Low count: 1
Low values: [381.5623474121094]

File: SN20USBHX2003764_21.json
Stream: away
Low count: 1
Low values: [355.3575439453125]

File: SN20USBHX2003764_22.json
Stream: away
Low count: 1
Low values: [406.898681640625]

File: SN20USBHX2003764_23.json
Stream: away
Low count: 1
Low values: [352.89544677734375]

File: SN20USBHX2003764_24.json
Stream: away
Low count: 1
Low values: [338.5513000488281]

File: SN20USBHX2003764_25.json
Stream: away
Low count: 1
Low values: [390.6334228515625]


Module: SN20USBHX2003768
--------------------------------------------------------------------------------
Module total values: 50

File: SN20USBHX2003768_01.json
Stream: away
Low count: 2
Low values: [384.4747314453125, 386.3196716308594]

File: SN20USBHX2003768_02.json
Stream: away
Low count: 2
Low values: [355.89337158203125, 343.1380920410156]

File: SN20USBHX2003768_03.json
Stream: away
Low count: 2
Low values: [342.8301086425781, 345.46148681640625]

File: SN20USBHX2003768_04.json
Stream: away
Low count: 2
Low values: [390.5334777832031, 388.8611145019531]

File: SN20USBHX2003768_05.json
Stream: away
Low count: 2
Low values: [341.7828674316406, 350.83990478515625]

File: SN20USBHX2003768_06.json
Stream: away
Low count: 2
Low values: [373.8046569824219, 386.7898254394531]

File: SN20USBHX2003768_07.json
Stream: away
Low count: 2
Low values: [344.3796081542969, 350.2362365722656]

File: SN20USBHX2003768_08.json
Stream: away
Low count: 2
Low values: [389.3469543457031, 380.59320068359375]

File: SN20USBHX2003768_09.json
Stream: away
Low count: 2
Low values: [354.8436584472656, 347.9299011230469]

File: SN20USBHX2003768_10.json
Stream: away
Low count: 2
Low values: [383.8974304199219, 387.6413879394531]

File: SN20USBHX2003768_11.json
Stream: away
Low count: 2
Low values: [348.2881774902344, 348.0251770019531]

File: SN20USBHX2003768_12.json
Stream: away
Low count: 2
Low values: [391.22711181640625, 397.3176574707031]

File: SN20USBHX2003768_13.json
Stream: away
Low count: 2
Low values: [351.8145446777344, 340.08673095703125]

File: SN20USBHX2003768_14.json
Stream: away
Low count: 2
Low values: [375.8594970703125, 389.6769104003906]

File: SN20USBHX2003768_15.json
Stream: away
Low count: 2
Low values: [332.0627136230469, 346.0266418457031]

File: SN20USBHX2003768_16.json
Stream: away
Low count: 2
Low values: [379.99334716796875, 384.30084228515625]

File: SN20USBHX2003768_17.json
Stream: away
Low count: 2
Low values: [348.5976257324219, 363.84881591796875]

File: SN20USBHX2003768_18.json
Stream: away
Low count: 2
Low values: [390.1092224121094, 393.0943298339844]

File: SN20USBHX2003768_19.json
Stream: away
Low count: 2
Low values: [336.3314208984375, 326.5877685546875]

File: SN20USBHX2003768_20.json
Stream: away
Low count: 2
Low values: [375.55181884765625, 388.4688415527344]

File: SN20USBHX2003768_21.json
Stream: away
Low count: 2
Low values: [335.24908447265625, 348.55718994140625]

File: SN20USBHX2003768_22.json
Stream: away
Low count: 2
Low values: [386.14288330078125, 399.1625061035156]

File: SN20USBHX2003768_23.json
Stream: away
Low count: 2
Low values: [343.4642639160156, 355.0360107421875]

File: SN20USBHX2003768_24.json
Stream: away
Low count: 2
Low values: [338.7819519042969, 348.74078369140625]

File: SN20USBHX2003768_25.json
Stream: away
Low count: 2
Low values: [395.1044006347656, 388.2717590332031]


Module: SN20USBHX2004234
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2004234_01.json
Stream: away
Low count: 1
Low values: [370.9116516113281]

File: SN20USBHX2004234_02.json
Stream: away
Low count: 1
Low values: [321.4319152832031]

File: SN20USBHX2004234_03.json
Stream: away
Low count: 1
Low values: [351.18804931640625]

File: SN20USBHX2004234_04.json
Stream: away
Low count: 1
Low values: [385.8630065917969]

File: SN20USBHX2004234_05.json
Stream: away
Low count: 1
Low values: [334.2252197265625]

File: SN20USBHX2004234_06.json
Stream: away
Low count: 1
Low values: [377.40496826171875]

File: SN20USBHX2004234_07.json
Stream: away
Low count: 1
Low values: [328.40472412109375]

File: SN20USBHX2004234_08.json
Stream: away
Low count: 1
Low values: [376.13897705078125]

File: SN20USBHX2004234_09.json
Stream: away
Low count: 1
Low values: [344.0310974121094]

File: SN20USBHX2004234_10.json
Stream: away
Low count: 1
Low values: [374.2167663574219]

File: SN20USBHX2004234_11.json
Stream: away
Low count: 1
Low values: [336.8450622558594]

File: SN20USBHX2004234_12.json
Stream: away
Low count: 1
Low values: [379.15545654296875]

File: SN20USBHX2004234_13.json
Stream: away
Low count: 1
Low values: [341.3808898925781]

File: SN20USBHX2004234_14.json
Stream: away
Low count: 1
Low values: [370.76336669921875]

File: SN20USBHX2004234_15.json
Stream: away
Low count: 1
Low values: [336.717041015625]

File: SN20USBHX2004234_16.json
Stream: away
Low count: 1
Low values: [389.85089111328125]

File: SN20USBHX2004234_17.json
Stream: away
Low count: 1
Low values: [352.1600036621094]

File: SN20USBHX2004234_18.json
Stream: away
Low count: 1
Low values: [380.8662109375]

File: SN20USBHX2004234_19.json
Stream: away
Low count: 1
Low values: [338.04443359375]

File: SN20USBHX2004234_20.json
Stream: away
Low count: 1
Low values: [366.63189697265625]

File: SN20USBHX2004234_21.json
Stream: away
Low count: 1
Low values: [337.0805969238281]

File: SN20USBHX2004234_22.json
Stream: away
Low count: 1
Low values: [366.25372314453125]

File: SN20USBHX2004234_23.json
Stream: away
Low count: 1
Low values: [329.5385437011719]

File: SN20USBHX2004234_24.json
Stream: away
Low count: 1
Low values: [347.15118408203125]

File: SN20USBHX2004234_25.json
Stream: away
Low count: 1
Low values: [379.0641174316406]


Module: SN20USBHX2004241
--------------------------------------------------------------------------------
Module total values: 22

File: SN20USBHX2004241_01.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004241_02.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2004241_03.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2004241_06.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004241_07.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004241_08.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004241_09.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004241_11.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004241_13.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004241_14.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004241_16.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004241_17.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2004241_19.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004241_21.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]

File: SN20USBHX2004241_22.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004241_23.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004241_24.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]


Module: SN20USBHX2004649
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2004649_01.json
Stream: away
Low count: 1
Low values: [374.5489807128906]

File: SN20USBHX2004649_02.json
Stream: away
Low count: 1
Low values: [328.5040283203125]

File: SN20USBHX2004649_03.json
Stream: away
Low count: 1
Low values: [374.0354309082031]

File: SN20USBHX2004649_04.json
Stream: away
Low count: 1
Low values: [385.8570251464844]

File: SN20USBHX2004649_05.json
Stream: away
Low count: 1
Low values: [357.3507080078125]

File: SN20USBHX2004649_06.json
Stream: away
Low count: 1
Low values: [388.0064392089844]

File: SN20USBHX2004649_07.json
Stream: away
Low count: 1
Low values: [341.5973815917969]

File: SN20USBHX2004649_08.json
Stream: away
Low count: 1
Low values: [388.96533203125]

File: SN20USBHX2004649_09.json
Stream: away
Low count: 1
Low values: [344.4179382324219]

File: SN20USBHX2004649_10.json
Stream: away
Low count: 1
Low values: [388.34613037109375]

File: SN20USBHX2004649_11.json
Stream: away
Low count: 1
Low values: [355.37225341796875]

File: SN20USBHX2004649_12.json
Stream: away
Low count: 1
Low values: [381.77392578125]

File: SN20USBHX2004649_13.json
Stream: away
Low count: 1
Low values: [329.3779602050781]

File: SN20USBHX2004649_14.json
Stream: away
Low count: 1
Low values: [396.33807373046875]

File: SN20USBHX2004649_15.json
Stream: away
Low count: 1
Low values: [365.6517333984375]

File: SN20USBHX2004649_16.json
Stream: away
Low count: 1
Low values: [375.34893798828125]

File: SN20USBHX2004649_17.json
Stream: away
Low count: 1
Low values: [323.1096496582031]

File: SN20USBHX2004649_18.json
Stream: away
Low count: 1
Low values: [383.6601257324219]

File: SN20USBHX2004649_19.json
Stream: away
Low count: 1
Low values: [331.6806335449219]

File: SN20USBHX2004649_20.json
Stream: away
Low count: 1
Low values: [378.75128173828125]

File: SN20USBHX2004649_21.json
Stream: away
Low count: 1
Low values: [356.7257385253906]

File: SN20USBHX2004649_22.json
Stream: away
Low count: 1
Low values: [384.45037841796875]

File: SN20USBHX2004649_23.json
Stream: away
Low count: 1
Low values: [365.13995361328125]

File: SN20USBHX2004649_24.json
Stream: away
Low count: 1
Low values: [308.8250427246094]

File: SN20USBHX2004649_25.json
Stream: away
Low count: 1
Low values: [388.52459716796875]


Module: SN20USBHX2004655
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2004655_01.json
Stream: under
Low count: 1
Low values: [385.7175598144531]

File: SN20USBHX2004655_02.json
Stream: under
Low count: 1
Low values: [348.7829284667969]

File: SN20USBHX2004655_03.json
Stream: under
Low count: 1
Low values: [357.016357421875]

File: SN20USBHX2004655_04.json
Stream: under
Low count: 1
Low values: [374.2933654785156]

File: SN20USBHX2004655_05.json
Stream: under
Low count: 1
Low values: [338.8742980957031]

File: SN20USBHX2004655_06.json
Stream: under
Low count: 1
Low values: [371.65179443359375]

File: SN20USBHX2004655_07.json
Stream: under
Low count: 1
Low values: [334.5476989746094]

File: SN20USBHX2004655_08.json
Stream: under
Low count: 1
Low values: [379.103759765625]

File: SN20USBHX2004655_09.json
Stream: under
Low count: 1
Low values: [357.3321533203125]

File: SN20USBHX2004655_10.json
Stream: under
Low count: 1
Low values: [384.4131164550781]

File: SN20USBHX2004655_11.json
Stream: under
Low count: 1
Low values: [338.78759765625]

File: SN20USBHX2004655_12.json
Stream: under
Low count: 1
Low values: [379.2132568359375]

File: SN20USBHX2004655_13.json
Stream: under
Low count: 1
Low values: [345.6508483886719]

File: SN20USBHX2004655_14.json
Stream: under
Low count: 1
Low values: [383.75274658203125]

File: SN20USBHX2004655_15.json
Stream: under
Low count: 1
Low values: [352.2211608886719]

File: SN20USBHX2004655_16.json
Stream: under
Low count: 1
Low values: [393.84814453125]

File: SN20USBHX2004655_17.json
Stream: under
Low count: 1
Low values: [340.95904541015625]

File: SN20USBHX2004655_18.json
Stream: under
Low count: 1
Low values: [390.8475341796875]

File: SN20USBHX2004655_19.json
Stream: under
Low count: 1
Low values: [349.7835388183594]

File: SN20USBHX2004655_20.json
Stream: under
Low count: 1
Low values: [389.0705871582031]

File: SN20USBHX2004655_21.json
Stream: under
Low count: 1
Low values: [338.56121826171875]

File: SN20USBHX2004655_22.json
Stream: under
Low count: 1
Low values: [386.5853271484375]

File: SN20USBHX2004655_23.json
Stream: under
Low count: 1
Low values: [355.53173828125]

File: SN20USBHX2004655_24.json
Stream: under
Low count: 1
Low values: [341.83447265625]

File: SN20USBHX2004655_25.json
Stream: under
Low count: 1
Low values: [381.26397705078125]


Module: SN20USBHX2004830
--------------------------------------------------------------------------------
Module total values: 48

File: SN20USBHX2004830_02.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_03.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_04.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_05.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_06.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_07.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_08.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_09.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_10.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_11.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_12.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_13.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_14.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_15.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_16.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_17.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_18.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_19.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_20.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_21.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_22.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_23.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_24.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_25.json
Stream: under
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_02.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_03.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_04.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_05.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_06.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_07.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_08.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_09.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_10.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_11.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_12.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_13.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_14.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_15.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_16.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_17.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_18.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_19.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_20.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_21.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_22.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_23.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_24.json
Stream: away
Low count: 1
Low values: [0.0]

File: SN20USBHX2004830_25.json
Stream: away
Low count: 1
Low values: [0.0]


Module: SN20USBHX2004836
--------------------------------------------------------------------------------
Module total values: 75

File: SN20USBHX2004836_01.json
Stream: under
Low count: 3
Low values: [374.1708068847656, 381.56011962890625, 392.2890625]

File: SN20USBHX2004836_02.json
Stream: under
Low count: 3
Low values: [341.5677490234375, 345.2126159667969, 339.95452880859375]

File: SN20USBHX2004836_03.json
Stream: under
Low count: 3
Low values: [337.5146484375, 337.18310546875, 340.88250732421875]

File: SN20USBHX2004836_04.json
Stream: under
Low count: 3
Low values: [390.6495361328125, 376.63714599609375, 383.5110168457031]

File: SN20USBHX2004836_05.json
Stream: under
Low count: 3
Low values: [347.9247741699219, 350.30889892578125, 333.80224609375]

File: SN20USBHX2004836_06.json
Stream: under
Low count: 3
Low values: [377.94952392578125, 386.8912353515625, 382.0897216796875]

File: SN20USBHX2004836_07.json
Stream: under
Low count: 3
Low values: [340.59698486328125, 342.8755798339844, 339.8984680175781]

File: SN20USBHX2004836_08.json
Stream: under
Low count: 3
Low values: [382.88336181640625, 379.9331970214844, 394.4629821777344]

File: SN20USBHX2004836_09.json
Stream: under
Low count: 3
Low values: [344.0728759765625, 330.8050537109375, 328.9173278808594]

File: SN20USBHX2004836_10.json
Stream: under
Low count: 3
Low values: [395.4801330566406, 372.6440734863281, 383.8052978515625]

File: SN20USBHX2004836_11.json
Stream: under
Low count: 3
Low values: [351.8410949707031, 324.9787902832031, 340.5419921875]

File: SN20USBHX2004836_12.json
Stream: under
Low count: 3
Low values: [370.7364501953125, 383.4402770996094, 390.05859375]

File: SN20USBHX2004836_13.json
Stream: under
Low count: 3
Low values: [340.36614990234375, 340.2578125, 334.4815673828125]

File: SN20USBHX2004836_14.json
Stream: under
Low count: 3
Low values: [383.103515625, 380.91796875, 385.0952453613281]

File: SN20USBHX2004836_15.json
Stream: under
Low count: 3
Low values: [343.0424499511719, 342.2506408691406, 341.47625732421875]

File: SN20USBHX2004836_16.json
Stream: under
Low count: 3
Low values: [386.7489318847656, 388.0162353515625, 380.00946044921875]

File: SN20USBHX2004836_17.json
Stream: under
Low count: 3
Low values: [330.4313049316406, 338.21124267578125, 345.0726318359375]

File: SN20USBHX2004836_18.json
Stream: under
Low count: 3
Low values: [383.0343017578125, 390.8868408203125, 373.8987731933594]

File: SN20USBHX2004836_19.json
Stream: under
Low count: 3
Low values: [338.5275573730469, 345.8805236816406, 346.208740234375]

File: SN20USBHX2004836_20.json
Stream: under
Low count: 3
Low values: [387.06622314453125, 372.50933837890625, 376.9022216796875]

File: SN20USBHX2004836_21.json
Stream: under
Low count: 3
Low values: [334.0997619628906, 328.0504150390625, 330.49139404296875]

File: SN20USBHX2004836_22.json
Stream: under
Low count: 3
Low values: [373.76617431640625, 371.69580078125, 381.2904357910156]

File: SN20USBHX2004836_23.json
Stream: under
Low count: 3
Low values: [350.0417785644531, 337.9535827636719, 353.8390808105469]

File: SN20USBHX2004836_24.json
Stream: under
Low count: 3
Low values: [331.9676513671875, 328.9905090332031, 352.5846252441406]

File: SN20USBHX2004836_25.json
Stream: under
Low count: 3
Low values: [387.7929382324219, 376.0825500488281, 388.0596618652344]


Module: SN20USBHX2004983
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2004983_01.json
Stream: away
Low count: 1
Low values: [393.8240661621094]

File: SN20USBHX2004983_02.json
Stream: away
Low count: 1
Low values: [344.4841613769531]

File: SN20USBHX2004983_03.json
Stream: away
Low count: 1
Low values: [336.425048828125]

File: SN20USBHX2004983_04.json
Stream: away
Low count: 1
Low values: [394.53509521484375]

File: SN20USBHX2004983_05.json
Stream: away
Low count: 1
Low values: [346.8409729003906]

File: SN20USBHX2004983_06.json
Stream: away
Low count: 1
Low values: [387.15277099609375]

File: SN20USBHX2004983_07.json
Stream: away
Low count: 1
Low values: [338.3089599609375]

File: SN20USBHX2004983_08.json
Stream: away
Low count: 1
Low values: [376.90325927734375]

File: SN20USBHX2004983_09.json
Stream: away
Low count: 1
Low values: [347.34283447265625]

File: SN20USBHX2004983_10.json
Stream: away
Low count: 1
Low values: [381.4718017578125]

File: SN20USBHX2004983_11.json
Stream: away
Low count: 1
Low values: [350.7365417480469]

File: SN20USBHX2004983_12.json
Stream: away
Low count: 1
Low values: [393.58941650390625]

File: SN20USBHX2004983_13.json
Stream: away
Low count: 1
Low values: [341.0383605957031]

File: SN20USBHX2004983_14.json
Stream: away
Low count: 1
Low values: [392.8285827636719]

File: SN20USBHX2004983_15.json
Stream: away
Low count: 1
Low values: [350.22613525390625]

File: SN20USBHX2004983_16.json
Stream: away
Low count: 1
Low values: [388.07861328125]

File: SN20USBHX2004983_17.json
Stream: away
Low count: 1
Low values: [343.9280090332031]

File: SN20USBHX2004983_18.json
Stream: away
Low count: 1
Low values: [364.1132507324219]

File: SN20USBHX2004983_19.json
Stream: away
Low count: 1
Low values: [349.7763671875]

File: SN20USBHX2004983_20.json
Stream: away
Low count: 1
Low values: [384.1327209472656]

File: SN20USBHX2004983_21.json
Stream: away
Low count: 1
Low values: [351.4002685546875]

File: SN20USBHX2004983_22.json
Stream: away
Low count: 1
Low values: [383.2178955078125]

File: SN20USBHX2004983_23.json
Stream: away
Low count: 1
Low values: [356.2360534667969]

File: SN20USBHX2004983_24.json
Stream: away
Low count: 1
Low values: [346.5417175292969]

File: SN20USBHX2004983_25.json
Stream: away
Low count: 1
Low values: [386.15924072265625]


Module: SN20USBHX2005038
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2005038_01.json
Stream: away
Low count: 1
Low values: [374.7625732421875]

File: SN20USBHX2005038_02.json
Stream: away
Low count: 1
Low values: [340.4615783691406]

File: SN20USBHX2005038_03.json
Stream: away
Low count: 1
Low values: [340.07525634765625]

File: SN20USBHX2005038_04.json
Stream: away
Low count: 1
Low values: [383.5696716308594]

File: SN20USBHX2005038_05.json
Stream: away
Low count: 1
Low values: [337.879150390625]

File: SN20USBHX2005038_06.json
Stream: away
Low count: 1
Low values: [371.86248779296875]

File: SN20USBHX2005038_07.json
Stream: away
Low count: 1
Low values: [325.2825927734375]

File: SN20USBHX2005038_08.json
Stream: away
Low count: 1
Low values: [390.42230224609375]

File: SN20USBHX2005038_09.json
Stream: away
Low count: 1
Low values: [332.1176452636719]

File: SN20USBHX2005038_10.json
Stream: away
Low count: 1
Low values: [366.2003479003906]

File: SN20USBHX2005038_11.json
Stream: away
Low count: 1
Low values: [328.43670654296875]

File: SN20USBHX2005038_12.json
Stream: away
Low count: 1
Low values: [373.4637756347656]

File: SN20USBHX2005038_13.json
Stream: away
Low count: 1
Low values: [329.2010803222656]

File: SN20USBHX2005038_14.json
Stream: away
Low count: 1
Low values: [379.2802734375]

File: SN20USBHX2005038_15.json
Stream: away
Low count: 1
Low values: [343.5033264160156]

File: SN20USBHX2005038_16.json
Stream: away
Low count: 1
Low values: [380.237548828125]

File: SN20USBHX2005038_17.json
Stream: away
Low count: 1
Low values: [332.10595703125]

File: SN20USBHX2005038_18.json
Stream: away
Low count: 1
Low values: [379.24676513671875]

File: SN20USBHX2005038_19.json
Stream: away
Low count: 1
Low values: [341.4275207519531]

File: SN20USBHX2005038_20.json
Stream: away
Low count: 1
Low values: [367.90313720703125]

File: SN20USBHX2005038_21.json
Stream: away
Low count: 1
Low values: [339.12664794921875]

File: SN20USBHX2005038_22.json
Stream: away
Low count: 1
Low values: [382.5079040527344]

File: SN20USBHX2005038_23.json
Stream: away
Low count: 1
Low values: [335.55340576171875]

File: SN20USBHX2005038_24.json
Stream: away
Low count: 1
Low values: [341.92742919921875]

File: SN20USBHX2005038_25.json
Stream: away
Low count: 1
Low values: [378.3236389160156]


Module: SN20USBHX2005039
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2005039_01.json
Stream: under
Low count: 1
Low values: [393.16796875]

File: SN20USBHX2005039_02.json
Stream: under
Low count: 1
Low values: [362.8542785644531]

File: SN20USBHX2005039_03.json
Stream: under
Low count: 1
Low values: [360.40753173828125]

File: SN20USBHX2005039_04.json
Stream: under
Low count: 1
Low values: [412.02813720703125]

File: SN20USBHX2005039_05.json
Stream: under
Low count: 1
Low values: [348.6335754394531]

File: SN20USBHX2005039_06.json
Stream: under
Low count: 1
Low values: [395.8945617675781]

File: SN20USBHX2005039_07.json
Stream: under
Low count: 1
Low values: [350.49945068359375]

File: SN20USBHX2005039_08.json
Stream: under
Low count: 1
Low values: [394.0195007324219]

File: SN20USBHX2005039_09.json
Stream: under
Low count: 1
Low values: [363.6122741699219]

File: SN20USBHX2005039_10.json
Stream: under
Low count: 1
Low values: [383.7923583984375]

File: SN20USBHX2005039_11.json
Stream: under
Low count: 1
Low values: [364.7920227050781]

File: SN20USBHX2005039_12.json
Stream: under
Low count: 1
Low values: [389.7299499511719]

File: SN20USBHX2005039_13.json
Stream: under
Low count: 1
Low values: [348.50274658203125]

File: SN20USBHX2005039_14.json
Stream: under
Low count: 1
Low values: [403.07073974609375]

File: SN20USBHX2005039_15.json
Stream: under
Low count: 1
Low values: [333.4677429199219]

File: SN20USBHX2005039_16.json
Stream: under
Low count: 1
Low values: [403.27203369140625]

File: SN20USBHX2005039_17.json
Stream: under
Low count: 1
Low values: [356.9209899902344]

File: SN20USBHX2005039_18.json
Stream: under
Low count: 1
Low values: [413.26373291015625]

File: SN20USBHX2005039_19.json
Stream: under
Low count: 1
Low values: [359.10284423828125]

File: SN20USBHX2005039_20.json
Stream: under
Low count: 1
Low values: [392.9287109375]

File: SN20USBHX2005039_21.json
Stream: under
Low count: 1
Low values: [346.2433166503906]

File: SN20USBHX2005039_22.json
Stream: under
Low count: 1
Low values: [415.40301513671875]

File: SN20USBHX2005039_23.json
Stream: under
Low count: 1
Low values: [366.4178466796875]

File: SN20USBHX2005039_24.json
Stream: under
Low count: 1
Low values: [363.48370361328125]

File: SN20USBHX2005039_25.json
Stream: under
Low count: 1
Low values: [408.2847595214844]


Module: SN20USBHX2005049
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2005049_01.json
Stream: away
Low count: 1
Low values: [393.08648681640625]

File: SN20USBHX2005049_02.json
Stream: away
Low count: 1
Low values: [349.10675048828125]

File: SN20USBHX2005049_03.json
Stream: away
Low count: 1
Low values: [350.7447204589844]

File: SN20USBHX2005049_04.json
Stream: away
Low count: 1
Low values: [385.8345031738281]

File: SN20USBHX2005049_05.json
Stream: away
Low count: 1
Low values: [367.562744140625]

File: SN20USBHX2005049_06.json
Stream: away
Low count: 1
Low values: [389.19415283203125]

File: SN20USBHX2005049_07.json
Stream: away
Low count: 1
Low values: [353.5692138671875]

File: SN20USBHX2005049_08.json
Stream: away
Low count: 1
Low values: [391.1476135253906]

File: SN20USBHX2005049_09.json
Stream: away
Low count: 1
Low values: [340.7641906738281]

File: SN20USBHX2005049_10.json
Stream: away
Low count: 1
Low values: [381.4944152832031]

File: SN20USBHX2005049_11.json
Stream: away
Low count: 1
Low values: [348.856689453125]

File: SN20USBHX2005049_12.json
Stream: away
Low count: 1
Low values: [406.3385314941406]

File: SN20USBHX2005049_13.json
Stream: away
Low count: 1
Low values: [351.3046875]

File: SN20USBHX2005049_14.json
Stream: away
Low count: 1
Low values: [393.38214111328125]

File: SN20USBHX2005049_15.json
Stream: away
Low count: 1
Low values: [348.6329040527344]

File: SN20USBHX2005049_16.json
Stream: away
Low count: 1
Low values: [409.2156066894531]

File: SN20USBHX2005049_17.json
Stream: away
Low count: 1
Low values: [340.8448181152344]

File: SN20USBHX2005049_18.json
Stream: away
Low count: 1
Low values: [409.00372314453125]

File: SN20USBHX2005049_19.json
Stream: away
Low count: 1
Low values: [348.6893310546875]

File: SN20USBHX2005049_20.json
Stream: away
Low count: 1
Low values: [388.3991394042969]

File: SN20USBHX2005049_21.json
Stream: away
Low count: 1
Low values: [358.5591735839844]

File: SN20USBHX2005049_22.json
Stream: away
Low count: 1
Low values: [408.1213073730469]

File: SN20USBHX2005049_23.json
Stream: away
Low count: 1
Low values: [350.4752502441406]

File: SN20USBHX2005049_24.json
Stream: away
Low count: 1
Low values: [353.6114196777344]

File: SN20USBHX2005049_25.json
Stream: away
Low count: 1
Low values: [388.32427978515625]


Module: SN20USBHX2005234
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2005234_01.json
Stream: under
Low count: 1
Low values: [373.18731689453125]

File: SN20USBHX2005234_02.json
Stream: under
Low count: 1
Low values: [330.0998840332031]

File: SN20USBHX2005234_03.json
Stream: under
Low count: 1
Low values: [348.4044189453125]

File: SN20USBHX2005234_04.json
Stream: under
Low count: 1
Low values: [377.4714660644531]

File: SN20USBHX2005234_05.json
Stream: under
Low count: 1
Low values: [345.44671630859375]

File: SN20USBHX2005234_06.json
Stream: under
Low count: 1
Low values: [391.6324157714844]

File: SN20USBHX2005234_07.json
Stream: under
Low count: 1
Low values: [329.5517272949219]

File: SN20USBHX2005234_08.json
Stream: under
Low count: 1
Low values: [379.7406311035156]

File: SN20USBHX2005234_09.json
Stream: under
Low count: 1
Low values: [330.771728515625]

File: SN20USBHX2005234_10.json
Stream: under
Low count: 1
Low values: [370.3697814941406]

File: SN20USBHX2005234_11.json
Stream: under
Low count: 1
Low values: [335.8021545410156]

File: SN20USBHX2005234_12.json
Stream: under
Low count: 1
Low values: [367.2659606933594]

File: SN20USBHX2005234_13.json
Stream: under
Low count: 1
Low values: [339.7910461425781]

File: SN20USBHX2005234_14.json
Stream: under
Low count: 1
Low values: [370.39422607421875]

File: SN20USBHX2005234_15.json
Stream: under
Low count: 1
Low values: [337.8077087402344]

File: SN20USBHX2005234_16.json
Stream: under
Low count: 1
Low values: [375.7676696777344]

File: SN20USBHX2005234_17.json
Stream: under
Low count: 1
Low values: [330.5905456542969]

File: SN20USBHX2005234_18.json
Stream: under
Low count: 1
Low values: [388.4571838378906]

File: SN20USBHX2005234_19.json
Stream: under
Low count: 1
Low values: [332.5722351074219]

File: SN20USBHX2005234_20.json
Stream: under
Low count: 1
Low values: [362.539794921875]

File: SN20USBHX2005234_21.json
Stream: under
Low count: 1
Low values: [320.733154296875]

File: SN20USBHX2005234_22.json
Stream: under
Low count: 1
Low values: [374.33721923828125]

File: SN20USBHX2005234_23.json
Stream: under
Low count: 1
Low values: [338.68853759765625]

File: SN20USBHX2005234_24.json
Stream: under
Low count: 1
Low values: [338.42742919921875]

File: SN20USBHX2005234_25.json
Stream: under
Low count: 1
Low values: [372.4063415527344]


Module: SN20USBHX2005248
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2005248_01.json
Stream: away
Low count: 1
Low values: [385.139892578125]

File: SN20USBHX2005248_02.json
Stream: away
Low count: 1
Low values: [345.98089599609375]

File: SN20USBHX2005248_03.json
Stream: away
Low count: 1
Low values: [350.0758972167969]

File: SN20USBHX2005248_04.json
Stream: away
Low count: 1
Low values: [392.6451416015625]

File: SN20USBHX2005248_05.json
Stream: away
Low count: 1
Low values: [344.5312805175781]

File: SN20USBHX2005248_06.json
Stream: away
Low count: 1
Low values: [380.767578125]

File: SN20USBHX2005248_07.json
Stream: away
Low count: 1
Low values: [369.72637939453125]

File: SN20USBHX2005248_08.json
Stream: away
Low count: 1
Low values: [381.2389221191406]

File: SN20USBHX2005248_09.json
Stream: away
Low count: 1
Low values: [338.8789367675781]

File: SN20USBHX2005248_10.json
Stream: away
Low count: 1
Low values: [390.0450439453125]

File: SN20USBHX2005248_11.json
Stream: away
Low count: 1
Low values: [362.94598388671875]

File: SN20USBHX2005248_12.json
Stream: away
Low count: 1
Low values: [386.29168701171875]

File: SN20USBHX2005248_13.json
Stream: away
Low count: 1
Low values: [337.8201599121094]

File: SN20USBHX2005248_14.json
Stream: away
Low count: 1
Low values: [388.76409912109375]

File: SN20USBHX2005248_15.json
Stream: away
Low count: 1
Low values: [350.58685302734375]

File: SN20USBHX2005248_16.json
Stream: away
Low count: 1
Low values: [393.32489013671875]

File: SN20USBHX2005248_17.json
Stream: away
Low count: 1
Low values: [338.3775939941406]

File: SN20USBHX2005248_18.json
Stream: away
Low count: 1
Low values: [396.3598327636719]

File: SN20USBHX2005248_19.json
Stream: away
Low count: 1
Low values: [338.3165283203125]

File: SN20USBHX2005248_20.json
Stream: away
Low count: 1
Low values: [399.13189697265625]

File: SN20USBHX2005248_21.json
Stream: away
Low count: 1
Low values: [341.0011901855469]

File: SN20USBHX2005248_22.json
Stream: away
Low count: 1
Low values: [393.4747009277344]

File: SN20USBHX2005248_23.json
Stream: away
Low count: 1
Low values: [358.80584716796875]

File: SN20USBHX2005248_24.json
Stream: away
Low count: 1
Low values: [345.58709716796875]

File: SN20USBHX2005248_25.json
Stream: away
Low count: 1
Low values: [406.8087463378906]


Module: SN20USBHX2005299
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2005299_01.json
Stream: away
Low count: 1
Low values: [388.84844970703125]

File: SN20USBHX2005299_02.json
Stream: away
Low count: 1
Low values: [329.3041076660156]

File: SN20USBHX2005299_03.json
Stream: away
Low count: 1
Low values: [347.30413818359375]

File: SN20USBHX2005299_04.json
Stream: away
Low count: 1
Low values: [386.8785400390625]

File: SN20USBHX2005299_05.json
Stream: away
Low count: 1
Low values: [339.9085388183594]

File: SN20USBHX2005299_06.json
Stream: away
Low count: 1
Low values: [366.2201843261719]

File: SN20USBHX2005299_07.json
Stream: away
Low count: 1
Low values: [350.6925964355469]

File: SN20USBHX2005299_08.json
Stream: away
Low count: 1
Low values: [381.71337890625]

File: SN20USBHX2005299_09.json
Stream: away
Low count: 1
Low values: [347.72308349609375]

File: SN20USBHX2005299_10.json
Stream: away
Low count: 1
Low values: [378.0365295410156]

File: SN20USBHX2005299_11.json
Stream: away
Low count: 1
Low values: [330.0684814453125]

File: SN20USBHX2005299_12.json
Stream: away
Low count: 1
Low values: [382.2278747558594]

File: SN20USBHX2005299_13.json
Stream: away
Low count: 1
Low values: [340.85858154296875]

File: SN20USBHX2005299_14.json
Stream: away
Low count: 1
Low values: [391.9931640625]

File: SN20USBHX2005299_15.json
Stream: away
Low count: 1
Low values: [348.648681640625]

File: SN20USBHX2005299_16.json
Stream: away
Low count: 1
Low values: [370.4561462402344]

File: SN20USBHX2005299_17.json
Stream: away
Low count: 1
Low values: [336.9269104003906]

File: SN20USBHX2005299_18.json
Stream: away
Low count: 1
Low values: [393.62738037109375]

File: SN20USBHX2005299_19.json
Stream: away
Low count: 1
Low values: [341.6053771972656]

File: SN20USBHX2005299_20.json
Stream: away
Low count: 1
Low values: [384.5771484375]

File: SN20USBHX2005299_21.json
Stream: away
Low count: 1
Low values: [344.5831604003906]

File: SN20USBHX2005299_22.json
Stream: away
Low count: 1
Low values: [368.8248291015625]

File: SN20USBHX2005299_23.json
Stream: away
Low count: 1
Low values: [340.6544494628906]

File: SN20USBHX2005299_24.json
Stream: away
Low count: 1
Low values: [343.46160888671875]

File: SN20USBHX2005299_25.json
Stream: away
Low count: 1
Low values: [369.9217224121094]


Module: SN20USBHX2005520
--------------------------------------------------------------------------------
Module total values: 25

File: SN20USBHX2005520_01.json
Stream: away
Low count: 1
Low values: [387.27459716796875]

File: SN20USBHX2005520_02.json
Stream: away
Low count: 1
Low values: [337.8443298339844]

File: SN20USBHX2005520_03.json
Stream: away
Low count: 1
Low values: [351.80157470703125]

File: SN20USBHX2005520_04.json
Stream: away
Low count: 1
Low values: [393.5741882324219]

File: SN20USBHX2005520_05.json
Stream: away
Low count: 1
Low values: [325.6495666503906]

File: SN20USBHX2005520_06.json
Stream: away
Low count: 1
Low values: [380.31500244140625]

File: SN20USBHX2005520_07.json
Stream: away
Low count: 1
Low values: [334.6705627441406]

File: SN20USBHX2005520_08.json
Stream: away
Low count: 1
Low values: [379.79840087890625]

File: SN20USBHX2005520_09.json
Stream: away
Low count: 1
Low values: [318.7734375]

File: SN20USBHX2005520_10.json
Stream: away
Low count: 1
Low values: [373.4195251464844]

File: SN20USBHX2005520_11.json
Stream: away
Low count: 1
Low values: [333.9327087402344]

File: SN20USBHX2005520_12.json
Stream: away
Low count: 1
Low values: [400.084228515625]

File: SN20USBHX2005520_13.json
Stream: away
Low count: 1
Low values: [330.40765380859375]

File: SN20USBHX2005520_14.json
Stream: away
Low count: 1
Low values: [392.83819580078125]

File: SN20USBHX2005520_15.json
Stream: away
Low count: 1
Low values: [342.0248718261719]

File: SN20USBHX2005520_16.json
Stream: away
Low count: 1
Low values: [387.5853271484375]

File: SN20USBHX2005520_17.json
Stream: away
Low count: 1
Low values: [321.6617736816406]

File: SN20USBHX2005520_18.json
Stream: away
Low count: 1
Low values: [381.1885070800781]

File: SN20USBHX2005520_19.json
Stream: away
Low count: 1
Low values: [346.66412353515625]

File: SN20USBHX2005520_20.json
Stream: away
Low count: 1
Low values: [374.19903564453125]

File: SN20USBHX2005520_21.json
Stream: away
Low count: 1
Low values: [339.3340759277344]

File: SN20USBHX2005520_22.json
Stream: away
Low count: 1
Low values: [396.51043701171875]

File: SN20USBHX2005520_23.json
Stream: away
Low count: 1
Low values: [333.0934753417969]

File: SN20USBHX2005520_24.json
Stream: away
Low count: 1
Low values: [338.8210754394531]

File: SN20USBHX2005520_25.json
Stream: away
Low count: 1
Low values: [377.820556640625]


Module: SN20USBHX2005564
--------------------------------------------------------------------------------
Module total values: 2

File: SN20USBHX2005564_20.json
Stream: away
Low count: 2
Low values: [0.0, 0.0]


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