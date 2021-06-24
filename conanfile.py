from conans import ConanFile, CMake


class VcConan(ConanFile):
    name = "Vc"
    version = "5824e56"
    license = "3-clause BSD license"
    author = "Matthias Kretz M.Kretz@gsi.de"
    url = "https://github.com/VcDevel/Vc"
    description = "SIMD Vector Classes for C++ "
    topics = ("c++", "simd", "vectorization")
    settings = "os", "compiler", "build_type", "arch"
    options = {}
    default_options = {}
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = False
        cmake.configure(source_folder=".", build_folder="./build")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.h", dst="include", src="Vc")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Vc"]
