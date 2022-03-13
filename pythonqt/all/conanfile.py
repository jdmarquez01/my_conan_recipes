from conans import ConanFile, CMake, tools


class pythonqtConanRecipe(ConanFile):
    name = "pythonqt"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Pythonqt here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False] }
    default_options = {"shared": True}
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/jdmarquez01/PythonQt.git -b qt6")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("PythonQt/CMakeLists.txt", "project(PythonQt)",
                              '''PROJECT(PythonQt)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')
    def build(self):
        cmake = CMake(self)
        cmake.definitions["PythonQt_INSTALL_INCLUDE_DIR"] = "include"
        cmake.configure(source_folder="PythonQt")
        cmake.build()
        cmake.install()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["pythonqt"]
        self.cpp_info.includedirs = ["include"]



