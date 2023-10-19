#!/bin/sh
##SCRIPT DIR
DIR_NAME=`dirname "$0"`
DIR_NAME=`cd "$DIR_NAME"; pwd`
cd "${DIR_NAME}"
##JAVA
JAVA_BUNDLED="./jre/bin/java"
if [ -f "${JAVA_BUNDLED}" ]; then
	JAVA="${JAVA_BUNDLED}"
fi
if [ -z ${JAVA} ]; then
	[ -z ${JAVA_HOME} ] && JAVA_HOME="/usr"
	[ ! -f "${JAVA}" ] && JAVA="${JAVA_HOME}/bin/java"
	[ ! -f "${JAVA}" ] && JAVA="java"
fi
##LIBRARY_PATH
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib64/tuxguitar-1.5.6/lib/
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/lib
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib/jni
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib
##CLASSPATH
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/tuxguitar.jar
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/tuxguitar-ui-toolkit.jar
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/tuxguitar-ui-toolkit-swt.jar
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/tuxguitar-lib.jar
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/tuxguitar-editor-utils.jar
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/tuxguitar-gm-utils.jar
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/tuxguitar-awt-graphics.jar
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/swt.jar
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/gervill.jar
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/itext-pdf.jar
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/itext-xmlworker.jar
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/commons-compress.jar
CLASSPATH=${CLASSPATH}:/usr/lib64/tuxguitar-1.5.6/lib/icedtea-sound.jar
CLASSPATH=${CLASSPATH}:/usr/share/tuxguitar-1.5.6/share/
CLASSPATH=${CLASSPATH}:/usr/share/tuxguitar-1.5.6/dist/
##MAINCLASS
MAINCLASS=org.herac.tuxguitar.app.TGMainSingleton
##JVM ARGUMENTS
VM_ARGS="-Xmx512m"
##EXPORT VARS
export CLASSPATH
export LD_LIBRARY_PATH
export SWT_GTK3=0
##LAUNCH
${JAVA} ${VM_ARGS} -cp :${CLASSPATH} -Dtuxguitar.home.path="${DIR_NAME}" -Dtuxguitar.share.path="/usr/share/tuxguitar-1.5.6/share/" -Djava.library.path="${LD_LIBRARY_PATH}" ${MAINCLASS} "$1" "$2"
