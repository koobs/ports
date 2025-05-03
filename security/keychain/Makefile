PORTNAME=	keychain
PORTVERSION=	2.9.2
CATEGORIES=	security

MAINTAINER=	garga@FreeBSD.org
COMMENT=	User-friendly front-end to ssh-agent(1)
WWW=		https://www.funtoo.org/Keychain

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/COPYING.txt

USES=		perl5
USE_GITHUB=	yes
USE_PERL5=	build

GH_ACCOUNT=	funtoo

OPTIONS_DEFINE=	DOCS

CONFLICTS_INSTALL=	py*-pycoin # bin/keychain

PLIST_FILES=	bin/${PORTNAME} \
		share/man/man1/keychain.1.gz

PORTDOCS=	ChangeLog.md README.md

.if !exists(${LOCALBASE}/bin/ssh-agent) && !exists(/usr/bin/ssh-agent)
RUN_DEPENDS+=	ssh-agent:security/openssh-portable
.endif

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/${PORTNAME} ${STAGEDIR}${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/keychain.1 ${STAGEDIR}${PREFIX}/share/man/man1
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${PORTDOCS:S|^|${WRKSRC}/|} ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
