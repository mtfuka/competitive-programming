A,B,C = map(int,input().split())
if A%10==0:print(0)
if A%10==1:print(1)
if A%10==2:
  if B%4==0:print(6)
  if B%4==1:print(2)
  if B%4==2:
    if C==1:print(4)
    else:print(6)
  if B%4==3:
    if C%2==0:print(2)
    if C%2==1:print(8)
if A%10==3:
  if B%4==0:print(1)
  if B%4==1:print(3)
  if B%4==2:
    if C==1:print(9)
    else:print(1)
  if B%4==3:
    if C%2==0:print(3)
    if C%2==1:print(7)
if A%10==4:
  if B%2==0:print(6)
  if B%2==1:print(4)
if A%10==5:print(5)
if A%10==6:print(6)
if A%10==7:
  if B%4==0:print(1)
  if B%4==1:print(7)
  if B%4==2:
    if C==1:print(9)
    else:print(1)
  if B%4==3:
    if C%2==0:print(7)
    if C%2==1:print(3)
if A%10==8:
  if B%4==0:print(6)
  if B%4==1:print(8)
  if B%4==2:
    if C==1:print(4)
    else:print(6)
  if B%4==3:
    if C%2==0:print(8)
    if C%2==1:print(2)
if A%10==9:
  if B%2==0:print(1)
  if B%2==1:print(9)
