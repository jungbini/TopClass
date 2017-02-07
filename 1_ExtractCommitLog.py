# -*- encoding:utf-8-*-
import re, string, os
from dateutil import parser

LOG_PATH         = 'd:/Tools/TOPClass/LogHistory/'
BASE_PATH       = 'd:/Tools/TopClass/FilesOfRevision/'
DOC_PATH         = 'd:/Tools/TopClass/LogMessages/'

PROGRAM_LIST_GIT    = ['Actor','Aeron','aerosolve','Alluxio','Anthelion','ApacheStorm','AsyncHttpClient','Atmosphere','Auto','Bazel','Buck','Cassandra','Che','Clojure','ClosureCompiler','Config','CoreNLP','Dagger','Deeplearning4j','dex2jar','Disruptor','Dropwizard','Druid','Dubbo','Eureka','FastJSON','FizzBuzz','GoCD','GoPlugin4IntelliJ','Gradle','GradleRetrolambda','Graylog','gRPC','Hackpad','Hadoop','Heron','HikariCP','Hugo','Hystrix','IdeaVim','IntelliJIDEA','J2ObjC','JADX','JavaDesignPatterns','JavaPoet','Jedis','Jersey','JNA','JodaTime','jsonschema2pojo','jsoup','JStorm','JUnit4','Kafka','Kotlin','Leakcanary','2017-02-01  ���� 05:25                 0 list.txt','Lombok','Lucida','MapDB','Metrics','Mockito','Motan','MyBatis3','NanoHTTPD','Netty','Nokogiri','OkHttp','Okio','openHAB','OpenRefine','OrientDB','PDE','PhysicalWeb','Pinpoint','Presto','PySonar2','Realm','Rebound','Retrofit','Retrolambda','RippleEffect','RxJava','ScribeJava','SimianArmy','Smile','Spark','SpringBoot','SpringFramework','SpringSecurity','SQLBrite','Storm','SwaggerCore','Titan','Vertx','WebMagic','YUICompressor','Zeppelin','Zipkin','ZooKeeper','Zxing']
    
def extractGitLog():
        
    re_commitStart  = re.compile('(commit)\s(.*)(\n)')                       # Commit number ����
    re_revStart     = re.compile('(Date:\s+)(.*)(\n)')                      # revision�� �����ϴ� ����
    re_fileStart    = re.compile('(diff --git)\s(.*)\s(.*)\n')              # revision ��� ���� ����
    re_revnumStart  = re.compile('(index\s)(.*)(\.\.)(.*)\s([0-9]+)')       # �ش� ������ ������ ��ȣ ����
        
    for program in PROGRAM_LIST_GIT:
        
        if not os.path.exists(BASE_PATH + program):
            os.makedirs(BASE_PATH + program)
        if not os.path.exists(DOC_PATH + program):
            os.makedirs(DOC_PATH + program)
        
        fileName            = ''                                            # ���ϸ�
        buggyRevisionNum    = ''                                            # buggy revision ��ȣ
        cleanRevisionNum    = ''                                            # clean revision ��ȣ
        commitNum           = ''                                            # Commit number
        commitMsg           = ''                                            # Commit Message    
        commitDate          = ''                                            # commit�� ����� ��¥  
        isCommitMsg         = False                                         # Commit Message�̳�?      
        for line in open(LOG_PATH + 'BUGFIX_LOG_' + program + '.txt', 'r'):  
            
            line = filter(lambda x: x in string.printable, line)
            
            if line == '\r\n':      continue
            
            if isCommitMsg:
                commitMsg += ' ' + line.strip()                             # Commit Message ����
            
            match_commitStart   = re_commitStart.match(line)
            if match_commitStart:
                
                # ���ο� commit�� �����ϹǷ� ���������� ���ϸ���Ʈ�� ����
                if fileName != '' and '.java' in fileName:                  # �ٸ� �������� �����̹Ƿ� ���� file�� ����ϱ�
                    print program + ':' + fileName
                    
                    OUT_FILE = open(BASE_PATH + program + '/[' + commitDate + ']' + commitNum + '.txt', 'a')                                                                     
                    OUT_FILE.write(fileName + ',' + buggyRevisionNum + ',' + cleanRevisionNum + '\n')
                    
                    OUT_FILE.flush()
                    
                    fileName = ''
                
                commitNum = match_commitStart.group(2)
                commitNum = commitNum[:7]
                isCommitMsg = False
                
            match_revStart       = re_revStart.match(line)                      # Revision�� ���� �κ�            
            if match_revStart:
                
                commitDate = match_revStart.group(2)
                dateObj = parser.parse(' '.join(commitDate.split(' ')[:-1])) 
                commitDate = dateObj.date().isoformat()
                
                isCommitMsg = True
                continue
            
            match_fileStart      = re_fileStart.match(line)
            if match_fileStart:
                
                if '0b96a8d' in commitNum:
                    print commitMsg
                
                # �ϴ� ��¥�� ��ϵ� Commit log�� ���� ����
                if isCommitMsg:
                    
                    if 'commit' in commitMsg:
                        commitMsg = commitMsg[commitMsg.index('commit')+48:commitMsg.index('diff')]
                    elif 'diff' in commitMsg:
                        commitMsg = commitMsg[:commitMsg.index('diff')]
                                        
                    LOGDocFile = open(DOC_PATH + program + '/[' + commitDate + ']' + commitNum + '.txt', 'a')           # topic modeling�� ���� �α� �޽��� ���� ����
                    LOGDocFile.write(commitMsg)
                    LOGDocFile.flush()
                    
                    commitMsg = ''
                    isCommitMsg = False                
                                       
                # fileName�� ��ĭ�� �ƴϸ� �� �ٸ� revision�� ���� �����ϹǷ� ���� revision ����ϱ�
                if fileName != '' and '.java' in fileName:             
                    print program + ':' + fileName                                                 
                    
                    OUT_FILE = open(BASE_PATH + program + '/[' + commitDate + ']' + commitNum + '.txt', 'a')                                                                     
                    OUT_FILE.write(fileName + ',' + buggyRevisionNum + ',' + cleanRevisionNum + '\n')
                    
                    OUT_FILE.flush()
                
                fileName = match_fileStart.group(2).strip()
                fileName = fileName[fileName.rfind('/')+1:]
                                    
                continue
            
            match_revnumStart   = re_revnumStart.match(line)
            if match_revnumStart:
                if '.java' in fileName:            
                    buggyRevisionNum = match_revnumStart.group(2)
                    cleanRevisionNum = match_revnumStart.group(4)
                continue
            
        # ������ revision �������� ����ϰ� ������        
        if fileName != '' and '.java' in fileName:                                              
            OUT_FILE = open(BASE_PATH + program + '/[' + commitDate + ']' + commitNum + '.txt', 'a')                                                                     
            OUT_FILE.write(fileName + ',' + buggyRevisionNum + ',' + cleanRevisionNum + '\n')
            OUT_FILE.close ()                
            
# def extractSVNLog():
#     
#     re_revStart     = re.compile('(r[0-9]+\s)\|(\s(.*)\s)\|\s([0-9]+-[0-9]+-[0-9]+)(.*)(\n)')
#     re_fileStart    = re.compile('Index: (.*)\n')
#     re_buggyRevnumStart = re.compile('--- (.*)\t\((.*) ([0-9]+)\)')
#     re_cleanRevnumStart = re.compile('[\+]+ (.*)\t\((.*) ([0-9]+)\)')
#     
#     for program in PROJECT_LIST_SVN:
#         
#         if not os.path.exists(BASE_PATH + program):
#             os.makedirs(BASE_PATH + program)
#         if not os.path.exists(DOC_PATH + program):
#             os.makedirs(DOC_PATH + program)
#         
#         PROGRAM_PATH = DB_PATH + program + '/COMMIT_LOG/'
#         
#         fileName            = ''                                            # ���ϸ�
#         buggyRevisionNum    = ''                                            # buggy revision ��ȣ
#         cleanRevisionNum    = ''                                            # clean revision ��ȣ
#         commitNum           = ''                                            # Commit Number
#         commitMsg           = ''                                            # Commit Message    
#         commitDate          = ''                                            # commit�� ����� ��¥  
#         isCommitMsg         = False                                         # Commit Message�̳�?      
#         for line in open(PROGRAM_PATH + 'BUGFIX_LOG.txt', 'r'):  
#             
#             line = filter(lambda x: x in string.printable, line)
#             
#             if line == '\r\n':      continue
#             
#             if isCommitMsg:         commitMsg += ' ' + line.strip()             # Commit Message ����
#             
#             match_revStart       = re_revStart.match(line)                      # Revision�� ���� �κ�            
#             if match_revStart:
#                 commitNum = match_revStart.group(1)       
#                 commitNum = commitNum[1:].strip()        
#                 commitDate = match_revStart.group(4)
#                 
#                 isCommitMsg = True
#                 continue
#             
#             match_fileStart      = re_fileStart.match(line)
#             if match_fileStart:
#                                        
#                 # fileName�� ��ĭ�� �ƴϸ� �� �ٸ� revision�� ���� �����ϹǷ� ���� revision ����ϱ�
#                 if fileName != '' and '.java' in fileName:
#                     if (buggyRevisionNum != '0'):
#                         if not '(deleted)' in fileName:
#                             fileName = fileName[fileName.rindex('/')+1:]                                         
#                             print program + ':' + fileName                   
#                             
#                             OUT_FILE = open(BASE_PATH + program + '/[' + commitDate + ']' + commitNum + '.txt', 'a')                                                                     
#                             OUT_FILE.write(fileName + ',' + buggyRevisionNum + ',' + cleanRevisionNum + '\n')
#                                                 
#                             fileName    = ''
#                             OUT_FILE.flush()
#                 
#                 fileName = match_fileStart.group(1).strip()
#                     
#                 # �ϴ� ��¥�� ��ϵ� Commit log�� ���� ����
#                 if isCommitMsg:                    
#                     commitMsg = commitMsg[:commitMsg.index('Index:')]
#                     
#                     LOGDocFile = open(DOC_PATH + program + '/[' + commitDate + ']' + commitNum + '.txt', 'a')                                # topic modeling�� ���� �α� �޽��� ���� ����
#                     LOGDocFile.write(commitMsg)
#                     LOGDocFile.flush()
#                     
#                     commitMsg = ''
#                     isCommitMsg = False 
#                                     
#                 continue
#             
#             match_buggyRevnumStart = re_buggyRevnumStart.match(line)
#             if match_buggyRevnumStart:
#                 if '.java' in fileName:            
#                     buggyRevisionNum = match_buggyRevnumStart.group(3)
#                 continue
#         
#             match_cleanRevnumStart = re_cleanRevnumStart.match(line)
#             if match_cleanRevnumStart:
#                 if '.java' in fileName:
#                     cleanRevisionNum = match_cleanRevnumStart.group(3)
#                 continue
#         
#         # ������ revision �������� ����ϰ� ������        
#         if commitMsg and commitDate and buggyRevisionNum != '0' and not '(deleted)' in fileName:
#             
#             commitMsg = commitMsg[:commitMsg.index('Index:')]
#             LOGDocFile = open(DOC_PATH + program + '/[' + commitDate + ']' + commitNum + '.txt', 'a')                                # topic modeling�� ���� �α� �޽��� ���� ����
#             LOGDocFile.write(commitMsg)
#             LOGDocFile.close()
#             
#             if fileName != '' and '.java' in fileName and buggyRevisionNum != '0' and not '(deleted)' in fileName:                                              
#                 OUT_FILE = open(BASE_PATH + program + '/[' + commitDate + ']' + commitNum + '.txt', 'a')                                                                     
#                 OUT_FILE.write(fileName + ',' + buggyRevisionNum + ',' + cleanRevisionNum + '\n')
#                 OUT_FILE.close()
#         
extractGitLog()
#extractSVNLog()