PORTNAME=	lief
DISTVERSION=	0.15.1
CATEGORIES=	devel python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	ports@nicandneal.net
COMMENT=	Library to instrument executable formats
WWW=		https://github.com/lief-project/lief

LICENSE=	APACHE20

USES=		cmake:indirect python

USE_GITHUB=	yes
USE_PYTHON=	concurrent distutils

GH_ACCOUNT=	lief-project
GH_PROJECT=	LIEF

PYSETUP=	${WRKSRC}/api/python/backend/setup.py
PY_VER=		${PYTHON_VER:S/.//}
PLIST_SUB=	PY_VER=${PY_VER}

post-install:
	@${STRIP_CMD} ${STAGEDIR}${PYTHON_SITELIBDIR}/lief.cpython-${PY_VER}.so

.include <bsd.port.mk>
