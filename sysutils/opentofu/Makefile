PORTNAME=	opentofu
DISTVERSIONPREFIX=	v
DISTVERSION=	1.9.1
CATEGORIES=	sysutils

MAINTAINER=	bofh@FreeBSD.org
COMMENT=	Tool for building, changing, and versioning infrastructure
WWW=		https://opentofu.org/

LICENSE=	MPL20
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		go:1.24,modules
GO_MODULE=	github.com/opentofu/opentofu
GO_TARGET=	./cmd/tofu
GO_BUILDFLAGS=	-o bin/

PLIST_FILES=	bin/tofu

.include <bsd.port.mk>
