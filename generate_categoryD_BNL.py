import re

text = """


================================================================================
Category D
Incomplete dataset or missing generated files.
================================================================================

SN20USBML1235885
----------------
1. SN20USBML1235885_13.json — empty
2. SN20USBML1235885_14.json — empty
3. SN20USBML1235885_15.json — empty
4. SN20USBML1235885_16.json — empty
5. SN20USBML1235885_17.json — empty
6. SN20USBML1235885_18.json — empty
7. SN20USBML1235885_19.json — empty
8. SN20USBML1235885_20.json — empty
9. SN20USBML1235885_21.json — empty
10. SN20USBML1235885_22.json — empty
11. SN20USBML1235885_23.json — empty
12. SN20USBML1235885_24.json — empty

SN20USBML1235907
----------------
1. SN20USBML1235907_14.json — empty
2. SN20USBML1235907_15.json — empty
3. SN20USBML1235907_16.json — empty
4. SN20USBML1235907_17.json — empty
5. SN20USBML1235907_18.json — empty
6. SN20USBML1235907_19.json — empty
7. SN20USBML1235907_20.json — empty
8. SN20USBML1235907_21.json — empty
9. SN20USBML1235907_22.json — empty
10. SN20USBML1235907_23.json — empty
11. SN20USBML1235907_24.json — empty

SN20USBML1235927
----------------
1. SN20USBML1235927_21.json — empty
2. SN20USBML1235927_22.json — empty
3. SN20USBML1235927_23.json — empty
4. SN20USBML1235927_24.json — empty

SN20USBML1235928
----------------
1. SN20USBML1235928_21.json — empty
2. SN20USBML1235928_22.json — empty
3. SN20USBML1235928_23.json — empty
4. SN20USBML1235928_24.json — empty

SN20USBML1235929
----------------
1. SN20USBML1235929_21.json — empty
2. SN20USBML1235929_22.json — empty
3. SN20USBML1235929_23.json — empty
4. SN20USBML1235929_24.json — empty

SN20USBML1236106
----------------
1. SN20USBML1236106_20.json — empty
2. SN20USBML1236106_21.json — empty
3. SN20USBML1236106_22.json — empty
4. SN20USBML1236106_23.json — empty
5. SN20USBML1236106_24.json — empty

SN20USBML1236155
----------------
1. SN20USBML1236155_21.json — empty
2. SN20USBML1236155_22.json — empty
3. SN20USBML1236155_23.json — empty
4. SN20USBML1236155_24.json — empty

SN20USBML1236694
----------------
1. SN20USBML1236694_21.json — empty
2. SN20USBML1236694_22.json — empty
3. SN20USBML1236694_23.json — empty
4. SN20USBML1236694_24.json — empty

SN20USBML1236711
----------------
1. SN20USBML1236711_21.json — empty
2. SN20USBML1236711_22.json — empty
3. SN20USBML1236711_23.json — empty
4. SN20USBML1236711_24.json — empty

SN20USBML1237014
----------------
1. SN20USBML1237014_21.json — empty
2. SN20USBML1237014_22.json — empty
3. SN20USBML1237014_23.json — empty
4. SN20USBML1237014_24.json — empty

SN20USBML1237019
----------------
1. SN20USBML1237019_17.json — empty
2. SN20USBML1237019_18.json — empty
3. SN20USBML1237019_19.json — empty
4. SN20USBML1237019_20.json — empty
5. SN20USBML1237019_21.json — empty
6. SN20USBML1237019_22.json — empty
7. SN20USBML1237019_23.json — empty
8. SN20USBML1237019_24.json — empty

SN20USBML1237020
----------------
1. SN20USBML1237020_17.json — empty
2. SN20USBML1237020_18.json — empty
3. SN20USBML1237020_19.json — empty
4. SN20USBML1237020_20.json — empty
5. SN20USBML1237020_21.json — empty
6. SN20USBML1237020_22.json — empty
7. SN20USBML1237020_23.json — empty
8. SN20USBML1237020_24.json — empty

SN20USBML1237021
----------------
1. SN20USBML1237021_17.json — empty
2. SN20USBML1237021_18.json — empty
3. SN20USBML1237021_19.json — empty
4. SN20USBML1237021_20.json — empty
5. SN20USBML1237021_21.json — empty
6. SN20USBML1237021_22.json — empty
7. SN20USBML1237021_23.json — empty
8. SN20USBML1237021_24.json — empty

SN20USBML1237879
----------------
1. SN20USBML1237879_17.json — empty
2. SN20USBML1237879_18.json — empty
3. SN20USBML1237879_19.json — empty
4. SN20USBML1237879_20.json — empty
5. SN20USBML1237879_21.json — empty
6. SN20USBML1237879_22.json — empty
7. SN20USBML1237879_23.json — empty
8. SN20USBML1237879_24.json — empty

SN20USBML1237882
----------------
1. SN20USBML1237882_09.json — empty
2. SN20USBML1237882_10.json — empty
3. SN20USBML1237882_11.json — empty
4. SN20USBML1237882_12.json — empty
5. SN20USBML1237882_13.json — empty
6. SN20USBML1237882_14.json — empty
7. SN20USBML1237882_15.json — empty
8. SN20USBML1237882_16.json — empty
9. SN20USBML1237882_17.json — empty
10. SN20USBML1237882_18.json — empty
11. SN20USBML1237882_19.json — empty
12. SN20USBML1237882_20.json — empty
13. SN20USBML1237882_21.json — empty
14. SN20USBML1237882_22.json — empty
15. SN20USBML1237882_23.json — empty
16. SN20USBML1237882_24.json — empty

SN20USBML1237883
----------------
1. SN20USBML1237883_17.json — empty
2. SN20USBML1237883_18.json — empty
3. SN20USBML1237883_19.json — empty
4. SN20USBML1237883_20.json — empty
5. SN20USBML1237883_21.json — empty
6. SN20USBML1237883_22.json — empty
7. SN20USBML1237883_23.json — empty
8. SN20USBML1237883_24.json — empty

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