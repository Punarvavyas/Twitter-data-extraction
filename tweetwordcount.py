import operator
import pyspark

def main():

    with pyspark.SparkContext("local", "frequency") as sc:
        search_words = ["Canada", "university", "Dalhousie", "Halifax", "education","expensive","good school","good schools",
                        "bad school","bad schools","poor school","poor schools","faculty","computer science","graduate"]
        file = sc.textFile("mongotweetext.txt")
        words = file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1))
        counts = words.reduceByKey(operator.add)


        for word,count in counts.toLocalIterator():
            if word in search_words:
                print(u"{} --> {}".format(word, count))
                f=open("sparktweetoutput.txt",'a')
                f.write(u"{} --> {}".format(word, count) + "\n")


if __name__ == "__main__":
    main()