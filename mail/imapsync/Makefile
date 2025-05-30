PORTNAME=	imapsync
PORTVERSION=	2.290
CATEGORIES=	mail perl5
MASTER_SITES=	https://imapsync.lamiral.info/dist/

MAINTAINER=	pi@FreeBSD.org
COMMENT=	IMAP synchronization, copy or migration tool
WWW=		https://imapsync.lamiral.info/

LICENSE=	NO_LIMIT_PUBLIC_LICENSE
LICENSE_NAME=	NO LIMIT PUBLIC LICENSE
LICENSE_FILE=	${WRKSRC}/LICENSE
LICENSE_PERMS=	dist-mirror dist-sell pkg-mirror pkg-sell auto-accept

RUN_DEPENDS=	p5-Crypt-OpenSSL-RSA>0:security/p5-Crypt-OpenSSL-RSA \
		p5-Data-Uniqid>0:devel/p5-Data-Uniqid \
		p5-Digest-SHA>0:security/p5-Digest-SHA \
		p5-Encode-IMAPUTF7>0:converters/p5-Encode-IMAPUTF7 \
		p5-File-Copy-Recursive>0:devel/p5-File-Copy-Recursive \
		p5-File-Tail>0:devel/p5-File-Tail \
		p5-IO-Socket-INET6>0:net/p5-IO-Socket-INET6 \
		p5-IO-Socket-SSL>0:security/p5-IO-Socket-SSL \
		p5-IO-Tee>0:devel/p5-IO-Tee \
		p5-JSON-WebToken>0:www/p5-JSON-WebToken \
		p5-Mail-IMAPClient>0:mail/p5-Mail-IMAPClient \
		p5-Proc-ProcessTable>0:devel/p5-Proc-ProcessTable \
		p5-Readonly>0:devel/p5-Readonly \
		p5-Regexp-Common>0:textproc/p5-Regexp-Common \
		p5-Sys-MemInfo>0:devel/p5-Sys-MemInfo \
		p5-Term-ReadKey>0:devel/p5-Term-ReadKey \
		p5-Test-MockObject>0:devel/p5-Test-MockObject \
		p5-Unicode-String>0:converters/p5-Unicode-String \
		p5-libwww>=0:www/p5-libwww

USES=		cpe perl5 tar:tgz shebangfix
SHEBANG_FILES=	${PORTNAME}

CPE_VENDOR=	gilles_lamiral
NO_BUILD=	yes
NO_ARCH=	yes

PORTSCOUT=	limit:^1\.(\d\.){3}

PLIST_FILES=	bin/${PORTNAME} share/man/man1/${PORTNAME}.1.gz

POD2MAN?=	pod2man

do-install:
	${POD2MAN} ${WRKSRC}/${PORTNAME} ${WRKSRC}/${PORTNAME}.1
	${INSTALL_SCRIPT} ${WRKSRC}/${PORTNAME} ${STAGEDIR}${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/${PORTNAME}.1 ${STAGEDIR}${PREFIX}/share/man/man1

.include <bsd.port.mk>
