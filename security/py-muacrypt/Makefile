PORTNAME=	muacrypt
PORTVERSION=	0.9.1
PORTREVISION=	1
CATEGORIES=	security mail python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	egypcio@FreeBSD.org
COMMENT=	Support tool and API for Autocrypt mail agents
WWW=		https://pypi.org/project/muacrypt/

LICENSE=	MIT

RUN_DEPENDS=	gpg2:security/gnupg	\
	${PYTHON_PKGNAMEPREFIX}click>=0:devel/py-click@${PY_FLAVOR}		\
	${PYTHON_PKGNAMEPREFIX}attrs>=0:devel/py-attrs@${PY_FLAVOR}		\
	${PYTHON_PKGNAMEPREFIX}six>=0:devel/py-six@${PY_FLAVOR} 		\
	${PYTHON_PKGNAMEPREFIX}execnet>=0:sysutils/py-execnet@${PY_FLAVOR}	\
	${PYTHON_PKGNAMEPREFIX}pluggy>=0:devel/py-pluggy@${PY_FLAVOR}		\
	${PYTHON_PKGNAMEPREFIX}termcolor>=0:devel/py-termcolor@${PY_FLAVOR}

TEST_DEPENDS=	${PYTHON_PKGNAMEPREFIX}tox>=0:devel/py-tox@${PY_FLAVOR}

USES=		python
USE_PYTHON=	autoplist distutils

NO_ARCH=	yes

.include <bsd.port.mk>
