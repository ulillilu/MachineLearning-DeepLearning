import pandas as pd

tbl = pd.DataFrame({
    "weight": [ 80.0, 70.4, 65.5, 45.9, 51.2, 72.5 ],
    "height": [ 170,  180,  155,  143,  154,  160  ],
    "gender": [ "f",  "m",  "m",  "f",  "f",  "m"  ]
})

# 최대값과 최소값을 이용한 정규화 함수
def norm(tbl, key):
    c = tbl[key]
    v_max = c.max() #각 속성의 최대값
    v_min = c.min() #각 속성의 최소값
    print(key, "=", v_min, "-", v_max)
    tbl[key] = (c - v_min) / (v_max - v_min) # 정규화((값-최소)/(최대-최소))
norm(tbl, "weight")
norm(tbl, "height")
print(tbl)