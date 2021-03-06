# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	matrix-synapse
DISTVERSIONPREFIX=	v
DISTVERSION=	0.12.0-rc3
CATEGORIES=	net python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	brendan+freebsd@bbqsrc.net
COMMENT=	Matrix protocol reference homeserver

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

TEST_DEPENDS=	${PYTHON_PKGNAMEPREFIX}virtualenv>0:${PORTSDIR}/devel/py-virtualenv \
		${PYTHON_PKGNAMEPREFIX}tox>0:${PORTSDIR}/devel/py-tox
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}frozendict>=0.4:${PORTSDIR}/devel/py-frozendict \
		${PYTHON_PKGNAMEPREFIX}unpaddedbase64>=1.0.1:${PORTSDIR}/devel/py-unpaddedbase64 \
		${PYTHON_PKGNAMEPREFIX}canonicaljson>=1.0.0:${PORTSDIR}/devel/py-canonicaljson \
		${PYTHON_PKGNAMEPREFIX}signedjson>=1.0.0:${PORTSDIR}/security/py-signedjson \
		${PYTHON_PKGNAMEPREFIX}pynacl>=0.3.0:${PORTSDIR}/security/py-pynacl \
		${PYTHON_PKGNAMEPREFIX}service_identity>=1.0.0:${PORTSDIR}/security/py-service_identity \
		${PYTHON_PKGNAMEPREFIX}twisted>=15.1.0:${PORTSDIR}/devel/py-twisted \
		${PYTHON_PKGNAMEPREFIX}openssl>=0.14:${PORTSDIR}/security/py-openssl \
		${PYTHON_PKGNAMEPREFIX}yaml>0:${PORTSDIR}/devel/py-yaml \
		${PYTHON_PKGNAMEPREFIX}pyasn1>0:${PORTSDIR}/devel/py-pyasn1 \
		${PYTHON_PKGNAMEPREFIX}daemonize>0:${PORTSDIR}/devel/py-daemonize \
		${PYTHON_PKGNAMEPREFIX}bcrypt>0:${PORTSDIR}/security/py-bcrypt \
		${PYTHON_PKGNAMEPREFIX}pillow>0:${PORTSDIR}/graphics/py-pillow \
		${PYTHON_PKGNAMEPREFIX}pydenticon>0:${PORTSDIR}/devel/py-pydenticon \
		${PYTHON_PKGNAMEPREFIX}ujson>0:${PORTSDIR}/devel/py-ujson \
		${PYTHON_PKGNAMEPREFIX}blist>0:${PORTSDIR}/devel/py-blist \
		${PYTHON_PKGNAMEPREFIX}pysaml2>0:${PORTSDIR}/security/py-pysaml2 \
		${PYTHON_PKGNAMEPREFIX}pymacaroons-pynacl>0:${PORTSDIR}/security/py-pymacaroons-pynacl \
		${PYTHON_PKGNAMEPREFIX}simplejson>0:${PORTSDIR}/devel/py-simplejson \
		${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3 \
		${PYTHON_PKGNAMEPREFIX}matrix-angular-sdk>0:${PORTSDIR}/devel/py-matrix-angular-sdk

USE_GITHUB=	yes
GH_ACCOUNT=	matrix-org
GH_PROJECT=	synapse

USES=		python:2.7
USE_PYTHON=	distutils autoplist

do-test:
	# -epy27 added to skip running python packaging and other dist tests
	@(cd ${WRKSRC}; ${SETENV} ${MAKE_ENV} ${PYTHON_CMD} ${PYDISTUTILS_SETUP} ${TEST_TARGET} \
		-a "-epy27")

.include <bsd.port.mk>
