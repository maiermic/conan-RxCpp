from conans import ConanFile

class RxCppConan(ConanFile):
  name = "RxCpp"
  version = "4.0.0"
  settings = None
  build_policy = "missing"
  url = "https://github.com/maiermic/conan-RxCpp"
  description = "The Reactive Extensions for C++ (RxCpp) is a library of algorithms for values-distributed-in-time."
  license = "Apache License 2.0"

  def source(self):
    self.run("git clone https://github.com/Reactive-Extensions/RxCpp")
    self.run("cd RxCpp && git checkout v4.0.0")
  
  def build(self):
    pass

  def package(self):
    self.copy("*.hpp", dst="include", src="RxCpp/Rx/v2/src", keep_path=True)
