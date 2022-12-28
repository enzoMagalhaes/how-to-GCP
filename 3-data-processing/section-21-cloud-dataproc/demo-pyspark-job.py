#!/usr/bin/python

import pyspark

sc = pyspark.SparkContext()
rdd = sc.parallelize(['Hello','World!'])
words = sorted(rdd.collect())
print(words)
