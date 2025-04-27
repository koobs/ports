# sed "/^\s*$/d" complains about trailing backslash (\)
# https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=253893
--- virtualenvwrapper.sh.orig	2025-04-14 02:04:21 UTC
+++ virtualenvwrapper.sh
@@ -579,7 +579,7 @@ function virtualenvwrapper_show_workon_options {
         | command \tr "\n" " " \
         | command \sed "s|/$VIRTUALENVWRAPPER_ENV_BIN_DIR/activate |/|g" \
         | command \tr "/" "\n" \
-        | command \sed "/^\s*$/d" \
+        | command \sed "/^[[:space:]]*$/d" \
         | (unset GREP_OPTIONS; command \egrep -v '^\*$') 2>/dev/null
 }
 
