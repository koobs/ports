PORTNAME=	influxdb
PORTVERSION=	5.0.0
PORTREVISION=	3
CATEGORIES=	databases python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	vladimirv@ixsystems.com
COMMENT=	Python Client for InfluxDB
WWW=		https://github.com/influxdata/influxdb-python

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}python-dateutil>0:devel/py-python-dateutil@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pytz>0:devel/py-pytz@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}six>0:devel/py-six@${PY_FLAVOR}

USES=		python
USE_PYTHON=	distutils concurrent autoplist
NO_ARCH=	yes

.include <bsd.port.mk>
