class Developer(object):
    def remind(self):
        raise NotImplementedError

class PythonDeveloper(Developer):
    def remind(self):
        print "In Python, don't forget your indentations."

class JavaDeveloper(Developer):
    def remind(self):
        print "In Java, don't forget your semicolons."

p = PythonDeveloper()
p.remind()

j = JavaDeveloper()
j.remind()

