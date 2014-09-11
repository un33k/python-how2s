class GetterSetterExample(object):

  _some_local_attribute = 1

  @property
  def some_attribute(self):
    return self._some_local_attribute

  @some_attribute.setter
  def some_attribute(self, value):
    self._some_local_attribute = value

# Usage
gs = GetterSetterExample()
print gs.some_attribute
# 1
gs.some_attribute = 2
print gs.some_attribute
# 2

