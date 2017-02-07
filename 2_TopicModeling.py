# -*- encoding:utf-8-*-
import os, re, random
from nltk import word_tokenize
    
# 토픽 모델링 전 소스파일 전처리
def runNLP():
    
    print " Natural Lanuguage Processing..."
    
    for subject in SUBJECT_LIST:
    
        for path, dir, files in os.walk(DOC_PATH + subject):
            
#             files = sorted(files)            
#             TrainFileList = files[:len(files)/2]
#             TestFileList = files[(len(files)/2)+1:]
            
#             TRAIN_NLP_PATH      = TM_PATH + 'TrainNLP/' + path[path.rindex('/')+1:] + '/'
#             TEST_NLP_PATH       = TM_PATH + 'TestNLP/' + path[path.rindex('/')+1:] + '/'
            NLP_PATH    = TM_PATH + 'NLP/' + path[path.rindex('/')+1:] + '/'
            
#             if not os.path.exists(TRAIN_NLP_PATH):
#                 os.makedirs(TRAIN_NLP_PATH)
#             if not os.path.exists(TEST_NLP_PATH):
#                 os.makedirs(TEST_NLP_PATH)
            if not os.path.exists(NLP_PATH):
                os.makedirs(NLP_PATH)
            
            selectedFile = random.sample(files, 500)
            
            for filename in selectedFile:
                        
                # 파일 읽어오기
                srcfile             = path + '/' + filename                                     # 소스파일 경로                                
                src_contents        = open(srcfile, 'r').read()                                 # 소스파일 읽기
                                
                # 자연어 처리            
                src_letters_only    = re.sub('[^a-zA-Z]', ' ', src_contents)                    # 문자만 남기기
                src_tokenized       = word_tokenize(src_letters_only)                           # 토큰 만들기
                src_tokenized2      = splitWords(src_tokenized)                                 # 합성어 분리
                src_rm_duplicate    = list(set(src_tokenized2))                                 # 중복 제거
                src_low_words       = [w.lower() for w in src_rm_duplicate]                     # 소문자로 만들기            
                                 
                # 파일 쓰기
#                 if filename in TrainFileList:                                                   # Train에 속하는 파일이면                                                             
#                     outFile = open(TRAIN_NLP_PATH + filename, 'w')                          
#                     outFile.write(" ".join(src_low_words))
#                     outFile.close()
#                 elif filename in TestFileList:                                                  # Test에 속하는 파일이면
#                     outFile = open(TEST_NLP_PATH + filename, 'w')                               
#                     outFile.write(" ".join(src_low_words))
#                     outFile.close()
                outFile = open(NLP_PATH + filename, 'w')                               
                outFile.write(" ".join(src_low_words))
                outFile.close()
                
# Util 함수: 대문자로 시작하는 합성어 분리
def splitWords(WordList):
    
    newWordList = []
    for wordItem in WordList:
        tmpList1 = re.findall('[A-Z]*[a-z]+', wordItem)                 # 대문자로 시작하는 합성어 (e.g. 클래스 명)        
        if tmpList1:
            newWordList += tmpList1
        else:
            newWordList.append(wordItem)
        
    return newWordList    

# 토픽 모델링을 위한 corpus 만들기
def makeBoW():
        
#     os.chdir(TOOL_PATH)
#             
#     # 1. bag of words 파일 만들기    
#     print 'Train Input 만들기'
#     cmd_result = os.system('mallet import-dir --input ' + TM_PATH + 'TrainNLP/' + ' --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/TopClass_extra.txt --output ' + TM_PATH + 'Train.mallet')                 
#     if not cmd_result == 0:
#         print '에러 발생\n'
#         
#     os.chdir(TOOL_PATH)
#     
#     print 'Test Input 만들기'
#     cmd_result = os.system('mallet import-dir --input ' + TM_PATH + 'TestNLP/' + ' --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/TopClass_extra --use-pipe-from ' + TM_PATH + 'Train.mallet' + ' --output ' + TM_PATH + 'Test.mallet')                 
#     if not cmd_result == 0:
#         print '에러 발생\n'
    os.chdir(TOOL_PATH)
     
    print 'Test Input 만들기'
    cmd_result = os.system('mallet import-dir --input ' + TM_PATH + 'NLP/' + ' --keep-sequence --remove-stopwords --extra-stopwords ../stoplists/TopClass_extra.txt --output ' + TM_PATH + 'corpus.mallet')                 
    if not cmd_result == 0:
        print '에러 발생\n'
  
        
# Topic Modeling 돌리기
def runTM(TOPIC_NUMBER, INTERVAL, BURNIN, ITERATIONS):
    
    os.chdir(TOOL_PATH)   
    
    for topicK in TOPIC_NUMBER:
        
        # 1. Train File 모델링
        cmd_result = os.system('mallet train-topics --input ' + TM_PATH + 'corpus.mallet --num-topics ' + str(topicK) +
                                 ' --optimize-interval ' + str(INTERVAL) + ' --num-iterations ' + str(ITERATIONS) +
                                 ' --num-top-words 20 --output-topic-keys ' + TM_PATH + 'AssociatedWords(' + str(topicK) + ').csv' + 
                                 ' --output-doc-topics ' + TM_PATH + 'TopicContribution(' + str(topicK) + ').csv' +
                                 ' --inferencer-filename ' + TM_PATH + 'Inferencer(' +  str(topicK) + ') --num-threads 16 --random-seed 0')
         
        if not cmd_result == 0:
            print '에러 발생\n'
            exit()
        
        else:

            # 파일 전처리 작업 시작
            os.rename(TM_PATH + 'AssociatedWords(' + str(topicK) + ').csv', TM_PATH + 'AssociatedWords(' + str(topicK) + ')2.csv')
            INPUT_FILE = open(TM_PATH + 'AssociatedWords(' + str(topicK) + ')2.csv', 'r')
            OUT_FILE = open(TM_PATH + 'AssociatedWords(' + str(topicK) + ').csv', 'a')
             
            for topicWords in INPUT_FILE:
                OUT_FILE.write(topicWords.replace('\t', ',').replace(' ', ','))         # \t, 스페이스를 콤마(,)로 바꾸기
            OUT_FILE.flush()
             
            INPUT_FILE.close()
            OUT_FILE.close()
            
            os.remove(TM_PATH + 'AssociatedWords(' + str(topicK) + ')2.csv')
             
            os.rename(TM_PATH + 'TopicContribution(' + str(topicK) + ').csv', TM_PATH + 'TopicContribution(' + str(topicK) + ')2.csv')
            INPUT_FILE = open(TM_PATH + 'TopicContribution(' + str(topicK) + ')2.csv', 'r')
            OUT_FILE = open(TM_PATH + 'TopicContribution(' + str(topicK) + ').csv', 'a')
                 
            for topicWords in INPUT_FILE:
                OUT_FILE.write(topicWords.replace('\t', ',').replace('%5B', '[').replace('%5D', ']'))       # \t, 특수문자 [, ]를 원래 []로 바꾸기 
            OUT_FILE.flush()
             
            INPUT_FILE.close()
            OUT_FILE.close()
            
            os.remove(TM_PATH + 'TopicContribution(' + str(topicK) + ')2.csv')
        
#         os.chdir(TOOL_PATH)   
        
#         # 2. Test File 추론
#         cmd_result = os.system('mallet infer-topics --inferencer ' + TM_PATH + 'Inferencer(' +  str(topicK) + ')' + 
#                                ' --input ' + TM_PATH + 'Test.mallet --output-doc-topics ' + TM_PATH + 'TopicContribution_Test(' + str(topicK) + ').csv')
#         if not cmd_result == 0:
#             print '에러 발생\n'
#             exit()
#         else:
#             # 파일 전처리 작업 시작
#             os.rename(TM_PATH + 'TopicContribution_Test(' + str(topicK) + ').csv', TM_PATH + 'TopicContribution_Test(' + str(topicK) + ')2.csv')
#             INPUT_FILE = open(TM_PATH + 'TopicContribution_Test(' + str(topicK) + ')2.csv', 'r')
#             OUT_FILE = open(TM_PATH + 'TopicContribution_Test(' + str(topicK) + ').csv', 'a')
#                  
#             for topicWords in INPUT_FILE:
#                 OUT_FILE.write(topicWords.replace('\t', ',').replace('%5B', '[').replace('%5D', ']'))
#             OUT_FILE.flush()
#              
#             INPUT_FILE.close()
#             OUT_FILE.close()
#             
#             os.remove(TM_PATH + 'TopicContribution_Test(' + str(topicK) + ')2.csv')            


##############################################

DOC_PATH    = 'd:/Tools/TopClass/LogMessages/'
TM_PATH     = 'd:/Tools/TopClass/TM/'
TOOL_PATH   = 'D:/Tools/mallet/bin/'
SUBJECT_LIST = ['Actor','Alluxio','Bazel','Buck','Cassandra','ClosureCompiler','CoreNLP',
                'Deeplearning4j','Druid','GoPlugin4IntelliJ','Gradle','Graylog','Hadoop',
                'IntelliJIDEA','Kotlin','Netty','openHAB','OrientDB','PDE','SpringFramework',
                'ApacheStorm','Atmosphere','FastJSON','JNA','Kafka','Nokogiri','Pinpoint',
                'Titan','Vertx','Zeppelin']

if not os.path.exists(TM_PATH):
    os.makedirs(TM_PATH)

TOPIC_NUMBER    = [10, 20, 30, 50, 100, 200, 300, 500, 1000, 2000, 3000]

runNLP() 
makeBoW()
runTM(TOPIC_NUMBER, 20, 50, 1000)