from django.shortcuts import render
import sys
# Create your views here.

def home(request):
    return render(request,'pycom/index.html')

def runcode(request):
    if request.method=="POST":
        codeareadata = request.POST['codearea']
        input_part = request.POST['inputarea']
        y= input_part
        input_part = input_part.replace("\n"," ").split(" ")

        def input(): #input overriding
            a = input_part[0]
            del input_part[0]
            return a
        # here we will use the concept of stdout
        try:     # So first  we will create file => then execute our code and save output in that file => finally save
                #save original standard output reference
            original_stdout = sys.stdout
            sys.stdout = open('file.txt','w')  #change  the standard output to the file we created
            #execute code
            exec(codeareadata)  # example => print("Hello World")
            sys.stdout.close()
            sys.stdout = original_stdout   # reset the standardoutput to its original value
            #finally read output from file and save in output variable

            output = open('file.txt','r').read()

        except Exception as e:
            sys.stdout.close()
            #returning error in the code
            sys.stdout = original_stdout
            output = e

    return render(request,'pycom/index.html', {'code':codeareadata, 'input':y, 'output':output})
