from conans import ConanFile, CMake


class VcConan(ConanFile):
    name = "Vc"
    version = "553abc7c"
    license = "3-clause BSD license"
    author = "Matthias Kretz M.Kretz@gsi.de"
    url = "https://github.com/VcDevel/Vc"
    description = "SIMD Vector Classes for C++ "
    topics = ("c++", "simd", "vectorization")
    settings = "os", "compiler", "build_type", "arch"
    options = {"VC_BUILD_TESTING": [True, False]}
    default_options = {"VC_BUILD_TESTING": False}
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        # pylint: disable=no-member

        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = False
        if self.settings.compiler == "Visual Studio":
            runtimes = {
                'MT': 'MultiThreaded',
                'MTd': 'MultiThreadedDebug',
                'MD': 'MultiThreadedDLL',
                'MDd': 'MultiThreadedDebugDLL',
            }
            cmake.definitions["CMAKE_MSVC_RUNTIME_LIBRARY"] = runtimes[str(
                self.settings.compiler.runtime)]

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
