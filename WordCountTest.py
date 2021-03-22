logFile = "file:///home/hadoop/spark-2.1.0-bin-hadoop2.7/README.md"


sc.textFile(r'C:\Users\bryanleekw\PycharmProjects\WordCount\file.txt')

logFile = "C:\\tmp\\hadoop\\file.txt"


logData = sc.textFile(logFile).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
print "Lines with a: %i, lines with b: %i" % (numAs, numBs)