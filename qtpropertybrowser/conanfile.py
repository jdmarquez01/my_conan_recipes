from conans import ConanFile, CMake, tools


class ttpropertybrowserConanRecipe(ConanFile):
    name = "qtpropertybrowser"
    version = "0.2"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Qtpropertybrowser here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    #exports_sources = "*"

    def source(self):
        ##use tools.Git() in future
        self.run("git clone https://github.com/jdmarquez01/QtPropertyBrowser.git -b qt6")
        
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="QtPropertyBrowser")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["qtpropertybrowser"]
        self.cpp_info.include_dirs = ["include"]


