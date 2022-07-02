K=int(input())
HH=21+K//60
MM=K%60
if 0<=MM<10:MM=f"0{MM}"
print(f"{HH}:{MM}")