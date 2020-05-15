import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["twitter"]
mycol = mydb["tweets"]
mycol1=mydb["news"]

for x in mycol.find({},{"_id": 0,"tweet_text": 1 }):
  for z,y in x.items():
      print(type(y))
      f=open("mongotweetext.txt",'a')
      if y != None:
        f.write(y+'\n')
f.close()

for x in mycol1.find({},{"_id": 0,"content": 1 }):
  for z,y in x.items():
      print(y)
      f=open("mongonewsext.txt",'a')
      if y != None:
        f.write(y+'\n')
f.close()