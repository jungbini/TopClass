# -*- encoding:utf-8-*-
import os
from rake_nltk import Rake

def mergeLogFile():
    
    OUT_FILE = open(LOG_PATH + 'logmessages.txt', 'w')
    LogMsgs = list()
     
    for subject in SUBJECT_LIST:
     
        for path, dir, files in os.walk(LOG_PATH + subject):
             
            print 'Reading ' + path
 
            for filename in files:
                 
                srcfile             = path + '/' + filename                                     # 소스파일 경로                                
                src_contents        = open(srcfile, 'r').read()
                 
                LogMsgs.append(src_contents) 
                 
                OUT_FILE.write(src_contents + '\n')
    
#     r = Rake()
#     
#     r.extract_keywords_from_sentences(LogMsgs)
#     print r.get_ranked_phrases()

LOG_PATH = './logmessages/'
SUBJECT_LIST = ['Actor','Alluxio','Bazel','Buck','Cassandra','ClosureCompiler','CoreNLP',
                'Deeplearning4j','Druid','GoPlugin4IntelliJ','Gradle','Graylog','Hadoop',
                'IntelliJIDEA','Kotlin','Netty','openHAB','OrientDB','PDE','SpringFramework',
                'ApacheStorm','Atmosphere','FastJSON','JNA','Kafka','Nokogiri','Pinpoint',
                'Titan','Vertx','Zeppelin']

mergeLogFile()