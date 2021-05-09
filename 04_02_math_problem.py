
import re

op = ["*", ""]
for i in range(1000,10000,1):
    c = str(i)
    for j in range(0, len(op)):
        for k in range(0, len(op)):
            for l in range(0, len(op)):

                val = c[3] + op[j] + c[2] + op[k] + c[1] + op[l] + c[0]
                val = re.sub(r'\b0+(?!\b)', '', val)

                if len(val) > 4:
                    if i == eval(val):
                        
                        print("------------")
                        print("step:" + str(i))
                        print("------------")
                        print(val)
