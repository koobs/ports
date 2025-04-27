# https://github.com/pypa/setuptools-scm/commit/98b70785ab99ee32b6863c32d0fc844cd2c3dd95
# https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=258891
# https://github.com/pypa/setuptools-scm/issues/353
# https://github.com/pypa/setuptools-scm/issues/1103
# See Also:
# https://github.com/distro-core-curated-mirrors/poky-contrib/commit/4a2ee5b63af43f300bcebcefa7ca8734a6684bb6
--- src/setuptools_scm/_run_cmd.py.orig	2025-04-14 03:22:10 UTC
+++ src/setuptools_scm/_run_cmd.py
@@ -94,7 +94,7 @@ def no_git_env(env: Mapping[str, str]) -> dict[str, st
         k: v
         for k, v in env.items()
         if not k.startswith("GIT_")
-        or k in ("GIT_EXEC_PATH", "GIT_SSH", "GIT_SSH_COMMAND")
+        or k in ("GIT_CEILING_DIRECTORIES", "GIT_EXEC_PATH", "GIT_SSH", "GIT_SSH_COMMAND")
     }
 
 
