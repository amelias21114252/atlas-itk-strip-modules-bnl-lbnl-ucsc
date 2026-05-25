import re

text = """

================================================================================
Category D
Incomplete dataset or missing generated files.
================================================================================

SN20USBML1236980
----------------
1. SN20USBML1236980_24.json — empty

SN20USBML1236982
----------------
1. SN20USBML1236982_24.json — empty

SN20USBML1237030
----------------
1. SN20USBML1237030_24.json — empty

SN20USBML1237068
----------------
1. SN20USBML1237068_24.json — empty

SN20USBML1238136
----------------
1. SN20USBML1238136_24.json — empty

SN20USBML1238167
----------------
1. SN20USBML1238167_24.json — empty

SN20USBML1238208
----------------
1. SN20USBML1238208_24.json — empty

SN20USBML1238214
----------------
1. SN20USBML1238214_24.json — empty

SN20USBML1238356
----------------
1. SN20USBML1238356_24.json — empty

SN20USBML1238531
----------------
1. SN20USBML1238531_02.json — empty
2. SN20USBML1238531_03.json — empty
3. SN20USBML1238531_04.json — empty
4. SN20USBML1238531_05.json — empty
5. SN20USBML1238531_06.json — empty
6. SN20USBML1238531_07.json — empty
7. SN20USBML1238531_08.json — empty
8. SN20USBML1238531_09.json — empty
9. SN20USBML1238531_10.json — empty
10. SN20USBML1238531_11.json — empty
11. SN20USBML1238531_12.json — empty
12. SN20USBML1238531_13.json — empty
13. SN20USBML1238531_14.json — empty
14. SN20USBML1238531_15.json — empty
15. SN20USBML1238531_16.json — empty
16. SN20USBML1238531_17.json — empty
17. SN20USBML1238531_18.json — empty
18. SN20USBML1238531_19.json — empty
19. SN20USBML1238531_20.json — empty
20. SN20USBML1238531_21.json — empty
21. SN20USBML1238531_22.json — empty
22. SN20USBML1238531_23.json — empty
23. SN20USBML1238531_24.json — empty

SN20USBML1238590
----------------
1. SN20USBML1238590_24.json — empty

SN20USBML1238591
----------------
1. SN20USBML1238591_24.json — empty

SN20USBML1238592
----------------
1. SN20USBML1238592_24.json — empty

SN20USBML1238838
----------------
1. SN20USBML1238838_23.json — empty
2. SN20USBML1238838_24.json — empty

SN20USBML1238843
----------------
1. SN20USBML1238843_02.json — empty
2. SN20USBML1238843_03.json — empty
3. SN20USBML1238843_04.json — empty
4. SN20USBML1238843_05.json — empty
5. SN20USBML1238843_06.json — empty
6. SN20USBML1238843_07.json — empty
7. SN20USBML1238843_08.json — empty
8. SN20USBML1238843_09.json — empty
9. SN20USBML1238843_10.json — empty
10. SN20USBML1238843_11.json — empty
11. SN20USBML1238843_12.json — empty
12. SN20USBML1238843_13.json — empty
13. SN20USBML1238843_14.json — empty
14. SN20USBML1238843_15.json — empty
15. SN20USBML1238843_16.json — empty
16. SN20USBML1238843_17.json — empty
17. SN20USBML1238843_18.json — empty
18. SN20USBML1238843_19.json — empty
19. SN20USBML1238843_20.json — empty
20. SN20USBML1238843_21.json — empty
21. SN20USBML1238843_22.json — empty
22. SN20USBML1238843_23.json — empty
23. SN20USBML1238843_24.json — empty

SN20USBML1238846
----------------
1. SN20USBML1238846_02.json — empty
2. SN20USBML1238846_03.json — empty
3. SN20USBML1238846_04.json — empty
4. SN20USBML1238846_05.json — empty
5. SN20USBML1238846_06.json — empty
6. SN20USBML1238846_07.json — empty
7. SN20USBML1238846_08.json — empty
8. SN20USBML1238846_09.json — empty
9. SN20USBML1238846_10.json — empty
10. SN20USBML1238846_11.json — empty
11. SN20USBML1238846_12.json — empty
12. SN20USBML1238846_13.json — empty
13. SN20USBML1238846_14.json — empty
14. SN20USBML1238846_15.json — empty
15. SN20USBML1238846_16.json — empty
16. SN20USBML1238846_17.json — empty
17. SN20USBML1238846_18.json — empty
18. SN20USBML1238846_19.json — empty
19. SN20USBML1238846_20.json — empty
20. SN20USBML1238846_21.json — empty
21. SN20USBML1238846_22.json — empty
22. SN20USBML1238846_23.json — empty
23. SN20USBML1238846_24.json — empty

SN20USBML1238849
----------------
1. SN20USBML1238849_02.json — empty
2. SN20USBML1238849_03.json — empty
3. SN20USBML1238849_04.json — empty
4. SN20USBML1238849_05.json — empty
5. SN20USBML1238849_06.json — empty
6. SN20USBML1238849_07.json — empty
7. SN20USBML1238849_08.json — empty
8. SN20USBML1238849_09.json — empty
9. SN20USBML1238849_10.json — empty
10. SN20USBML1238849_11.json — empty
11. SN20USBML1238849_12.json — empty
12. SN20USBML1238849_13.json — empty
13. SN20USBML1238849_14.json — empty
14. SN20USBML1238849_15.json — empty
15. SN20USBML1238849_16.json — empty
16. SN20USBML1238849_17.json — empty
17. SN20USBML1238849_18.json — empty
18. SN20USBML1238849_19.json — empty
19. SN20USBML1238849_20.json — empty
20. SN20USBML1238849_21.json — empty
21. SN20USBML1238849_22.json — empty
22. SN20USBML1238849_23.json — empty
23. SN20USBML1238849_24.json — empty
"""

# Find serials like SN20USBML1236980, 20USBML1236980, SN20USBHX2004272, etc.
serials = re.findall(r'\bSN?(20USB(?:HX|ML)\d+)\b', text)

# Remove duplicates but keep original order
unique_serials = []
seen = set()

for serial in serials:
    if serial not in seen:
        unique_serials.append(serial)
        seen.add(serial)

# Print in requested format
for serial in unique_serials:
    print(f'"{serial}",')
    print()