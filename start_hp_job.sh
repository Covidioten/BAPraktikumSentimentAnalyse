hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar -files tokenmapper.py,sumreducer.py -mapper tokenmapper.py -reducer sumreducer.py -input /data/twitter2020 -output twitter_wc
