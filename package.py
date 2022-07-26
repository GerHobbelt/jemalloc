name = "jemalloc"

version = "5.3.0"

description = \
   """
   Jemalloc (Jason Evans' memory allocator)
   """

with scope("config") as c:
   # Determine location to release: internal (int) vs external (ext)

   # NOTE: Modify this variable to reflect the current package situation
   release_as = "ext"

   # The `c` variable here is actually rezconfig.py
   # `release_packages_path` is a variable defined inside rezconfig.py

   import os
   if release_as == "int":
       c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
   elif release_as == "ext":
       c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

   #c.build_thread_count = "physical_cores"

requires = [
]

private_build_requires = [
]

variants = [
   ["platform-linux", "arch-x86_64", "os-centos-7"],
]

uuid = "repository.jemalloc"

# NOTE: If the root of the repo has no "configure" file (not the "configure.ac"),
# you need to run "autoconf" from the root first.

def pre_build_commands():
   command("source /opt/rh/devtoolset-6/enable")

def commands():
   env.PATH.prepend("{root}/bin")
   env.LD_LIBRARY_PATH.append("{root}/lib")
   env.JEMALLOC_LOCATION = "{root}"
