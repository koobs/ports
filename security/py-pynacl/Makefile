# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	pynacl
PORTVERSION=	0.3.0
CATEGORIES=	security devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTNAME=	PyNaCl-${DISTVERSION}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Python binding to the Networking and Cryptography (NaCl) library

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}cffi>0:${PORTSDIR}/devel/py-cffi
LIB_DEPENDS=	libsodium.so:${PORTSDIR}/security/libsodium
TEST_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pytest>0:${PORTSDIR}/devel/py-pytest

USES=		python
USE_PYTHON=	autoplist distutils

post-install:
	${STRIP_CMD} ${STAGEDIR}${PYTHON_SITELIBDIR}/nacl/_lib/*.so

do-test:
	@(cd ${WRKSRC} && ${PYTHON_CMD} -m pytest tests)

.include <bsd.port.mk>
