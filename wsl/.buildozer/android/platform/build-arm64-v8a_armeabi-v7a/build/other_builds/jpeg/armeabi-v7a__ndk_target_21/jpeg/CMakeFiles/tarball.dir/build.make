# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/d/pycharm/pythonProject1/wsl/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/d/pycharm/pythonProject1/wsl/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg

# Utility rule file for tarball.

# Include any custom commands dependencies for this target.
include CMakeFiles/tarball.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/tarball.dir/progress.make

CMakeFiles/tarball:
	sh pkgscripts/maketarball

tarball: CMakeFiles/tarball
tarball: CMakeFiles/tarball.dir/build.make
.PHONY : tarball

# Rule to build all files generated by this target.
CMakeFiles/tarball.dir/build: tarball
.PHONY : CMakeFiles/tarball.dir/build

CMakeFiles/tarball.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/tarball.dir/cmake_clean.cmake
.PHONY : CMakeFiles/tarball.dir/clean

CMakeFiles/tarball.dir/depend:
	cd /mnt/d/pycharm/pythonProject1/wsl/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/d/pycharm/pythonProject1/wsl/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg /mnt/d/pycharm/pythonProject1/wsl/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg /mnt/d/pycharm/pythonProject1/wsl/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg /mnt/d/pycharm/pythonProject1/wsl/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg /mnt/d/pycharm/pythonProject1/wsl/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg/CMakeFiles/tarball.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/tarball.dir/depend

