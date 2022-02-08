# Conan sample project

Use this skeleton for generation of conan project on any platform.
Uses conan 2.0 approach of cmake generation.

For switchable IDE projects generate both Debug and Release dependencies, if working on unix and
you don't bother about performance running with debug is enough.

```
conan install . --build=missing -if=build -pr:b=default -pr:h=default -s build_type=Debug
conan install . --build=missing -if=build -pr:b=default -pr:h=default -s build_type=Release
```

To configure cmake
```
conan build . -bf build -c
```