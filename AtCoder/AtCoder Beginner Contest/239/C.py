x1,y1,x2,y2=map(int,input().split())
ans='No'
if abs(x1-x2)==0 and abs(y1-y2)==0:ans='Yes'
if abs(x1-x2)==0 and abs(y1-y2)==2:ans='Yes'
if abs(x1-x2)==0 and abs(y1-y2)==4:ans='Yes'
if abs(x1-x2)==1 and abs(y1-y2)==1:ans='Yes'
if abs(x1-x2)==1 and abs(y1-y2)==3:ans='Yes'
if abs(x1-x2)==2 and abs(y1-y2)==0:ans='Yes'
if abs(x1-x2)==2 and abs(y1-y2)==4:ans='Yes'
if abs(x1-x2)==3 and abs(y1-y2)==1:ans='Yes'
if abs(x1-x2)==3 and abs(y1-y2)==3:ans='Yes'
if abs(x1-x2)==4 and abs(y1-y2)==0:ans='Yes'
if abs(x1-x2)==4 and abs(y1-y2)==2:ans='Yes'
print(ans)