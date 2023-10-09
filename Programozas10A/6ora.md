# Programozás óra 6. óra 2023.10.09

### Eldöntés
```Python
i := 1
Ciklus i <= N and not T(x[i])
    i:= i+1
Ciklus vége
van := i <= N
```

```mermaid
---
title: Folyamatábra
---
flowchart TD
    id["i := 1"] --> id1{"Ciklus i <= N and not T(x[i])"} --> id2["i := i+1"]
```
flowchart Top-Down vagy Left-Right

![asd](6-1.png)

### Kiválasztás
```Python
i := 1
nem T(x[i])
    i := i+1
ind := i
érték := x[i]
```
![asd](6-2.png)