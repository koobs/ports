# Duplicating CFLAGS/CXXFLAGS
--- configure.py.orig	2025-04-14 12:28:06 UTC
+++ configure.py
@@ -405,12 +405,9 @@ def shell_escape(str):
         return "'%s'" % str.replace("'", "\\'")
     return str
 
-if 'CFLAGS' in configure_env:
-    cflags.append(configure_env['CFLAGS'])
-    ldflags.append(configure_env['CFLAGS'])
 if 'CXXFLAGS' in configure_env:
     cflags.append(configure_env['CXXFLAGS'])
-    ldflags.append(configure_env['CXXFLAGS'])
+#    ldflags.append(configure_env['CXXFLAGS'])
 n.variable('cflags', ' '.join(shell_escape(flag) for flag in cflags))
 if 'LDFLAGS' in configure_env:
     ldflags.append(configure_env['LDFLAGS'])
