import datetime
  
data1 = "2019-08-02T21:56:22Z"
data2 = datetime.datetime.strptime(data1,"%Y-%m-%dT%H:%M:%SZ")
data3 = "'%s'" % data2
print(data3)