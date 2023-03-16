from os import path
import subprocess
import random

def javaRunnable():
    try:
        process = subprocess.Popen(["java.exe","-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True, "java.exe 실행 가능"
    except:
        return False, "java.exe를 실행할 수 없습니다. JDK 설치와 환경변수 설정이 잘 되었는지 확인해 보세요."    

def fileExist(filename):
    if path.exists(filename) and path.isfile(filename): return True, f"{filename} 파일 존재"
    else: return False, f"{filename} 파일이 존재하지 않습니다."

def runSingleJavaFile(filename, input, *output):
    '''
    Run a single .java file with input string and
        compare the output with the list of items in *output

    If the output is correct, return (True, ""); otherwise, return (Flase, output)
    '''
    process = subprocess.Popen(["java.exe",filename], 
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,            
            universal_newlines=True) # All data communicated with the pipe should be in utf-8 format, rather than the byte format
    process.stdin.write(input)    
    process.stdin.close()

    id = 0
    numPassed = 0
    results = [f"{filename}", "\n입력: " + input, "\n기대 출력:", *output, "\n실제 출력:"]
    for e in process.stdout:
        e = e.strip()
        results.append(e)
        if e == output[id]:
            numPassed += 1        
        id += 1
        if id >= len(output): break        

    if numPassed == len(output): return True, f"{filename}"
    else: return False, " ".join(results)    

def test(function, *args):
    '''
    Run an arbitrary function with arguments *args
    If the function returns True, print pass; otherwise, print the error message
    '''
    passed, msg = function(*args)
    if passed: 
        print(f"pass {msg}")
        return True
    else: 
        print(f"** FAIL ** {msg}")
        return False

if __name__ == "__main__":
    if test(javaRunnable):
        if test(fileExist, "P1.java"):            
            for _ in range(10):
                n = random.randint(-100,100)
                expectedResult = n**2 - 3*n + 7                
                test(runSingleJavaFile, "P1.java", str(n), str(expectedResult))
        
        if test(fileExist, "P2.java"):
            words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
            for i in range(len(words)):
                test(runSingleJavaFile, "P2.java", str(i), words[i])   

        if test(fileExist, "P3.java"):            
            for _ in range(10):
                n = random.randint(1,10)
                inputString, outputList = str(n), []
                for _ in range(n):
                    e = random.randint(-100,100)
                    inputString += " " + str(e)
                    if e>=10: outputList.append("0")
                    else: outputList.append(str(e))                            
                test(runSingleJavaFile, "P3.java", inputString, *outputList)

    print("Test finished. Press enter to close the window.")
    input()        

    