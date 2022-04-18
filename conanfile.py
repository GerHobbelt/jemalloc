import os
from conans import ConanFile, CMake, tools

class JEMallocConan(ConanFile):
    name = "jemalloc"
    version = "5.2.1"
    license = "Proprietary"
    url = "https://github.com/gurumnet/jemalloc"
    description = "General purpose malloc implementation"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/gurumnet/jemalloc.git -b 5.2.1-0")

    def build(self):
        os.chdir('jemalloc')
        os.system('./autogen.sh --with-jemalloc-prefix=je_')
        os.system('make build_lib_static')

    def package(self):
        self.copy("*.a", dst="lib", src="jemalloc/lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["jemalloc"]
