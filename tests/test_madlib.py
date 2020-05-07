from madlib_cli import __version__
from madlib_cli.madlib import openFile
from madlib_cli.madlib import readFile
from madlib_cli.madlib import parse
from madlib_cli.madlib import injectUserInputs
from madlib_cli.madlib import writeToFile

def test_version():
    assert __version__ == '0.1.0'

def test_openFile_one():
    input_file=openFile("madlib_cli/assets/sample.txt")         
    assert input_file !=IOError

def test_openFile_two():
    assert openFile("madlib_cli/assets/sample.txt")  

def test_openFile_three():
    input_file=openFile("assets/sampl.txt") 
    assert input_file == None


def test_readFile_one():
    tempfile = open("madlib_cli/assets/sample.txt")
    assert readFile(tempfile) == "A {Adjective} and {Adjective} {Noun}"

def test_readFile_two():    
    assert readFile(openFile("madlib_cli/assets/sample.txt")) == "A {Adjective} and {Adjective} {Noun}"

def test_readFile_three():
    tempfile = open("tmp.txt","w")
    tempfile.write("A {Adjective} and {Adjective} {Noun}")
    tempfile.close()
    tempfile = open("tmp.txt","r")
    filedata = readFile(tempfile) 
    tempfile.close()
    assert filedata == "A {Adjective} and {Adjective} {Noun}"

def test_parse():
    assert parse("A {Adjective} and {Adjective} {Noun}") == ["Adjective","Adjective","Noun"]
     
def test_injectUserInputs():
    template = "A {Adjective} and {Adjective} {Noun}"
    choices = ["Adjective","Adjective","Noun"]
    userinputs = ["dark","storyn","night"]
    assert injectUserInputs(template,choices,userinputs) == "A dark and storyn night"

def test_writeFile():
    writeToFile("A dark and storyn night","tmp.txt") 
    file = open("tmp.txt")
    assert file.read() == "A dark and storyn night"




