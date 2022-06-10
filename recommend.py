
def recommend(customers):
    d={}
    for i in range(1,26):
        d[i]=0

    for i in customers:
        x=i[0]
        y=i[1]

        if x<20 and y<20:
            d[1]+=1
        elif x<40 and y<20:
            d[2]+=1
        elif x<60 and y>20:
            d[3]+=1
        elif x<80 and y>20:
            d[4]+=1
        elif x>80 and y<20:
            d[5]+=1
        elif x<20 and y<40:
            d[6]+=1
        elif x<40 and y<40:
            d[7]+=1
        elif x<60 and y<40:
            d[8]+=1
        elif x<80 and y<40:
            d[9]+=1
        elif x>80 and y<40:
            d[10]+=1
        elif x<20 and y<60:
            d[11]+=1
        elif x<40 and y<60:
            d[12]+=1
        elif x<60 and y<60:
            d[13]+=1
        elif x<80 and y<60:
            d[14]+=1
        elif x>80 and y<60:
            d[15]+=1
        elif x<20 and y<80:
            d[16]+=1
        elif x<40 and y<80:
            d[17]+=1
        elif x<60 and y<80:
            d[18]+=1
        elif x<80 and y<80:
            d[19]+=1
        elif x>80 and y<80:
            d[20]+=1
        elif x<20 and y<80:
            d[21]+=1
        elif x<40 and y<80:
            d[22]+=1
        elif x<60 and y<80:
            d[23]+=1
        elif x<80 and y<80:
            d[24]+=1
        elif x>80 and y<80:
            d[25]+=1
    return d


