PORTNAME=	cpuid
DISTVERSION=	20250419
DISTVERSIONSUFFIX=	.src
CATEGORIES=	sysutils
MASTER_SITES=	https://www.etallen.com/cpuid/
PKGNAMESUFFIX=	${CPUID_SUFFIX}

MAINTAINER=	pkubaj@FreeBSD.org
COMMENT=	Tool to dump x86 CPUID information about the CPU(s)
WWW=		https://www.etallen.com/cpuid.html

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/LICENSE

ONLY_FOR_ARCHS=	amd64 i386
ONLY_FOR_ARCHS_REASON=	only works with x86 CPUs

USES=		gmake perl5
USE_PERL5=	build

CFLAGS+=	-pthread

ALL_TARGET=	default
WRKSRC=		${WRKDIR}/${PORTNAME}-${DISTVERSION}

# Renamed to avoid conflict with misc/cpuid
CPUID_SUFFIX=	-etallen

PLIST_FILES=	bin/cpuid${CPUID_SUFFIX} \
		share/man/man1/cpuid${CPUID_SUFFIX}.1.gz

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/cpuid ${STAGEDIR}${PREFIX}/bin/cpuid${CPUID_SUFFIX}
	${INSTALL_MAN} ${WRKSRC}/cpuid.man.gz ${STAGEDIR}${PREFIX}/share/man/man1/cpuid${CPUID_SUFFIX}.1.gz

.include <bsd.port.mk>
