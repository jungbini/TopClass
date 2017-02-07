# -*- encoding:utf-8-*-
import re, string, os
from dateutil import parser

LOG_PATH         = 'd:/Tools/TOPClass/LogHistory/'
BASE_PATH       = 'd:/Tools/TopClass/FilesOfRevision/'
DOC_PATH         = 'd:/Tools/TopClass/LogMessages/'

PROGRAM_LIST_GIT    = ['Actor','Aeron','aerosolve','Alluxio','Anthelion','ApacheStorm','AsyncHttpClient','Atmosphere','Auto','Bazel','Buck','Cassandra','Che','Clojure','ClosureCompiler','Config','CoreNLP','Dagger','Deeplearning4j','dex2jar','Disruptor','Dropwizard','Druid','Dubbo','Eureka','FastJSON','FizzBuzz','GoCD','GoPlugin4IntelliJ','Gradle','GradleRetrolambda','Graylog','gRPC','Hackpad','Hadoop','Heron','HikariCP','Hugo','Hystrix','IdeaVim','IntelliJIDEA','J2ObjC','JADX','JavaDesignPatterns','JavaPoet','Jedis','Jersey','JNA','JodaTime','jsonschema2pojo','jsoup','JStorm','JUnit4','Kafka','Kotlin','Leakcanary','2017-02-01  오후 05:25                 0 list.txt','Lombok','Lucida','MapDB','Metrics','Mockito','Motan','MyBatis3','NanoHTTPD','Netty','Nokogiri','OkHttp','Okio','openHAB','OpenRefine','OrientDB','PDE','PhysicalWeb','Pinpoint','Presto','PySonar2','Realm','Rebound','Retrofit','Retrolambda','RippleEffect','RxJava','ScribeJava','SimianArmy','Smile','Spark','SpringBoot','SpringFramework','SpringSecurity','SQLBrite','Storm','SwaggerCore','Titan','Vertx','WebMagic','YUICompressor','Zeppelin','Zipkin','ZooKeeper','Zxing']
    
def extractGitLog():
        
    re_commitStart  = re.compile('(commit)\s(.*)(\n)')                       # Commit number 패턴
    re_revStart     = re.compile('(Date:\s+)(.*)(\n)')                      # revision이 시작하는 패턴
    re_fileStart    = re.compile('(diff --git)\s(.*)\s(.*)\n')              # revision 대상 파일 패턴
    re_revnumStart  = re.compile('(index\s)(.*)(\.\.)(.*)\s([0-9]+)')       # 해당 파일의 리비전 번호 패턴
        
    for program in PROGRAM_LIST_GIT:
        
        if not os.path.exists(BASE_PATH + program):
            os.makedirs(BASE_PATH + program)
        if not os.path.exists(DOC_PATH + program):
            os.makedirs(DOC_PATH + program)
        
        fileName            = ''                                            # 파일명
        buggyRevisionNum    = ''                                            # buggy revision 번호
        cleanRevisionNum    = ''                                            # clean revision 번호
        commitNum           = ''                                            # Commit number
        commitMsg           = ''                                            # Commit Message    
        commitDate          = ''                                            # commit이 수행된 날짜  
        isCommitMsg         = False                                         # Commit Message이냐?      
        for line in open(LOG_PATH + 'BUGFIX_LOG_' + program + '.txt', 'r'):  
            
            line = filter(lambda x: x in string.printable, line)
            
            if line == '\r\n':      continue
            
            if isCommitMsg:
                commitMsg += ' ' + line.strip()                             # Commit Message 누적
            
            match_commitStart   = re_commitStart.match(line)
            if match_commitStart:
                
                # 새로운 commit이 시작하므로 그전까지의 파일리스트는 저장
                if fileName != '' and '.java' in fileName:                  # 다른 리비전의 시작이므로 그전 file은 기록하기
                    print program + ':' + fileName
                    
                    OUT_FILE = open(BASE_PATH + program + '/[' + commitDate + ']' + commitNum + '.txt', 'a')                                                                     
                    OUT_FILE.write(fileName + ',' + buggyRevisionNum + ',' + cleanRevisionNum + '\n')
                    
                    OUT_FILE.flush()
                    
                    fileName = ''
                
                commitNum = match_commitStart.group(2)
                commitNum = commitNum[:7]
                isCommitMsg = False
                
            match_revStart       = re_revStart.match(line)                      # Revision의 시작 부분            
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
                
                # 일단 날짜와 기록된 Commit log를 쓰고 시작
                if isCommitMsg:
                    
                    if 'commit' in commitMsg:
                        commitMsg = commitMsg[commitMsg.index('commit')+48:commitMsg.index('diff')]
                    elif 'diff' in commitMsg:
                        commitMsg = commitMsg[:commitMsg.index('diff')]
                                        
                    LOGDocFile = open(DOC_PATH + program + '/[' + commitDate + ']' + commitNum + '.txt', 'a')           # topic modeling을 위해 로그 메시지 따로 보관
                    LOGDocFile.write(commitMsg)
                    LOGDocFile.flush()
                    
                    commitMsg = ''
                    isCommitMsg = False                
                                       
                # fileName이 빈칸이 아니면 또 다른 revision이 새로 시작하므로 기존 revision 기록하기
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
            
        # 마지막 revision 정보까지 기록하고 끝내기        
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
#         fileName            = ''                                            # 파일명
#         buggyRevisionNum    = ''                                            # buggy revision 번호
#         cleanRevisionNum    = ''                                            # clean revision 번호
#         commitNum           = ''                                            # Commit Number
#         commitMsg           = ''                                            # Commit Message    
#         commitDate          = ''                                            # commit이 수행된 날짜  
#         isCommitMsg         = False                                         # Commit Message이냐?      
#         for line in open(PROGRAM_PATH + 'BUGFIX_LOG.txt', 'r'):  
#             
#             line = filter(lambda x: x in string.printable, line)
#             
#             if line == '\r\n':      continue
#             
#             if isCommitMsg:         commitMsg += ' ' + line.strip()             # Commit Message 누적
#             
#             match_revStart       = re_revStart.match(line)                      # Revision의 시작 부분            
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
#                 # fileName이 빈칸이 아니면 또 다른 revision이 새로 시작하므로 기존 revision 기록하기
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
#                 # 일단 날짜와 기록된 Commit log를 쓰고 시작
#                 if isCommitMsg:                    
#                     commitMsg = commitMsg[:commitMsg.index('Index:')]
#                     
#                     LOGDocFile = open(DOC_PATH + program + '/[' + commitDate + ']' + commitNum + '.txt', 'a')                                # topic modeling을 위해 로그 메시지 따로 보관
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
#         # 마지막 revision 정보까지 기록하고 끝내기        
#         if commitMsg and commitDate and buggyRevisionNum != '0' and not '(deleted)' in fileName:
#             
#             commitMsg = commitMsg[:commitMsg.index('Index:')]
#             LOGDocFile = open(DOC_PATH + program + '/[' + commitDate + ']' + commitNum + '.txt', 'a')                                # topic modeling을 위해 로그 메시지 따로 보관
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