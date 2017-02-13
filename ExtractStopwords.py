# -*- encoding:utf-8-*-
import os, re, random
from nltk import word_tokenize
from collections import defaultdict

# Util �Լ�: �빮�ڷ� �����ϴ� �ռ��� �и�
def splitWords(WordList):
    
    newWordList = []
    for wordItem in WordList:
        tmpList1 = re.findall('[A-Z]*[a-z]+', wordItem)                 # �빮�ڷ� �����ϴ� �ռ��� (e.g. Ŭ���� ��)        
        if tmpList1:
            newWordList += tmpList1
        else:
            newWordList.append(wordItem)
        
    return newWordList  

# ��ó��
def runNLP():
    
    print " Natural Lanuguage Processing..."
    
    for subject in SUBJECT_LIST:
    
        for path, dir, files in os.walk(DOC_PATH + subject):
            NLP_PATH    = TM_PATH + 'NLP/' + path[path.rindex('/')+1:] + '/'
            
            if not os.path.exists(NLP_PATH):
                os.makedirs(NLP_PATH)
            
            selectedFile = random.sample(files, 500)
            
            for filename in selectedFile:
                        
                # ���� �о����                                                
                src_contents        = open(path + '/' + filename , 'r').read()                  # �ҽ����� �б�
                                
                # �ڿ��� ó��            
                src_letters_only    = re.sub('[^a-zA-Z]', ' ', src_contents)                    # ���ڸ� �����
                src_tokenized       = word_tokenize(src_letters_only)                           # ��ū �����
                src_tokenized2      = splitWords(src_tokenized)                                 # �ռ��� �и�
                src_rm_duplicate    = list(set(src_tokenized2))                                 # �ߺ� ����
                src_low_words       = [w.lower() for w in src_rm_duplicate]                     # �ҹ��ڷ� �����            
                
                outFile = open(NLP_PATH + filename, 'w')                               
                outFile.write(" ".join(src_low_words))
                outFile.close()

# ���� �𵨸��� ���� corpus �����
def makeBoW():
    
    os.chdir(TOOL_PATH)  
    print os.getcwd()
    
    print 'Basket of Words �����'
    cmd_result = os.system('mallet import-dir --input ../../TM/NLP/ --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/TopClass_extra.txt --output ../../TM/corpus.mallet')                 
    if not cmd_result == 0:
        print '���� �߻�\n'
        
    os.chdir('../..')  
        
# Topic Modeling ������
def runTM(TOPIC_NUMBER, INTERVAL, BURNIN, ITERATIONS):
    
    os.chdir(TOOL_PATH)   
    
    for topicK in TOPIC_NUMBER:
        
        # 1. Train File �𵨸�
        cmd_result = os.system('mallet train-topics --input ../../TM/corpus.mallet --num-topics ' + str(topicK) +
                                 ' --optimize-interval ' + str(INTERVAL) + ' --num-iterations ' + str(ITERATIONS) +
                                 ' --num-top-words 20 --output-topic-keys ../../TM/AssociatedWords(' + str(topicK) + ').csv' + 
                                 ' --output-doc-topics ../../TM/TopicContribution(' + str(topicK) + ').csv' +
                                 ' --inferencer-filename ../../TM/Inferencer(' +  str(topicK) + ') --num-threads 32 --random-seed 0')
          
        if not cmd_result == 0:
            print '���� �߻�\n'
            exit()
         
        else:

            # ���� ��ó�� �۾� ����
            os.rename('../../TM/AssociatedWords(' + str(topicK) + ').csv', '../../TM/AssociatedWords(' + str(topicK) + ')2.csv')
            INPUT_FILE = open('../../TM/AssociatedWords(' + str(topicK) + ')2.csv', 'r')
            OUT_FILE = open('../../TM/AssociatedWords(' + str(topicK) + ').csv', 'a')
             
            for topicWords in INPUT_FILE:
                OUT_FILE.write(topicWords.replace('\t', ',').replace(' ', ','))         # \t, �����̽��� �޸�(,)�� �ٲٱ�
            OUT_FILE.flush()
             
            INPUT_FILE.close()
            OUT_FILE.close()
            
            os.remove('../../TM/AssociatedWords(' + str(topicK) + ')2.csv')
             
            os.rename('../../TM/TopicContribution(' + str(topicK) + ').csv', '../../TM/TopicContribution(' + str(topicK) + ')2.csv')
            INPUT_FILE = open('../../TM/TopicContribution(' + str(topicK) + ')2.csv', 'r')
            OUT_FILE = open('../../TM/TopicContribution(' + str(topicK) + ').csv', 'a')
                 
            for topicWords in INPUT_FILE:
                OUT_FILE.write(topicWords.replace('\t', ',').replace('%5B', '[').replace('%5D', ']'))       # \t, Ư������ [, ]�� ���� []�� �ٲٱ� 
            OUT_FILE.flush()
             
            INPUT_FILE.close()
            OUT_FILE.close()
            
            os.remove('../../TM/TopicContribution(' + str(topicK) + ')2.csv')
            
    os.chdir('../..')
            
def findFirstSameWord(TOPIC_NUMBER):
    
    STOPWORD_FILE = open('./mallet/stoplists/TopClass_extra.txt', 'a')
    
    firstWordList = list()    
    for topicK in TOPIC_NUMBER:
    
        for line in open('./TM/AssociatedWords(' + str(topicK) + ').csv'):            
            firstWordList.append(line.split(',')[2])
        
        dups = defaultdict(list)
        for i, e in enumerate(firstWordList):
            dups[e].append(i)
        for k, v in sorted(dups.iteritems()):
            if len(v) >= 2:
                print k + ' is added to stopwords'
                STOPWORD_FILE.write(k + '\n')      
                
def findDomainSpecificWords(TOPIC_NUMBER):
    
    STOPWORD_FILE = open('./mallet/stoplists/TopClass_extra.txt', 'a')
    
    for topicK in TOPIC_NUMBER:
    
        row, col = len(SUBJECT_LIST), topicK
        topicCntMatrix = [[0 for x in range(col)] for y in range(row)]

        # �࿡ subject, ���� topic#���� �����ϰ� ���� �� ���� ���� �ܾ��� �󵵸� ���        
        for line in open('./TM/TopicContribution(' + str(topicK) + ').csv'):        
            
            if line.startswith('#'):        continue                        # ù �� ������
                        
            tokenizedLine = line.split(',')
            filePath = tokenizedLine[1]
            subjectName = filePath[filePath.find('NLP')+4:filePath.rfind('/')]
            topicNum = int(tokenizedLine[2])
            
            topicCntMatrix[SUBJECT_LIST.index(subjectName)][topicNum] += 1
            
        # �� ���ȿ��� ��� subject�� �󵵼��� �� �� ���ϱ�
        sumOfTopicList = [0 for x in range(col)]
        for mCol in range(0,col):
            for mRow in range(0,row):
                sumOfTopicList[mCol] += topicCntMatrix[mRow][mCol]            
           
        sumOfTopicList = [x/2 for x in sumOfTopicList]                      # ���Ⱥ� ���տ��� 2�� ������
        
        # ���Ⱥ��� subject�� ��ȸ�ϸ鼭 ���� ����/2���� ū subject ã�Ƴ���
        existResult = False   
        for mCol in range(0,col):
            for mRow in range(0,row):
                if topicCntMatrix[mRow][mCol] > sumOfTopicList[mCol]:
                    
                    existResult = True
                    
                    firstWordofTopic = ''
                    for line in open('./TM/AssociatedWords(' + str(topicK) + ').csv'):
                        if line.startswith('#'):    continue
                        
                        if int(line.split(',')[0]) == mCol:                            
                            firstWordofTopic = line.split(',')[2]
                            break
                                     
                    print firstWordofTopic + " is added to stopwords."
                    STOPWORD_FILE.write(firstWordofTopic + '\n')

        return existResult
    
############################################################################################

DOC_PATH    = './documents/'
TM_PATH     = './TM/'
TOOL_PATH   = './mallet/bin/'
SUBJECT_LIST = ['Actor','Alluxio','Bazel','Buck','Cassandra','ClosureCompiler','CoreNLP',
                'Deeplearning4j','Druid','GoPlugin4IntelliJ','Gradle','Graylog','Hadoop',
                'IntelliJIDEA','Kotlin','Netty','openHAB','OrientDB','PDE','SpringFramework',
                'ApacheStorm','Atmosphere','FastJSON','JNA','Kafka','Nokogiri','Pinpoint',
                'Titan','Vertx','Zeppelin']

if not os.path.exists(TM_PATH):
    os.makedirs(TM_PATH)

TOPIC_NUMBER    = [30]

# runNLP() 
# makeBoW()
# runTM(TOPIC_NUMBER, 20, 50, 1000)

stopFlag = True
while stopFlag:
    makeBoW()
    runTM(TOPIC_NUMBER, 20, 50, 1000)
    findFirstSameWord(TOPIC_NUMBER)
    stopFlag = findDomainSpecificWords(TOPIC_NUMBER)
