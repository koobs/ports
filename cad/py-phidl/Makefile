PORTNAME=	phidl
PORTVERSION=	1.0.1
PORTREVISION=	3
CATEGORIES=	cad python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	hrs@FreeBSD.org
COMMENT=	GDS-based CAD tool for photonic and superconducting circuits
WWW=		https://github.com/amccaugh/phidl

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}gdspy>0:cad/py-gdspy@${PY_FLAVOR}

USES=		python
USE_PYTHON=	distutils autoplist
USE_GITHUB=	yes
GH_ACCOUNT=	amccaugh

.include <bsd.port.mk>
