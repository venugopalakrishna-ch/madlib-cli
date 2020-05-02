from madlib_cli import __version__
from madlib_cli.madlib import openFile
from madlib_cli.madlib import readFile
from madlib_cli.madlib import parse
from madlib_cli.madlib import injectUserInputs
from madlib_cli.madlib import writeToFile

def test_version():
    assert __version__ == '0.1.0'

def test_openFile():
    input_file=openFile("assets/sample.txt") 
    assert input_file != IOError
def test_openFile_one():
    input_file=openFile("assets/sampl.txt") 
    assert input_file == None

def test_readFile():
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





