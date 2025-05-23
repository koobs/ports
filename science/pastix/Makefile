PORTNAME=	pastix
PORTVERSION=	6.3.2
PORTREVISION=	2
CATEGORIES=	science
MASTER_SITES=	https://gitlab.inria.fr/solverstack/pastix/uploads/${GL_TAG}/

MAINTAINER=	thierry@FreeBSD.org
COMMENT=	PaStiX: a sparse direct solver
WWW=		https://solverstack.gitlabpages.inria.fr/pastix/

LICENSE=	LGPL3

DEPRECATED=	Depends on expired lang/julia
EXPIRATION_DATE=2025-06-01

BUILD_DEPENDS=	bash:shells/bash	\
		${PYNUMPY}
LIB_DEPENDS=	libmetis.so:math/metis	\
		libjulia.so:lang/julia	\
		libscotch.so:cad/scotch	\
		libhwloc.so:devel/hwloc2
RUN_DEPENDS=	bash:shells/bash	\
		${PYNUMPY}

USES=		cmake blaslapack:openblas fortran pkgconfig python

#USE_GITLAB=	yes
#GL_SITE=	https://gitlab.inria.fr/
#GL_ACCOUNT=	solverstack
#GL_PROJECT=	pastix spm:s morse_cmake:m
#GL_TAGNAME=	6e35c2ba179013b058f5d4e1afd4b451953149c6	\
#		14e36c1586c9ba13f938b1a89f51c080d6551392:s	\
#		31cd2bbb0d76f2b9fd83011d8f079d97540b0ba8:m
#GL_SUBDIR=	spm:s cmake_modules/morse_cmake:m
GL_TAG=		32711239db22edb6c291282b581b9e0b	# tarball with submodules

LDFLAGS+=	-lm
CMAKE_ARGS=	-DBUILD_SHARED_LIBS:BOOL=ON	\
		-DPASTIX_ORDERING_METIS:BOOL=ON	\
		-DPython_VERSION_MAJOR=${PYTHON_MAJOR_VER}	\
		-DPython_VERSION_MINOR=${PYTHON_VER:E}
USE_LDCONFIG=	yes
TEST_TARGET=	test

PLIST_SUB=	VER=${PORTVERSION}

OPTIONS_DEFINE=	EXAMPLES
EX2FIX=		spm/examples spm/wrappers/fortran90 spm/wrappers/python
EX2FIX2=	example example/old wrappers/julia wrappers/fortran90 wrappers/python

pre-configure:
.for ex in ${EX2FIX}
	${REINPLACE_CMD} -e 's|DESTINATION examples|DESTINATION ${EXAMPLESDIR}/${ex:C/examples//:C/example//}|'	\
			-e 's|share/doc/spm/examples|${EXAMPLESDIR}/spm|'	\
		${WRKSRC}/${ex}/CMakeLists.txt
.endfor
.for ex in ${EX2FIX2}
	${REINPLACE_CMD} -e 's|share/doc/pastix/examples|share/examples/pastix|' \
		${WRKSRC}/${ex}/CMakeLists.txt
.endfor

.include <bsd.port.mk>
