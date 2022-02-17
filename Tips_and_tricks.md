###TIPS AND TRICKS

***Bitwise operation***

**XOR** - Cancels out same digits. 
```bash
So, 
10 XOR 10 = 0
```

**Left Shift** - Multiplies a number by 2. 
```bash
So, 
10 << 1 = 20
10 << 2 = 40
```
**Right Shift** - Divides a number by 2. 
```bash
So, 
10 >> 1 = 5
10 >> 2 = 2
```
**Check for last bit of the no.**
```bash
if number & 1 == 0 then last bit is 0
else if number & 1 == 1 then last bit is 1

eg. 7(111) & 1(001) = 1(001)
    6(110) & 1(001) = 0(000)

```
