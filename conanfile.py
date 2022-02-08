from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class SampleProject(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    # build dependencies
    requires = []
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def configure(self):
        # Some generic c++ settings can be set here instead of setting it in cmake.
        self.settings.compiler.cppstd = 20

    def imports(self):
        # If dynamic linking is involved copy the libraries.
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def generate(self):
        # Use conan 2.0 style of generating CMake.
        # This approach works for multiconfig visual studio without any additional magic.
        # Just do conan install ... with "-s build_type=Debug" and then again with "-s build_type=Release"
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        if self.should_configure:
            cmake.configure()
        if self.should_build:
            cmake.build()
        if self.should_test:
            cmake.test()