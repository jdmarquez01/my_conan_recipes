from conans import ConanFile, tools, CMake

class CTKConanRecipe(ConanFile):
    name = "CTK"
    version = "0.3"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of hello here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False }
    generators = "cmake"
   
    build_requires = "pythonqt/0.1"

    def source(self):
        git = tools.Git("CTK")
        git.clone("https://github.com/jdmarquez01/CTK.git", branch="qt6")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="CTK")
        cmake.build()
        cmake.install()

        # Explicit way:
        # self.run('cmake "%s/src" %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
       #self.cpp_info.name = "CTK"
       #self.cpp_info.components["CTKCore"].names["cmake"] = "CTKCore"
       #self.cpp_info.components["CTKCore"].includedirs = ["include/CTKCore"]
       #self.cpp_info.components["CTKCore"].libs = ["CTKCore"]
       #
       #self.cpp_info.components["CTKWidgets"].set_property("cmake_target_name","CTK::CTKWidgets")
       #self.cpp_info.components["CTKWidgets"].names["cmake"] = "CTKCore"
       #self.cpp_info.components["CTKWidgets"].includedirs = ["include/CTKWidgets"]
       #self.cpp_info.components["CTKWidgets"].libs = ["CTKWidgets"]
       #self.cpp_info.components["CTKWidgets"].requires = ["CTKCore"]
       #
       #self.cpp_info.components["CTKScriptingPythonCore"].names["cmake"] = "CTKScriptingPythonCore"
       #self.cpp_info.components["CTKScriptingPythonCore"].includedirs = ["include/CTKScriptingPythonCore"]
       #self.cpp_info.components["CTKScriptingPythonCore"].libs = ["CTKCore"]
       #
    #
       #self.cpp_info.components["CTKScriptingPythonWidgets"].names["cmake"] = "CTKScriptingPythonWidgets"
       #self.cpp_info.components["CTKScriptingPythonWidgets"].includedirs = ["include/CTKScriptingPythonWidgets"]
       #self.cpp_info.components["CTKScriptingPythonWidgets"].libs = ["CTKCore", "CTKScriptingPythonCore"]
        
    
        self.cpp_info.libs = ["CTKCore","CTKScriptingPythonCore", "CTKWidgets","CTKScriptingPythonWidgets"]
        self.cpp_info.includedirs = ["include/CTKCore","include/CTKScriptingPythonCore", "include/CTKWidgets","include/CTKScriptingPythonWidgets" ]
        #if self.options.VTK_DIR != "":
        self.cpp_info.libs+= ["CTKVisualizationVTKCore" , "CTKVisualizationVTKWidgets"]
        self.cpp_info.includedirs+=["include/CTKVisualizationVTKCore", "include/CTKVisualizationVTKWidgets"]
