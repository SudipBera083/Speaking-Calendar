import datetime
import bonggoQuery
date = str(datetime.datetime.now())
# print(type(date))
# print(date)
list1 = date.split(" ")
# print(list1)
date1 = str(list1[0])
time1 = str(list1[1])
time2 = time1.split(":")


# print(date1)
date2 = date1.split("-")
month = date2[1]
# print(date2)

def printDate(month):
    data= str(month)
    
    if data == "01":
        print("January")
        bonggoQuery.Query.normal_query.speaking("January")
    elif data =="02":
        print("February")
        bonggoQuery.Query.normal_query.speaking("February")
    elif data =="03":
        print("March")
        bonggoQuery.Query.normal_query.speaking("March")
    elif data =="04":
        print("April")
        bonggoQuery.Query.normal_query.speaking("April")
    elif data =="05":
        print("May")
        bonggoQuery.Query.normal_query.speaking("May")
    elif data =="06":
        print("June")
        bonggoQuery.Query.normal_query.speaking("June")
    elif data =="07":
        print("Julay")
        bonggoQuery.Query.normal_query.speaking("Julay")
    elif data =="08":
        print("August")
        bonggoQuery.Query.normal_query.speaking("August")
    elif data =="09":
        print("September")
        bonggoQuery.Query.normal_query.speaking("September")
    elif data =="10":
        print("Octabor")
        bonggoQuery.Query.normal_query.speaking("Octabor")
    elif data =="11":
        print("November")
        bonggoQuery.Query.normal_query.speaking("November")
    elif data =="12":
        print("December")
        bonggoQuery.Query.normal_query.speaking("December")
    
if __name__== '__main__':
    
    
    print(date2[2])
    d1 = str(date2[2])
    bonggoQuery.Query.normal_query.speaking(d1)

    printDate(month)

    print(date2[0])
    d2 = str(date2[0])
    bonggoQuery.Query.normal_query.speaking(d2)
    print(f"{time2[0]} {time2[2]} {time2[2]}")


